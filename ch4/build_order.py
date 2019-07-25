def build_order(projects, dependencies):
  nodes = {}
  for project in projects:
    nodes[project] = GraphNode(project)

  for dependency in dependencies:
    nodes[dependency[0]].add_edge(nodes[dependency[1]])

  #找出沒有起始點的
  queue = []
  for project in projects:
    node = nodes[project]
    if not node.dependencies_left:
      queue.append(node)
  
  build_order = []
  #若沒起始點 則加入order
  while queue:
    node = queue.pop(0)
    build_order.append(node.data)
    for dependent in node.edges:
      dependent.dependencies_left -= 1
      if not dependent.dependencies_left:
        queue.append(dependent)

  if len(build_order) < len(projects):
    return Exception("Cycle detected")
  return build_order

class GraphNode():
  def __init__(self, data):
    self.data = data
    self.edges = []
    self.dependencies_left = 0
    
  def add_edge(self, node):
    self.edges.append(node)
    node.dependencies_left += 1



projects = ["A", "B", "C", "D", "E", "F", "G"]
dependencies1 = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
    ("A", "E"), ("B", "E"), ("D", "G")]
print(build_order(projects, dependencies1))
    #["D", "F", "G", "B", "C", "A", "E"])
