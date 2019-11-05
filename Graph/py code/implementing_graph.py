#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Implementing Graph using Adjacency List
from IPython.display import Image
Image("graph.png")


# In[6]:


# Initializing a class that will create a Adjacency Node.
class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None


# In[15]:


# A class to represent the graph
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None] * self.V
        
# Function to add an EDGE to the undirected graph
   # Adding the node to the source
    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        
    # Adding the node to the Destination (since it is undirected graph)
    
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
        
# Function to print the Graph
    def printGraph(self):
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 


# In[16]:


# Driver Program 
V = 5
graph = Graph(V)
graph.addEdge(0, 1) 
graph.addEdge(0, 4) 
graph.addEdge(1, 2) 
graph.addEdge(1, 3) 
graph.addEdge(1, 4) 
graph.addEdge(2, 3) 
graph.addEdge(3, 4) 
  
graph.printGraph()


# In[ ]:


# stay Tuned :)

