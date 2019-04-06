import turtle as t
import random as r

SIZE = 6

a = t.heading()
x, y = t.pos()

def generateTree(size):
    lWord = 'X'
    for i in range(size):
        j = 0
        while j < len(lWord):
            if(lWord[j] == 'F'):
                lWord = lWord[:j] + 'F' + lWord[j:]
                j += 1
            elif (lWord[j] == 'X'):
                lWord = list(lWord)
                lWord[j] = 'F'
                lWord = "".join(lWord)
                j += 1
                lWord = lWord[:j] + '+[[X]-X]-F[-FX]+X' + lWord[j:]
                j += 17
            j += 1
    return lWord

word = generateTree(SIZE)
print(word)

exs = []

t.speed(0)
t.begin_poly()
t.color('red', 'yellow')
xinit, yinit = t.pos()
angle = 90
t.setheading(angle)
t.penup()
t.backward(350)
t.pendown()
xinit, yinit = t.pos()
#begin draw
for i in range(1):
    t.setheading(angle)
    t.penup()
    t.setpos(xinit, yinit)
    t.pendown()
    for letter in word:
        if letter == 'F':
            t.forward(5)        
        elif letter == '-':
            t.left(25)
        elif letter == '+':
            t.right(25)
        elif letter == '[':
            a = t.heading()
            x, y = t.pos()
            exs.append([a, x, y])        
        elif letter == ']':
            a, x, y = exs.pop()
            t.setheading(a)
            t.penup()
            t.setpos(x, y)
            t.pendown()
    angle += 10
#end
t.hideturtle()
t.end_poly()
t.done()
