import sys



while True:
    fahrenheit = input("enter Fahrenheit Temp")  
    try:
        fahrenheit = float(fahrenheit)
    except:
       continue
    break
    


    
celsius = (fahrenheit - 32) * (5/9)
print("That is", celsius, "degree Celsius")


sys.exit()
