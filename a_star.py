#!/usr/local/bin/python3

# From Trevor Payne YouTube video https://www.youtube.com/watch?v=ob4faIum4kQ

'''
A* algorithm is used in a variety of situations, including AI and pathfinding

This program performs the following steps:
1. Generate a list of all possible next steps towards goal from current possible
2. Store children in priority quque based on distance to goal, closest first
3. Select closest child and repeat until goal reached or no more children
'''
# Python3 renamed this from cap "Q" to lower "q"
# Priority Queue is a dictionary of lists
from queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        # to be set later, in subclasses of the State
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDist(self):
        pass

    def CreateChildren(self):
        pass


class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def CreateChildren(self):
        if not self.children:
            for i in range(len(self.goal) - 1):
                val = self.value
                val = val[:i] + val[i + 1] + val[i] + val[i + 2:]
                child = State_String(val, self)
                self.children.append(child)


class AStar_Solver:
    def __init__(self, start, goal):
        # will store the final solution from start to goal and exact sequence
        self.path = []
        # tracks all children we've visited, prevent visit any twice/looping
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_String(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("Goal of {0} is not possible".format(self.goal))
        return self.path


if __name__ == "__main__":
    start1 = 'cfabed'
    goal1 = 'abcdef'
    print("Starting...")
    a = AStar_Solver(start1, goal1)
    a.Solve()
    for i in range(len(a.path)):
        print("{0} - {1}".format(i, a.path[i]))
