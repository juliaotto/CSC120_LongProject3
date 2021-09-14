""" File name: animated_graphics.py
    Author: Julia Otto
    Purpose: This file creates an animated
    graphic of stick figures dancing to 
    YMCA.
"""

import graphics

def drawperson(frame,headx, heady, stand_b):
    """ This function draws the body and legs of the four
        figures. It draws either the crouched or standing version.
        Arguments: This function takes in a reference to the 
        graphics window, the x and y coordinates of the head and 
        a value that indicates position. 
    """
    if stand_b == 1:
        for i in range(headx, 400, 100):
            frame.ellipse(i, heady, 50, 50)
            frame.line(i, heady + 25, i, heady + 120)
            frame.line(i, heady + 120, i - 25, 400)
            frame.line(i, heady + 120, i + 25, 400)
    else:
        for i in range(headx, 400, 100):
            frame.ellipse(i, heady + 30, 50, 50)
            frame.line(i, heady + 55, i, heady + 150)
            frame.line(i, heady + 150, i - 25, heady + 175)
            frame.line(i, heady + 150, i + 25, heady + 175)
            frame.line(i - 25, heady + 175, i - 25, 400)
            frame.line(i + 25, heady + 175, i + 25, 400)
    
def alldown(frame, headx, heady, stand_b):
    """ This function draws the downward arms of the foour figures. 
        It draws either the crouched or standing version.
        Arguments: This function takes in a reference to the 
        graphics window, the x and y coordinates of the head and 
        a value that indicates position. 
    """
    if stand_b == 1:
        drawperson(frame, headx, heady, stand_b)
        for i in range(headx, 400, 100):
            frame.line(i, heady + 45, i - 20, heady + 120)
            frame.line(i, heady + 45, i + 20, heady + 120)
    else:
        drawperson(frame, headx, heady, stand_b)
        for i in range(headx, 400, 100):
            frame.line(i, heady + 75, i - 20, heady + 150)
            frame.line(i, heady + 75, i + 20, heady + 150)

def Y(frame, headx, heady, stand_b):
    """ This function draws the 'Y' arms for the first figure. 
        It draws either the crouched or standing version.
        Arguments: This function takes in a reference to the 
        graphics window, the x and y coordinates of the head and 
        a value that indicates position. 
    """
    if stand_b == 1:
        frame.line(headx, heady + 45, headx - 70, heady - 60, "red")
        frame.line(headx, heady + 45, headx + 70, heady - 60, "red")
    else:
        frame.line(headx, heady + 75, headx - 70, heady - 30, "red")
        frame.line(headx, heady + 75, headx + 70, heady - 30, "red")
    

def M(frame, headx, heady, stand_b):
    """ This function draws the 'M' arms for the second figure. 
        It draws either the crouched or standing version.
        Arguments: This function takes in a reference to the 
        graphics window, the x and y coordinates of the head and 
        a value that indicates position. 
    """
    if stand_b == 1:
        frame.line(headx, heady + 45, headx - 30, heady - 40, "blue")
        frame.line(headx, heady + 45, headx + 30, heady - 40,"blue")
        frame.line(headx + 30, heady - 40, headx, heady - 25, "blue")
        frame.line(headx - 30, heady - 40, headx, heady - 25, "blue")
    else:
        frame.line(headx, heady + 75, headx - 30, heady - 10, "blue")
        frame.line(headx, heady + 75, headx + 30, heady - 10,"blue")
        frame.line(headx + 30, heady - 10, headx, heady + 5, "blue")
        frame.line(headx - 30, heady - 10, headx, heady + 5, "blue")

def C(frame, headx, heady, stand_b):
    """ This function draws the 'C' arms for the third figure. 
        It draws either the crouched or standing version.
        Arguments: This function takes in a reference to the 
        graphics window, the x and y coordinates of the head and 
        a value that indicates position. 
    """
    if(stand_b == 1):
       frame.line(headx, heady + 45, headx + 50, heady + 5, "green")
       frame.line(headx, heady + 45, headx + 50, heady + 80,"green")
    else:
       frame.line(headx, heady + 75, headx + 50, heady + 35, "green")
       frame.line(headx, heady + 75, headx + 50, heady + 110,"green")

