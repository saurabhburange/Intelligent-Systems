from random import randint
from copy import deepcopy as copy
from math import ceil
from math import ceil



class State:
    def __init__(self,n,Qposition):
        self.Qposition = Qposition
        self.n = n
        self.board = self.generationBoard()
        self.h = self.calculateH()



    def printingstate(self):
        if self.board is not None:
            for i in range(self.n):
                for j in range(self.n):
                    if self.board[i][j] == 1:
                        print("Q",end=" ")
                    else:
                        print("x",end=" ")
                print()
            print()

    def generationBoard(self):
        board = []
        for i in range(self.n):
            row = [0] * self.n
            board.append(row)

        for x, y in self.Qposition:
            board[x][y] = 1
        return board


    def calculateH(self):
        costofline = 0
        costofdiagonal = 0

        #Costofline Calculation
        for x,y in self.Qposition:
            for index in range(self.n):
                if self.board[x][index] == 1:
                    costofline +=1
                if self.board[index][y] == 1:
                    costofline +=1
            #eliminate it from counting itself
            costofline -=2

            #LEFT UP
            indexA, indexB = x - 1, y - 1
            while indexA >= 0 and indexB >= 0:
                if self.board[indexA][indexB] == 1:
                    costofdiagonal += 1
                indexA -= 1
                indexB -= 1
            #RIGHT DOWN
            indexA, indexB = x + 1, y + 1
            while indexA < self.n and indexB < self.n:
                if self.board[indexA][indexB] == 1:
                    costofdiagonal += 1
                indexA += 1
                indexB += 1
            #LEFT DOWN
            indexA, indexB = x + 1, y - 1
            while indexA < self.n and indexB >= 0:
                if self.board[indexA][indexB] == 1:
                    costofdiagonal += 1
                indexA += 1
                indexB -= 1
            #RIGHT UP
            indexA, indexB = x - 1, y + 1
            while indexA >= 0 and indexB < self.n:
                if self.board[indexA][indexB] == 1:
                    costofdiagonal += 1
                indexA -= 1
                indexB += 1

        return (costofdiagonal+costofline)/2

class HillClimbing:
    def __init__(self,numberofqueens):
        self.numberofqueens = numberofqueens
        self.initialState = None



    def compareh(self, stateA, stateB):
        pass

    def InitialStategeneration(self):
        pass

    def Successorgeneration(self,CurrState):
        pass


    def GoalState(self,state):
        if state.h == 0:
            return True
        return False

    def steepestHillClimbing(self,min=300,max=1000,Seq=False):
        if Seq:
            iterations = 3
        else:
            iterations = randint(min,max)
        success = 0
        successsteps = 0
        failure = 0
        total = 0
        failures = 0
        for i in range(iterations):
            iniState = self.InitialStategeneration()
            if(self.GoalState(iniState)):
                continue
            curstate = iniState
            if Seq:
                print("RandomState Search Sequence is ", i + 1)
                curstate.printingstate()
            loop = 0
            while(True):
                isnotCurState = False

                for successor in self.Successorgeneration(curstate):
                    if self.compareh(curstate,successor) == 1:
                        #currstate is greater than successor
                        curstate = successor
                        isnotCurState = True
                loop +=1
                if Seq and isnotCurState:
                    curstate.printingstate()

                if self.GoalState(curstate) and isnotCurState:
                    successsteps += loop
                    success += 1
                    total += loop
                    if Seq:
                        print("The Goal has been Reached")
                    break
                if isnotCurState == False:
                    failure += loop
                    failures += 1
                    total +=loop
                    if Seq:
                        print("The Goal hasn't Reached")
                    break

        return success, successsteps, failures, failure, iterations



    def Sideways(self,min=300,max=1000,Seq=False):
        if Seq:
            iterations = 3
        else:
            iterations = randint(min, max)
        success = 0
        successsteps = 0
        failure = 0
        total = 0
        failures = 0
        for i in range(iterations):
            iniState = self.InitialStategeneration()
            if (self.GoalState(iniState)):
                continue
            curstate = iniState
            if Seq:
                print("RandomState Search Sequence is ", i + 1)
                curstate.printingstate()
            isnotCurState = False
            loop = 0
            sidewayiterations = 100
            while (True):
                isnotCurState = False
                equalsucstates = []
                for successor in self.Successorgeneration(curstate):
                    compareval = self.compareh(curstate, successor)
                    if compareval == 1:
                        # currstate is greater than successor
                        curstate = successor
                        isnotCurState = True
                        sidewayiterations = 100
                    elif compareval == 0:
                        equalsucstates.append(successor)
                loop += 1
                if Seq and isnotCurState:
                    curstate.printingstate()
                if self.GoalState(curstate) and isnotCurState:
                    successsteps += loop
                    success += 1
                    total += loop
                    if Seq:
                        print("The Goal has been Reached")
                    break
                if isnotCurState == False:
                    if len(equalsucstates) == 0 or sidewayiterations == 0:
                        failure += loop
                        failures += 1
                        total += loop
                        if Seq:
                            print("The Goal hasn't Reached")
                        break
                    else:
                        i = randint(0,len(equalsucstates)-1)
                        curstate = equalsucstates[i]
                        if Seq:
                            curstate.printingstate()
                        sidewayiterations -=1
        return success, successsteps, failures, failure, iterations

    def steepestHCSequences(self):
        self.steepestHillClimbing(Seq=True)

    def sidewaysHillclimbingSequences(self):
        self.Sideways(Seq=True)



    def RRWithSideways(self,min,max):
        iterations = randint(min, max)
        noofrestarts = 0
        total =  0
        for i in range(iterations):
            iniState = self.InitialStategeneration()
            if (self.GoalState(iniState)):
                continue
            curstate = iniState

            while (True):
                sidewayiterations = 100
                loop = 0
                while (True):
                    isnotCurState = False
                    equalsucstates = []
                    for successor in self.Successorgeneration(curstate):
                        compareval = self.compareh(curstate, successor)
                        if compareval == 1:
                            # currstate is greater than successor
                            curstate = successor
                            isnotCurState = True
                            sidewayiterations = 100
                        elif compareval == 0:
                            equalsucstates.append(successor)
                    loop += 1
                    if self.GoalState(curstate) and isnotCurState:
                        total += loop
                        break
                    if isnotCurState == False:
                        if len(equalsucstates) == 0 or sidewayiterations == 0:
                            total += loop
                            break
                        else:
                            i = randint(0, len(equalsucstates) - 1)
                            curstate = equalsucstates[i]
                            sidewayiterations -= 1

                if not self.GoalState(curstate):
                    curstate = self.InitialStategeneration()
                    noofrestarts += 1
                else:
                    break
        return ceil(noofrestarts / iterations), ceil(total / iterations)
    def RRWithOutSideways(self,min,max):
        iterations = randint(min, max)
        noofrestarts = 0
        total = 0
        for i in range(iterations):
            iniState = self.InitialStategeneration()
            if (self.GoalState(iniState)):
                continue
            curstate = iniState

            while(True):
                loop = 0
                while (True):
                    isnotCurState = False
                    for successor in self.Successorgeneration(curstate):
                        if self.compareh(curstate, successor) == 1:
                            #currstate is greater than successor
                            curstate = successor
                            isnotCurState = True
                    loop += 1
                    if self.GoalState(curstate) and isnotCurState:
                        total += loop
                        break
                    if isnotCurState == False:
                        total += loop
                        break
                if not self.GoalState(curstate):
                    curstate = self.InitialStategeneration()
                    noofrestarts += 1
                else:
                    break
        return ceil(noofrestarts/iterations), ceil(total/iterations)
