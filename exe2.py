import copy
class Calculate_Matrix:
    def __init__(self,m1In,m2In):
        self.m1 = copy.deepcopy(m1In)
        self.m2 = copy.deepcopy(m2In)
        sameLevel = self.check_matrixs_same_level()
        if sameLevel == True:
            sum = self.find_sum()
            print('Sum 2 matrixs : '+str(sum))
            product = self.find_product()
            print('Product 2 matrixs : '+ str(product))
        else:
            print('matrix m1, m2 have to be same level')
            exit()

    def find_sum(self):
        size = len(self.m1)
        result=[[0]*size, [0]*size]
        for i in range(0,size):
            for j in range (0,size):
                result[i][j] = self.m1[i][j] + self.m2[i][j]
        return result
    
    def find_product(self):
        size = len(self.m1)
        result=[[0]*size,[0]*size]
        for i in range(0,size):
            for k in range (0,size):
                result[i][k] =0
                for j in range(0,size):
                    result[i][k] = result[i][k] + self.m1[i][j]*self.m2[j][k]
        return result
    
    def check_matrixs_same_level(self):
        m1Width = len(self.m1)
        m2Width = len(self.m2)
        if m1Width == m2Width:
            return True
        else:
            return False

class Matrix:
    def __init__(self, matrixIn):
        self.matrix = matrixIn[:]
        squareMatrix = self.check_square_matrix()
        if squareMatrix == False:
            print('Matrix have to be square')
            exit()

    def get_matrix(self):
        matrixOut = copy.deepcopy(self.matrix)
        return matrixOut

    def find_det(self):
        matrixNew = copy.deepcopy(self.matrix)
        det=1
        counter=0
        size = len(matrixNew)
        cache=[None]*size
        cache2=[None]*size
        kt=0
        for i in range(0,size-1):
            if matrixNew[i][i] == 0:
                kt=0
                for j in range(0, size):
                    if matrixNew[i][j] !=0:
                        for k in range(0,size):
                            cache[k] = matrixNew[k][i]
                            matrixNew[k][i] = matrixNew[k][j]
                            matrixNew[k][j] = cache[k]
                        counter+=1
                        kt+=1
                        break
                if kt==0: return 0
            cache2[i]=matrixNew[i][i]
            for j in range(0,size):
                matrixNew[i][j] = matrixNew[i][j]/cache2[i]
                
            for j in range(i+1, size):
                h = matrixNew[j][i]
                for k in range(0, size):
                    matrixNew[j][k] = matrixNew[j][k] - h*matrixNew[i][k]
        #cache2[1]=0
        cache2[size-1]=matrixNew[size-1][size-1]
        for i in range(0, size):
            det = det*cache2[i]
        if counter%2 == 0:
            return det
        else:
            return -det     
    
    def check_square_matrix(self):
        if len(self.matrix) == len(self.matrix[0]):
            return True
        else:
            return False


m1=Matrix([[1,1],[2,2]])
matrix1 = m1.get_matrix()
print('Matrix m1 : '+str(matrix1))

m2=Matrix([[1,2],[3,4]])
matrix2 = m2.get_matrix()
print('matrix m2 :' + str(matrix2))

print ('det m1 : '+str(m1.find_det()))
print ('det m2 : '+str(m2.find_det()))
if(m1.find_det()>m2.find_det()):
    print("m1 > m2")
elif(m1.find_det()<m2.find_det()):
    print("m1 < m2")
else:
    print("m1 = m2")

calMatrix = Calculate_Matrix(matrix1, matrix2)



