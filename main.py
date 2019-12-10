from solve import Solution
# from temp import Solution
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-m", "--method", required=False, help="Specify which method to use")
arg.add_argument("-l", "--legend", required=False, help="Specify if you want to display legend on graph")

args = vars(arg.parse_args())

solve_method = args.get("method", "bfs")
legend_flag = args.get("legend", False)

def main():
    s = Solution()

    if(s.solve(solve_method)):
        
        # Display SOlution on console
        s.show_solution()

        # Draw legend if legend_flag is set
        if legend_flag:
            if legend_flag[0].upper() == 'T' :
                s.draw_legend()
        # Write State space tree
        s.write_image(f"{solve_method}.png")
    else:
        raise Exception("No solution found")


if __name__ == "__main__":
    main()