class Node():
  def __init__(self, data, adjacency_list=None):
    self.data = data
    self.adjacency_list = adjacency_list or []
    self.visited = False
  
  def add_edge_to(self, node):
    self.adjacency_list += [node]

  def __str__(self):
    return self.data

class Queue():
  def __init__(self):
    self.array = []
  
  def add(self, item):
    self.array.append(item)
  
  def remove(self):
    if not len(self.array):
      return None
    item = self.array[0]
    del self.array[0]
    return item

def route_between_nodes(n1,n2):
  q=Queue()
  n1.visited=True
  q.add(n1)
  curr=q.remove()
  while curr:
    print(curr)
    for i in curr.adjacency_list:
      if i.visited==False:
        if i==n2:
          return True
        else:
          q.add(i)
        i.visited=True
    curr=q.remove()
  return False

node_j = Node('J')
node_i = Node('I')
node_h = Node('H')
node_d = Node('D')
node_f = Node('F', [node_i])
node_b = Node('B', [node_j])
node_g = Node('G', [node_d, node_h])
node_c = Node('C', [node_g])
node_a = Node('A', [node_b, node_c, node_d])
node_e = Node('E', [node_f, node_a])
node_d.add_edge_to(node_a)

print(route_between_nodes(node_a,node_g))
