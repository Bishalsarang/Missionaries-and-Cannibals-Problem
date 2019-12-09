from solve import Solution

def main():
    s = Solution()
    if(s.solve("dfs")):
        s.show_solution()
    else:
        print("No")
    
    
if __name__ == "__main__":
    main()