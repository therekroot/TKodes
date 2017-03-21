# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here
import os
def rename_files():
    # get file names
    file_list = os.listdir(r"C:\Users\tkroot\version-control\TKodes\stage_3\lesson_3.2_using_functions\secret_message\prank")
    print file_list
    
    # rename files using rename(original, modified)
    os.chdir(r"C:\Users\tkroot\version-control\TKodes\stage_3\lesson_3.2_using_functions\secret_message\prank")
    for f in file_list:
        new_name = f.translate(None,"0123456789")
        os.rename(f,new_name)
    
    # get file names
    file_list = os.listdir(r"C:\Users\tkroot\version-control\TKodes\stage_3\lesson_3.2_using_functions\secret_message\prank")
    print file_list
    
rename_files()
