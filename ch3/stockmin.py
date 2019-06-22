class MinStack():
  def __init__(self):
    self.top, self._min = None, None
    
  def min(self):
    if not self._min:
      return None
    return self._min.data
    
  def push(self, item):
    if self._min and (self._min.data < item):
      self._min = Node(data=self._min.data, next=self._min)
    else:
      self._min = Node(data=item, next=self._min)
    self.top = Node(data=item, next=self.top)
  
  def pop(self):
    if not self.top:
      return None
    self._min = self._min.next
    item = self.top.data
    self.top = self.top.next
    return item

class Node():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
 


