# Create node
class Node():
    def __init__(self, state, parent, action, heuristic):
        self.state = state # The state of the node
        self.parent = parent # The previous node
        self.action = action # The action of previous node that move to the state node
        self.heuristic = heuristic # the heuristic from state node to goal

# Create the frontier
class QueueFrontier():
    # Create an empty frontier
    def __init__(self):
        self.frontier = []

    # Add node to the frontier (enqueue)
    def add(self,node):
        self.frontier.append(node)

    # Check the node is in frontier or not
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    # Return the empty frontier
    def empty(self):
        return len(self.frontier) == 0

    # Remove the previous node (dequeue) by FIFO
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            self.frontier.sort(key = lambda node: node.heuristic)
            node = self.frontier.pop(0)
            return node    