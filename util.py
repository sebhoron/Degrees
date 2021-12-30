class Node():
    def __init__(self, state, parent, movie):
        self.state = state
        self.parent = parent
        self.movie = movie


class QueueFrontier():

    # Initialize frontier.
    def __init__(self):
        self.frontier = []

    # Add a node.
    def add(self, node):
        self.frontier.append(node)
        node = self.frontier[-1]

    # Check the frontier for the given state.
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    # Check if empty.
    def empty(self):
        return len(self.frontier) == 0

    # Remove the first node.
    def remove(self):

        # Check if empty.
        if self.empty():
            raise Exception("empty frontier")
        else:
            self.frontier = self.frontier[1:]
