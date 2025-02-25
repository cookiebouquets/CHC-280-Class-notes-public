def converttonum(message):
    converted = []
    for c in message:
        converted.append(ord(c))
    return converted

def shift(message,key):
    shifted = []
    for c in message:
        shifted.append(c + key)

    return shifted

def converttotext(message):
    converted = ""
    for c in message:
        c = chr(c)
        converted = converted + c
        
    return converted

message = "Hello calvert hall"
print(f"Message: {message}")
message = converttonum(message)
message = shift(message,2)
cipher = converttotext(message)
print(f"Cipher: {cipher}")
plaintext = converttotext(shift(converttonum(cipher),-2))
print(f"unencrypted: {plaintext}")