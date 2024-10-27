import math

def CircleCollision(Circle1Position,Circle2Position,Radius):
    Pos1 = [Circle1Position.x, Circle1Position.y]
    Pos2 = [Circle2Position.x, Circle2Position.y]
    if math.dist(Pos1,Pos2) < Radius:
        return True
    return False