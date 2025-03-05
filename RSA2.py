def fast_mod_exp(b, exp, m):
    res = 1
    while exp > 1:
        if exp & 1:
            res = (res * b) % m
        b = b ** 2 % m
        exp >>= 1
    return (b * res) % m


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def modInverse(A, M):
    if gcd(A, M) > 1:
      
        # modulo inverse does not exist
        return -1
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

p = 3571
q = 4787
n = p*q
print(f"result of p times q: {n}")
on = (p-1)*(q-1)
print(f"Result of euler's totient function: {on}")
e = 7 #I chose this because 7 is greater than 1, less than 8, and is coprime to 8
d = modInverse(e,on)
print(f"modular inverse of e mod o(n) {d}")

message = 383
encrypted = fast_mod_exp(message,e,n)
print(f"encrypted message: {encrypted}")

#Now we want to decrypt our message
decrypted = fast_mod_exp(message,d,n)
print(f"Decrypted message: {decrypted}")
