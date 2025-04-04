#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Banker's Algorithm in Python

# Number of processes and resources
n = 5  # Number of processes
m = 3  # Number of resources

# Available resources
available = [3, 3, 2]

# Maximum demand of each process
max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

# Allocated resources to each process
allocated = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Calculate the need matrix
need = [[max_demand[i][j] - allocated[i][j] for j in range(m)] for i in range(n)]

# Function to check if the system is in a safe state
def is_safe(processes, available, allocated, need):
    work = available.copy()
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for p in range(n):
            if not finish[p] and all(need[p][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocated[p][j]
                safe_sequence.append(p)
                finish[p] = True
                found = True
        if not found:
            return False, []
    return True, safe_sequence

# Check if the system is in a safe state
safe, sequence = is_safe(n, available, allocated, need)
if safe:
    print("System is in a safe state. Safe sequence:", sequence)
else:
    print("System is not in a safe state.")


# In[2]:


if __name__ == "__main__":
    # P0, P1, P2, P3, P4 are the Process names here
    n = 5  # Number of processes
    m = 3  # Number of resources

    # Allocation Matrix
    alloc = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # MAX Matrix
    max_demand = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    avail = [3, 3, 2]  # Available Resources

    f = [0] * n  # Initialize finish flags
    ans = [0] * n  # To store the safe sequence
    ind = 0  # Index for ans array

    # Initialize finish flags to 0 (False)
    for k in range(n):
        f[k] = 0

    # Calculate the need matrix (max - allocated)
    need = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max_demand[i][j] - alloc[i][j]

    # Find a safe sequence
    y = 0
    for k in range(5):
        for i in range(n):
            if (f[i] == 0):
                flag = 0
                for j in range(m):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break

                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    print("Following is the SAFE Sequence")
    for i in range(n - 1):
        print(f" P{ans[i]} ->", end="")
    print(f" P{ans[n - 1]}")


# In[ ]:




