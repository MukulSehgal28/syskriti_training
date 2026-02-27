#Sample Data
data = [4, 2, 8, 2, 5, 8, 2]

#finding mean
sum = 0
n = 0

for i in data:
    sum = sum + i
    n = n + 1

mean = sum / n
print("Mean is", mean)




# sorting values for median
for i in range(n):
    for j in range(n - 1):
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp


# checking middle value
if n % 2 == 0:
    median = (data[n//2] + data[n//2 - 1]) / 2
else:
    median = data[n//2]

print("Median is", median)




#countin frequency for mode
maxCount = 0
mode = data[0]

for i in range(n):
    count = 0
    for j in range(n):
        if data[i] == data[j]:
            count = count + 1

    if count > maxCount:
        maxCount = count
        mode = data[i]

print("Mode is", mode)