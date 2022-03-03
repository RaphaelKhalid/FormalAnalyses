#!/usr/bin/env python
# coding: utf-8

# ### Pre-Class Work

# ##### Q1. Read through the following Python code. What does each function (i.e., qsort, randomized_quicksort, test_quicksort) do? Explain your answer as carefully as you can. Use these insights to include docstrings in the code cells below.

# In[4]:


import time
import numpy as np
import random
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
get_ipython().run_line_magic('matplotlib', 'inline')

def qsort(lst, pivot_relative_location):
    """
    Implements iterative version of quicksort

    Parameters
    ----------
    lst : Python list or numpy array
    locations : int
        relative location of the pivot with respect to the input list
        should vary between 0 and 0.5

    Returns
    -------
    array: a sorted Python list

    """
    # initialising the indices list
    indices = [(0, len(lst))]
    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue
        N = to - frm
        # choose the pivot from pivot_relative_location
        pivot = lst[frm + int(N * pivot_relative_location)]
        # split into 3 partitions
        lower = [a for a in lst[frm:to] if a < pivot]
        upper = [a for a in lst[frm:to] if a > pivot]
        counts = sum([1 for a in lst[frm:to] if a == pivot])
        # record the indices that signal the end/start of the partitions
        ind1 = frm + len(lower)
        ind2 = ind1 + counts
        # push back into the correct place
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [pivot] * counts
        lst[ind2:to] = upper
        # enqueue other locations to keep sorting the remaining array
        indices.append((frm, ind1))
        indices.append((ind2, to))
    return lst

def randomized_quicksort(N, pivot_location):
    lst = [i for i in range(N)]
    random.shuffle(lst)
    return qsort(lst, pivot_location)


def test_quicksort(N, pivot_location):
    lst = randomized_quicksort(N, pivot_location)
    assert (lst == [i for i in range(N)])


# Qsort is the iterative version of the recursive quicksort we did in the previous session. The main difference is that we have 3 partitions being made, the left and right partitions are still following the rules that they are $\le$ and $\ge$ to the pivot respectively, but the middle partition is just the sum of all instances of the pivot for e.g. if your pivot is 5, and 5 shows up in the list 3 times, then the middle partition will be 3. Another difference is that the selected pivot is going to be a relative position i.e. rather than selecting the final element as the default pivot, if the pivot_relative_location argument is 0.4 for example, the pivot will be ~40% of the way along the list implying a 40:60 ratio of the left and right partitions.
# 
# Randomized quicksort implements qsort from above but shuffles the list of N consecutive integers before selecting the pivot based on the pivot_relative_location rule. And test quicksort asserts whether the randomized quick sort function returns the sorted version of the shuffled list which is the intended behavior.

# ##### Q2. What are the main differences between the randomized_quicksort in the code and RANDOMIZED-QUICKSORT in Cormen et al.? Explain your answer.

# The obvious difference is that randomized_quicksort relies on the iterative implementation of the quicksort algorithm rather than the recursive one which used two recursive calls to itself and also used an auxillary function i.e. partition. The other difference is the method of randomization: the RANDOMIZED-QUICKSORT uses the auxillary function RANDOMIZED-PARTITION which selects a random pivot rather than shuffling the list and selecting a given pivot which is what the code above does. The code above has an advantage in that it ensures a middle partition relying on randomizing the underlying distribution of the list, whereas Cormen et al. relies on the underlying distribution of the list while randomizing the pivot which may or may not ensure even partition splits.

# ##### Q3. What is the time complexity of this randomized_qsort if you use the middle of the list to consecutively split the array (in other words, pivot_location=0.5)? Time the algorithm on lists of various lengths, each list being a list of the first $n$ consecutive positive integers. Produce a graph with list lengths on the x axis and running time on the y axis. As always, don’t forget to time the algorithm several times for each list’s length and then average the results.
# 
# 
# 
# Note: this scenario corresponds to choosing the median, given that the array is originally sorted.

# Based on the experiment below where input sizes increase by 2 all the way from 1 to 2^14 with 100 trials, the average runtime of randomize_quicksort is seemingly linear i.e. as input size increases by a factor of 2, so does the runtime which implies a big O notation of O(n).

# In[6]:


trials = 100
inputsize = [2**k for k in range (15)]
times = []
for N in inputsize:
    trial_time = 0
    for i in range(trials):
        start = time.time()
        randomized_quicksort(N, 0.5)
        end = time.time()
        trial_time += (end-start)
    times.append(trial_time/trials)


# In[17]:


plt.figure()
plt.xlabel('Input Size')
plt.ylabel('Runtime (s)')
sns.lineplot(x=inputsize,y=times)
plt.show()


# ##### Q4. Now, instead of using the middle element, what happens to the efficiency of the algorithm if you systematically just use the first element in the array? Justify your response and complement it with a graph.
# 
# 

# The efficiency remains the same i.e. linear runtime and this is to be expected because we aren't randomizing the pivot, rather the list itself so whether the pivot location is 0.5 or 0, it won't make a difference on the average partition ratios.

# In[20]:


trials = 100
inputsize = [2**k for k in range (15)]
times = []
for N in inputsize:
    trial_time = 0
    for i in range(trials):
        start = time.time()
        randomized_quicksort(N, 0)
        end = time.time()
        trial_time += (end-start)
    times.append(trial_time/trials)


plt.figure()
plt.xlabel('Input Size')
plt.ylabel('Runtime (s)')
sns.lineplot(x=inputsize,y=times)
plt.show()

