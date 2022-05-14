numberList = []
roundingValue = int(input("To what degree would you like to round: "))
dataSetNum = input("How many units in your data set: ")
for i in range(0, int(dataSetNum)):
    nums = input("Enter Number:\n")
    numberList.append(float(nums))

print("The list is: %s" % numberList)

mean1 = 0
for j in range(0, int(dataSetNum)):
    mean1 = mean1 + numberList[j]
mean2 = float(mean1)/float(dataSetNum)
print("Sum: %s" % mean1)
print("Average: %s" % mean2)

numberList2 = []
for k in range(0, int(dataSetNum)):
    numberList2.append(abs(numberList[k]-mean2))

numberList3 = []
for m in range(0, int(dataSetNum)):
    rounded_list2 = round(numberList2[m], roundingValue)
    numberList3.append(rounded_list2)


print("The list is: %s" % numberList3)

mean3 = 0
for l in range(0, int(dataSetNum)):
    mean3 = mean3 + numberList3[l]
mean4 = float(mean3)/float(dataSetNum)
print("Sum: %s" % mean3)
mean5 = round(mean4, 1)
print("MAD: %s" % mean5)
