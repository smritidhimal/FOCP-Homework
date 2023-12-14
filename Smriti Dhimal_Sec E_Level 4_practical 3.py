
result1 = 10 < 100
print(result1)

result2 = 100 != 100
print(result2)

result3 = 50 >= 50
print(result3)


age = 18
print(age < 18)  
print(age < 21)  
print(age < 31)  


print("a" < "b")       
print("b" < "a")       
print("John" < "Terry") 

result = "john" < "Terry"
print(result)

result1 = 5 < 10.2
print(result1) 


age = 30
result1 = age >= 18 and age <= 65
result2 = age < 18 or age > 65
result3 = not age > 18

print(result1)  
print(result2)  
print(result3)  
result4 = (age >= 18 and age <= 65) and (not age == 30)
print(result4) 
result5 = 18 < age <= 65
result6 = 18 < age and age <= 65
print(result5)  
print(result6)  


weight = 150
height = 140
expression1 = 100 < weight < 200
expression2 = height > 131 and height < 160

print(expression1)  
print(expression2)  



weight_true = 150
height_true = 140
weight_false = 80
height_false = 170
expression1_true = 100 < weight_true < 200
expression2_true = height_true > 131 and height_true < 160

expression1_false = 100 < weight_false < 200
expression2_false = height_false > 131 and height_false < 160
print(expression1_true)   
print(expression2_true)   

print(expression1_false)  
print(expression2_false)  


age = 25  
if 18 <= age <= 30:
    print("You are still young!")
else:
    print("You are not in the age range of 18 to 30.")



age = 35  
if 18 <= age <= 30:
    print("You are still young!")
elif 30 < age <= 40:
    print("You are in the age range of 30 to 40.")
else:
    print("You are not in the age range of 18 to 40.")

    
name = input("Enter your name: ")
if name != "":
    print("Your name is", name)
else:
    print("Name not entered")

age_status = "you are an adult" if age >= 18 else "you are not an adult, yet!"
print(age_status)


names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(name)



for exponent in range(2, 11, 2):  
    result = 2 ** exponent
    print(f"{exponent} to the power of {exponent} = {result}")



numbers = [10, 20, 30, 90, 200, 30, 22, 11]
running_total = 0
found_value_over_100 = False
for num in numbers:
    running_total += num
    if num > 100:
        found_value_over_100 = True
        break  
print(f"Running total: {running_total}")

if not found_value_over_100:
    print("All numbers processed")







