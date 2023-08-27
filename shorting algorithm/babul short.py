"""def babulshort(L):
    n = len(L)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
if __name__ == "__main__":
    L = [4,8,7,5,6,2,1,9,3]
    print("Before this list:",L)
    babulshort(L)
    print("After this list:",L)"""



def babulshort(L):
    n = len(L)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if L[j] < L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]


if __name__ == "__main__":
    L = [4,6,7,9,1,3,8,2,5]
    print("Before this list: ",L)
    babulshort(L)
    print("After this list: ",L)






    
