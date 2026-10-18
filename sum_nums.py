num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum += i
sum_gauss = num * (num + 1) // 2
print("Sym:", sum)
if sum == sum_gauss:
    print("My running sum code workd coreectly")
else:
    print("My running sum code failed badly")