############# small to big ################
def selectionshort(L):
    n = len(L)

    for i in range(0,n-1):
        index_min = i
        for j in range(i+1,n):
            if L[j] < L[index_min]:
                index_min = j
        if index_min != i:
            L[i],L[index_min] = L[index_min],L[i]

if __name__ == "__main__":
    
    L = [5,6,8,4,9,2,7,3,1]
    print("Before the list",L)
    result = selectionshort(L)
    print("After the list",result,L)

############### big to small #############

def selectionshort(L):
    n = len(L)
    for i in range(0,n-1):
        index_min = i
        for j in range(i+1,n):
            if L[j] > L[index_min]:
                index_min = j
        if index_min != i:
            L[i],L[index_min] = L[index_min],L[i]

if __name__ == "__main__":
    L = [4,7,9,6,3,5,8,2]
    print("Before this list: ",L)
    result = selectionshort(L)
    print("After this list:",L,result)
            
