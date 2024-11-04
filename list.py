#Note Test2:Functions
#forloop
#list, dictionary for a test

#List use data collections 
#lists are mutable

#Example
# Define the list of student names and other lists
studentNames = ['sandra', 'patricia', 'Anita', 'phionah']  # Properly separated each name
studentMarks = [80, 56, 78, 90]  # Integer list for marks
data = ['sandra', 60, 'Anitah']  # Mixed types list

# Access the whole list
print("a list of Students:", studentNames, type(studentNames))

# Access list items using positive indexing
print("First Student:", studentNames[0])#first item
print("Second Student:", studentNames[1])#second item
print("Third Student:", studentNames[2])#third item
print("Fourth Student:", studentNames[3])#fourth item

# Using negative indexing
print("Second Last Student:", studentNames[-2])
print("Last Student:", studentNames[-1])

# Appending and Inserting elements
# Append 'Mishelle' at the end of the list
studentNames.append('Mishelle')
print("Appending Mishelle:", studentNames)

# Insert 'Faith' at the second position (index 2)
studentNames.insert(2, 'faith')
print(" Inserting Faith at Index 2:", studentNames)




#Assignment

#qn1. print Patrice ,Faith , Phionah and Anita Using slicing.

print(studentNames[1:5])

#qn2. add Masha at the forth position

studentNames[3] = 'Masha'
print(studentNames)

#qn3. update name phiona to phiona Aladinah

studentNames[4] ='Phionah Aladinah'
print(studentNames)

#qn4. display the length of the students list

length = len(studentNames)
print(f"The Number of Students is ",len(studentNames))

#qn5. print all the students names using a for loop
for each_student_name in studentNames:
    print(each_student_name)
#qn6. calculate the total marks for the students marks variable

def total_marks():
    student_marks = [80, 56, 78, 90]
    return sum(student_marks)

student_total_marks = total_marks()
print(f'Total student marks is: {student_total_marks}')



