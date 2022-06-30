def gridPlay(l):
    l1=[[0 for i in range(len(l[0]))]for j in range(len(l))]
    m=len(l)
    #m is the number of rows in matrix l1
    if m==0:
        return 0
    else:
        n=len(l[0])
        #n is the number of columns in matrix l1
        if n==0:
            return 0
        else:
            for i in range(2,m+1):
                l1[-i][-1]=l1[-i+1][-1]+l[-i+1][-1]
                #Last column of matrix l1 now stores the minimum penalty require to reach the (m-1,n-1) cell from the cell in which penalty is stored
            for j in range(2,n+1):
                l1[-1][-j]=l1[-1][-j+1]+l[-1][-j+1]
                #Last row of matrix l1 now stores the minimum penalty require to reach the (m-1,n-1) cell from the cell in which penalty is stored
            for x in range(2,n+1):
                for y in range(2,m+1):
                    #INV is that the matrix l1 upto column index (-x+1) and row  index (-y+1) contains the minimum penalty require to reach the (m-1,n-1) cell from the cell in which penalty is stored
                    l1[-y][-x]=min(l1[-y+1][-x]+l[-y+1][-x],l1[-y][-x+1]+l[-y][-x+1],l1[-y+1][-x+1]+l[-y+1][-x+1])
            #Finally matrix l1 stores the minimum penalty required to go from the particular cell to the lowermost rightmost cell for full matrix
            return l1[0][0]+l[0][0]
            #l1[0][0] denotes minimum penalty to go from first cell to last cell and l[0][0] is the penalty to step on first cell





def checklist(L,x):
    for i in range(len(L)):
        if x==L[i]:
            #x is found in list L 
            return True
    #Full list L is searched and x is not found in it
    return False
def stringProblem(A,B):
    l=[[0 for i in range(len(A)+1)]for j in range(len(B)+1)]
    l1=["a","e","i","o","u"]
    #l1 is the list of vowels
    for i in range(len(B)+1):
        l[i][0]=i
        #First column of matrix l now contain the minimum possible ways to convert A[:0] to B[:i] in cell (i,0) [where 0<=i<=m] based on given constraints
    for j in range(len(A)+1):
        l[0][j]=j
        #First row of matrix l now contain the minimum possible ways to convert A[:j] to B[:0] in cell (0,j) [where 0<=j<=n]based on given constraints
    for n in range(1,len(A)+1):
        for m in range(1,len(B)+1):
            #INV is that the matrix l upto column index (n-1) and row index (m-1) stores the minimum possible ways to convert A[:j] to B[:i] in the cell (i,j) [where (0<=i<=m-1),(0<=j<=n-1)] based on given constraints
            if A[n-1]==B[m-1]:
                l[m][n]=l[m-1][n-1]
            elif checklist(l1,A[n-1])==False:
                l[m][n]=min(l[m-1][n]+1,l[m][n-1]+1,l[m-1][n-1]+1)
            elif checklist(l1,A[n-1]) and checklist(l1,B[m-1]):
                l[m][n]=min(l[m-1][n]+1,l[m][n-1]+1,l[m-1][n-1]+1)
            else:
                l[m][n]=min(l[m-1][n]+1,l[m][n-1]+1)
    #Finally matrix l is now completed 
    return l[-1][-1]







def checkLyear(n):
#checkLyear checks whether n is leap year or not
    if n%400==0:
        return True
    elif n%100==0:
        return False
    elif n%4==0:
        return True
    else:
        return False
def janday(n):
    #Finds the day of 1st january as a number from 0 to 6
    if (n//100)%4==0 and checkLyear(n):
        d=(n%100)//4+(n%100)%7-1
        d=(d-1)%7
    elif (n//100)%4==0:
        d=(n%100)//4+(n%100)%7
        d=(d-1)%7
    elif (n//100)%4!=0  and checkLyear(n):
        i=(n//100)%4
        d=(n%100)//4+(n%100)%7+2*i-2
        d=(d-1)%7
    else:
        i=(n//100)%4
        d=(n%100)//4+(n%100)%7+2*i-1
        d=(d-1)%7
    return d 
def mlist(n):
    if checkLyear(n):
        l=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        l=[31,28,31,30,31,30,31,31,30,31,30,31]
    return l
    
def printCalendar(n):
    sweek="M  T  W  T  F  S  S"
    mname=["          -JANUARY-        ","       -FEBRUARY-       ","        -MARCH-","           -APRIL-         ","         -MAY-         ","          -JUNE-","           -JULY-         ","         -AUGUST-        ","       -SEPTEMBER-","          -OCTOBER-        ","       -NOVEMBER-      ","        -DECEMBER-"]
    dc=[janday(n),(janday(n)+6+mlist(n)[1]%7)%7,(janday(n)+6+mlist(n)[1]%7)%7,(janday(n)+mlist(n)[1]%7)%7]
    l=[]
    s=""
    for i in range(38):
        if i<37:
            s+=" "
        else:
            s+=str(n)
    l.append(s)
    for e in range(4):
        s1=""
        for i in range(3*e,3*e+3):
            s1+=mname[i]
        l.append(s1)
        s2=""
        for i in range(3):
            s2+="     "
            s2+=sweek
        l.append(s2)
        s3=""
        l1=[]
        d=dc[e]
        for i in range(3):
            s3+="   "
            k=1
            for j in range(7):
                if j<d:
                    s3+="   "
                else:
                    s3+="  "
                    s3+=str(k)
                    k+=1
            l1.append(k)
            d=(d+mlist(n)[3*e+i])%7
        l.append(s3)
        while l1!=[mlist(n)[3*e]+1,mlist(n)[3*e+1]+1,mlist(n)[3*e+2]+1]:
            s4=""
            for i in range(3):
                s4+="   "
                k=l1[i]
                for j in range(7):
                    if k>mlist(n)[3*e+i]:
                        s4+="   "
                        continue
                    elif k//10==0:
                        s4+="  "
                    else:
                        s4+=" "
                    s4+=str(k)
                    k+=1
                l1[i]=k
            l.append(s4)
    f=open("calendar.txt","w+")
    for i in l:
        f.write(i+"\n")
    f.close()
