#!/usr/bin/env python
# coding: utf-8

# # Pre-class work

# ## Question 1
# 
# Edge List: [[0,1],[0,6],[0,8],[1,4],[1,6],[1,9],[2,4],[2,6],
# [3,4],[3,5],[3,8],[4,5],[4,9],[7,8],[7,9]]
# 
# Adjacency Matrix:
# $\begin{bmatrix}
# 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0\\
# 1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 1\\
# 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0\\
# 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 0\\
# 0 & 1 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1\\
# 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0\\
# 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
# 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1\\
# 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0\\
# 0 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0\\
# \end{bmatrix}$
# 
# 
# Adjacency List:[[1,6,8],[0,4,6,9],[4,6],[4,5,8],[1,2,3,5,9],[3,4],[0,1,2],[8,9],[0,3,7],[1,4,7]]
# 
# 

# ## Question 2
# i) D,B,H,E,I,A,F,C,J,G,K
# 
# ii) A,B,D,E,H,I,C,F,G,J,K
# 
# iii) D,H,I,E,B,F,J,K,G,C,A
# 
# iv) A,B,C,D,E,F,G,H,I,J,K

# ## Question 3
# 
# For the depth first search we will first look at G and then keep going until there is no child node and we have to back track so its : A, G, E, B, F, C, H
# Then backtracking we will go to D giving a final:
#  A, G, E, B, F, C, H
#  
#  
# For breadth first search we look at the immediate neighbours first:
# 
# A, B, D, E, G
# 
# Continuing now we go and check F, then C then H giving the following
# 
# A, B, D, E, G, F, C, H
# 

# ## Question 4

# In[6]:


class Graph:
	def __init__(self, n):
		self.adjacency_matrix = [[] for _ in range(n)]


	def add_directed_edge(self, from_node, to_node):
		""" 
		Create a directed edge between the starting node and ending node value
		Parameters
		---------- 
			from_node: int
				the starting node of an edge
			to_node: int
				the ending node of an edge
		Returns
		----------
			None
		"""
		self.adjacency_matrix[from_node].append(to_node)

		return None
		
	def add_undirected_edge(self, node1, node2):
		""" 
		Create an undirected edge between the starting node and ending node value
		Parameters
		----------
			node1: int
				the first node
			node2: int
				the second node 
		Returns
		----------
			None
		"""
		self.adjacency_matrix[node1].append(node2)
		self.adjacency_matrix[node2].append(node1)
		return None

cityGraph = Graph(10)
# adding directed edges (unique direction)
cityGraph.add_directed_edge(0, 2)
cityGraph.add_directed_edge(3, 5)
cityGraph.add_directed_edge(2, 8)
cityGraph.add_directed_edge(1, 6)
cityGraph.add_directed_edge(7, 9)
cityGraph.add_directed_edge(8, 1)

# adding undirected edges (double direction)
cityGraph.add_undirected_edge(1, 2)
cityGraph.add_undirected_edge(4, 6)
cityGraph.add_undirected_edge(3, 4)
cityGraph.add_undirected_edge(1, 9)



assert (cityGraph.adjacency_matrix == [[2], [6, 2, 9], [8, 1], [5, 4], [6, 3], [], [4], [9], [1], [1]])


# In[7]:


edges = [[0,1],[0,6],[0,8],[1,4],[1,6],[1,9],[2,4],[2,6], [3,4],[3,5],[3,8],[4,5],[4,9],[7,8],[7,9]]

testGraph = Graph(10)

for edge in edges:
    testGraph.add_undirected_edge(edge[0],edge[0])
    
testGraph.adjacency_matrix


# ## Question 5

# In[8]:


class Lesson:
    '''
    Generates a Lesson and respective dependencies

    Attributes
    ----------
    name: string
        Lesson name
    depends: list
        Dependencies of Lesson


    '''
    def __init__(self, name):
        self.name = name
        self.depends = []

    def requires(self, node):
        '''
        Adds nodes to dependency list for a Lesson
        
        Parameters
        ----------
        node: string
            Name of dependency
            
        Returns
        -------
        None
        
        '''
        self.depends.append(node)
        return None


# In[9]:


big_o = Lesson("Big O notation")
binary_trees = Lesson("Binary Search Trees")
complexity = Lesson("Complexity")
dynamic_p = Lesson("Dynamic Programming")
heaps = Lesson("Heaps")
heapsort = Lesson("Heap Sort")
mergesort = Lesson('Merge Sort')
quicksort = Lesson("Quicksort")
randomization = Lesson('Randomization')
recursion = Lesson("Recursion")
iteration = Lesson("Iteration")
red_black = Lesson("Red Black trees")

