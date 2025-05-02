m = int(input())
for _ in range(m):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[False] * k for _ in range(n)]
    dp[0][(A[0] % k + k) % k] = True

    for i in range(1, n):
        for j in range(k):
            if dp[i-1][j]:
                add_mod = (j + A[i]) % k
                sub_mod = (j - A[i]) % k
                dp[i][add_mod] = True
                dp[i][sub_mod] = True

    if dp[n-1][0]:
        print("Divisible")
    else:
        print("Not divisible")
