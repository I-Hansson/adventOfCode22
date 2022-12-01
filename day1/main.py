lst = []
f = open("./day1/day1.txt", "r")
for x in f:
  lst.append(x.replace("\n", ""))
sum = 0
sum_lst = []
for i in range(len(lst)):
  if lst[i] == "":
      sum_lst.append(sum)
      sum = 0
  else:
    sum += int(lst[i])

sum_lst.sort()
# task 1
print("Task 1: " + str(sum_lst[-1]))
# task 2
print("Task 2: " + str(sum_lst[-1] + sum_lst[-2] + sum_lst[-3]))



