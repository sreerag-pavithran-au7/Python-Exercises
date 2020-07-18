numbers = [10, 20, 30, 400, 50];
print(numbers[2]);

for i in numbers: 
    print (i)

print(numbers[:-2]);

# THIS IS LINEAR SEARCH
maximum = numbers[0];
for num in numbers:
    if num > maximum:
        maximum = num;
print("Maximum number is: ",maximum);