import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'
    return bool(re.match(pattern, email))

print(is_valid_email("amankushwaha3328@gmail.com"))   
print(is_valid_email("aman_123@xyz.co.in"))  
print(is_valid_email("bob@website"))         
print(is_valid_email("charlie@.com"))        
print(is_valid_email("david@@mail.com"))     
