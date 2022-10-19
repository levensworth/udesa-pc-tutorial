

def dec_to_hex_recursive(hexstr = "", dec_number = 0): 
    hexa_values = "0123456789ABCDEF"
    if dec_number == 0: 
        return hexstr 
    else: 
        least_sig_byte = dec_number % 16 
        next_val = dec_number / 16 
        return dec_to_hex_recursive(hexa_values[least_sig_byte] + hexstr, next_val) 