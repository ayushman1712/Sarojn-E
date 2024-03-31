def count_less_equal(mid, arr):
    count = 0
    for num in arr:
        if num <= mid:
            count += 1
    return count

def count_elmnts_less_equal(mid, A, B, C):
    count = 0
    #print([A,B,C])
    for arr in [A, B, C]:
        count += count_less_equal(mid, arr)
    return count
 
def kth_smallestelmtn(A, B, C, k, n):
    low, high = 0, 3*n-1

    while low < high:
        mid = (low + high) // 2
        if mid>=n and mid<2*n:
            mid = mid%n
        elif(mid>=2*n):
            mid = mid%2*n
        count = count_elmnts_less_equal(mid, A, B, C)

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low

l = [1,3,6,8]
m = [2,4,7,9]
n = [0,10,12,13]

mid = kth_smallestelmtn(l,m,n,5,4)

print(mid)

if mid>=4 and mid<2*4:
            mid = mid%4
            print(m[mid])
elif(mid>=2*4):
            mid = mid%2*4
            print(n[mid])
else:
    print(l[mid])




