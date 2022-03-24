### Dive and conquer방법으로 풀이 O(nlogn)만큼 걸린다.
import sys

def maxCrossingSum(arr, l, m, h):
    # Include elements on left of mid.
    sm = 0
    left_sum = -10000

    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if (sm > left_sum):
            left_sum = sm

    # Include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if (sm > right_sum):
            right_sum = sm

    # Return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2, 1]
    return max(left_sum + right_sum, left_sum, right_sum)


# Returns sum of maximum sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h):
    # Base Case: Only one element
    if (l == h):
        return arr[l]

    # Find middle point
    m = (l + h) // 2

    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #     subarray crosses the midpoint
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m + 1, h),
               maxCrossingSum(arr, l, m, h))

X = int(sys.stdin.readline())
for _ in range(X):
    N = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    max_sum = maxSubArraySum(arr,0,N-1)
    print(max_sum)


