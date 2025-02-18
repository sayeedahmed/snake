#---------------------------
#        SNAKE (GAME)
#---------------------------

from tkinter import * # Import all definitions from tkinter
from tkinter import messagebox
import random
import time
# from _overlapped import NULL

class CanvasDemo:
    def __init__(self):
        
        self.__x1 = 300
        self.__y1 = 350
        self.__x2 = 320
        self.__y2 = 370
        self.diameter = abs(self.__x1 - self.__x2)
        self.__step = self.diameter#20
        self.snake = [[self.__x1, self.__y1], [self.__x1-self.diameter, self.__y1], [self.__x1-2*self.diameter, self.__y1], [self.__x1-3*self.diameter, self.__y1], [self.__x1-4*self.diameter, self.__y1]]
        self.segments = []
        self.food = None
        self.foodX = 0
        self.foodY = 0
        self.keyPressed = None
        self.tail = None
        self.preTail = None
        self.__canvasWidth = 1000
        self.__canvasHeight = 800
        self.colors = ["blue"]#["red", "orange", "yellow", "green", "blue", "violet"]
        self.window = Tk()
        self.window.title("SSSSSNAKE")
        
        self.canvas = Canvas(self.window, width = self.getCanvasWidth(), height = self.getCanvasHeight(), bg = "white")
        self.canvas.pack()

        self.frame = Frame(self.window)
        #self.frame.pack()
        
        #self.canvas.create_oval(self.getX1(), self.getY1(), self.getX2(), self.getY2(), fill = "blue", tags = "oval")
        self.redraw_snake()
        
        self.canvas.bind('<Button-1>',self.click)
        self.canvas.pack()
        
        self.canvas.bind("<Key>", self.key)
        self.canvas.pack()
        
        self.canvas.focus_set()
        
        #B1 = Button(self.window, text = "Replay?", command = self.hello())
        #B1.pack()
        
        btLeft = Button(self.frame, text = "Left",
                             command = self.moveLeft)
        btRight = Button(self.frame, text = "Right",
                        command = self.moveRight)
        btUp = Button(self.frame, text = "Up",
                       command = self.moveUp)
        btDown = Button(self.frame, text = "Down",
                           command = self.moveDown)
        #btClear = Button(frame, text = "Clear",
        #                command = self.clearCanvas)
        
        self.create_food()
        
        btLeft.grid(row = 1, column = 1)
        btRight.grid(row = 1, column = 2)
        btUp.grid(row = 1, column = 3)
        btDown.grid(row = 1, column = 4)
        #btClear.grid(row = 1, column = 7)
        
        self.window.mainloop()
    
    def getX1(self):
        return self.__x1
    def getY1(self):
        return self.__y1
    def getX2(self):
        return self.__x2
    def getY2(self):
        return self.__y2
    def getCanvasHeight(self):
        return self.__canvasHeight
    def getCanvasWidth(self):
        return self.__canvasWidth
    def getStep(self):
        return self.__step
    def setX1(self,x):
        self.__x1 = x
    def setY1(self,y):
        self.__y1 = y
    def setX2(self,x):
        self.__x2 = x
    def setY2(self,y):
        self.__y2 = y
    def setCanvasHeight(self,ht):
        self.__canvasHeight = ht
    def setCanvasWidth(self,wid):
        self.__canvasWidth = wid
    def setStep(self,st):
        self.__step = st
        
    def moveLeft(self):
        #self.clearCanvas()
        #self.canvas.create_oval(self.getX1() - self.getStep(), self.getY1(), self.getX2() - self.getStep(), self.getY2(), fill = random.choice(self.colors), tags = "oval")
        if (self.getX1() >= 2*self.diameter):
            self.setX1(self.getX1() - self.getStep())
            self.setX2(self.getX2() - self.getStep())
        else:
            self.setX1(self.getX1() + self.getCanvasWidth() - self.diameter)#5*self.getStep())
            self.setX2(self.getX2() + self.getCanvasWidth() - self.diameter)#5*self.getStep())
        self.snake.insert(0,[self.getX1(),self.getY1()])
        if(self.capture()):
            self.snake.insert(0,[self.getX1()-self.diameter,self.getY1()])
        del self.snake[-1]
        #if (self.collision()):
            #print("Collision ! --> ",self.snake[0][0]," ",self.snake[0][1])
            #self.retry()
        self.clear_snake_on_canvas()
        #self.canvas.delete(self.tail)
        self.redraw_snake()
        if self.keyPressed == "Left":
            self.window.after(100, self.moveLeft)
        
        
    def moveRight(self):
        #self.clearCanvas()
        #self.canvas.create_oval(self.getX1() + self.getStep(), self.getY1(), self.getX2() + self.getStep(), self.getY2(), fill = random.choice(self.colors), tags = "oval")
        if (self.getX2() <= self.getCanvasWidth()-2*self.diameter):
            self.setX1(self.getX1() + self.getStep())
            self.setX2(self.getX2() + self.getStep())
        else:
            self.setX1(self.getX1() - self.getCanvasWidth() + self.diameter)#5*self.getStep())
            self.setX2(self.getX2() - self.getCanvasWidth() + self.diameter)#5*self.getStep())
        self.snake.insert(0,[self.getX1(),self.getY1()])
        if(self.capture()):
            self.snake.insert(0,[self.getX1()+self.diameter,self.getY1()])
        #self.snake.pop((len(self.snake))-1)
        del self.snake[-1]
        #if (self.collision()):
            #print("Collision ! --> ",self.snake[0][0]," ",self.snake[0][1])
            #self.retry()
        self.clear_snake_on_canvas()
        #self.canvas.delete(self.tail)
        
        #self.canvas.delete(self.preTail)
        self.redraw_snake()
        if self.keyPressed == "Right":
            self.window.after(100, self.moveRight)
                    
    def moveUp(self):
        #self.clearCanvas()
        #self.canvas.create_oval(self.getX1(), self.getY1() - self.getStep(), self.getX2(), self.getY2() - self.getStep(), fill = random.choice(self.colors), tags = "oval")
        if (self.getY1() >= 2*self.diameter):
            self.setY1(self.getY1() - self.getStep())
            self.setY2(self.getY2() - self.getStep())
        else:
            self.setY1(self.getY1() + self.getCanvasHeight() - 2*self.diameter)#5*self.getStep())
            self.setY2(self.getY2() + self.getCanvasHeight() - 2*self.diameter)#5*self.getStep())
        self.snake.insert(0,[self.getX1(),self.getY1()])
        if(self.capture()):
            self.snake.insert(0,[self.getX1(),self.getY1()-self.diameter])
        del self.snake[-1]
        #if (self.collision()):
            #print("Collision ! --> ",self.snake[0][0]," ",self.snake[0][1])
            #self.retry()
        self.clear_snake_on_canvas()
        #self.canvas.delete(self.tail)
        self.redraw_snake()
        if self.keyPressed == "Up":
            self.window.after(100, self.moveUp)
        
    def moveDown(self):
        #self.clearCanvas()
        #self.canvas.create_oval(self.getX1(), self.getY1() + self.getStep(), self.getX2(), self.getY2() + self.getStep(), fill = random.choice(self.colors), tags = "oval")
        if (self.getY2() <= self.getCanvasHeight() -2*self.diameter):
            self.setY1(self.getY1() + self.getStep())
            self.setY2(self.getY2() + self.getStep())
        else:
            self.setY1(self.getY1() - self.getCanvasHeight() + 2*self.diameter)#5*self.getStep())
            self.setY2(self.getY2() - self.getCanvasHeight() + 2*self.diameter)#5*self.getStep())
        self.snake.insert(0,[self.getX1(),self.getY1()])
        if(self.capture()):
            self.snake.insert(0,[self.getX1(),self.getY1()+self.diameter])
        #self.tail = self.snake.pop()
        #tail = self.snake[len(self.snake)-1]
        #self.canvas.delete(self.snake[len(self.snake)-1])
        #self.snake.pop((len(self.snake))-1)
        del self.snake[-1]
        #if (self.collision()):
            #print("Collision ! --> ",self.snake[0][0]," ",self.snake[0][1])
            #self.retry()
        self.clear_snake_on_canvas()
        #self.canvas.delete(self.tail)
            
        #self.canvas.delete(self.preTail)
        self.redraw_snake()
        if self.keyPressed == "Down":
            self.window.after(100, self.moveDown)
        
    def clearCanvas(self):
        self.canvas.delete("oval")
        
    def click(self, event):
        #print("Clicked at: ",event.x, event.y)
        #self.frame.focus_set()
        '''
        self.canvas.create_oval(self.getX1() + self.getStep(), self.getY1(), self.getX2() + self.getStep(), self.getY2(), fill = random.choice(self.colors), tags = "oval")
        if (self.getX2() <= self.getCanvasWidth()-2*self.diameter):
            self.setX1(self.getX1() + self.getStep())
            self.setX2(self.getX2() + self.getStep())
        else:
            self.setX1(self.getX1() - self.getCanvasWidth() + 5*self.getStep())
            self.setX2(self.getX2() - self.getCanvasWidth() + 5*self.getStep())
        '''
        
    def key(self, event):
        # Make sure the frame is receiving input!
        self.frame.focus_force()
        keyVal = event.keysym
        #print("Pressed", event.keysym)
        self.keyPressed = str(keyVal)
        if self.keyPressed == "Left":
            self.moveLeft()
        elif self.keyPressed == "Right":
            self.moveRight()
        elif self.keyPressed == "Up":
            self.moveUp()
        elif self.keyPressed == "Down":
            self.moveDown()
    
    def clear_snake_on_canvas(self):
        for segment in self.segments:
            self.canvas.delete(segment)
        del self.segments[:]
             
    def redraw_snake(self):#, snakeBody):
        
        #    self.snake = [[self.__x1, self.__y1], [self.__x1-self.diameter, self.__y1-self.diameter], [self.__x1-2*self.diameter, self.__y1-2*self.diameter]]
        segment = self.canvas.create_oval(self.snake[0][0], self.snake[0][1], self.snake[0][0]+self.diameter, self.snake[0][1]+self.diameter, fill = "black", tags = "oval")
        self.segments.append(segment)
        for i in range (1,len(self.snake)-1):
            #self.canvas.create_oval(self.snake[i][0], self.snake[i][1], self.snake[i][0]+self.diameter, self.snake[i][1]+self.diameter, fill = "", tags = "oval")
            segment = self.canvas.create_oval(self.snake[i][0], self.snake[i][1], self.snake[i][0]+self.diameter, self.snake[i][1]+self.diameter, fill = "green", tags = "oval")
            self.segments.append(segment)
        #self.preTail = self.canvas.create_oval(self.snake[len(self.snake)-2][0], self.snake[len(self.snake)-2][1], self.snake[len(self.snake)-2][0]+self.diameter, self.snake[len(self.snake)-2][1]+self.diameter, fill = "blue", tags = "oval")
        #self.tail = self.canvas.create_oval(self.snake[len(self.snake)-1][0], self.snake[len(self.snake)-1][1], self.snake[len(self.snake)-1][0]+self.diameter, self.snake[len(self.snake)-1][1]+self.diameter, fill = "", tags = "oval")
        self.tail = self.canvas.create_oval(self.snake[len(self.snake)-1][0], self.snake[len(self.snake)-1][1], self.snake[len(self.snake)-1][0]+self.diameter, self.snake[len(self.snake)-1][1]+self.diameter, fill = "green", tags = "oval")
        self.segments.append(self.tail)
        
    def destroy_food(self):
        #self.canvas.create_oval(x, y, self.diameter+x, self.diameter+y, fill = "blue", tags = "oval")
        self.canvas.delete(self.food)
        
    def create_food(self):
        try:
            boundX = self.__canvasWidth-self.diameter
            boundY = self.__canvasHeight-self.diameter
            self.foodX = random.randrange(self.diameter, boundX, self.diameter) 
            self.foodY = random.randrange(self.diameter, boundY, self.diameter)        
            #print("Food at : ",randX," ",randY)
            while [self.foodX,self.foodY] in self.snake:
                self.foodX = random.randrange(self.diameter, boundX, self.diameter) 
                self.foodY = random.randrange(self.diameter, boundY, self.diameter)        
            
            self.destroy_food()
            self.food = self.canvas.create_oval(self.foodX, self.foodY, self.diameter + self.foodX, self.diameter + self.foodY, fill = "red", tags = "oval")
            
        except :
            pass

        self.window.after(3000, self.create_food)
    
    def capture(self):
        if ( abs(self.foodX - self.getX1()) <= self.diameter ) and ( abs(self.foodY - self.getY1()) <= self.diameter ):
            self.destroy_food()
            #self.create_food()
            return True
        else:
            return False
    
    def collision(self):
        if self.snake[0] in self.snake[1:]:
            return True
        else:
            return False
    
    def retry(self):
        #messagebox.showinfo("", "Game Over")
        #messagebox.RETRY
        self.resetSnake()
    
    def resetSnake(self):
        self.__x1 = 300
        self.__y1 = 350
        self.__x2 = 320
        self.__y2 = 370
        self.snake = [[self.__x1, self.__y1], [self.__x1-self.diameter, self.__y1], [self.__x1-2*self.diameter, self.__y1], [self.__x1-3*self.diameter, self.__y1], [self.__x1-4*self.diameter, self.__y1]]
        self.redraw_snake()

CanvasDemo()
