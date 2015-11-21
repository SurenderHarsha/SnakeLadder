import turtle as t
from random import randint as r
t.ht()
t.title("Snakes And Ladders")
t.bgcolor('white')
def getcor(number):
    p=number/10
    q=number%10
    if q==0:
        return (p-1,9)
    #print p,q-1
    return (p,q-1)
    
class Drw(object):
    def __init__(self):
        t.up()
        t.goto(-80,-80)
        t.down()
        t.speed(0)
        for k in range(-80,40*8,40):
            for j in range(-80,40*8,40):
            #a=turtle.pos()
                t.sety(j)
                t.setx(k)
                for i in range(4):
                    t.right(90)
                    t.forward(40)
        t.up()
        t.goto(-120,-120)
        self.ox=-120
        self.oy=-120
        self.snakes=[]
        self.ladders=[]
        self.tails=[]
        self.b={}
        self.up=[]
        for i in range(1,101):
            self.b[i]='-'
        t.down()
    def drawsnakes(self,n=6):
        t.up()
        t.goto(-120,-120)
        t.down()
        for i in range(n):
            c=0
            while c in self.snakes or c==0 or c in self.ladders or c in self.tails:
                c=r(21,99)
                continue
            #self.b[c]='s'
            self.snakes.append(c)
            s=0
            while s in self.ladders or s in self.snakes or s==0 or s>=c or s in self.tails:
                s=r(2,c-1)
                continue
            self.tails.append(s)
            self.b[c]=(c,s,'s')
            print c,s
            t.color('red')
            m=getcor(c)
            t.up()
            x=m[0]*40-120
            y=m[1]*40-120
            t.goto(-120,-120)
            
            t.goto(y,x)
            nx=x+40
            ny=y+40
            t.goto(float((ny+y)/2),float((nx+x)/2))
            t.down()
            t.dot(40)
            t.color('red')
            m=getcor(s)
            x=m[0]*40-120
            y=m[1]*40-120
            
            
            t.goto(y,x)
            nx=x+40
            ny=y+40
            t.goto(float((ny+y)/2),float((nx+x)/2))
            #t.down()
            t.color('gray')
            t.dot(40)
            t.up()
            t.goto(-120,-120)
    def drawladder(self,n=5):
        t.up()
        t.goto(-120,-120)
        t.down()
        for i in range(n):
            c=0
            while c in self.snakes or c==0 or c in self.ladders or c in self.up or c in self.tails:
                c=r(3,90)
                continue
            #self.b[c]='l'
            self.ladders.append(c)
            s=0
            while s in self.ladders or s==0 or s<=c or s in self.snakes or s in self.tails or s in self.up:
                s=r(c,99)
                continue
            
            self.b[c]=(c,s,'l')
            print c,s
            t.color('blue')
            m=getcor(c)
            t.up()
            x=m[0]*40-120
            y=m[1]*40-120
            t.goto(-120,-120)
            
            t.goto(y,x)
            nx=x+40
            ny=y+40
            t.goto(float((ny+y)/2),float((nx+x)/2))
            t.down()
            t.dot(40)
            t.color('blue')
            m=getcor(s)
            x=m[0]*40-120
            y=m[1]*40-120
            
            
            t.goto(y,x)
            nx=x+40
            ny=y+40
            t.goto(float((ny+y)/2),float((nx+x)/2))
            #t.down()
            t.color('yellow')
            t.dot(40)
            t.up()
            t.goto(-120,-120)
    def p1move(self,x,sp,iden):
        
         t.up()
         t.goto(-120,-120)
         if iden==None:
             t.up()
             t.color('green')
             m=getcor(x+sp)
             #print m[0],m[1]
             x=m[0]*40-120
             y=m[1]*40-120
             t.goto(y,x)
             nx=x+40
             ny=y+40
             t.goto(float((ny+y)/2),float((nx+x)/2))
             t.down()
             s=t.stamp()
             t.up()
             t.goto(-120,-120)
             return s
         else:
             t.clearstamp(iden)
             t.up()
             t.color('green')
             m=getcor(x+sp)
             x=m[0]*40-120
             y=m[1]*40-120
             t.goto(y,x)
             nx=x+40
             ny=y+40
             t.goto(float((ny+y)/2),float((nx+x)/2))
             #print x+sp
             t.down()
             s=t.stamp()
             t.up()
             t.goto(-120,-120)
             t.up()
             return s
        
    def p2move(self,x,sp,iden):
         t.up()
         t.goto(-120,-120)
         if iden==None:
             t.up()
             t.color('black')
             m=getcor(x+sp)
             #print x+sp
             x=m[0]*40-120
             y=m[1]*40-120
             t.goto(y,x)
             nx=x+40
             ny=y+40
             t.goto(float((ny+y)/2),float((nx+x)/2))
             t.down()
             s=t.stamp()
             t.up()
             t.goto(-120,-120)
             return s
         else:
             t.clearstamp(iden)
             t.up()
             t.goto(-120,-120)
             t.color('black')
             m=getcor(x+sp)
             #print x+sp
             x=m[0]*40-120
             y=m[1]*40-120
             t.goto(y,x)
             nx=x+40
             ny=y+40
             t.goto(float((ny+y)/2),float((nx+x)/2))
             t.down()
             s=t.stamp()
             t.up()
             t.goto(-120,-120)
             return s
                
    def chk(self,x):
        #print 'inside chk:'
        return self.b[x]
            
