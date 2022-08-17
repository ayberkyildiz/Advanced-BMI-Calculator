mass= float(input("Enter mass in kg: ")) #Asking user's weight.



if mass<=0:
   print("Mass must be greater than zero.")    #Mass must be greater than zero.
    
if mass>=500: 
        print("Mass must be less than 500 kg.")    #Mass can't be greater than 500 kg. 
   
if mass>0 and mass<500:   
    height= float(input("Enter height in cm: "))   #Asking user's weight if the mass value is valid

    if height<=0:
        print("Height must be greater than zero.")   #Height must be greater than zero.
         
    
    if height>=300:
        print("Height must be less than 300 cm.")    #Height can't be greater than 300 cm.
        print("Please enter a valid number.")
        print("Goodbye!")  

if mass>0  and mass<500 and height>0:   #If the height value of the user is zero, It causes an error.(0 can't be a denominator)   
    bmi=mass/height**2*10000    #I multiplied  the equation with 10000 (100**2) in order to keep the unit cm .
    
    if bmi<15 and bmi>0 and height>0 and mass<500 and mass>0 and height<300:    #Any negative height values give us a positive bmi, which they shouldn't, because of the equation (height**2). So to prevent this, I added "if height>0". 
       print("Your BMI: ", bmi)
       print("You are underweight.")
       print("Please note that you are VERY SEVERELY underweight.")
       print("Goodbye!")
    
    elif bmi>15 and bmi<=16 and height>0 and mass<500 and mass>0 and height<300 :
        print("Your BMI: ", bmi)
        print("You are underweight.")
        print("Please note that you are SEVERELY underweight.")
        print("Goodbye!")
    
    elif bmi>16 and bmi<=18.5 and height>0 and mass<500 and mass>0 and height<300:
        print("Your BMI: ", bmi)
        print("You are underweight.")
        print("Please note that you are underweight.")
        print("Goodbye!")
    
    elif bmi>18.5 and bmi<=25 and height>0 and mass<500 and mass>0 and height<300:
        print("Your BMI: ", bmi)
        print("You are normal weight.")
        print("Goodbye!")
    
    elif bmi>25 and bmi<=30 and height>0 and mass<500 and mass>0 and height<300:
        print("Your BMI: ", bmi)
        print("You are overweight.")
        print("Goodbye!")
        
    elif bmi>30 and bmi<35 and height>0 and mass<500 and mass>0 and height<300:
        print("Your BMI: ", bmi)
        print("You are obese.")
        print("Please note that you are MODERATELY obese.")
        print("Goodbye!")
      
    elif bmi>=35 and bmi<40 and height>0 and mass<500 and mass>0 and height<300:
        print("Your BMI: ", bmi)
        print("You are obese.")
        print("Please note that you are SEVERELY obese.")
        print("Goodbye!") 
        
    elif bmi>40 and height>0 and mass<500 and mass>0 and height<300:
        print("Your BMI: ", bmi)
        print("You are obese.")
        print("Please note that you are VERY SEVERELY obese.")
        print("Goodbye!")    
        
else:
    print("Please enter a valid number.")   #If the previous conditions are wrong for the mass and height of the user, it will display "Please enter a valid number." and "Goodbye!"
    print("Goodbye!")    
        
    
        
        
    
        
