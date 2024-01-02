from graphics import *

def rectangle(win, tlPoint, brPoint, colours):
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colours)
    r.draw(win)
    return r

def line(win, point1, point2, colours):
    l = Line(point1, point2)
    l.setOutline(colours)
    l.draw(win)
    return l

def brPoint(tlPoint, width, height):
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint

def blPoint(trPoint, width, height):
    x = trPoint.getX() - width
    y = trPoint.getY() + height
    blPoint = Point(x, y)
    return blPoint


def main():
    colours = ["red", "green", "blue", "purple", "orange", "cyan"]
    print("Choose 3 colours to use to colour your graphics \nSelect from the menu below and enter the number:")
    print("0) Red \n1) Green \n2) Blue \n3) Purple \n4) Orange \n5) Cyan")
    col1 = int(input("Please enter the number of your first colour: "))
    col2 = int(input("Please enter the number of your second colour: "))
    col3 = int(input("Please enter the number of your third colour: "))
    print("Choose the size of your graphic from the menu below \n1) 5x5 \n2) 7x7 ")
    nSize = int(input("Please enter your answer: "))
    if nSize == 1:
        win = GraphWin("Up2062792", 500, 500)
        for y in range(0, 500, 100):
            for x in range(0, 500, 100):
                tlPoint = Point(x, y)
                br = Point(tlPoint.x + 100, tlPoint.y + 100)
                #colour 1
                if x < 400 and y == 0:
                    rectangle(win, tlPoint, br, colours[col1])
                elif x < 300 and y == 100:
                    rectangle(win, tlPoint, br, colours[col1])
                #colour 3
                elif x > 400 and y == 0:
                    rectangle(win, tlPoint, br, colours[col3])
                elif x > 300 and y == 100:
                    rectangle(win, tlPoint, br, colours[col3])
                elif x > 200 and y >= 200:
                    rectangle(win, tlPoint, br, colours[col3])
                #patch1
                elif x == 100 and y == 300:
                    colour = colours[col2]
                    patch1(win, colour, tlPoint)
                #patch2
                elif 0 <= x <= 100 and 200 <= y <= 300:
                    colour = colours[col1]
                    patch2(win, colour, tlPoint)
                elif x == 0 and y == 400 or x == 200 and y == 200:
                    colour = colours[col2]
                    patch2(win, colour, tlPoint)
                elif 100 <= x <= 200 and 300 <= y <= 400:
                    colour = colours[col3]
                    patch2(win, colour, tlPoint)
                #colour 2
                else:
                    rectangle(win, tlPoint, br, colours[col2])
        win.getMouse()

    elif nSize == 2:
        win = GraphWin("Up2062792", 700, 700)
        for y in range(0, 700, 100):
            for x in range(0, 700, 100):
                tlPoint = Point(x, y)
                br = Point(tlPoint.x + 100, tlPoint.y + 100)
                #colour1
                if x < 600 and y == 0:
                    rectangle(win, tlPoint, br, colours[col1])
                elif x < 500 and y == 100:
                    rectangle(win, tlPoint, br, colours[col1])
                elif x < 400 and y == 200:
                    rectangle(win, tlPoint, br, colours[col1])
                #colour2
                elif x > 600 and y == 0:
                    rectangle(win, tlPoint, br, colours[col3])
                elif x > 500 and y == 100:
                    rectangle(win, tlPoint, br, colours[col3])
                elif x > 400 and y == 200:
                    rectangle(win, tlPoint, br, colours[col3])
                elif x > 300 and y >= 300:
                    rectangle(win, tlPoint, br, colours[col3])
                #patch1
                elif x == 100 and y == 400:
                    colour = colours[col1]
                    patch1(win, colour, tlPoint)
                elif x == 100 and y == 500 or x == 200 and y == 400:
                    colour = colours[col2]
                    patch1(win, colour, tlPoint)
                elif x == 200 and y == 500:
                    colour = colours[col3]
                    patch1(win, colour, tlPoint)
                #patch2
                elif 0 <= x <= 200 and 300 <= y <= 500:
                    colour = colours[col1]
                    patch2(win, colour, tlPoint)
                elif x == 0 and y == 600 or x == 300 and y == 300:
                    colour = colours[col2]
                    patch2(win, colour, tlPoint)
                elif 100 <= x <= 300 and 400 <= y <= 600:
                    colour = colours[col3]
                    patch2(win, colour, tlPoint)
                #colour3
                else:
                    rectangle(win, tlPoint, br, colours[col2])
        win.getMouse()



