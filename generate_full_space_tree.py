from collections import deque
import pydot
import argparse
import os

# Set it to bin folder of graphviz
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

options = [(1, 0), (0, 1), (1, 1), (0, 2), (2, 0)]
Parent = dict()
graph = pydot.Dot(graph_type='graph',strict=True, bgcolor="#fff3af", label="fig: Missionaries and Cannibal State Space Tree", fontcolor="red", fontsize="24", overlap="true")


arg = argparse.ArgumentParser()
arg.add_argument("-d", "--depth", required=False, help="MAximum depth upto which you want to generate Space State Tree")

args = vars(arg.parse_args())

max_depth = int(args.get("depth", 20))


def is_valid_move(number_missionaries, number_cannnibals):
        """
        Checks if number constraints are satisfied
        """
        return (0 <= number_missionaries <= 3) and (0 <= number_cannnibals <= 3)

def write_image(file_name="state_space"):
        try:
            graph.write_png(f"{file_name}_{max_depth}.png")
        except Exception as e:
            print("Error while writing file", e)
        print(f"File {file_name}_{max_depth}.png successfully written.")

def draw_edge(number_missionaries, number_cannnibals, side, depth_level, node_num):
        u, v = None, None
        if Parent[(number_missionaries, number_cannnibals, side, depth_level, node_num)] is not None:
            u = pydot.Node(str(Parent[(number_missionaries, number_cannnibals, side, depth_level, node_num)]), label=str(Parent[(number_missionaries, number_cannnibals, side, depth_level, node_num)][:3]))
            graph.add_node(u)

            v = pydot.Node(str((number_missionaries, number_cannnibals, side, depth_level, node_num)), label=str((number_missionaries, number_cannnibals, side)))
            graph.add_node(v)

            edge = pydot.Edge(str(Parent[(number_missionaries, number_cannnibals, side, depth_level, node_num)]), str((number_missionaries, number_cannnibals, side, depth_level, node_num) ), dir='forward')
            graph.add_edge(edge)
        else:
            # For start node
            v = pydot.Node(str((number_missionaries, number_cannnibals, side, depth_level, node_num)), label=str((number_missionaries, number_cannnibals, side)))
            graph.add_node(v)        
        return u, v

def is_start_state(number_missionaries, number_cannnibals, side):
    return (number_missionaries, number_cannnibals, side) == (3, 3, 1)

def is_goal_state(number_missionaries, number_cannnibals, side):
    return (number_missionaries, number_cannnibals, side) == (0, 0, 0)

def number_of_cannibals_exceeds(number_missionaries, number_cannnibals):
    number_missionaries_right = 3 - number_missionaries
    number_cannnibals_right = 3 - number_cannnibals
    return (number_missionaries > 0 and number_cannnibals > number_missionaries) \
            or (number_missionaries_right > 0 and number_cannnibals_right > number_missionaries_right)

def generate():
        q = deque()
        node_num = 0
        q.append((3, 3, 1, 0, node_num))

        
        Parent[(3, 3, 1, 0, node_num)] = None

        while q:
            number_missionaries, number_cannnibals, side, depth_level, node_num = q.popleft()
            # print(number_missionaries, number_cannnibals)
            # Draw Edge from u -> v
            # Where u = Parent[v]
            # and v = (number_missionaries, number_cannnibals, side, depth_level)
            u, v = draw_edge(number_missionaries, number_cannnibals, side, depth_level, node_num)    

            
            if is_start_state(number_missionaries, number_cannnibals, side):   
                v.set_style("filled")
                v.set_fillcolor("blue")
                v.set_fontcolor("white")
            elif is_goal_state(number_missionaries, number_cannnibals, side):
                v.set_style("filled")
                v.set_fillcolor("green")
                continue
                # return True
            elif number_of_cannibals_exceeds(number_missionaries, number_cannnibals):
                v.set_style("filled")
                v.set_fillcolor("red")
                continue
            else:
                v.set_style("filled")
                v.set_fillcolor("orange")

            if depth_level == max_depth:
                return True

            op = -1 if side == 1 else 1

            can_be_expanded = False

            i = node_num
            for x, y in options:
                next_m, next_c, next_s = number_missionaries + op * x, number_cannnibals + op * y, int(not side)
                if Parent[(number_missionaries, number_cannnibals, side, depth_level, node_num)] is None or (next_m, next_c, next_s) != Parent[(number_missionaries, number_cannnibals, side, depth_level, node_num)][:3]:
                    if is_valid_move(next_m, next_c):
                        can_be_expanded = True
                        i += 1
                        q.append((next_m, next_c, next_s, depth_level + 1, i))
                        
                        # Keep track of parent and corresponding move
                        Parent[(next_m, next_c, next_s, depth_level + 1, i)] = (number_missionaries, number_cannnibals, side, depth_level, node_num)

            if not can_be_expanded:
                v.set_style("filled")
                v.set_fillcolor("gray")
        return False

if __name__ == "__main__":
    if generate():
        write_image()