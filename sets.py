#sets in python#set is a collection of unique values that is unodered and mutable
numbers ={10,20,30,20,10}

print(numbers)

#why use sets
# suppose students have selected subjects
subjects = {"python","java","python","SQL","java"}

print(subjects)

#add values to a set
subjects ={"python","java"}
subjects.add("SQL")
print(subjects)

#remove values from a set
subjects.remove("java")
print(subjects)


#sets do not allow duplicate values
numbers=[1,2,2,3,3,4]

print(numbers)