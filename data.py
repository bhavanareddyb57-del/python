#list in python
#list is an odered and changeable collection than can store multiple value
marks=[80,90,75,85]

print(marks)

#accessing elements in a list
marks=[80,90,75,85]
print(marks[0])
print(marks[2])
print(marks[3])



#change elements in a list
marks =[80,90,75]
marks[1]=95
print(marks)

#add elements to a list
marks =[80,90,75]

marks.append(85)

print(marks)

#remove element from a list
marks =[80,90,75]

marks.remove(90)

print(marks)
#insert method
numbers =[10,20,30]
numbers.insert(1,15)

print(numbers)
#extend method
a=[1,2,3]
b=[4,5,6]
a.extend(b)

print(a)
#clear method
numbers=[10,20,30]

numbers.clear()

print(numbers)


#index method
numbers=[10,20,30,40]
print(numbers.index(30))
print(numbers.index(20))
print(numbers.index(40))

#count method

numbers=[10,16,18,19,25,42,9,25,16]
print(numbers.count(16))

#sort method
numbers =[40,10,30,20]

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#reverse method
numbers=[10,20,30,40]
numbers.reverse()
print(numbers)

#copy method
a =[1,2,3]

b =a.copy()
print(b)

#slicing method (start ,stop,step)
numbers =[10,20,30,40,50]

print(numbers[1:4])
print(numbers[ :3])
print(numbers[2: ])
print(numbers[::-1])

numbers[10,20,30,40,50,60,70,80]
print(numbers[1:7:2])
print(numbers[6:1:-2])

