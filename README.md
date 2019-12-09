# Missionaries and Cannibals Problem 

> In the missionaries and cannibals problem, three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). The boat cannot cross the river by itself with no people on board. And, in some variations, one of the cannibals has only one arm and cannot row.[[1]](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem#cite_note-PressmanSingmaster-1)

I'll be using BFS and DFS to find the solution space tree for Missionaries and Cannibal Problem. To build the tree I'll be using [pydot](https://github.com/pydot/pydot) which is a Python binder for [graphviz](https://www.graphviz.org/download/).

## Requirements
```
graphviz
emoji==0.5.4
pydot==1.4.1
pyparsing==2.4.5
```

Download graphviz https://www.graphviz.org/download/

### How to run

 - Download [graphviz binary](https://www.graphviz.org/download/) 
 - Open solve.py and  update  the directory to point graphviz bin directory
```
# Set it to bin folder of graphviz
os.environ["PATH"] += os.pathsep +  'C:/Program Files (x86)/Graphviz2.38/bin/'
``` 
 - For dfs run
```
python main.py -m dfs
  ``` 
  
 - For bfs run
 ```
python main.py -m bfs
  ``` 
 - The state space tree are saved as **bfs.png** and **dfs.png** in the current directory.

### Note:
You can change the order of following line inside solve.py to get different solution space tree. 
```
self.options = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0),]
```
### Issue:
Windows cmd doesnt support emoji as of now. Try running on bash or terminal to see the graphics properly.

## Screenshots
### 1. BFS
![BFS](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/solutionbfs.JPG)
---

### 2. BFS Tree
![BFS Tree](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/bfs.png)
---

### 3. DFS
![DFS](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/solution1.JPG)
---

### 4. DFS Tree
![DFS Tree](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/dfs.png)
