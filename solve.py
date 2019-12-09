import os
import emoji
import pydot
from collections import deque

# from gvanim import Animation, render, gif
# from gvanim.jupyter import interactive
# import imageio
Parent = dict()
Move = dict()

class Node():
    # Node types: killed, goal, start, normal
    def __init__(self, node_value, state, node_type="normal", parent=None):
        self.state = state
        self.node_type = node_type
        self.parent = parent
        self.node_value = node_value
        self.set_color()

    def set_color(self):
        self.node_value.set_style("filled")
        if self.node_type == "killed":
            self.node_value.set_fillcolor("red")
        elif self.node_type == "goal":
            self.node_value.set_fillcolor("green")
        elif self.node_type == "start":
            self.node_value.set_fillcolor("blue")


class Solution():

    def __init__(self):
        # Start state (3M, 3C, Left)
        # Goal State (0M, 0C, Right)
        # Each state gives the number of missionaries and cannibals on the left side

        self.start_state = (3, 3, 1)
        self.goal_state = (0, 0, 0)
        self.options = [(1, 0), (1, 1), (0, 1), (0, 2), (2, 0), ]
        self.boat_side = ["right", "left"]

        self.graph = pydot.Dot(graph_type='graph', overlap='false', splines='curved')
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

    def number_of_cannibals_exceeds(self, number_missionaries, number_cannnibals):
        number_missionaries_right = 3 - number_missionaries
        number_cannnibals_right = 3 - number_cannnibals
        return (number_missionaries > 0 and number_cannnibals > number_missionaries) or (number_missionaries_right > 0 and number_cannnibals_right > number_missionaries_right)

    def write_image(self, file_name="state_space.png"):
        self.graph.write_png(file_name)

    def solve(self, solve_method="dfs"):
        self.visited = dict()
        
        Parent[self.start_state] = None
        Move[self.start_state] = None

        return self.dfs(*self.start_state, 0) if solve_method == "dfs" else self.bfs()

    def show_solution(self):
        # Recursively start from Goal State
        # And find parent until start state is reached

        state = self.goal_state
        path = []
        steps = []
        while state is not None:
            path.append(state)
            steps.append(Move[state])
            state = Parent[state]
        
        steps = steps[::-1]

        print("*" * 60)
        for i, (number_missionaries, number_cannnibals, side) in enumerate(steps[1:], start=1):
            print(emoji.emojize(f"{i}. Move {number_missionaries} :old_man:  and {number_cannnibals} :ogre:  from {self.boat_side[side]} to {self.boat_side[int(not side)]}."))
            # print(emoji.emojize(f'Python is {i}:thumbs_up:'))
        print("Congratulations!!! you have solved the problem")
        print("*" * 60)
        

    def bfs(self):
        q = deque()
        q.append(self.start_state + (0, ))

        self.visited[self.start_state] = True


        while q:
            number_missionaries, number_cannnibals, side, depth_level = q.popleft()

            if self.is_goal_state(number_missionaries, number_cannnibals, side):
                return True

            if self.number_of_cannibals_exceeds(number_missionaries, number_cannnibals):
                continue

            op = -1 if side == 1 else 1

            for x, y in self.options:
                next_m, next_c, next_s = number_missionaries + op * x, number_cannnibals + op * y, int(not side)
                
                if (next_m, next_c, next_s) not in self.visited:
                    if self.is_valid_move(next_m, next_c):
                        self.visited[(next_m, next_c, next_s)] = True
                        q.append((next_m, next_c, next_s, depth_level + 1))

                        # Keep track of parent and corresponding move
                        Parent[(next_m, next_c, next_s)] = (number_missionaries, number_cannnibals, side)
                        Move[(next_m, next_c, next_s)] = (x, y, side);
                
        return False

    def dfs(self, number_missionaries, number_cannnibals, side, depth_level):
        if self.is_goal_state(number_missionaries, number_cannnibals, side):
            return True

        if self.number_of_cannibals_exceeds(number_missionaries, number_cannnibals):
            return False

        self.visited[(number_missionaries, number_cannnibals, side)] = True

        solution_found = False
        operation = -1 if side == 1 else 1

        for x, y in self.options:
            next_m, next_c, next_s = number_missionaries + operation * x, number_cannnibals + operation * y, int(not side)

            if (next_m, next_c, next_s) not in self.visited:
                if self.is_valid_move(next_m, next_c):
                    solution_found = (solution_found or self.dfs(next_m, next_c, next_s, depth_level + 1))
                    
                    # Keep track of Parent state and corresponding move
                    Parent[(next_m, next_c, next_s)] = (number_missionaries, number_cannnibals, side)
                    Move[(next_m, next_c, next_s)] = (x, y, side)
                    if(solution_found):
                        return True
            else:
                # Dead Node
                pass

        self.solved = solution_found
        return solution_found
