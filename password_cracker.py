import hashlib

def crack_sha1_hash(hash, use_salts = False):
    #Load the list of top 10000 passwords 
    with open("top-10000-passwords.txt", "r") as f:
        passwords = f.readlines()
    passwords = [password.strip() for password in passwords]

    #Load salt if use_salts is true
    salts = []
    if use_salts:
        with open("known-salts.txt", "r") as f:
            salts = f.readlines()
        salts = [salt.strip() for salt in salts]

    # Iterate through each password and salt combination
    for password in passwords:
        hashed_password = password.encode()
        # Apply salts if use_salts is True
        if use_salts:
            for salt in salts:
                # hashed_password = salt.encode() + hashed_password + salt.encode()
                salted_password = salt.encode() + password.encode() 
                hashed_password = hashlib.sha1(salted_password).hexdigest()
        else:
            # Hash the password
            hashed_password = hashlib.sha1(hashed_password).hexdigest()
    
        # Compare the hashed password with the provided hash
        if hashed_password == hash:
            return password
    return "PASSWORD NOT IN DATABASE"