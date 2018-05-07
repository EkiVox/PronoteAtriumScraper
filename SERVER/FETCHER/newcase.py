import hashlib
import pickle
import random
import string
import os

id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

hasher = hashlib.md5()
hasher.update(password)
hashedpassword = hasher.digest()
ids = [id, password]

with open('ALL-NEW-IDS.list', 'a+') as idsfile:
    idsfile.write("" + str(ids) + "\n")
os.makedirs('user/' + id + '/')
with open('user/' + id + '/password-' + id + '.conf', 'w') as passfile:
    pickle.dump(hashedpassword, passfile)
