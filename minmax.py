def minmax(A):
    minpos = A.index(min(A))
    maxpos = A.index(max(A))
    print('Min is at {0} and max is at {1}'.format(minpos+1, maxpos+1))
    

A = list()
n = int(input('No of elements :: '))
print('Enter the elements\n')
for i in range(0, n):
    k = int(input())
    A.append(k)
minmax(A)