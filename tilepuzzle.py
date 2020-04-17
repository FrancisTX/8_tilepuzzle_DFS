import copy

def tilepuzzle(start, goal):
    return reverse(statesearch([start],goal,[]))

def statesearch(unexplored,goal,path):
    if unexplored == []:
        return []
    elif goal == head(unexplored):
        return cons(goal,path)
    else:       
        result = statesearch(generateNewStates(head(unexplored), path),
                             goal,
                             cons(head(unexplored), path))
        if result != []:
            return result
        else:
            return statesearch(tail(unexplored),
                               goal,
                               path)

def FindSpace(currState):
    row = 0
    for x in currState:
        if 0 in x:
            return row, x.index(0)
        row += 1

def SwapPosition(currState, currPosition, MoveToRow, MoveToCol):
    result = copy.deepcopy(currState)
    if (MoveToRow >= 0 and MoveToRow < len(result[0])
        and  MoveToCol >= 0 and MoveToCol < len(result[0])):
        result[currPosition[0]][currPosition[1]] = result[MoveToRow][MoveToCol]
        result[MoveToRow][MoveToCol] = 0
        return result
    return None

def MoveUp(currState, path):
    currPosition = FindSpace(currState)
    newState =  SwapPosition(currState, currPosition, 
                        currPosition[0] - 1, currPosition[1])
    if newState in path:
        return None
    else:
        return newState

def MoveDown(currState, path):
    currPosition = FindSpace(currState)
    newState = SwapPosition(currState, currPosition, 
                        currPosition[0] + 1, currPosition[1])
    if newState in path:
        return None
    else:
        return newState
    
def MoveRight(currState, path):
    currPosition = FindSpace(currState)
    newState = SwapPosition(currState, currPosition, 
                        currPosition[0], currPosition[1] + 1)
    if newState in path:
        return None
    else:
        return newState

def MoveLeft(currState, path):
    currPosition = FindSpace(currState)
    newState = SwapPosition(currState, currPosition, 
                        currPosition[0], currPosition[1] - 1)
    if newState in path:
        return None
    else:
        return newState

def generateNewStates(currState, path):
    return (MoveUp(currState, path), MoveDown(currState, path) ,
            MoveRight(currState, path) , MoveLeft(currState, path))

def reverse(lst):
    return lst[::-1]

def head(lst):
    newlst = list(filter(None,lst))
    if len(newlst) == 0:
        return None
    else: 
        return newlst[0]

def cons(item,lst):
    return [item] + lst

def tail(lst):
    return lst[1:]

tilepuzzle([[2,8,3],[1,0,4],[7,6,5]],[[1,2,3],[8,0,4],[7,6,5]])