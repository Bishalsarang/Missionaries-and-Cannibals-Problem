import os
import emoji
import pydot
import random
from collections import deque



# Set it to bin folder of graphviz
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

Parent = dict()
Move = dict()
node_list = dict()

class Solution():

    def __init__(self):
        # Start state (3M, 3C, Left)
        # Goal State (0M, 0C, Right)
        # Each state gives the number of missionaries and cannibals on the left side

        self.start_state = (3, 3, 1)
        self.goal_state = (0, 0, 0)
        self.options = [ (0, 1), (0, 2), (1, 0), (1, 1),  (2, 0), ]
        # random.shuffle(self.options)

        self.boat_side = ["right", "left"]

        self.graph = pydot.Dot(graph_type='graph')
        # self.ga = Animation()
        # self.last_state = None
        self.visited = {}
        self.solved = False

    def is_valid_move(self, number_missionaries, number_cannnibals):
        """
        Checks if number constraints are satisfied
        """
        return (0 <= number_missionaries <= 3) and (0 <= number_cannnibals <= 3)

    def is_goal_state(self, number_missionaries, number_cannnibals, side):
        return (number_missionaries, number_cannnibals, side) == self.goal_state

    def is_start_state(self, number_missionaries, number_cannnibals, side):
        return (number_missionaries, number_cannnibals, side) == self.start_state

    def number_of_cannibals_exceeds(self, number_missionaries, number_cannnibals):
        number_missionaries_right = 3 - number_missionaries
        number_cannnibals_right = 3 - number_cannnibals
        return (number_missionaries > 0 and number_cannnibals > number_missionaries) or (number_missionaries_right > 0 and number_cannnibals_right > number_missionaries_right)

    def write_image(self, file_name="state_space.png"):
        print(f"File {file_name} successfully written.")
        self.graph.write_png(file_name)

    def solve(self, solve_method="dfs"):
        self.visited = dict()
        
        Parent[self.start_state] = None
        Move[self.start_state] = None
        node_list[self.start_state] = None

        return self.dfs(*self.start_state, 0) if solve_method == "dfs" else self.bfs()

    def draw(self, *, number_missionaries_left, number_cannnibals_left, number_missionaries_right, number_cannnibals_right):
        left_m = emoji.emojize(f":old_man: " * number_missionaries_left)
        left_c = emoji.emojize(f":ogre: " * number_cannnibals_left)
        right_m = emoji.emojize(f":old_man: " * number_missionaries_right)
        right_c = emoji.emojize(f":ogre: " * number_cannnibals_right)
        
        print('{}{}{}{}{}'.format(left_m ,left_c  + " " * (14 - len(left_m) - len(left_c)), "_" * 40, " " * (12 - len(right_m) - len(right_c)) + right_m, right_c))
        print("")
        # print (left_m ,  left_c, "__________________", right_m , right_c)

    def show_solution(self):
        # Recursively start from Goal State
        # And find parent until start state is reached

        state = self.goal_state
        path = []
        steps = []
        nodes = []
        while state is not None:
            path.append(state)
            steps.append(Move[state])
            nodes.append(node_list[state])
        
            state = Parent[state]
        
        steps = steps[::-1]
        nodes = nodes[::-1]

        
        number_missionaries_left, number_cannnibals_left = 3, 3
        number_missionaries_right, number_cannnibals_right = 0, 0
        print("*" * 60)
        self.draw(number_missionaries_left=number_missionaries_left, number_cannnibals_left=number_cannnibals_left, number_missionaries_right=number_missionaries_right, number_cannnibals_right=number_cannnibals_right)
     
        for (number_missionaries, number_cannnibals, side), node in zip(steps[1:], nodes[1:]):
            node.set_style("filled")
            node.set_fillcolor("yellow")
            # print(side)
            # print(f". Move " , emoji.emojize(" :old_man: " * number_missionaries)  ,f"and " , emoji.emojize(" :ogre: " * number_cannnibals) , f" from {self.boat_side[side]} to {self.boat_side[int(not side)]}.")
            print(f"Move {number_missionaries} missionaries  and {number_cannnibals} cannibals from {self.boat_side[side]} to {self.boat_side[int(not side)]}.")
            if side == 1:
                number_missionaries_left -= number_missionaries
                number_missionaries_right += number_missionaries

                number_cannnibals_left -= number_cannnibals
                number_cannnibals_right += number_cannnibals
            else:
                number_missionaries_left += number_missionaries
                number_missionaries_right -= number_missionaries
                number_cannnibals_left += number_cannnibals
                number_cannnibals_right -= number_cannnibals
            self.draw(number_missionaries_left=number_missionaries_left, number_cannnibals_left=number_cannnibals_left, number_missionaries_right=number_missionaries_right, number_cannnibals_right=number_cannnibals_right)
            
        print("Congratulations!!! you have solved the problem")
        print("*" * 60)
        

    def bfs(self):
        q = deque()
        q.append(self.start_state + (0, ))

        self.visited[self.start_state] = True


        while q:
            number_missionaries, number_cannnibals, side, depth_level = q.popleft()

            u = pydot.Node(str((number_missionaries, number_cannnibals, side, depth_level)), label=str((number_missionaries, number_cannnibals, side)))
            self.graph.add_node(u)

            if self.is_start_state(number_missionaries, number_cannnibals, side):
                u.set_style("filled")
                u.set_fillcolor("blue")
                u.set_fontcolor("white")
            elif self.is_goal_state(number_missionaries, number_cannnibals, side):
                u.set_style("filled")
                u.set_fillcolor("green")
                return True

            elif self.number_of_cannibals_exceeds(number_missionaries, number_cannnibals):
                u.set_style("filled")
                u.set_fillcolor("red")
                continue

            op = -1 if side == 1 else 1

            can_be_expanded = False

            for x, y in self.options:
                next_m, next_c, next_s = number_missionaries + op * x, number_cannnibals + op * y, int(not side)
                
                if (next_m, next_c, next_s) not in self.visited:
                    if self.is_valid_move(next_m, next_c):
                        can_be_expanded = True
                        self.visited[(next_m, next_c, next_s)] = True
                        q.append((next_m, next_c, next_s, depth_level + 1))
                        
                        v = pydot.Node(str((next_m, next_c, next_s, depth_level + 1)), label=str((next_m, next_c, next_s)))
                        self.graph.add_node(v)                
                        
                        edge = pydot.Edge(str((number_missionaries, number_cannnibals, side, depth_level)), str((next_m, next_c, next_s, depth_level + 1) ), dir='forward')
                        
                        self.graph.add_edge(edge)
                        # self.graph.add_node(pydot.Node(str(next_m, next_c, next_s, depth_level + 1)), str((next_m, next_c, next_s)))
                        # self.graph.add_edge(str((number_missionaries, number_cannnibals, side, depth_level)), str((next_m, next_c, next_s, depth_level + 1)))
                        # Keep track of parent and corresponding move
                        Parent[(next_m, next_c, next_s)] = (number_missionaries, number_cannnibals, side)
                        Move[(next_m, next_c, next_s)] = (x, y, side)
                        node_list[(next_m, next_c, next_s)] = v

            if not can_be_expanded:
                u.set_style("filled")
                u.set_fillcolor("gray")

          

                
        return False

    def dfs(self, number_missionaries, number_cannnibals, side, depth_level):

        u = pydot.Node(str((number_missionaries, number_cannnibals, side, depth_level)), label=str((number_missionaries, number_cannnibals, side)))
        self.graph.add_node(u)

        if self.is_start_state(number_missionaries, number_cannnibals, side):
            u.set_style("filled")
            u.set_fillcolor("blue")
        elif self.is_goal_state(number_missionaries, number_cannnibals, side):
            u.set_style("filled")
            u.set_fillcolor("green")
            
            return True

        elif self.number_of_cannibals_exceeds(number_missionaries, number_cannnibals):
            u.set_style("filled")
            u.set_fillcolor("red")
            return False

        self.visited[(number_missionaries, number_cannnibals, side)] = True

        solution_found = False
        operation = -1 if side == 1 else 1

        
        can_be_expanded = False

        for x, y in self.options:
            next_m, next_c, next_s = number_missionaries + operation * x, number_cannnibals + operation * y, int(not side)

            if (next_m, next_c, next_s) not in self.visited:
                if self.is_valid_move(next_m, next_c):
                    can_be_expanded = True
                    v = pydot.Node(str((next_m, next_c, next_s, depth_level + 1)), label=str((next_m, next_c, next_s)))
                    self.graph.add_node(v)

                    edge = pydot.Edge(str((number_missionaries, number_cannnibals, side, depth_level)), str((next_m, next_c, next_s, depth_level + 1) ), dir='forward')
                        
                    self.graph.add_edge(edge)
                    
                    solution_found = (solution_found or self.dfs(next_m, next_c, next_s, depth_level + 1))
                    
                    # Keep track of Parent state and corresponding move
                    Parent[(next_m, next_c, next_s)] = (number_missionaries, number_cannnibals, side)
                    Move[(next_m, next_c, next_s)] = (x, y, side)
                    node_list[(next_m, next_c, next_s)] = v
                   
                    if(solution_found):
                        return True
     
        if not can_be_expanded:
            u.set_style("filled")
            u.set_fillcolor("gray")

        self.solved = solution_found
        return solution_found
