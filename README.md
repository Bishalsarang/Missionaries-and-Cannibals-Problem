
# Missionaries and Cannibals Problem 

> In the missionaries and cannibals problem, three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). The boat cannot cross the river by itself with no people on board. And, in some variations, one of the cannibals has only one arm and cannot row.[[1]](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem#cite_note-PressmanSingmaster-1)

Table of contents
=================

<!--ts-->
   * [Problem Statement](#missionaries-and-cannibals-problem)
   * [Table of contents](#table-of-contents)
   * [Requirements](#requirements)
   * [Usage](#usage)
	   * [Generate State Space Tree](#generate-state-space-tree)
	   * [Generate DFS Tree](#generate-dfs-tree)
	   * [Generate BFS Tree](#generate-bfs-tree)
   * [Screenshots](#screenshots)
	   * [State Space Tree Depth 8](#state-space-tree-with-depth-8)
	   * [State Space Tree Depth 20](#state-space-tree-with-depth-20)
	   * [State Space Tree Depth 40](#state-space-tree-with-depth-40)
	   * [Legends](#legends)
	   * [BFS Solution](#bfs)
	   * [BFS Tree](#bfs-tree)
	   * [BFS Tree with Legends](#bfs-tree-with-legends)
	   * [DFS Solution](#dfs)
	   * [DFS Tree](#dfs-tree)
	   * [DFS Tree with Legends](#dfs-tree-with-legends)
	
<!--te-->
In this repo I'll be building state space tree upto certain depth and use BFS and DFS to find the solution space tree for Missionaries and Cannibal Problem. To build the tree I'll be using [pydot](https://github.com/pydot/pydot) which is a Python wrapper  for [graphviz](https://www.graphviz.org/download/).

## Requirements
```
emoji==0.5.4
pydot==1.4.1
```

Graphviz Binary
Download graphviz https://www.graphviz.org/download/

## Usage

 - Download [graphviz binary](https://www.graphviz.org/download/) 
 - Open solve.py and  update  the directory to point graphviz bin directory
```
# Set it to bin folder of graphviz
os.environ["PATH"] += os.pathsep +  'C:/Program Files (x86)/Graphviz2.38/bin/'
``` 
- Install all the requirements
```
pip install -r requirements.txt
  ``` 
  ### Generate State Space Tree
```
python generate_full_space_tree.py -d 20
 ```
 where d is the depth.
  ### Generate DFS Tree
 - For dfs without legends on graph run
```
python main.py -m dfs
 ```
 
- For dfs with legends on graph run
```
python main.py -m dfs -l True
 ``` 
 ### Generate BFS Tree
 - For bfs without legends on graph run
 ```
python main.py -m bfs
  ``` 
  - For bfs with legends on graph run
```
python main.py -m bfs -l True
 ```

 - The state space tree are saved as **bfs.png** and **dfs.png** or **bfs_legend.png** and **dfs_legend.png**  or state_space{depth}.png in the current directory.
 The solution moves are displayed on console as in [solution](#bfs).

### Note:
You can change the order of *self.options* following line inside solve.py  or *options* inside generate_full_space_tree.py  to get different state space tree. 
```
self.options = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0),]
```
### Issue:
Windows cmd doesnt support emoji as of now. Try running on bash or terminal to see the graphics properly.

## Screenshots

### State Space Tree with Depth 8
![State Space Tree_8](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/state_space_8.png)
---

### State Space Tree with Depth 20
![BFS](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/state_space_20.png)
---
### State Space Tree with Depth 40
![BFS](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/state_space_40.png)
---
### Legends
![BFS](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/legend.JPG)
---
###  BFS
![BFS](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/solution_bfs.JPG)
---

### BFS Tree
![BFS Tree](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/bfs.png)
---

### BFS Tree with legends
![BFS Tree](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/bfs_legend.png)
---

### DFS
![DFS](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/solution_dfs.JPG)
---

### DFS Tree
![DFS Tree](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/dfs.png)
---

### DFS Tree with Legends
![BFS Tree](https://github.com/sarangbishal/Missionaries-and-Cannibals-Problem/blob/master/assets/dfs_legend.png)
---