def A(frame, headx, heady, stand_b):
    """ This function draws the 'A' arms for the last figure. 
        It draws either the crouched or standing version.
        Arguments: This function takes in a reference to the 
        graphics window, the x and y coordinates of the head and 
        a value that indicates position. 
    """
    if(stand_b == 1):
       frame.line(headx, heady + 45, headx + 45, heady - 35, "purple")
       frame.line(headx, heady + 45, headx - 45, heady - 35,"purple")
       frame.line(headx - 45, heady - 35, headx, heady - 55, "purple")
       frame.line(headx + 45, heady - 35, headx, heady - 55,"purple")
    else:
       frame.line(headx, heady + 75, headx + 45, heady - 5, "purple")
       frame.line(headx, heady + 75, headx - 45, heady - 5,"purple")
       frame.line(headx - 45, heady - 5, headx, heady - 25, "purple")
       frame.line(headx + 45, heady - 5, headx, heady - 25,"purple")

def armsup(frame, headx, heady, stand_b, a):
    """ This function draws the upward arms of the foour figures. 
        It draws either the crouched or standing version.
        Arguments: This function takes in a reference to the 
        graphics window, the x and y coordinates of the head and 
        a value that indicates position and another value, a, that 
        indicates the number of figures with arms up in the air.
    """
    drawperson(frame, headx, heady, stand_b)
    if(a == 1):
        Y(frame, headx, heady, stand_b )
        alldown(frame, headx + 100, heady, stand_b)
    elif(a == 2):
        Y(frame, headx, heady, stand_b)
        M(frame, headx + 100, heady, stand_b)
        alldown(frame, headx + 200, heady, stand_b)
    elif (a == 3):
        Y(frame, headx, heady, stand_b)
        M(frame, headx + 100, heady, stand_b)
        C(frame, headx + 200, heady, stand_b)
        alldown(frame, headx + 300, heady, stand_b)
    elif(a == 4):
        Y(frame, headx, heady, stand_b)
        M(frame, headx + 100, heady, stand_b)
        C(frame, headx + 200, heady, stand_b)
        A(frame, headx + 300, heady, stand_b)
        
def main():
    win = graphics.graphics(400, 400, "animation")

    position = 150
    
    while not win.is_destroyed():
        
        win.clear()
        
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0

        while(count1 != 4):
            drawperson(win, 50, 200, 1)
            alldown(win, 50, 200, 1)
            win.update_frame(3)
            win.clear()     
            drawperson(win, 50, 200, 0)
            alldown(win, 50, 200, 0)
            win.update_frame(3)
            win.clear()
            count1 += 1

        while(count2 != 2):
            drawperson(win, 50, 200, 1)
            armsup(win, 50, 200, 1, 1)
            win.update_frame(3)
            win.clear()     
            drawperson(win, 50, 200, 0)
            armsup(win, 50, 200, 0, 1)
            win.update_frame(3)
            win.clear()
            count2+=1

        while count3 != 1:
            drawperson(win, 50, 200, 1)
            armsup(win, 50, 200, 1, 2)
            win.update_frame(3)
            win.clear()     
            drawperson(win, 50, 200, 0)
            armsup(win, 50, 200, 0, 2)
            win.update_frame(3)
            win.clear()
            count3 += 1
 
        while count4 != 1:
            drawperson(win, 50, 200, 1)
            armsup(win, 50, 200, 1, 3)
            win.update_frame(5)
            win.clear()     
            drawperson(win, 50, 200, 0)
            armsup(win, 50, 200, 0, 3)
            win.update_frame(3)
            win.clear()
            count4 += 1
       
        while count5 != 4:
            drawperson(win, 50, 200, 1)
            armsup(win, 50, 200, 1, 4)
            win.update_frame(3)
            win.clear()     
            drawperson(win, 50, 200, 0)
            armsup(win, 50, 200, 0, 4)
            win.update_frame(3)
            win.clear()
            count5 += 1

if __name__ == "__main__":
    main()

