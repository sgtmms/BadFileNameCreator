import os
import shutil
import sys 

print(sys.argv[1])


def file_rename(old_file_name):
    badNames = ["ti\`ck", "p\%er\%cent", "as\*ter\*ick", "p\|ip\|e", "co\:on", "semi\;colon",
                    "amp\&ersand", "gre\>ater\>than", "less\<than", "qu\'o\"te", "ca\^rat"];
    print(badNames)
    split = old_file_name.split(".", 1)
    fileExtension = "." + split[1]

    src_dir= os.curdir

    dst_dir= os.path.join(os.curdir , "/renamed")
    print(os.curdir)

    src_file = os.path.join(src_dir, old_file_name)
    print(src_dir)
    shutil.copy(src_file,dst_dir)


        
    for badName in badNames:
        newName = fileExtension  + badName 
        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, newName)
        os.rename(dst_file, new_dst_file_name)

file_rename(sys.argv[1])