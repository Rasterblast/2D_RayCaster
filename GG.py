from Processing import *
from Graphics import *
from random import *
window(500,500)
s=15
#background(255)
#fill(255)
#ellipse(250,250,s,s)
#mouseEnter = False
#Store the x-coordinates and y-coordinates of the segments of my pologyons and the walls
segmentX = []
segmentY = []
slopeX = []
slopeY = []
vectorX=[]
vectorY=[]
vectorX2=[]
vectorY2=[]
vectorX3=[]
vectorY3=[]
vectorX4=[]
vectorY4=[]
vectorX5=[]
vectorY5=[]

slopeRight=[]
slopeLeft=[]
slopeRight2=[]
slopeLeft2=[]
slopeRight3=[]
slopeLeft3=[]
slopeRight4=[]
slopeLeft4=[]
slopeRight5=[]
slopeLeft5=[]


#Beginning of ray
originX = mouseX()
originY = mouseY()
originX2 = mouseX()
originY2 = mouseY()
originX3=mouseX()
originY3=mouseY()
originX4=mouseX()
originY4=mouseY()
originX5=mouseX()
originY5=mouseY()

def triangles(x1,y1,x2,y2,x3,y3):
    global segmentX,segmentY,slopeX,slopeY
    triangle(x1,y1,x2,y2,x3,y3)
    segmentX.append(x1)
    segmentX.append(x2)
    segmentX.append(x3)
    
    segmentY.append(y1)
    segmentY.append(y2)
    segmentY.append(y3)

    slopeX=slopeX + [x2-x1,x3-x2,x1-x3]
    slopeY=slopeY + [y2-y1,y3-y2,y1-y3]

def quadcore(x1,y1,x2,y2,x3,y3,x4,y4):
    global segmentX,segmentY,slopeX,slopeY
    quad(x1,y1,x2,y2,x3,y3,x4,y4)
    segmentX.append(x1)
    segmentX.append(x2)
    segmentX.append(x3)
    segmentX.append(x4)
    
    segmentY.append(y1)
    segmentY.append(y2)
    segmentY.append(y3)
    segmentY.append(y4)   
          
    slopeX=slopeX + [x2-x1,x3-x2,x4-x3,x1-x4]            
    slopeY=slopeY + [y2-y1,y3-y2,y4-y3,y1-y4]
    
def recttails(x,y,w,h):
    global segmentX,segmentY,slopeX,slopeY
    rect(x,y,w,h)
    segmentX.append(x)
    segmentX.append(x+w)
    segmentX.append(x)
    segmentX.append(x+w)
    
    segmentY.append(y)
    segmentY.append(y)
    segmentY.append(y+h)
    segmentY.append(y+h)
    
    slopeX=slopeX + [w,0,0, -w]
    slopeY=slopeY + [0,h,-h, 0]

