import os
import shutil

pathtocod4 = input('type your cod4 root path: ') or "C:/Program Files (x86)/Call of Duty 4"
print(pathtocod4)
pathtomaps = pathtocod4 + "/" + "usermaps"

# getting usermaps subdirectories as list of names

dir_list = os.listdir(pathtomaps)
actual_list = []
for i in dir_list:
    if i.startswith("mp_") and not i.endswith(".rar"):

        actual_list.append(i)

# creating new folder for renamed files

newdirname = input('type name for a folder: ') or "renamed_shaders"
try:
    newdir = os.path.join(pathtocod4, newdirname)
    os.mkdir(newdir)
    print(f'Created directory {newdirname}')
except FileExistsError:
    print('Directory already exists, continuing')

pathtoshaders = pathtocod4 + "/" + newdirname

# copying files using names from list above

filename = input('type your shader file name: ') # type the name of your shader

src = pathtocod4 + "/shaders" + "/" + filename

print(src)
for i in actual_list:
    new_name = i

    dst = pathtoshaders + "/" + new_name + "_load.ff"
    shutil.copy(src, dst)

