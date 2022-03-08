""" Finding private key of DSA"""

m2 = 2151657259407048953791701

if 'ssh-rsa' in public_key:

    public_key_container = RSA.importKey(public_key)
    private_key_container = RSA.importKey(private_key)

    encrypted_m1 = public_key_container.encrypt(m2, 0)
    decrypted_m1 = private_key_container.decrypt(encrypted_m2)

    if m2 == decrypted_m1:
        return True
    
    elif 'ssh-dss' in public_key:
    q = 19928344283621
    p = 3986625417249813809 
    g = 2890026512265626020

    pub_k = ""
    for b in bytearray(public_key, 'utf-8'):
        pub_k += str(b)

    priv_k = ""
    for b in bytearray(private_key, 'utf-8'):
        priv_k += str(b)

    params = (long(pub_k), long(g), long(p), long(q), long(priv_k))
    key = DSA.construct(params)

    if key.verify(m2, key.sign(m2,3)):
        return True
    
    
    
    
    
    