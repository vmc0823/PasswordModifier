word = input()
password = ''

for char in word:
    if char == 'i':
        password += '1'
    elif char == 'a':
        password += '@'
    elif char == 'm':
        password += 'M'
    elif char == 'B':
        password += '8'
    elif char == 's':
        password += '$'
    else:
        password += char

# Append "!" to the end of the password
password += '!'

# Output the stronger password
print(password)