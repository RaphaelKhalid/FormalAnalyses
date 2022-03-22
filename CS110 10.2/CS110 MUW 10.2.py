#!/usr/bin/env python
# coding: utf-8

# # Preclass work

# In[1]:


class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.data = val

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        """
        Insert a node/ value of the node into the tree

        Parameters
        ----------
        node: Node/ int
            the node or the value of the node

        Returns
        ----------
        None
        """

        if type(node) is int: 
            node = Node(node)

        if self.root is None:
            self.root = node
            return
        else:
            self._insert_node(node, self.root)

    def _insert_node(self, node, root):
        """
        Insert a node into an existing subtree

        Parameters
        ----------
        root: Node
            the root of the subtree
        node: Node
            the node to be inserted

        Returns
        ----------
        None
        """
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
                node.parent = root
            else:
                self._insert_node(node, root.l_child)
        else:
            if root.r_child is None:
                root.r_child = node
                node.parent = root
            else:
                self._insert_node(node, root.r_child)


# Question 1
# Below you are provided the code for insertion in an AVL tree. However, to make it work, you need to complete the function right_rotate. Use the pseudo-code LEFT-ROTATE in Cormen et al. as well as the Python implementation above to motivate your right_rotate code.

# In[2]:


class AVLNode(Node):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.data = val
        self.lr_balance = 0
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_violating_node(self, node):
        if not self.root or node == self.root:
            return None
        if node == node.parent.r_child:
            if not node.parent.l_child:
                node.parent.height = max(-1, node.height) + 1
                node.parent.lr_balance = -1-node.height
            else:
                node.parent.height = max(node.parent.l_child.height, node.height) + 1
                node.parent.lr_balance = node.parent.l_child.height-node.height
        else:
            if not node.parent.r_child:
                node.parent.height = max(-1, node.height) + 1
                node.parent.lr_balance = node.height + 1
            else:
                node.parent.height = max(node.parent.r_child.height, node.height) + 1
                node.parent.lr_balance = node.height-node.parent.r_child.height
        if abs(node.parent.lr_balance) > 1:
            return node.parent
        else:
            return self.get_violating_node(node.parent)
                

    def insert(self, node):
        """inserts a node into a AVL Tree"""
        if not self.root:
            self.root = node
            return

        violating_node = None
        curr_node = self.root
        root = self.root
        while curr_node:
            if curr_node.data > node.data:
                if curr_node.l_child is None:
                    curr_node.l_child = node
                    node.parent = curr_node
                    break
                else:
                    curr_node = curr_node.l_child 
            else:   
                if curr_node.r_child is None:
                    curr_node.r_child = node
                    node.parent = curr_node
                    break
                else:
                    curr_node = curr_node.r_child
        # fix up the tree
        violating_node = self.get_violating_node(node)
        
        while violating_node:
            x = violating_node
            if x.lr_balance < 0: # right heavy
                y = x.r_child
                if y.lr_balance < 0:
                    root = left_rotate(x, root)
                    x.lr_balance = 0
                    x.height -= 2
                    y.lr_balance = 0
                elif y.lr_balance == 0:
                    root = left_rotate(x, root)
                    x.lr_balance = -1
                    x.height -= 1
                    y.lr_balance = 1
                    y.height += 1 
                else:
                    z = x.r_child
                    y = z.l_child
                    root = right_rotate(z, root)
                    root = left_rotate(x, root)
                    x.height -= 2
                    y.lr_balance = 0
                    y.height += 1
                    z.height -= 1 
                    if y.lr_balance == -1: 
                        x.lr_balance = 1
                        z.lr_balance = 0
                    elif y.lr_balance == 0: 
                        x.lr_balance = 0
                        z.lr_balance = 0
                    else: 
                        x.lr_balance = 0
                        z.lr_balance = -1 
       
            else:
                y = x.l_child
                if y.lr_balance > 0:
                    root = right_rotate(x, root)
                    x.lr_balance = 0
                    x.height -= 2
                    y.lr_balance = 0
                elif y.lr_balance == 0:
                    root = right_rotate(x, root)
                    x.lr_balance = 1
                    x.height -= 1
                    y.lr_balance = -1
                    y.height += 1
                else:
                    z = x.l_child 
                    y = z.r_child
                    root = left_rotate(z, root)
                    root = right_rotate(x, root)
                    x.height -= 2
                    y.lr_balance = 0
                    y.height += 1
                    z.height -= 1
                    if y.lr_balance == -1: # B: k-2, C: k-1
                        x.lr_balance = 0
                        z.lr_balance = 1
                    elif y.lr_balance == 0: # B=C=k-1
                        x.lr_balance = 0
                        z.lr_balance = 0
                    else: # B: k-1, C: k-2
                        x.lr_balance = -1
                        z.lr_balance = 0
            if root == y: 
                violating_node = None
                continue
            elif y == y.parent.l_child:
                y.parent.lr_balance = y.height - y.parent.r_child.height
                y.parent.height = max(y.height, y.parent.r_child.height) + 1
            elif y == y.parent.r_child:
                y.parent.lr_balance = y.parent.l_child.height - y.height
                y.parent.height = max(y.parent.l_child.height, y.height) + 1
            if abs(y.parent.lr_balance) > 1:
                violating_node = y.parent
            else: violating_node = None 

        self.root = root
        return root
    
