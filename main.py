from solve import Solution
import argparse


arg = argparse.ArgumentParser()
arg.add_argument("-m", "--method", required=False, help="Specify which method to use")
args = vars(arg.parse_args())

solve_method = args.get("method", "bfs")

def main():
    s = Solution()
    if(s.solve(solve_method)):
        s.show_solution()
        s.write_image(f"{solve_method}.png")
    else:
        raise Exception("No solution found")
    
    
if __name__ == "__main__":
    

    main()