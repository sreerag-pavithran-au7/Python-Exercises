# ONLY APPLICABLE FOR NON-REPEATING NUMBERS

list1 = [2,8,0,12,5,3] #Unsorted List
print(list1)
for i in range(len(list1)): 
  min_value = min(list1[i:])
  min_index = list1.index(min_value)
  list1[i],list1[min_index] = list1[min_index],list1[i] #Swapping 
print(list1)


# APPLICABLE FOR ALL NUMBERS INCLUDING REPEATING

list1 = [5,2,8,0,12,5,3] #Unsorted List
print(list1)
for i in range(len(list1)): 
  min_value = min(list1[i:])
  min_index = list1.index(min_value,i)
  list1[i],list1[min_index] = list1[min_index],list1[i] #Swapping 
print(list1)


# REDUCING TIME COMPLEXITY

list1 = [5,2,8,0,12,5,3] #Unsorted List
print(list1)
for i in range(len(list1)): 
  min_value = min(list1[i:])
  min_index = list1.index(min_value,i)
  if list1[i] != list1[min_index]: # Sometimes same value will be there so need to swap between them
    list1[i],list1[min_index] = list1[min_index],list1[i] #Swapping 
print(list1)