nums=[1,2,3,6,7,8,23,78,34,12]

# Ədədlərin cəmini tapan metod yazın
print("Ədədlərin cəmini tapan metod yazın : ")
sum = 0
for i in range(0,len(nums)):
    sum = sum + nums[i]
print(sum)

# Ədədlərin böyükdən kiçiyə doğru sıralayın
print("Ədədlərin böyükdən kiçiyə doğru sıralayın : ")
nums.sort(reverse=True)
print(nums)

# Ədədlər arasında rəqəmlərinin cəmi ən böyük olan ədədi tapın
print("Ədədlər arasında rəqəmlərinin cəmi ən böyük olan ədədi tapın : ")
figureSum = []
for elem in nums:
    value = 0
    for el in str(elem):
        value += int(el)
    figureSum.append(value)

print(figureSum[0])

# Ədədlərin kvadratlarının olduğu yeni bir massiv yaradan metod yazın
print ("Ədədlərin kvadratlarının olduğu yeni bir massiv yaradan metod yazın : ")
list1 = []
for num in nums:
    num **=2
    
    list1.append(str(num))
print(list1)

# Tək ədədlərin cəmini tapan metod yazın
print("Tək ədədlərin cəmini tapan metod yazın : ")
oddNum = 0

for j in range(0,len(nums)):
    if nums[j] % 2 == 1:
        oddNum = oddNum + nums[j]
print(oddNum)

# Daxilində 3 rəqəmi olan neçə ədəd olduğunu ekrana çap edən metod yazın
print ("Daxilində 3 rəqəmi olan neçə ədəd olduğunu ekrana çap edən metod yazın : ")
say = 0
for s in range(0,len(nums)):
    if "3" in str(nums[s]):
        say +=1
print (say)

# Tək ədədləri ayıraraq ayrıca bir massivə yığan metod yazın
print ("Tək ədədləri ayıraraq ayrıca bir massivə yığan metod yazın : ")
list2 = []
for k in range(0,len(nums)):
    if nums[k] % 2 !=0:
        list2.append(str(nums[k]))
print(list2)