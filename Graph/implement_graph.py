#Implementation of Graph
import queue

class Graph:
 node_lookup = {}


 class Node:
   adjacent = []
   def __init__(self,id):
     this.id = id

 def get_node(self, id):
   return node_lookup.get(id)

 def add_edge(self, source, dest):
   s = self.get_node(source)
   d = self.get_node(dest)

   s.adjacent.append(d)

 def has_path_dfs(self, source, dest):
    s = self.get_node(source)
    d = self.get_node(dest)
    visited = set()
    return self.has_path_dfs_helper(source, dest, visited)

 def has_path_dfs_helper(self, source, dest, visited):
   visited.add(source.id)
   if source == dest:
     return True

   for node in source.adjacent:
     if node.id not in visited:
       self.has_path_dfs_helper(node, dest, visited)

   return False

 def has_path_bfs(self, source, dest):
   q = queue.Queue(maxsize=20)
   q.put(source)

   visited = set()

   while not q.empty():
     current_node = q.get()
     if current_node.id in visited:
       continue

     if current_node == dest:
       return True

     visited.add(current_node.id)

     for child in current_node.adjacent:
       q.put(child)



   return False
