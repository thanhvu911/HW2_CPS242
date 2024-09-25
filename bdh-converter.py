import sys
# Binary to Decimal conversion 
def b2d(b_input, exponent=0):
    if not b_input:
        return 0
    return int(b_input[-1]) * (2 ** exponent) + b2d(b_input[:-1], exponent + 1)

# Decimal to Binary conversion 
def d2b(decimal_value):
    if decimal_value == 0:
        return ""
    return d2b(decimal_value // 2) + str(decimal_value % 2)

# Decimal to Hexadecimal conversion 
def d2h(decimal_value):
    if decimal_value == 0:
        return ""
    remainder = decimal_value % 16
    h_digit = "0123456789ABCDEF"[remainder]
    return d2h(decimal_value // 16) + h_digit

# Binary to Hexadecimal conversion 
def b2h(b_input):
    dec_value = b2d(b_input)
    return "0x" + d2h(dec_value)

# Hexadecimal to Decimal conversion 
def h2d(h_input, exponent=0):
    if not h_input:
        return 0
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    h_value = hex_map[h_input[-1].upper()]
    return h_value * (16 ** exponent) + h2d(h_input[:-1], exponent + 1)

# Hexadecimal to Binary conversion 
def h2b(h_input):
    dec_value = h2d(h_input)
    return d2b(dec_value)

#https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
def main():
    value = sys.argv[1]     
    from_ = sys.argv[2]    
    to_ = sys.argv[3]     

    if from_ == 'b':  
        if to_ == 'd':
            print(b2d(value)) 
        elif to_ == 'h':
            print(b2h(value))  
        elif to_ == 'b':
            print(value)
        else:
            print("Invalid conversion type")

    elif from_ == 'd': 
        decimal_value = int(value) 
        if to_ == 'b':
            print(d2b(decimal_value)) 
        elif to_ == 'h':
            print("0x" + d2h(decimal_value))
        elif to_ == 'd':
            print(value)  
        else:
            print("Invalid conversion type")

    elif from_ == 'h': 
        if to_ == 'd':
            print(h2d(value))
        elif to_ == 'b':
            print(h2b(value)) 
        elif to_ == 'h':
            print("0x" + value.upper()) 
        else:
            print("Invalid conversion type")

    else:
        print("Invalid format.")

main()