def draw():
    #global w,h, mouseEnter
    #if(mouseX()<500 and mouseX()>0 and mouseY()>0 and mouseY()<500):
    #    mouseEnter = True
    #if(mouseEnter == True):
    #    background(255)
    #    fill(255)
    #    ellipse(mouseX(),mouseY(),w,h) 
    global segmentX,segmentY,slopeX,slopeY,vectorX,vectorY,slopeLeft,slopeRight
    global vectorX2, vectorY2, slopeRight2, slopeLeft2
    global vectorX3, vectorY3, slopeRight3, slopeLeft3
    global vectorX4, vectorY4, slopeRight4, slopeLeft4
    global vectorX5, vectorY5, slopeRight5, slopeLeft5
    originX = mouseX()
    originY = mouseY()
    originX2 = mouseX()+6
    originY2 = mouseY()+6
    originX3= mouseX()-6
    originY3=mouseY()+6
    originX4=mouseX()+6
    originY4=mouseY()-6
    originX5=mouseX()-6
    originY5=mouseY()-6
    
    segmentX=[]
    segmentY=[]
    slopeX=[]
    slopeY=[]
    vectorX=[]
    vectorY=[]
    vectorX2=[]
    vectorY2=[]
    vectorX3=[]
    vectorY3=[]
    vectorX4=[]
    vectorY4=[]
    vectorX5=[]
    vectorY5=[]
    
    slopeRight=[]
    slopeLeft=[]
    slopeRight2=[]
    slopeLeft2=[]
    slopeRight3=[]
    slopeLeft3=[]
    slopeRight4=[]
    slopeLeft4=[]
    slopeRight5=[]
    slopeLeft5=[]
    
    background(0)
    fill(0)
    stroke(255)
    quadcore(0, 0, 0, 500, 500, 500, 500, 0)
    recttails(50,50,60,70)
    
    fill(0)
    stroke(255)
    triangles(250, 400, 350, 380, 400, 400)
    
    fill(0)
    stroke(255)
    quadcore(336, 320, 329, 309, 330, 340, 429, 330)
    
    fill(0)
    stroke(255)
    triangles(100, 350, 110, 200, 170, 265)
    
    
    
    #this is the orgin
    fill(255)
    ellipse(originX,originY,10,10)
    closest = 0
    
    
    
    #end of ray
    
    
    ##This is a brand new direction vector of the ray##
    for i in range(len(segmentX)):
        #vectorX.append(segmentX[i]-mouseX())
        #vectorY.append(segmentY[i]-mouseY())
        vectorX5.append(segmentX[i]-originX5-.00001)
        vectorY5.append(segmentY[i]-originY5-.00001)
        vectorX5.append(segmentX[i]-originX5+.00001)
        vectorY5.append(segmentY[i]-originY5+.00001)
        
    closest = 0
    for h in range(len(vectorX5)):
        endX=originX5
        endY=originY5
        smallest = 1000000000000000002
        for i in range(len(segmentX)):
            #coordinates of a point in a polygon
            s_px = segmentX[i]
            s_py = segmentY[i]
            #vector off that point, making a side of the polygon
            s_dx = slopeX[i]
            s_dy = slopeY[i]
            if (not(((s_dx*vectorY5[h] - s_dy*vectorX5[h]) == 0) or (vectorX5[h] == 0))):
                T2 = (vectorX5[h]*(s_py-originY5) + vectorY5[h]*(originX5-s_px))/(s_dx*vectorY5[h] - s_dy*vectorX5[h])
                T1 = (s_px+s_dx*T2-originX5)/(vectorX5[h])
                if(0<=T2<=1):
                    if(0<=T1<=smallest):
                        closest = i
                        smallest = T1
                        endX = s_px+s_dx*T2
                        endY = s_py+s_dy*T2   
        stroke(0) 
        #line(originX,originY,endX,endY)
        if (vectorX5[h] > 0):
            slopeRight5.append([endX, endY, (vectorY5[h]/vectorX5[h])])
        else:
            slopeLeft5.append([endX, endY, (vectorY5[h]/vectorX5[h])])
    slopeRight5=sorted(slopeRight5, key= lambda sloped:sloped[2])
    slopeLeft5=sorted(slopeLeft5, key= lambda sloped:sloped[2])+slopeRight5
    fill(0)
    for i in range(len(slopeLeft5)):
        triangle(originX5, originY5, slopeLeft5[i][0], slopeLeft5[i][1], slopeLeft5[(i+1)%len(slopeLeft5)][0], slopeLeft5[(i+1)%len(slopeLeft5)][1]+.00000000001)
    
    
    
    
    ##ALL NEW direction vector of the ray##
    for i in range(len(segmentX)):
        #vectorX.append(segmentX[i]-mouseX())
        #vectorY.append(segmentY[i]-mouseY())
        vectorX4.append(segmentX[i]-originX4-.00001)
        vectorY4.append(segmentY[i]-originY4-.00001)
        vectorX4.append(segmentX[i]-originX4+.00001)
        vectorY4.append(segmentY[i]-originY4+.00001)
        
    closest = 0
    for h in range(len(vectorX4)):
        endX=originX4
        endY=originY4
        smallest = 1000000000000000002
        for i in range(len(segmentX)):
            #coordinates of a point in a polygon
            s_px = segmentX[i]
            s_py = segmentY[i]
            #vector off that point, making a side of the polygon
            s_dx = slopeX[i]
            s_dy = slopeY[i]
            if (not(((s_dx*vectorY4[h] - s_dy*vectorX4[h]) == 0) or (vectorX4[h] == 0))):
                T2 = (vectorX4[h]*(s_py-originY4) + vectorY4[h]*(originX4-s_px))/(s_dx*vectorY4[h] - s_dy*vectorX4[h])
                T1 = (s_px+s_dx*T2-originX4)/(vectorX4[h])
                if(0<=T2<=1):
                    if(0<=T1<=smallest):
                        closest = i
                        smallest = T1
                        endX = s_px+s_dx*T2
                        endY = s_py+s_dy*T2   
        stroke(81) 
        #line(originX,originY,endX,endY)
        if (vectorX4[h] > 0):
            slopeRight4.append([endX, endY, (vectorY4[h]/vectorX4[h])])
        else:
            slopeLeft4.append([endX, endY, (vectorY4[h]/vectorX4[h])])
    slopeRight4=sorted(slopeRight4, key= lambda sloped:sloped[2])
    slopeLeft4=sorted(slopeLeft4, key= lambda sloped:sloped[2])+slopeRight4
    fill(81)
    for i in range(len(slopeLeft4)):
        triangle(originX4, originY4, slopeLeft4[i][0], slopeLeft4[i][1], slopeLeft4[(i+1)%len(slopeLeft4)][0], slopeLeft4[(i+1)%len(slopeLeft4)][1]+.00000000001)
    
    
    
    ##the direction vector of the ray##
    for i in range(len(segmentX)):
        #vectorX.append(segmentX[i]-mouseX())
        #vectorY.append(segmentY[i]-mouseY())
        vectorX3.append(segmentX[i]-originX3-.00001)
        vectorY3.append(segmentY[i]-originY3-.00001)
        vectorX3.append(segmentX[i]-originX3+.00001)
        vectorY3.append(segmentY[i]-originY3+.00001)
        
    closest = 0
    for h in range(len(vectorX3)):
        endX=originX3
        endY=originY3
        smallest = 1000000000000000002
        for i in range(len(segmentX)):
            #coordinates of a point in a polygon
            s_px = segmentX[i]
            s_py = segmentY[i]
            #vector off that point, making a side of the polygon
            s_dx = slopeX[i]
            s_dy = slopeY[i]
            if (not(((s_dx*vectorY3[h] - s_dy*vectorX3[h]) == 0) or (vectorX3[h] == 0))):
                T2 = (vectorX3[h]*(s_py-originY3) + vectorY3[h]*(originX3-s_px))/(s_dx*vectorY3[h] - s_dy*vectorX3[h])
                T1 = (s_px+s_dx*T2-originX3)/(vectorX3[h])
                if(0<=T2<=1):
                    if(0<=T1<=smallest):
                        closest = i
                        smallest = T1
                        endX = s_px+s_dx*T2
                        endY = s_py+s_dy*T2   
        stroke(162) 
        #line(originX,originY,endX,endY)
        if (vectorX3[h] > 0):
            slopeRight3.append([endX, endY, (vectorY3[h]/vectorX3[h])])
        else:
            slopeLeft3.append([endX, endY, (vectorY3[h]/vectorX3[h])])
    slopeRight3=sorted(slopeRight3, key= lambda sloped:sloped[2])
    slopeLeft3=sorted(slopeLeft3, key= lambda sloped:sloped[2])+slopeRight3
    fill(162)
    for i in range(len(slopeLeft3)):
        triangle(originX3, originY3, slopeLeft3[i][0], slopeLeft3[i][1], slopeLeft3[(i+1)%len(slopeLeft3)][0], slopeLeft3[(i+1)%len(slopeLeft3)][1]+.00000000001)
    
    #####other ray#####
    
    for i in range(len(segmentX)):
        #vectorX.append(segmentX[i]-mouseX())
        #vectorY.append(segmentY[i]-mouseY())
        vectorX2.append(segmentX[i]-originX2-.00001)
        vectorY2.append(segmentY[i]-originY2-.00001)
        vectorX2.append(segmentX[i]-originX2+.00001)
        vectorY2.append(segmentY[i]-originY2+.00001)
        
    closest = 0
    for h in range(len(vectorX2)):
        endX=originX2
        endY=originY2
        smallest = 1000000000000000001
        for i in range(len(segmentX)):
            #coordinates of a point in a polygon
            s_px = segmentX[i]
            s_py = segmentY[i]
            #vector off that point, making a side of the polygon
            s_dx = slopeX[i]
            s_dy = slopeY[i]
            if (not(((s_dx*vectorY2[h] - s_dy*vectorX2[h]) == 0) or (vectorX2[h] == 0))):
                T2 = (vectorX2[h]*(s_py-originY2) + vectorY2[h]*(originX2-s_px))/(s_dx*vectorY2[h] - s_dy*vectorX2[h])
                T1 = (s_px+s_dx*T2-originX2)/(vectorX2[h])
                if(0<=T2<=1):
                    if(0<=T1<=smallest):
                        closest = i
                        smallest = T1
                        endX = s_px+s_dx*T2
                        endY = s_py+s_dy*T2   
        stroke(209) 
        #line(originX,originY,endX,endY)
        if (vectorX2[h] > 0):
            slopeRight2.append([endX, endY, (vectorY2[h]/vectorX2[h])])
        else:
            slopeLeft2.append([endX, endY, (vectorY2[h]/vectorX2[h])])
    slopeRight2=sorted(slopeRight2, key= lambda sloped:sloped[2])
    slopeLeft2=sorted(slopeLeft2, key= lambda sloped:sloped[2])+slopeRight2
    fill(209)
    for i in range(len(slopeLeft2)):
        triangle(originX2, originY2, slopeLeft2[i][0], slopeLeft2[i][1], slopeLeft2[(i+1)%len(slopeLeft2)][0], slopeLeft2[(i+1)%len(slopeLeft2)][1]+.00000000001)
