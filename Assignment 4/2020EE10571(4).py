def checklist(L,x):
    for i in range(len(L)):
        if L[i]==x:
            #INV that L[0:i]doesn't contain x
            return True
    #Finally if L[i] is equal to x then true else if loop ends with no L[i] equal to x then false        
    return False

def readNumber(s,i):
    l1 = ["*","+","-","/","(",")"]
    #assert: list l1 contains the string elements which mark the end of a particular number
    k=i
    while checklist(l1,s[k])==False:
        #INV is that string s[i:k] doesn't contain any element present in list l1 
        k+=1
        if k==len(s):
            break
    # Finally s[i:k] contains the number with starting index i and k is the index of the element after that number
    return (float(s[i:k]),k)
def evalParen(s,i):
    a1,b1=readNumber(s,i+1)
    #assert: a1 is the number starting from index i+1 and b1 is the index of element just before which number ends
    a2,b2=readNumber(s,b1+1)
    #assert: a2 is the number starting from index b1+1 and b2 is the index of element just before which number ends
    #assert: s[b1] is the operator between the two numbers
    if "*"==s[b1]:
        return (a1*a2,b2+1)
    elif "+"==s[b1]:
        return (a1+a2,b2+1)
    elif "-"==s[b1]:
        return (a1-a2,b2+1)
    elif "/"==s[b1]:
        return (a1/a2,b2+1)
def evaluate(s):
    m=-1
    for i in range(len(s)):
        #INV is that m is the index of last opening parenthesis in strings[0:i]
        if s[i]=="(":
            m=i
        elif s[i]==")":
            break
        #Finally m is the index of innermost opening parenthesis bracket and no more bracket is present in that parenthesis
    if m==-1:
        a,b=evalParen(s,-1)
        return a
    else:
        a,b=evalParen(s,m)
        #assert: a is the number which resulted after calculating innermost bracket in string s
        #assert: b is the index of the element present just after the innermost bracket 
        s1=s[0:m]+str(a)+s[b:]
        return evaluate(s1)







def sumSequence(n):
    if n==1:
        return [1]
    elif n==2:
        return [1,2]
    else:
        L=[1,2]
        for i in range(3,n+1):
            #INV that L is the list of sequence containing first i-1 terms of sequence
            c = 1
            count = 0
            while count != 1:
                #assert: n is the possible number which can be the next element of the list L (initialised from 0)
                #assert: c is the amount by which n is greater than last element of L (initialised from 1)
                n = L[-1]+c
                k = 1
                while k<(n+1)//2:
                    #assert: k is basically the number which is added to n-k to yield n (initialised from 1)
                    #INV that count is the number of ways n can be written as sum of two distinct numbers from list L for some k
                    if count > 1:
                        break
                    elif checklist(L,k) and checklist(L,n-k):
                        count+=1
                        k+=1
                    else:
                        k+=1
                #Finally count is number of ways n can be written as sum of two distinct numbers from list
                if count==1:
                    L.append(n)
                else:
                    c+=1
                    count=0
        #Finally L is the list containing first n elements of the given sequence
        return L








def add(L):
    s=0
    for i in range(len(L)):
        #INV that s is sum of all elements of list L[0:i]
        s+=L[i]
    #Finally s is the sum all elements of list L
    return s
def  minLength(A,n):
    if n<0:
        return 0
    else:
        c=1
        #assert: c is initialised from 1
        while c<=len(A):
            #INV that there is no contiguous sublist with length less than of c that can sum greater than n
            k=0
            while (k+c)<=len(A):
                #assert: k is the starting index of the list whose sum is to be compared with n
                if add(A[k:k+c])>n:
                    #Finally c is the minimum length of contiguous sublist which can sum strictly greater than n
                    return c
                else:
                    k+=1
            c+=1
        #Finally no such c is possible such that contiguous sublist sum strictly greater than n
        return -1









# Merges two subarrays of arr[] write the output to b[l:r]
# First subarray is arr[l:m] # Second subarray is arr[m:r]
def mergeAB(arr,b,l,m,r):
    i = l
    j = m
    k = l
    while i < m and j < r:
        if arr[i]<= arr[j]:
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]
            j += 1
        k += 1
    # Copy the remaining elements of arr[i:m], if there are	any
    while i < m:
        b[k] = arr[i]
        i += 1
        k += 1
    # Copy the remaining elements of arr[j:r], if there are	any
    while j < r:
        b[k] = arr[j]
        j += 1
        k += 1
def mergeIt(A,B,n,l):
# A of size n consists of n/l sorted lists of size l each [last list may be shorter]
# merge them in pairs writing the result to B [there may be one unpaired if not even]

    right = 0
    if n % l == 0:
        count = n // l
    else:
        count = n // l + 1
    for i in range(count // 2):
        left = i * l * 2
        right = min(left + (2 * l), n)
        mergeAB(A, B, left, left + l, right)
    # Copy the last list if there is any (may happen if count is odd) 

    for i in range(right, n):
        B[i] = A[i]
def mergeSort(A):
    n = len(A)
    l = 1
    B = [0 for x in range(n)]
    dir = 0
    while l < n:
        if dir == 0:
            mergeIt(A, B, n, l)
            dir = 1
        else:
            mergeIt(B, A, n, l)
            dir = 0
        l *= 2
    #if result is in B copy result to A
    if dir == 1:
        for i in range(n):
            A[i] = B[i]
def mergeContacts(L):
    mergeSort(L)
    #assert: L is now the sorted list according to the name of the people
    L1=[(L[0][0],[L[0][1]])]
    #L1 is established and initiated
    for i in range(1,len(L)):
        #INV is that L1 is the mergeContacts list of the list L[0:i]
        if L[i][0]==L[i-1][0]:
            L1[-1][1].append(L[i][1])
        else:
            L1.append((L[i][0],[L[i][1]]))
    #Finally L1 is the mergeContacts list of the whole list L
    return L1









