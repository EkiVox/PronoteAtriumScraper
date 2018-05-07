import os
with open('ALL-NEW-IDS.list', 'r') as idsfile:
    print idsfile.read()
os.remove('ALL-NEW-IDS.list')