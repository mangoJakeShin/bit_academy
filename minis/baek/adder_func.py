def solve(a):
    ans = 0
    for nums in a:
        ans += nums
    return ans

a = [1, 1,2,3,5,3]

b = solve(a)
print(b)