obj=Drw()
sn=int(raw_input('Enter the number of snakes, if the number is less than 3 or greater than 9. Default value 6 will be taken:'))
if sn<3 or sn>9:
    obj.drawsnakes()
else:
    obj.drawsnakes(sn)
ln=int(raw_input('Enter number of ladders,if the number is less than 0 or more than 6. Default value 5 will be taken:'))
if ln<0 or ln>6:
    obj.drawladder()
else:
    obj.drawladder(ln)
print "Snakes' mouth is denoted by RED, Snakes' tail is denoted by GREY. Ladders' foot is denoted by BLUE and top is denoted by WHITE"
print 'GAME BEGINS: Roll a Six to step into the game'
player1=None
player2=None
pc=0
p2c=0
flag=0
while 1:
    flag=0
    print 'Player 1, press r to throw the dice:'
    d=raw_input()
    if d!='r':
        print 'Wrong input! Throw again!'
        continue
    p=r(1,6)
    if pc+p>100:
        flag=1
        print 'no more steps to go, Player 2 turn'
    print p
    if flag==0:
        flag1=1
        player1=obj.p1move(pc,p,player1)
        pc=pc+p
        if pc==100:
            print 'Player 1 has WON!'
            break
        m=obj.chk(pc)
        if m=='-':
            flag1=0
        if flag1!=0:
            print m
            if m[2]=='l':
                print 'Its a ladder, Player 1 moves up!'
                pc=m[1]
                player1=obj.p1move(m[1],0,player1)
            if m[2]=='s':
                print 'Oh no its a snake! Player 1 falls down'
                pc=m[1]
                player1=obj.p1move(m[1],0,player1)
        
    print 'Player 1 current Position: '+str(pc)    
    flag=0        
    while 1:
        print 'Player 2, press r to throw dice:'
        d=raw_input()
        if d!='r':
            print 'Wrong input! Throw again!'
            continue
        else:
            break
    p2=r(1,6)
    print p2
    if p2c+p2>100:
        flag=1
        print 'no more steps to go, Player 1 turn'
    player2=obj.p2move(p2c,p2,player2)
    if flag==0:
        flag1=1
        player2=obj.p2move(p2c,p2,player2)
        p2c=p2c+p2
        if p2c==100:
            print 'Player 2 has WON!'
            break
        m=obj.chk(p2c)
        if m=='-':
            flag1=0
        if flag1!=0:
            print m
            if m[2]=='l':
                print 'Its a ladder, Player 2 moves up!'
                p2c=m[1]
                player2=obj.p2move(m[1],0,player2)
            if m[2]=='s':
                print 'Oh no its a snake! Player 2 falls down'
                p2c=m[1]
                player2=obj.p2move(m[1],0,player2)
    print 'Player 2 Current Position: '+str(p2c)
t.bye()    
    