def left_rotate(x, root):
    """Performs left-rotation on x, returns the root.
    This procedure does NOT update any augmented data (if any)
    of the nodes (e.g., height, left-right balance, etc.), simply
    changing the pointers and the parent-child relationship,
    and setting the new root (if any). The updating task belongs to 
    the procedure that calls this function.
    
    Input:
    - x: a node, to be performed the rotation on
    - root: the root node of the tree.
    
    Output:
    - root: the (new) root of the tree
    """
    y = x.r_child
    x.r_child = y.l_child
    if not y.l_child is None:
        y.l_child.parent = x
    y.parent = x.parent
    if not x.parent:
        root = y
    elif x == x.parent.l_child:
        x.parent.l_child = y
    else:
        x.parent.r_child = y
    y.l_child = x
    x.parent = y
    return root

def right_rotate(y, root):
    """Performs right-rotation on x, returns the root.
    This procedure does NOT update any augmented data (if any)
    of the nodes (e.g., height, left-right balance, etc.), simply
    changing the pointers and the parent-child relationship,
    and setting the new root (if any). The updating task belongs to 
    the procedure that calls this function.
    
    Input:
    - x: a node, to be performed the rotation on
    - root: the root node of the tree.
    
    Output:
    - root: the (new) root of the tree
    """
    x = y.l_child
    y.l_child = x.r_child
    if not x.r_child is None:
        x.r_child.parent = y
    x.parent = y.parent
    if not y.parent:
        root = x
    elif y == y.parent.r_child:
        y.parent.r_child = x
    else:
        y.parent.l_child = x
    x.r_child = y
    y.parent = x
    return root
    


# Question 2
# Complete the function height to compute the height of a tree rooted at a node. This should also be a matter of copying and pasting because you can utilize what you wrote for max_depth in lesson "Randomly built BSTs" (recall that maximum depth of a tree rooted at a node is the node's height in the tree.)

# In[7]:


import random
import numpy as np
import matplotlib.pyplot as plt


def height(node):
    """Finds the height of a BST rooted at a node.
    
    Input:
    - node: a node, the root of the BST
    
    Output:
    - h: int, the height of the BST"""
    
    
    #Base case
    if node == None:
        return -1
    
    #Find heights of left/right trees
    l = height(node.l_child)
    r = height(node.r_child)
    

    
    if l > r:
        return l + 1
    else:
        return r + 1


# Question 3
# Fill in the get_expected_height_stats function below to get the data ready for plotting. You need to follow the template code and the following steps to produce consistent data to plot. The missing step is step number 4. All the other steps have already been coded for you. 

# In[8]:


import random 

def get_expected_height_stats(iterations):
    """Generate the data for plotting the expected heights of BST and AVL.
    
    Input:
    - iterations: int, the number of times to insert into the tree for each 
    value of the number of nodes to insert. For each iteration, a height is 
    computed. After all the iterations, all the computed heights are averaged
    to get an estimate of the expected height. 
    
    Output:
    - bst_expected_heights, avl_expected_heights: list of float, containing
    the expected heights for the two types of trees. Each element in each list
    corresponds to one value of N, the number of nodes in the tree. The values 
    of N are taken from range(1, 500, 10) (i.e., 1, 11, 21, 31, etc.)"""
    bst_expected_heights = []
    avl_expected_heights = []
    
    for N in range(1, 500, 10):
        bst_heights = []
        avl_heights = []
        for trial in range(iterations):
            bst = BinarySearchTree() 
            avl = AVLTree()
            
            vals = list(range(int(N)))
            random.seed(trial) #for reproducibility
            random.shuffle(vals)
            
            BSTnodes = [Node(val) for val in vals]
            AVLnodes = [AVLNode(val) for val in vals]
            # insert nodes below
            for node in BSTnodes:
                bst.insert(node)
            for node in AVLnodes:
                avl.insert(node)
            # compute the resulting tree heights here
            bst_heights.append(height(bst.root))
            avl_heights.append(height(avl.root))
            # compute the average heights
        bst_expected_heights.append(np.sum(bst_heights)/iterations)
        avl_expected_heights.append(np.sum(avl_heights)/iterations)
    return bst_expected_heights, avl_expected_heights


bst_expected_heights, avl_expected_heights = get_expected_height_stats(10)

assert(bst_expected_heights == [0.0, 5.3, 6.8, 7.8, 9.9, 10.2, 9.9, 11.2, 12.0, 12.2, 12.3, 
                                12.2, 12.1, 13.4, 13.2, 13.0, 14.3, 14.7, 13.8, 14.1, 14.5, 
                                15.5, 14.9, 16.0, 16.1, 16.2, 15.4, 17.5, 16.7, 16.1, 16.4, 
                                17.4, 16.1, 17.3, 16.8, 16.2, 16.7, 17.5, 17.1, 18.4, 17.5, 
                                17.0, 17.8, 18.4, 18.3, 17.8, 17.7, 17.3, 18.0, 19.5])
