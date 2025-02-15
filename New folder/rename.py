import os
folder_path=r'C:\Users\krish\OneDrive\Desktop\New folder\png'
i=1
for filename in os.listdir(folder_path):
    old_file_path = os.path.join(folder_path,filename)
    new_filename = f"{i}.png"
    new_file_path = os.path.join(folder_path,new_filename)
    os.rename(old_file_path,new_file_path)
    i += 1
print("all files renamed")