#################other direction of ray###########################
    for i in range(len(segmentX)):
        vectorX.append(segmentX[i]-mouseX()-.00001)
        vectorY.append(segmentY[i]-mouseY()-.00001)
        vectorX.append(segmentX[i]-mouseX()+.00001)
        vectorY.append(segmentY[i]-mouseY()+.00001)
        
    closest = 0
    for h in range(len(vectorX)):
        endX=originX
        endY=originY
        smallest = 100000000000000000000
        for i in range(len(segmentX)):
            #coordinates of a point in a polygon
            s_px = segmentX[i]
            s_py = segmentY[i]
            #vector off that point, making a side of the polygon
            s_dx = slopeX[i]
            s_dy = slopeY[i]
            if (not(((s_dx*vectorY[h] - s_dy*vectorX[h]) == 0) or (vectorX[h] == 0))):
                T2 = (vectorX[h]*(s_py-originY) + vectorY[h]*(originX-s_px))/(s_dx*vectorY[h] - s_dy*vectorX[h])
                T1 = (s_px+s_dx*T2-originX)/(vectorX[h])
                if(0<=T2<=1):
                    if(0<=T1<=smallest):
                        closest = i
                        smallest = T1
                        endX = s_px+s_dx*T2
                        endY = s_py+s_dy*T2   
        stroke(255) 
        #line(originX,originY,endX,endY)
        if (vectorX[h] > 0):
            slopeRight.append([endX, endY, (vectorY[h]/vectorX[h])])
        else:
            slopeLeft.append([endX, endY, (vectorY[h]/vectorX[h])])
    slopeRight=sorted(slopeRight, key= lambda sloped:sloped[2])
    slopeLeft=sorted(slopeLeft, key= lambda sloped:sloped[2])+slopeRight
    fill(255)
    for i in range(len(slopeLeft)):
        triangle(originX, originY, slopeLeft[i][0], slopeLeft[i][1], slopeLeft[(i+1)%len(slopeLeft)][0], slopeLeft[(i+1)%len(slopeLeft)][1]+.00000000001)
     
          
frameRate(15)
onLoop += draw
loop()        