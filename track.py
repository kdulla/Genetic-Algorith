from tkinter import Tk, Canvas, Frame, BOTH
import math


'''class TrackPart:
    def __init__(self, x1, y1, x2, y2):
        self.length = ((x1 - x2) ** 2.0 + (y1 - y2) ** 2.0) ** 0.5
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
'''

class TrackObject:
    def __init__(self, point_list1, point_list2):
        self.innerEdge = [(i) for i in point_list1]
        self.outerEdge = [(i) for i in point_list2]
        
    def draw(self, canvas):
        for i in range (len(self.innerEdge)):
            point1 = self.innerEdge[i]
            point2 = self.innerEdge[(i + 1) % len(self.innerEdge)]
            canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill="red") 
        for i in range (len(self.outerEdge)):
            point1 = self.outerEdge[i]
            point2 = self.outerEdge[(i + 1) % len(self.innerEdge)]
            canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill="blue")

class Track:
    def ang(x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)

    def rotate(origin, point, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.

        The angle should be given in radians.
        """
        ox = origin[0]
        oy = origin[1]
        px = point[0]
        py = point[1]
    #print(str(ox) + "\n" + str(oy) + "\n" + str(px) + "\n" + str(py) + "\n" + str(angle))

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return (qx, qy)

    def path_to_track(point_list):
        import random
        inner_list = []
        outer_list = []
        for i in range(len(point_list)):
            point1 = point_list[i] 
            point2 = point_list[(i + 1) % len(point_list)]
            angle = Track.ang(point1[0], point1[1], point2[0], point2[1])
            above = (point1[0], point1[1] + random.randint(100, 105))  
            below = (point1[0], point1[1] - random.randint(100, 105))
            xnew, ynew = Track.rotate(point1, below, angle)
            inner_list.append((xnew, ynew))
        #inner_list += (rotate(point1, below, angle))
            outer_list.append(Track.rotate(point1, above, angle))
    #print(inner_list)
    #print(outer_list)
        return TrackObject(inner_list, outer_list)