# The dependencies our lessons have:
binary_trees.requires(recursion)
binary_trees.requires(complexity)
binary_trees.requires(heaps)
big_o.requires(complexity)
complexity.requires(recursion)
complexity.requires(iteration)
dynamic_p.requires(recursion)
dynamic_p.requires(complexity)
heaps.requires(recursion)
heaps.requires(complexity)
heapsort.requires(complexity)
heapsort.requires(recursion)
heapsort.requires(heaps)
mergesort.requires(complexity)
quicksort.requires(complexity)
quicksort.requires(recursion)
quicksort.requires(randomization)
quicksort.requires(mergesort)
randomization.requires(big_o)
randomization.requires(binary_trees)
red_black.requires(binary_trees)

# Our syllabus requires that we cover all lessons.
syllabus = [big_o, binary_trees, complexity, dynamic_p, heaps, heapsort, mergesort, 
               quicksort, randomization, red_black, recursion, iteration]

print('Syllabus loaded!')


# ## Question 6
# 
# 1. The nodes are the lessons and the edges represent if one lesson is dependent on another
# 
# 2. Directed graph which allows for lesson A to be dependent on lesson B without having lesson B dependent on A since that would be a circular dependency and we would have no course syllabus!
# 
# 3. Since we would want to start by looking at what the non-dependent course are i.e. ones with not out edges, we would want to use a post-order traversal.

# # Polls
# 
# ### Prep poll B: (started at 0:16:01)
# (1) Write the adjacency-list representation of the graph in the companion resource. (2) What type of graph is this?​Explain your answers to the questions above.
# 
# [[3,4],[4,7],[1,3,5],[4],[3,5],[2,6],[1],[6]]
# 
# This is a directed graph and the adjacency-list representation of the graph represents the nodes you can go to from a given node i.e. for the list above, list[0] indicates that you can go to nodes 3 and 4 from node 0. Importantly, this leaves out nodes that you come from but cannot go to e.g. list[5] = [2,6] but not including 4 since 4 goes to 5 but 5 cannot go to 4.
# 
# ### Reflection Poll: (started at 1:27:07)
# Based on the discussion in class today, explain why we might prefer one type of graph and tree traversal (BFS vs DFS) over another.
# 
# We might prefer directed graphs based on the context for example in the case of a CS110 Course Syllabus representation in the form of a graph, where you define edges as dependencies, you would want to have directed graphs to clarify which lesson is dependent on what. Similarly, context matters for tree traversal, based on Nastya's example of wanting to traverse through a seniority for escalation of issues, you would want to do BFS instead of DFS because BFS pertains to different levels of the tree.

# ## Summary
# Rhali made an insightful comment in the discussion of depth first search in Activity 1 at 42:51 that in depth first search you do not go back to a node which has already been covered which goes to show that any implementation of depth first search for graphs as a data structure need to ensure some form of running list that tracks which nodes have already been visited in order to avoid cases where you get stuck in circular paths, which is analogous to while loops without termination conditions or recursive algorithms with base cases. Ali then built on this at 47:01 where he discussed that stacks are a good data structure to use because they are last in first out which means that they can be used to store which nodes have been visited, but beyond that, they are capable to accomodating the depth first search algorithm such that you can backtrack once you have reached a node with no further new connections, and back tracking is implemented in Python, as discussed in class, using the pop method for the stack using simple lists, which is distinct from the queue data structure that requires a bit more complexity in implementing i.e. using an external library with deque.

# ## New polls
# 
# #### Prep poll: Consider a graph where the source node represents the CEO of a company, and the immediate nodes connected to the CEO are the executives, and those connected to the executives are managers and so on, representing a hierarchy in a company. Describe one scenario in which depth first search would be more appropriate and one where breadth first search would be more appropriate.  
# This would be a good start to thinking about applications of graphs beyond the example given in the PCW of the CS110 course guide, and help distinguish between the two algorithms and the concept behind how they work.
# 
# LO: #AlgorithmicStrategies because it asks students to describe two algorithms using examples.
# 
# Answer: Depth first search would be more appropriate when escalating issues from the lowest level where an employee might find something of importance that they think is relevant for the CEO to hear, this is because depth first search would allow you to get to the CEO in the least number of edges possible without having to run it by every single employee/manager/executive before that. BFS would be more appropriate when auditing a company where you would want to start by examining the CEO, then the usual suspects i.e. executives and move down each level from there.
# 
# #### Reflection poll: Based on the discussion in class today, explain the relevance of stacks and queues to implementing graphs and their search algorithms in Python.
# 
# This wraps up the session by integrating a data structure with python programming, based on class discussions.
# 
# LO: #DataStructures because it asks students to evaluate two data structures in the context of graphs.
# 
# Answer: Stacks are relevant for depth first search because of their last in first out structure which allows you to store the nodes you have already traversed and then lets you back track and check the children of ones that you have traversed after one call of the algorithm terminates. Queues are relevant for breadth first search because of their first in first out structure which supports the structure of traversing through the different levels in a graph such that you queue up a given level and move on only once the queue at the start is finished.
# 

# In[ ]:




