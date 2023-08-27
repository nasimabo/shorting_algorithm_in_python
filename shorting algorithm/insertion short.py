def insertionshort(L):
    n = len(L)
    for i in range(1,n):
        item = L[i]
        j = i-1

        while j>=0 and L[j] > item:
            L[j+1] = L[j]
            j = j-1
        L[j+1] = item

if __name__ == "__main__":
    L = [8,2,4,6,7,3,9,1]
    print("Before this list: ",L)
    insertionshort(L)
    print("After this list: ",L)
