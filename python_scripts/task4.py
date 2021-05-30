n = input("Enter the number of chocolates: ")
print("The value  of n is",n)
m = input("Enter the number of children: ")
print("The value of m is:",m)

dict = {}

if m > n:
        ans1 = m - n
        for i in range(n):
                i = i + 1
                dict[i] = 1
        for j in range(ans1):
                i = i + 1
                dict[i] = 0
elif n > m:
        diff = n % m
        ans1 = n/m
        if diff == 0:
                for i in range(m):
                        i = i + 1
                        dict[i] = ans1
        else:
                for i in range(m):
                        i = i + 1
                        dict[i] = ans1
                for j in range(1, diff+1):
                        dict[j] = ans1 + 1
else:
        for i in range(m):
                i = i + 1
                dict[i] = 1
print(dict)

