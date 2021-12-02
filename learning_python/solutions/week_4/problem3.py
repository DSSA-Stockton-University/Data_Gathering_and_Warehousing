# Problem 3 - Delegating Iteration to an Internal Container
# ===== Instructions:
# The following code creates container object (Called Node) that internally holds a list
# You would like to add a method to make iteration work with your new container.
# All you need to do is define a method called __iter__() that delegates iteration to
# the internally held container (called _children). In this case, the __iter__() method simply forwards the 
# iteration request using the built-in function called iter() to the internally held _children attributes
# You are not allowed to import external libraries
# Any libraries you may need are imported for you already from the python standard library.

class Node:
   def __init__(self, value):
      self._value = value
      self._children = [] # <- the internally held list

   def __repr__(self):
      return 'Node({!r})'.format(self._value)

   def add_child(self, node):
      self._children.append(node)

   def __iter__(self):
      """INSERT YOUR CODE HERE"""
      return iter(self._children)

def main():
   # Initialize a few containers
   root = Node(0)
   child1 = Node(1)
   child2 = Node(2)

   # Add the subsequent containers to the first container as a child
   root.add_child(child1)
   root.add_child(child2)

   # interate each container from the internally held list
   for child in root:
      print(child)
   

   
if __name__ == '__main__':
   # main execution
   main()

