def narcissistic(value):
    digits = str(value)  
    num_digits = len(digits)  
    total = sum(int(digit) ** num_digits for digit in digits)  
    return total == value  


print(narcissistic(153))  
print(narcissistic(370))  
print(narcissistic(123))  
