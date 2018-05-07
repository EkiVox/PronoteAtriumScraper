import os
with open('ALL-NEW-IDS.list', 'r') as idsfile:
    idsfile.read()
os.remove('ALL-NEW-IDS.list')