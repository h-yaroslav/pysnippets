import os
top = './'
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        print os.path.join(root, name)
    for name in dirs:
        pass
        #print os.path.join(root, name)
