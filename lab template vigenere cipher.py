def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


message = "Here, you can explore your passions to reach your potential and realize your purpose, on our campus and in the world beyond. A Calvert Hall education is a transformative experience that continues long after graduation. Our students become Men of Intellect, Men of Faith, and Men of Integrity, and the relationships they develop over four years at The Hall last forever."
key = "calvert hall" 

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