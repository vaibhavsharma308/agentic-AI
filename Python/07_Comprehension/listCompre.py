print("List Comprehension Examples")
natural_numbers =[1,2,3,4,5,
                  6,7,8,9,10]

print("Even Number List")
even_numbers = [ num for num in natural_numbers if num % 2 == 0]
print(even_numbers)



print("Odd Number List")
odd_numbers = [x for x in natural_numbers if x%2!=0 ]
print(odd_numbers)


beverages_menu =[
    "Masala Tea",
    "Iced Tea",
    "Coffee Latte",
    "Cold Coffee"
]

print("Our Menu ", beverages_menu)

tea_menu = [item for item in beverages_menu if "Tea" in item ]
print("Our Tea Menu" , tea_menu)



numbers = [1,2,3,4,5,6,7,8,9
           ,10,12,15,16,128,1662,24,52,4]

filterNumber = [x for x in numbers if x%3==0]
print("Number after fileration")
print(filterNumber)