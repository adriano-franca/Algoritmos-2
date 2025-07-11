def canMeasureWater(x, y, target):
    visited = set()
    stack = [ (0,0) ]
    visited.add( (0,0) )
    
    def state(j1,j2):
        if (j1,j2) not in visited:
            visited.add( (j1,j2) )
            stack.append( (j1,j2) )

    while stack:
        jug1, jug2 = stack.pop(-1)
        
        if jug1==target or jug2==target or jug1+jug2 == target:
            return True

        state(x, jug2)
        state(jug1, y)

        state(0, jug2)
        state(jug1, 0)

        move1 = min(jug1, y-jug2)
        state(jug1-move1, jug2+move1)
        
        move2 = min(jug2, x-jug1)
        state(jug1+move2, jug2-move2)
        
    return False