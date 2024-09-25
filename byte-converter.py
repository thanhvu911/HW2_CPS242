import sys

scales = {
    '': 1,         
    'k': 1000,   
    'm': 1000**2,    
    'ki': 1024,  
    'mi': 1024**2
}

units = {
    'b': 1, 
    'B': 8
}

# Function to calculate base unit conversion factor
def base_conversion(input_value, input_unit):
    unit_prefix = input_unit[:-1].lower() 
    unit_type = input_unit[-1] 
    
    conversion_factor = units[unit_type]  
    conversion_factor *= scales.get(unit_prefix, 1)  
    
    return input_value * conversion_factor

# Core conversion function from one format to another
def convert_units(input_value, input_format, output_format):
    base_value = base_conversion(input_value, input_format)
    
    target_prefix = output_format[:-1].lower() 
    target_type = output_format[-1]
    
    target_conversion_factor = units[target_type]
    target_conversion_factor *= scales.get(target_prefix, 1) 
    
    return base_value / target_conversion_factor


def main():
    if len(sys.argv) != 4:
        print("Error: Please provide three arguments.")
        sys.exit(1)

    value = float(sys.argv[1])
    input = sys.argv[2]
    output = sys.argv[3]

    result = convert_units(value, input, output)
    print(result)


main()
