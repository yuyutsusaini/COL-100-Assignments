class Student:
    def __init__(self,entryNo,Course):
        self.entryNo=entryNo
        self._listofcourses=Course
        self.totquizl=[]
        self.attemptedquizl=[]
        for i in range(len(self._listofcourses)):
            for j in range(len(self._listofcourses[i]._quizlist)):
                self.totquizl.append((self._listofcourses[i].courseCode,self._listofcourses[i]._quizlist[j].title,self._listofcourses[i]._quizlist[j].correctop))
    def attempt(self, courseCode, quizTitle, attemptedAnswers):
        self.attemptedquizl.append((courseCode, quizTitle, attemptedAnswers))
        self.unattemptedquizl=[]
        for i in range(len(self.totquizl)):
            a1,b1,c1=self.totquizl[i]
            for j in range(len(self.attemptedquizl)):
                d=0
                a2,b2,c2=self.attemptedquizl[j]
                if (a1,b1) == (a2,b2):
                    d=1
                    break
            if d==0:
                self.unattemptedquizl.append((a1,b1))
    def TotalQuiz(self):
        return self.totquizl
    def getUnattemptedQuizzes(self):
        return self.unattemptedquizl
    def  getAverageScore(self,courseCode):
        self.nattqcc=0
        self.correctquizlno=0
        for i in range(len(self.totquizl)):
            a1,b1,c1=self.totquizl[i]
            for j in range(len(self.attemptedquizl)):
                a2,b2,c2=self.attemptedquizl[j]
                if a1==courseCode and a2==courseCode and b1==b2:
                    self.nattqcc+=1
                    for i in range(len(c1)):
                        if c2[i]==c1[i]:
                            self.correctquizlno+=1
                break
        return self.correctquizlno/self.nattqcc
        
            
        
        
class Course:
    def __init__(self,courseCode,Quiz):
        self.courseCode=courseCode
        self._quizlist=Quiz
class Quiz:
    def __init__(self,title,correctop):
        self.title=title
        self.correctop=correctop