assert(avl_expected_heights == [0.0, 3.0, 4.1, 5.0, 5.4, 6.0, 6.0, 6.1, 6.8, 6.9, 7.0, 7.0, 
                                7.3, 7.3, 7.5, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.2, 8.2, 8.0, 
                                8.4, 8.5, 8.7, 8.8, 8.9, 8.8, 8.9, 9.0, 9.0, 9.0, 9.0, 9.0, 
                                9.0, 9.0, 9.3, 9.1, 9.1, 9.3, 9.3, 9.7, 9.5, 9.6, 9.8, 9.8, 
                                9.9, 9.8])


# Question 4
# If you have done everything correctly, running the following code will produce a plot that compares the expected heights of a BST and an AVL tree. 

# In[9]:


bst_expected_heights, avl_expected_heights = get_expected_height_stats(10)

plt.plot(range(1,500,10), bst_expected_heights, color = 'red',label = 'BST', linewidth = 1.0)
plt.plot(range(1,500,10), avl_expected_heights, color = 'blue',label = 'AVL', linewidth = 1.0)
plt.xlabel('$N$', fontsize=10)
plt.ylabel('Expected height', fontsize=10)
plt.legend()


# Question 5 
# Comment on the results above, making explicit application of #ComputationalCritique in no less than 50 words. Please include a word count. This is excellent practice for assignment questions---do not rush this question please. 

# Two features are of note: the graph for AVLs has a lower expected height over all N compared to BSTs i.e. closer to O(logn) for tree operations like look up, the graph of BSTs are more variable over different N with spikes and dips, meaning AVL's are the more reliable option when interested in balanced trees. (56 words)

# # Polls
# 
# ### Prep poll D
# Contrast AVL trees and RB trees. In which situations might one prefer one over the other? Justify your answer and be as specific as possible.
# 
# AVL trees are to be preferred when we are interested in maintaining a single data structure with few expected changes, because AVLs are more balanced than RB trees the lookup operations which take O(logn) time will be more efficient. But if we want to maintain a database where we consistently add nodes, then RB trees are better because the need to left/right rotate in AVLs everytime a node is added to maintain the tree property is computationally expensive.
# 
# ### Reflection Poll
# Red-black trees are guaranteed to be more balanced than heaps. This suggests that RBTs are better than heaps._ Do you agree or disagree with this statement? Explain your answer. Give as many examples as you can of operations that are more efficient with one of these data structures but less efficient than with the other.
# 
# It depends, if we want to use searching operations consistently than RBTs are better since they have run in O(logn) time compared to heaps which have O(n) time to look up an item, but if we want to access particular kinds of elements such as the root element then that is better in heaps (e.g. running median problem) which can be done in O(1) time compared to RBTs where their structure does not support an obvious implementation of accessing the root node.
# 
# # Summary
# 
# The most insightful discussion in class was after the prep poll where we dug into AVLs, first Yousaf offered an explanation which was then built upon by Gisele and the common understanding was reached that for AVLs each node's left and right child subtrees can only differ by a depth of 1 at most, which then led into the discussion about how to implement this in Python. Here, Krithik offered the suggestion of a left-right balance attribute and Dee explained the more primary attribute necessary for this which is depth that needs to be tracked across all nodes in order to pair it with the left/right rotation methods for when the rule is violated. Other useful discussion in class included comparisons of AVLs with red black trees and how in the latter the possible worst case where there are all black nodes on one subtree and alternating ones on the other one mean that the maximum depth difference could be 2x, compared to the maximum depth difference of AVLs as only by 1 which leads to better balance and therefore quicker operations like lookup. Finally there were also comparisons of AVLs with heaps and their specific use cases like priority queues were also discussed.
# 
# 
# 

# # New polls
# 
# Prep poll: Consider the inorder traversal operation for AVLs, what function can it serve and is it different compared to RBTs or BSTs?
# 
# This is a good way to link the understanding of the previous kinds of trees that we learned about to a new context and also tests understanding of the study guide where this concept is discussed.
# 
# #datastructures: Tests the understanding of a specific operation in the context of AVLs and how it is no different compared to the others.
# 
# Answer: The inorder traversal operation for AVLs will output a sorted list just like for RBTs and BSTs which means that it is no different in the function it serves and this is because the binary search tree invariant/property is still maintained, that no node has a left child which is larger than it or a right child which is smaller than it.
# 
# Reflection poll: Based on discussion from class, what are the most important considerations when implementing AVLs in Python? Make sure to justify your answer.
# 
# This is ties to the discussion of important aspects of AVL nodes and tree classes in python as discussed in class
# 
# Answer: The first consideration is having an attribute which keeps track of depth because this is needed to maintain the AVL invariant i.e. no node can have a left or right subtree whose depth differs by more than one, and this can then be paired with a maximum balance factor attribute and whenever this is violated, the left and right rotate methods will be helpful in fixing the violations.
# 
# #pythonprogramming: Tests the understanding of classes, attributes, and methods as they relate to AVLs

# In[ ]:




