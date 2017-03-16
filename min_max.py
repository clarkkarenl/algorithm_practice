#!/usr/local/bin/python3

# From Trevor Payne YouTube video https://www.youtube.com/watch?v=fInYh90YMJU
# with some updates by me, such as graceful exit and comments

'''
Used for perfect information games like chess
Win/lose states of game are represented by +/- infinity
Solves for best move of player

Checkers:
1. Create a tree of all moves for all players to a certain depth
2. Each position on the tree has a heuristic value (if P1 wins, "+ infinity")
3. Algorithm starts at bottom of tree then works upwards to find best move

Stick Game!
Start with 11 sticks
1. Each player takes turns picking up 1 or 2 sticks
2. Goal is to pick up the last stick
3. If you try to pick up two sticks when only one remains, you lose

'''

from sys import maxsize

# TREE BUILDER
class Node(object):
    def __init__(self, i_depth, i_playernum, i_sticksRemaining, i_value = 0):
        # depth of current location in tree
        self.i_depth  = i_depth
        # 1 or -1
        self.i_playernum = i_playernum
        self.i_sticksRemaining = i_sticksRemaining
        # game state: -infinity, 0, or +infinity
        self.i_value = i_value
        self.children = []
        self.CreateChildren()

    def CreateChildren(self):
        if self.i_depth >= 0:
            for i in range(1, 3):
                v = self.i_sticksRemaining - i
                self.children.append(Node(self.i_depth - 1, -self.i_playernum, v, self.RealVal(v)))

    def RealVal(self, value):
        if (value == 0):
            return maxsize * self.i_playernum
        elif (value < 0):
            return maxsize * -self.i_playernum
        return 0

# Algorithm
def MinMax( node, i_depth, i_playernum ):
    if (i_depth == 0) or (abs(node.i_value) == maxsize):
        return node.i_value

    i_bestValue = maxsize * -i_playernum

    for i in range(len(node.children)):
        child = node.children[i]
        i_val = MinMax(child, i_depth - 1, -i_playernum)
        if ( abs(maxsize * i_playernum - i_val) < abs(maxsize * i_playernum - i_bestValue) ):
            i_bestValue = i_val

    return i_bestValue

# Implementation
def WinCheck( i_sticks, i_playernum ):
    if i_sticks <= 0:
        print("*" * 30)
        if i_playernum > 0:
            if i_sticks == 0:
                print("\tHooray! You WIN!")
                quit(0)
            else:
                print("\tToo many! You LOSE!")
        else:
            if i_sticks == 0:
                print("\tComputer wins. Better luck next time!")
                quit(0)
            else:
                print("\tERROR!")
        print("*" * 30)
    return 1

if __name__ == '__main__':
    i_stickTotal = 11
    i_depth = 4
    i_curPlayer = 1
    print('''
          INSTRUCTIONS: The player who picks up the last stick wins.
          \tYou can only pick up one (1) or two (2) sticks at a time
          ''')
    while i_stickTotal > 0:
        print("\n{0} sticks remain. How many would you like to pick up?".format(i_stickTotal))
        i_choice = input("\n1 or 2: ")
        i_stickTotal -= int(float(i_choice))
        if WinCheck(i_stickTotal, i_curPlayer):
            i_curPlayer *= -1
            # create the tree that the algorithm will run on
            node = Node(i_depth, i_curPlayer, i_stickTotal)
            bestChoice = -100
            i_bestValue = -i_curPlayer * maxsize
            # iterate through children and find the best choice
            for i in range(len(node.children)):
                n_child = node.children[i]
                i_val = MinMax(n_child, i_depth, -i_curPlayer)
                if (abs(i_curPlayer * maxsize - i_val) <= abs(i_curPlayer * maxsize - i_bestValue)):
                    i_bestValue = i_val
                    bestChoice = i
        bestChoice += 1
        print("Computer chooses {0} \tBased on value:  {1}".format(str(bestChoice), str(i_bestValue)))
        i_stickTotal -= bestChoice
        WinCheck(i_stickTotal, i_curPlayer)
        i_curPlayer *= -1
