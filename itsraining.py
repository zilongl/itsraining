def iterAndFindVolume(tupleI, theWall):
    vol=0
    usedValues = set()
    for i in range(0,len(tupleI)-1):
        x=tupleI[i]
        y=tupleI[i+1]
        for i in range(min(x[1],y[1])+1, max(x[1],y[1])):
            if i not in usedValues:
                vol+=y[0]-theWall[i] if theWall[i]<y[0] else 0
                usedValues.add(i)
    return vol

def findVolume(theWall):
    index = 0
    tupleIUnsorted=[]
    #[3,1,2] -> (3,1),(1,2),(2,3)
    for v in theWall:
        tupleIUnsorted.append((v,index))
        index+=1
    #(3,1),(1,2),(2,2) -> (3,1),(2,3),(1,2)
    tupleI = sorted(tupleIUnsorted, key=lambda tup: tup[0], reverse=True)
    return iterAndFindVolume(tupleI, theWall)

if __name__ == '__main__':
    theWall = [3,1,2,5,1,4]
    theWall = [2,5,1,2,3,4,7,7,6]
    theWall = [6,7,7,4,3,2,1,5,2]
    theWall = [2,5,1,2,3,4,7,7,6]
    theWall = [2,0,1]
    theWall = [2,1]
    theWall = [1]
    theWall = [1,2,3,4,5,6,7,8,9]
    theWall = [2,5,1,3,1,2,1,7,7,6]
    print findVolume(theWall)