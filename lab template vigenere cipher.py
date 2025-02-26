def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


message = ""
key = "" 

key = generate_key(message,key)


converted = []
ckey = []

for char in message:
    #TODO implement conversion for message
    
for char in key:
    #TODO implement conversion for key
    
encrypted = ""     
    
for num in converted:
    for key in ckey:
        #TODO implement math formula
        

print(encrypted) 

converted = []
for char in encrypted:
    #TODO implement conversion 
    
    
decrypted = ""
for num in converted:
    for key in ckey:
        #TODO implement math formula
        
print(decrypted)