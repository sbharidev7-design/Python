#1.Adding  elements
n=int(input("Enter number of elements:"))
list = []
for i in range(n):
     list.append(input("Enter element: "))
print(list)



#2.Add new item to the list
list = ["Apple", "Orange", "Banana"]
item = input("Enter new item:")
list.append(item)
print(list)



#4.Combining of two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)



#5.Remove items from the list
fruits = ["Apple", "Orange", "Banana"]
fruit = input("Enter fruit:")
if fruit in fruits:
     fruits.remove(fruit)
     print(fruits)
else:
     print("Item Not Found")



#6.Removing last element from the list
list = [10, 20, 30, 40, 50]
a =list.pop()
print("Removed:", a)
print(list)



#7.Ask the user for a name check whether it exist in the list
students = ["Adith", "Arjun", "Gokul"]
name = input("Enter name:")
if name in students:
     print("Found")
else:
     print("Not Found")



#8.Diplay elements and how many times it appears in the list
list = [1, 2, 1, 2, 4, 1]
a = int(input("Enter element:"))
print(list.count(a))



#10.Reverse elements in the list
list = [15, 20, 30, 45]
list.reverse()
print(list)


#11.Find the largest number
list = [5, 10, 20, 30]
print(max(list))



#12.Find the smallest number
# list = [5, 10, 20, 30]
print(min(list))




#13.Find sum of all elements
lst = [10, 15, 20, 25]
print(sum(lst))



#15.Count even and odd numbers
list = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0
for i in list:
     if i % 2 == 0:
         even += 1
     else:
         odd += 1
print("Even =", even)
print("Odd =", odd)



#16.Store pos and neg numbers in lists
list = [1, -2, 3, -4, 5]
pos = []
neg = []
for i in list:
     if i >= 0:
         pos.append(i)
     else:
         neg.append(i)
print(pos)
print(neg)




#17.Display elements in ascending and descending order
list = [10, 20, 5, 15, 25]
list.sort()
print("Ascending:", list)
list.sort(reverse=True)
print("Descending:", list)

