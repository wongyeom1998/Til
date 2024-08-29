def decimal_to_binary(n):
    binary_number = ''
    if n == 0:
        return "0"

    while n >0:
        remainder = n % 2
        binary_number = str(remainder) + binary_number 
        n = n // 2
    
    return binary_number


def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""
    if n == 0:
        return '0'
    
    while n >0:
        remainder = n % 16
        hexadecimal_number = hex_digits[remainder] + hexadecimal_number
        n = n//16

    return hexadecimal_number
