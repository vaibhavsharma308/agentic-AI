

numbers =[1,2,1,3,2,3,4,23,12,1,1,1,2,2]

unique_numbers = { x for x in numbers}
print("Unqiue Numbers we have", len(unique_numbers))
print(unique_numbers)

student_marks = [
    {1 :[84,35,43,93]},
    {2 :[90,53,71,83]},
    {3 :[82,83,71,33]},
]

maximum_marks = [ max(marks) for s_data in student_marks 
                 for marks in s_data.values() 
                 ]
print(maximum_marks)