class NQueens(HillClimbing):
    def __init__(self, n):
        HillClimbing.__init__(self,n)


    def InitialStategeneration(self):
        Qposition = []
        for y in range(self.numberofqueens):
            x = randint(0,self.numberofqueens-1)
            queen = [x,y]
            Qposition.append(queen)
        #print(*Qposition, sep=", ")
        initialState = State(self.numberofqueens,Qposition)
        self.initialState = initialState
        return initialState

    def Successorgeneration(self,CurrState):
        for index,[x,y] in enumerate(CurrState.Qposition):
            for xcord in range(self.numberofqueens):
                    if CurrState.board[xcord][y] != 1:
                        successor = copy(CurrState.Qposition)
                        successor[index] = [xcord,y]
                        successorState = State(self.numberofqueens,successor)
                        yield successorState


    def compareh(self,stateA,stateB):
        if stateA.h < stateB.h:
            return -1
        elif stateA.h > stateB.h:
            return 1
        else:
            return 0


if __name__ == '__main__':
    print("Number of Queens -",end=" ")
    numberofqueens = int(input())
    min = 100
    max = 500
    nQueensHillClmbing = NQueens(numberofqueens)
    print("Steepest-Ascent Hill Climbing -")
    print("")
    success, successSteps, failures, failure, noOfTimes = nQueensHillClmbing.steepestHillClimbing(min,max)
    try:
        print("Rate of Failure is",(failures/noOfTimes)*100)
        print("Average of Number of Steps for Failures is", ceil(failure / failures))
        print("Rate of Success is", (success / noOfTimes) * 100)
        print("Average of Number of Steps for Success is",ceil(successSteps/success))

    except ZeroDivisionError:
        pass
    print()
    nQueensHillClmbing.steepestHCSequences()

    print('')
    print("Sideways move Hill Climbing")
    print("."*70)
    success, successSteps, failures, failure, noOfTimes = nQueensHillClmbing.Sideways(min,max)
    try:
        print("Rate of Failure is",(failures/noOfTimes)*100)
        print("Average of no. of Steps for Failures is", ceil(failure / failures))
        print("Rate of Success is", (success / noOfTimes) * 100)
        print("Average of no. of Steps for Success is",ceil(successSteps/success))

    except ZeroDivisionError:
        pass
    print()
    for i in range(3):
        print("RandomState search sequence is ")
        nQueensHillClmbing.sidewaysHillclimbingSequences()

    print("."*70)
    print("."*70)

    print("Random Restarts Hill Climbing")
    print("."*70)
    AvgRandomRestarts, avgSteps = nQueensHillClmbing.RRWithSideways(min,max)
    print("Average of no. of Random Restarts used With Sideways Move:",AvgRandomRestarts)
    print("Average of no. of Steps used With Sideways Move:",avgSteps)

    AvgRandomRestarts, avgSteps = nQueensHillClmbing.RRWithOutSideways(min, max)
    print("Average of no. of Random Restarts WithOut Sideways Move:", AvgRandomRestarts)
    print("Average of no. of Steps WithOut Sideways Move:", avgSteps)
    print("." * 70)
    print("." * 70)
    print("FINISHED")


