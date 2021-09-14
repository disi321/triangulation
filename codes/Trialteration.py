import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

def Trialteration(pointA, pointB, pointC, fDA, fDB, fDC):
    cord_in_meters = 1.0                                            # check og variant, could be 4.5

    centerX = (pointA.getX() + pointB.getX() + pointC.getX()) / 3
    centerY = (pointA.getY() + pointB.getY() + pointC.getY()) / 3
    center_point = Point(centerX, centerY)

    nearest_base = Point(0, 0)
    shortest = -1.0
    if (fDA < fDB and fDA < fDC):
        nearest_base = pointA
        shortest = fDA
    elif fDB < fDC:
        nearest_base = pointB
        shortest = fDB
    else:
        nearest_base = pointC
        shortest = fDC

    distance_to_center = float(math.sqrt(math.pow(center_point.getX() - nearest_base.getX(), 2)))
    distance_to_center += float(math.pow(center_point.getY() - nearest_base.getY(), 2))  #the length was to big

    shortestDinCo = shortest * cord_in_meters

    t = shortestDinCo / distance_to_center
    pointDiff = Point(center_point.getX() - nearest_base.getX(), center_point.getY() - nearest_base.getY())
    tKefelDiff = Point(pointDiff.getX() * t, pointDiff.getY() * t)

    final_location = Point(nearest_base.getX() + tKefelDiff.getX(), nearest_base.getY() + tKefelDiff.getY())

    return final_location



