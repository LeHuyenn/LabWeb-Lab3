import math;
class Sphere:
    def __init__(self,r, x,y,z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volumn(self):
        v=(4/3)* (math.pi) * math.pow(self.r,3)
        return round(v,3)

    def get_square(self):
        s= 4*(math.pi)*math.pow(self.r,2)
        return round(s,3)

    def get_radius(self):
        return round(self.r,3)

    def get_center(self):
        return round(self.x,3),round(self.y,3), round(self.z,3)
    
    def set_radius(self,rIn):
        self.r=rIn

    def set_center(self, xIn,yIn,zIn):
        self.x=xIn
        self.y=yIn
        self.z=zIn

    def is_point_inside(self, xIn, yIn,zIn):
        distance = math.sqrt(math.pow((xIn-self.x),2)+math.pow((yIn-self.y),2)+math.pow((zIn-self.z),2))
        if distance>self.r:
            return False
        else:
            return True

ob=Sphere(4,5,3,2)
print ('->Volumn of sphere : '+str(ob.get_volumn()))
print('->Square : ' + str(ob.get_square()))
print('->radius of sphere : '+str(ob.get_radius()))
xOut,yOut,zOut = ob.get_center()
print('->\nX = '+str(xOut)+'\nY = '+str(yOut)+'\nZ = '+str(zOut))
ob.set_radius(14.6)
print('->Radius after set : '+str(ob.get_radius()))
ob.set_center(10,11,12)
xOut,yOut,zOut = ob.get_center()
print('->After set center\nX = '+str(xOut)+'\nY = '+str(yOut)+'\nZ = '+str(zOut))
xTest = 9
yTest = 11
zTest = 7
print('->Is point ('+str(xTest)+','+str(yTest)+','+str(zTest) +') inside sphere : '+str(ob.is_point_inside(xTest,yTest,zTest)))
xTest = 40
yTest = 28
zTest = -6
print('->Is point ('+str(xTest)+','+str(yTest)+','+str(zTest) +') inside sphere : '+str(ob.is_point_inside(xTest,yTest,zTest)))