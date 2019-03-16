from typing import List
import math

def get_average_elevation(m: List[List[int]]) -> float:
    """
    Returns the average elevation across the elevation map m.

    Examples
    >>> get_average_elevation([])
    0
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> get_average_elevation(m)
    5.0
    >>> m = [[1,2,2,5],[4,5,4,8],[7,9,9,1],[1,2,1,4]]
    >>> get_average_elevation(m)
    4.0625
    """
    # Your code goes here
    sum:float=0
    for i in range(len(m)):
        for j in range(len(m)):
            sum+=m[i][j]
    return sum/(len(m)**2)



def find_peak(m: List[List[int]]) -> List[int]:
    """
    Given an non-empty elevation map m, returns the cell of the
    highest point in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [9,8,7],
             [5,4,6]]
    >>> find_peak(m)
    [1,0]
    >>> m = [[6,2,3],
             [1,8,7],
             [5,4,9]]
    >>> find_peak(m)
    [2,2]
    """
    # Your code goes here
    t: float = 0
    l:List=[]
    for i in range(len(m)):
        for j in range(len(m)):
            if (t<m[i][j]):
                t=m[i][j]
                l.clear()
                l.append(i)
                l.append(j)
    return l


def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink(m, [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    """
    # Your code goes here
    mov=[0,1,-1]
    x:int=c[0]
    y:int=c[1]
    if(x<0 or y>=len(m) or y<0 or x>=len(m)):
        return False
    for i in mov:
        for j in mov:
            newx=x+mov[i]
            newy=y+mov[j]
            if((i==0 and j==0)or(newx<0)or(newx>len(m)-1)or(newy<0)or(newy>len(m)-1)):
                continue
            elif (m[x][y]>m[newx][newy]):
                return False
    return True


def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink(m, [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    # Your code goes here
    if(is_sink(m,start)):
        return start
    mov=[0,1,-1]
    cur:list=[start[0],start[1]]
    pre: list = [-1, -1]
    while cur!=pre:
        pre[0] = cur[0]
        pre[1] = cur[1]
        for i in mov:
            for j in mov:
                newx=cur[0]+mov[i]
                newy=cur[1]+mov[j]
                if((i==0 and j==0)or(newx<0)or(newx>=len(m))or(newy<0)or(newy>=len(m))):
                    continue
                elif (m[cur[0]][cur[1]] > m[newx][newy]):
                    cur[0]=newx
                    cur[1]=newy
    return cur


def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    """
    # Your code goes here
    startx:int=s[0]
    starty:int=s[1]
    mv=[0,0]
    while(True):
        if(supplies<0):
            return False
        if (supplies >= 0):
            if(startx==d[0] and starty==d[1]):
                return True
            curElv: int = m[startx][starty]
            cos:int=math.inf
            if(startx < d[0] and cos>math.fabs(curElv-m[startx+1][starty])):
                cos=math.fabs(curElv-m[startx+1][starty])
                mv=[1,0]
            if(starty < d[1] and cos>=math.fabs(curElv-m[startx][starty+1])):
                cos=math.fabs(curElv - m[startx][starty + 1])
                mv = [0, 1]
            supplies-=cos
            startx +=mv[0]
            starty += mv[1]


def rotate_map(m: List[List[int]]) -> None:
    """
    Rotates the orientation of an elevation map m 90 degrees counter-clockwise.
    See the examples to understand what's meant by rotate.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> rotate_map(m)
    >>> m
    [[3,3,3],
     [2,3,4],
     [1,2,5]]
    >>> m = [[5,9,1,8],
             [2,4,5,7],
             [6,3,3,2],
             [1,7,6,3]]
    >>> rotate_map(m)
    >>> m
    [[8,7,2,3],
     [1,5,3,6],
     [9,4,3,7],
     [5,2,6,1]]
    """
    # Your code goes here
    nMap=[[0]*len(m) for i in range(5)]
    for i in range (len(m)):
        for j in range (len(m)):
            nMap[j][len(m)-1-i]=m[i][j]
    for i in range(len(m)):
        for j in range(len(m)):
            m[j][len(m) - 1 - i] = nMap[i][j]
    for i in range(len(m)):
        for j in range(len(m)):
            nMap[j][len(m) - 1 - i] = m[i][j]
    for i in range (len(m)):
        for j in range (len(m)):
            m[i][j]=nMap[i][j]


"""
You are not required to understand or use the code below. It is there for
curiosity and testing purposes.
"""


def create_real_map() -> List[List[int]]:
    """
    Creates and returns an elevation map from the real world data found
    in the file elevation_data.csv.

    Make sure this .py file and elevation_data.csv are in the same directory
    when you run this function to ensure it works properly.
    """
    data = open("elevation_data.csv")
    m = []
    for line in data:
        m.append(line.split(","))
    data.close()
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m
