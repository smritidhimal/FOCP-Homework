input_name=input("your name?")
if len(input_name)>=1:
    print("welcome,",input_name)
else:
    print("nothing entered")


pw = input("Enter password: ")
upper = lower = special = num =False
char_list=["!","@","#","$"]
num_list = ['0','1','2','3','4']
if 8 <= len(pw) <=16:
    for i in pw:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i in char_list:
            special=True
        if i in num_list:
            num = True
    
    print("Successfully registered." if upper and lower and special and num  
          else "PW does not meet criteria")        
else:
    print("Check password length!")




    name=["Roshan", "Chandra","Sabin","Ashmita","Smriti"]
    list(map(lambda name: name.lower() + "tbc.edu.np",name))





def enter_pin():
    while True:
        pin = input("Enter your 4-digit pin: ")
        if len(pin) == 4 and pin.isdigit():
            pin = int(pin)
            break
        else:
            print("Invalid pin. Please enter a 4-digit pin.")
    return pin

user_pin = enter_pin()
print(f"Your pin is: {user_pin}")