import abc
import copy
import heapq



class node:
    def __init__(self,state,parent = None):             #At the initial state parent node will be none
        self.state = state                              #storing the state of node
        self.parent = parent                            #storing the parent node
        self.h = 0                                      #storing value of H
        self.f = 0                                      #storing value of f
        self.g = 0                                      #storing value of g

    def __lt__(self,ob1):
        return ob1.f

    def setP(self,p):
        self.parent = p

    def getP(self):
        return self.parent

class ASTAR:
    def __init__(self,inputState):
        self.Expandednodes = []                         #List of closed nodes
        self.Fringe = []                                #Priority Queue for open nodes
        self.inputState = inputState                    #Initial state entered by the user

    def AstarSearch(self):
        if(self.GoalState(self.inputState)):
            print('Input is Goal state')
            return None
        while len(self.Fringe) != 0:

            f, x = heapq.heappop(self.Fringe)            #poping nodes from the open node priority queue
            childs = self.generateChildrennodes(x)
            for child in childs:
                if(self.GoalState(child.state)):         #Goal achieved
                    print('Goal Reached ',child.state)   #Printing Goal
                    return child
                if self.LowerF(self.Fringe,child) ==False:
                    heapq.heappush(self.Fringe,(child.f,child))
                elif self.LowerF(self.Expandednodes,child) == False:
                    heapq.heappush(self.Fringe,(child.f,child))
            heapq.heappush(self.Expandednodes,(x.f,x))       #Adding nodes to the closed list.
        return None

    def GoalState(self,state):
        pass
    def LowerF(self,lists,x):   #samestatewithlowerF
        pass
    def G(self,parent):
        pass
    def Path(self,x):
        pass
    def Equalstates(self, state1, state2):
        pass
    def generateChildrennodes(self, x):
        pass
    def F(self,x):
        return x.g + x.h
    def Nodes(self, n):
        pass


class Puzzle8(ASTAR):
    def __init__(self,inputState,goalState,manhattandistance):
        ASTAR.__init__(self,inputState)
        self.goalState = goalState
        self.manhattandistance = manhattandistance
        self.noofNodesGenerated = 0
        x = self.nodecreation()
        heapq.heappush(self.Fringe,(x.f, x))

    def GoalState(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goalState[i][j]:
                    return False
        return True

    def nodecreation(self,state=None,parent=None):
        self.noofNodesGenerated += 1
        if state is None:
            state = self.inputState
            x = node(state)
            x.g = 0
            x.h = self.H(state)
            x.f = self.F(x)
            return x
        else:
            x = node(state, parent)
            x.g = self.G(parent)
            x.h = self.H(state)
            x.f = self.F(x)
            return x

    def Equalstates(self,state1,state2):    #Checking for equal states
        for i in range(3):
            for j in range(3):
                if state1[i][j] != state2[i][j]:
                    return False
        return True

    def Index(self,state,number):
        for i, row in enumerate(state):
            try:
                j = row.index(number)
            except ValueError:
                continue
            return i, j
    def G(self, parent):
        return parent.g+1

    def manhattanHvalue(self,state):         #Value of H when using Manhattan Distance as the Heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if (state[i][j] != 0):
                    (goalRow,goalColumn) = self.Index(self.goalState,state[i][j])
                    distance += abs(goalColumn - j) + abs(goalRow - i)
        return distance

    def H(self,state):
        if(self.manhattandistance):
            return self.manhattanHvalue(state)
        else:
            return self.misplacedHvalue(state)
    def misplacedHvalue(self,state):           #Value of H when using Misplaced Tiles as the Heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if ((state[i][j] !=0) and  (state[i][j] != self.goalState[i][j])):
                    distance +=1
        return distance

    def Path(self,x):
        path = []
        while(True):
            if(x is None):
                break
            else:
                path.append(x.state)
                x = x.parent
        print('The Path length is ',len(path))
        print('Path Trace')
        for state in reversed(path):
            self.printstate(state)

    def Nodes(self,x):
        print('Values are g = {}, f = {}, h = {}, and state = {}'.format(x.g,x.f,x.h,x.state))


    def printstate(self,state):

        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    print(' ',end=' ')
                else:
                    print(state[i][j], end=' ')
            print()
        print()


    def generateChildrennodes(self,x):

        abc = []
        children = []
        i,j = self.Index(x.state,0)
        properindexes = []     #Generating Indexes
        #UP LEFT DOWN RIGHT
        if i-1 >=0:
            properindexes.append((i-1,j))
            abc.append("Down")
        if j-1 >=0:
            properindexes.append((i,j-1))
            abc.append("Right")
        if i+1 <=2:
            properindexes.append((i+1,j))
            abc.append("Up")
        if j+1 <=2:
            properindexes.append((i,j+1))
            abc.append("Left")
        for k in abc:
            print(k)



        for index,(row,col) in enumerate(properindexes):
            state = copy.deepcopy(x.state)
            y = state[i][j]
            state[i][j] = state[row][col]
            state[row][col] = y
            children.append(self.nodecreation(state,x))
        return children







    def LowerF(self,list,x):
        for i,l in list:
            if self.Equalstates(l.state,x.state):
               if(x.f<l.f):
                    l = x
                    return True
               else:
                   return True
        return False

def parseInput():
    number1 = input()
    number2 = input()
    number3 = input()
    inputlist = [list(map(int, number1.split(' '))),list(map(int, number2.split(' '))),list(map(int, number3.split(' ')))]
    return inputlist


if __name__ == '__main__':
    print('Please enter the input state:')
    inputState = parseInput()
    print('Please enter the goal state:')
    goalState = parseInput()
    Inputlen = inputState[0]+inputState[1]+inputState[2]
    Goallen = goalState[0]+goalState[1]+goalState[2]
    if len(Inputlen) != 9 or len(Goallen) !=9:
        print('Invalid Input')
    elif len(set(Inputlen) - set([1,2,3,4,5,6,7,8,0])) > 0 or len(set(Goallen) - set([1,2,3,4,5,6,7,8,0])) > 0:
        print('Invalid Input')
    else:
        manhattandistance = False
        Heuristic = input('Heuristic function?\n1.Manhattan Distance \n2.Misplaced Tiles\n(1/2) :') #Taking the Heuristic Type Input
        Heuristic = int(Heuristic)
        if Heuristic == 1:
            manhattandistance = True     #If manhattandistance is true, it'll be considered as the heuristic. Else, Misplaced Tiles.
        print('Directions are -')
        P = Puzzle8(inputState,goalState,manhattandistance)
        goalNode = P.AstarSearch()                             #Implementing A* Algorithm
        P.Path(goalNode)                                       #The path from Input to Goal State
        print('Generated Nodes ', P.noofNodesGenerated)        #Printing no. of generated nodes
        print('Expanded Nodes ', len(P.Expandednodes)+1)       #Printing no. of expanded nodes


