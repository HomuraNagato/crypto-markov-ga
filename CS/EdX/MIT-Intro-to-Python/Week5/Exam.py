def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

l1 = search([], 1)
e1 = newsearch([], 1)

l2 = search([1,2,3,4,5], 3)
e2 = newsearch([1,2,3,4,5], 3)

l3 = search([2,3,4], 1)
e3 = newsearch([2,3,4], 1)

l4 = search([1,2,3,4], 6)
e4 = newsearch([1,2,3,4], 6)


print('search vs newsearch e=1 in empty list: ' + str(l1) + ' ' + str(e1))
print('search vs newsearch e=3 in list: ' + str(l2) + ' ' + str(e2))
print('search vs newsearch e=1 before list: ' + str(l3) + ' ' + str(e3))
print('search vs newsearch e=6 before list: ' + str(l4) + ' ' + str(e4))

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

swap1 = swapSort([1,4,2,3])
print("increasing " + str(swap1))


def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

swap2 = swapSort([1,4,2,3])
print("increasing " + str(swap2))