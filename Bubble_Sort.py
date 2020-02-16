list1 = [8,5,2,4,3,7,2,0]
print("Unsorted List = ", list1)

for i in range(len(list1)-1):
  for j in range(len(list1)-1):
    if list1[j] > list1[j+1]:
      list1[j],list1[j+1] = list1[j+1],list1[j]
print("Sorted List = ", list1)