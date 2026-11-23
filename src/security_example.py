import hashlib
import os

# Pour que le workflow passe sans bloquer sur l'opération cryptographique sensible (MD5),
#  il faut remplacer hashlib.md5 par une fonction de hachage adaptée aux mots de passe (comme hashlib.scrypt de la bibliothèque standard Python, ou argon2 / bcrypt),
def hash_password(password: str) -> str:
    salt = os.urandom(16)
    dk = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=16384,
        r=8,
        p=1,
    )
    return f"{salt.hex()}:{dk.hex()}"