def patch1(win, colour, tlOffset):
    dimension = 100
    scale = 25
    strOutput = ""
    for y in range(0, dimension, scale):
        strOutput = ""
        isOdd = True
        if y % 2 == 0:
            isOdd = False
        for x in range(0, dimension, scale):
            isHalf = True
            if x == 0 or x == 1:
                isHalf = False
            tl = Point(tlOffset.getX() + x, tlOffset.getY() + y)
            br = brPoint(tl, scale, scale)
            ## For normal H
            tl1Up = Point(tlOffset.getX() + x + 5, tlOffset.getY() + y)
            br1Up = brPoint(tl1Up, 15, 10)
            tl2Up = Point(tlOffset.getX() + x + 5, tlOffset.getY() + y + 15)
            br2Up = brPoint(tl2Up, 15, 10)

            ## For side H
            tl1Side = Point(tlOffset.getX() + x, tlOffset.getY() + y + 5)
            br1Side = brPoint(tl1Side, 10, 15)
            tl2Side = Point(tlOffset.getX() + x + 15, tlOffset.getY() + y + 5)
            br2Side = brPoint(tl2Side, 10, 15)

            if isOdd and (x == 1 * scale):
                rectangle(win, tl, br, "white")
                rectangle(win, tl1Side, br1Side, colour)
                rectangle(win, tl2Side, br2Side, colour)
            elif isOdd and (x == 2 * scale):
                rectangle(win, tl, br, colour)
                rectangle(win, tl1Up, br1Up, "white")
                rectangle(win, tl2Up, br2Up, "white")
            elif isOdd and (x == 3 * scale):
                rectangle(win, tl, br, colour)
                rectangle(win, tl1Side, br1Side, "white")
                rectangle(win, tl2Side, br2Side, "white")
            else:
                if isOdd == False and (x == 0):
                    rectangle(win, tl, br, colour)
                    rectangle(win, tl1Up, br1Up, "white")
                    rectangle(win, tl2Up, br2Up, "white")
                elif isOdd == False and (x == 2 * scale):
                    rectangle(win, tl, br, "white")
                    rectangle(win, tl1Up, br1Up, colour)
                    rectangle(win, tl2Up, br2Up, colour)
                elif isOdd == False and (x == 1 * scale):
                    rectangle(win, tl, br, colour)
                    rectangle(win, tl1Side, br1Side, "white")
                    rectangle(win, tl2Side, br2Side, "white")
                elif isOdd == False and (x == 3 * scale):
                    rectangle(win, tl, br, "white")
                    rectangle(win, tl1Side, br1Side, colour)
                    rectangle(win, tl2Side, br2Side, colour)
                else:
                    rectangle(win, tl, br, "white")
                    rectangle(win, tl1Up, br1Up, colour)
                    rectangle(win, tl2Up, br2Up, colour)

def patch2(win, colour, tlOffset):
    dimension = 100
    scale = 20
    for y in range(0, dimension, scale):
        for x in range(0, dimension, scale):
            point1 = Point(tlOffset.getX() + x, tlOffset.getY() + y)
            point2 = brPoint(point1, scale, scale)
            point3 = Point(tlOffset.getX() + dimension - x, tlOffset.getY() + y)
            point4 = blPoint(point3, scale, scale)
            line(win, point1, point2, colour)
            line(win, point3, point4, colour)


##### Main Code #####
main()
