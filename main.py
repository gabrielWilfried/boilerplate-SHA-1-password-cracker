# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

cracked_password1 = password_cracker.crack_sha1_hash(
    "fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2")
print(cracked_password1)

cracked_password2 = password_cracker.crack_sha1_hash(
    "dcc466796201f7232b22a03781110a8871fd038c", True)
print(cracked_password2)

cracked_password3 = password_cracker.crack_sha1_hash(
    "b305921a3723cd5d70a375cd21a61e60aabb84ec")
print(cracked_password3)

cracked_password4 = password_cracker.crack_sha1_hash(
    "c7ab388a5ebefbf4d550652f1eb4d833e5316e3e")
print(cracked_password4)

cracked_password5 = password_cracker.crack_sha1_hash(
    "ea3f62d498e3b98557f9f9cd0d905028b3b019e1", True)
print(cracked_password5)

# Run unit tests automatically
# main(module = "test_module", exit = False)
