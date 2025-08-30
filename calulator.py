
answer="y"
while answer=="y":
    num1=int(input("Enter the first Number!\n"))
    num2=int(input("Enter the Second Number!\n"))
    choice=int(input("Enter desired number for desired operation \n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Modulus (%)\n"))   
    try:
        if choice==1:
            print(num1+num2)
            
        elif choice==2:
            print(num1-num2)
               
        elif choice==3:
            print(num1*num2)        
            
        elif choice==4:
            if num2==0:
                print("Cannnot be divided by zero!")
            else:
                print(num1/num2)
               
        elif choice==5:
            if num2==0:
                print("Cannot perform for zero!")
            else:
                print(num1%num2)                
                          
        else:
            print("Try numbers within choices!")
            
    except:
        print("Invalid choice!")
    answer=input("Calculate Again? Type y\n").lower()