class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    def rowcol(self):
        r=len(self.matrix)
        c=len(self.matrix[0])
        return (r,c)
    def __add__(self,m):
        a,b=self.rowcol()
        l=[[0 for j in range(b)]for i in range(a)]
        for i in range(a):
            for j in range(b):
                l[i][j]=self.matrix[i][j]+m.matrix[i][j]
        return Matrix(l)
    def __sub__(self,m):
        a,b=self.rowcol()
        l=[[0 for j in range(b)]for i in range(a)]
        for i in range(a):
            for j in range(b):
                l[i][j]=self.matrix[i][j]-m.matrix[i][j]
        return Matrix(l)
    def __str__(self):
        l=[]
        for j in range(len(self.matrix[0])):
            m=1
            for i in range(len(self.matrix)):
                m=max(m,len(str(self.matrix[i][j])))
            l.append(m)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                n=l[j]-len(str(self.matrix[i][j]))
                for k in range(n+1):
                    if k<n:
                        print(" ",end="")
                    else:
                        print(str(self.matrix[i][j]),end=" ")
            print("")
        return ""
    def __mul__(self,m):
        if isinstance(m,Matrix):
            l1=[[0 for i in range(len(m.matrix))]for j in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(m.matrix[0])):
                    for k in range(len(m.matrix)):
                        l1[i][j]+=(self.matrix[i][k]*m.matrix[k][j])
            return Matrix(l1)
        else:
            l1=[[0 for i in range(len(self.matrix[0]))]for j in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    l1[i][j]=m*self.matrix[i][j]
            return Matrix(l1)
                                
    def toSparse(self):
        l1=[[] for i in range(len(self.matrix))]
        for i in range(len(l1)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j]!=0:
                    l1[i].append((j,self.matrix[i][j]))
        return SparseMatrix(l1,len(l1),len(l1)[0])
class SparseMatrix:
    def __init__(self,sparsematrix,nrows,ncols):
        self.sparsematrix=sparsematrix
        self.nrows=nrows
        self.ncols=ncols
    def toDense(self):
        self.matrix=[[0 for i in range(self.ncols)]for j in range(self.nrows)]
        for i in range(len(self.sparsematrix)):
            for j in range(len(self.sparsematrix[i])):
                n=self.sparsematrix[i][j][0]
                self.matrix[i][n]=self.sparsematrix[i][j][1]
        return Matrix(self.matrix)
    def __str__(self):
        l=[]
        for j in range(len(self.toDense().matrix[0])):
            m=1
            for i in range(len(self.toDense().matrix)):
                m=max(m,len(str(self.toDense().matrix[i][j])))
            l.append(m)
        for i in range(len(self.toDense().matrix)):
            for j in range(len(self.toDense().matrix[0])):
                n=l[j]-len(str(self.toDense().matrix[i][j]))
                for k in range(n+1):
                    if k<n:
                        print(" ",end="")
                    else:
                        print(str(self.toDense().matrix[i][j]),end=" ")
            print("")
        return ""
    def __add__(self,m):
        l=[[]for a in self.sparsematrix]
        for i in range(len(self.sparsematrix)):
            k=0
            for j in range(len(self.sparsematrix[i])):
                if len(m.sparsematrix[i])==0:
                    l[i].append(self.sparsematrix[i][j])
                elif k==len(m.sparsematrix[i]):
                    l[i].append(self.sparsematrix[i][j])
                elif self.sparsematrix[i][j][0]!= m.sparsematrix[i][k][0]:
                    l[i].append(self.sparsematrix[i][j])
                else:
                    l[i].append((self.sparsematrix[i][j][0],self.sparsematrix[i][j][1]+m.sparsematrix[i][k][1]))
                    k+=1
                    
            for t in range(k,len(m.sparsematrix[i])):
                l[i].append(m.sparsematrix[i][t])
        return SparseMatrix(l,self.nrows,self.ncols)
    def __sub__(self,m):
        l=[[]for a in self.sparsematrix]
        for i in range(len(self.sparsematrix)):
            k=0
            for j in range(len(self.sparsematrix[i])):
                if len(m.sparsematrix[i])==0:
                    l[i].append(self.sparsematrix[i][j])
                elif k==len(m.sparsematrix[i]):
                    l[i].append(self.sparsematrix[i][j])
                elif self.sparsematrix[i][j][0]!= m.sparsematrix[i][k][0]:
                    l[i].append(self.sparsematrix[i][j])
                else:
                    l[i].append((self.sparsematrix[i][j][0],self.sparsematrix[i][j][1]-m.sparsematrix[i][k][1]))
                    k+=1
                    
            for t in range(k,len(m.sparsematrix[i])):
                l[i].append(m.sparsematrix[i][t])
        return SparseMatrix(l,self.nrows,self.ncols)
    def __mul__(self,m):
        if isinstance(m,SparseMatrix):
            l1=[[]for a in self.sparsematrix]
            l2=[]
            for a in range(len(m.sparsematrix)):
                if len(m.sparsematrix[a])==0:
                    l2.append([-1,-1])
                else:
                    l2.append([0,m.sparsematrix[a][0][0]])
            for i in range(len(self.sparsematrix)):
                c=0
                while c<m.ncols:
                    s=0
                    for j in range(len(self.sparsematrix[i])):
                        x=self.sparsematrix[i][j][0]
                        if l2[x][1]==c:
                            s+=self.sparsematrix[i][j][1]*m.sparsematrix[x][l2[x][0]][1]
                            l2[x][0]+=1
                            if l2[x][0]>=len(m.sparsematrix[x]):
                                l2[x][1]=-1
                            else:
                                l2[x][1]=m.sparsematrix[x][l2[x][0]][0]
                    
                    l1[i].append((c,s))
                    c+=1
            return SparseMatrix(l1,self.nrows,m.ncols)
        else:
            l1=[[]for a in self.sparsematrix]
            for i in range(len(self.sparsematrix)):
                for j in range(len(self.sparsematrix[i])):
                    l1[i].append((self.sparsematrix[i][j][0],self.sparsematrix[i][j][1]*m))
            return SparseMatrix(l1,self.nrows,self.ncols)








f=open("file.txt","r")
#file is opened
lines=f.readlines()
l=[]
for i in range(len(lines)):
    l.append(lines[i].split())
#matrix is formed from text file
def traverseMaze(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]=="S":
                strcor=(i,j) #Coordinates of Starting point are found
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]=="E":
                endcor=(i,j) #Coordinates of Starting point are found
    (i,j)=strcor
    (a,b)=endcor
    m1=[[i for i in a]for a in m]
    m1[i][j]="_"
    m1[a][b]="_"
    #A matrix duplicte to input matrix is formed with S and E replaced with _ and _
    l=[]
    #List l which will be returned at last is initialized
    while (i,j)!=endcor:
        if j+1<len(m[0]) and m1[i][j+1]=="_": #right element in the matrix is empty space
            m1[i][j]="X" #the element on which we were standing is replaced with a wall i.e X
            j+=1 #Coordinate is are changed and set to new coordinate where we are currently standing
            l.append("R") #l is now appended with "R" as move towards right
        elif i+1<len(m) and m1[i+1][j]=="_": #right element in the matrix is empty space
            m1[i][j]="X" #the element on which we were standing is replaced with a wall i.e X
            i+=1 #Coordinate is are changed and set to new coordinate where we are currently standing
            l.append("D") #l is now appended with "R" as move towards right
        elif j-1>=0 and m1[i][j-1]=="_": #right element in the matrix is empty space
            m1[i][j]="X" #the element on which we were standing is replaced with a wall i.e X
            j-=1 #Coordinate is are changed and set to new coordinate where we are currently standing
            l.append("L") #l is now appended with "R" as move towards right
        elif i-1>=0 and m1[i-1][j]=="_": #right element in the matrix is empty space
            m1[i][j]="X" #the element on which we were standing is replaced with a wall i.e X
            i-=1 #Coordinate is are changed and set to new coordinate where we are currently standing
            l.append("U") #l is now appended with "R" as move towards right
        elif len(l)==0: #if there is nowhere to go and l is also empty then we cannot reach end and hence break
            break
        else: #if there is nowhere to go but we can go backwards as l is not empty and find a new way from previous cells
            x=l.pop() #we move backwards therefore last element is removed
            m1[i][j]="X" #the element on which we were there is now replaced with wall i.e. X as it will not provide the way to end
            #below written conditions tells us when we go backwards in which direction we should go. Basically it is just reverse of the way we reached there.
            if x=="R":
                j-=1
                m1[i][j]="_"
            elif x=="D":
                i-=1
                m1[i][j]="_"
            elif x=="L":
                j+=1
                m1[i][j]="_"
            elif x=="U":
                i+=1
                m1[i][j]="_"
    #At last we got our list of direction we should follow to reach end. If there is no possibe way then list is empty.
    return l
print(traverseMaze(l))  #Input taken as text file is given as correct output
