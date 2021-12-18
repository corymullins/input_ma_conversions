import math
print("Instrumentation Conversion Calculator")

# clear values to prevent recursive errors
outp = 0
out_val = 0
sq_outp = 0
sq_out_val = 0

print("Select operation.")
print("1 - Convert linear input to mA output")
print("2 - Convert mA input to linear output")
print("3 - Convert square root input to mA output")
print("4 - Convert mA input to square root output")

while True:
    # take input from the user
    choice = input("Enter choice(1 - 4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        lower = float(input("Enter lower range value: "))
        upper = float(input("Enter upper range value: "))
        
        if choice == '1':
            inp = float(input("Enter input value: "))
            outp = float(4 + (16 * ((inp - lower) / (upper - lower))))
            print(outp, "mA")

        elif choice == '2':
            inp_ma = float(input("Enter mA value: "))
            out_val = float(lower + (upper - lower) * (inp_ma - 4) / 16)
            print(out_val)

        elif choice == '3':
            sq_inp = float(input("Enter input value: "))
            sq_calc = math.sqrt((sq_inp - lower) / (upper - lower))
            sq_outp = float(4 + (16 * (sq_calc))) 
            print(sq_outp, "mA")

        elif choice == '4':
            sq_inp_ma = float(input("Enter mA value: "))
            sq_out_val = (lower + (upper - lower) * (((sq_inp_ma - 4) / 16) ** 2))
            print(sq_out_val)
        
        # check for further conversions, close if answer is no
        next_calculation = input("Another conversion? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")