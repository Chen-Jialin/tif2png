# tif/tiff -> png picture format converter
import os
from PIL import Image

cwd = os.path.split(os.path.realpath(__file__))[0]
print("The current working directory: " + cwd)
print("Now to convert all pictures in the current working directory and its subdirectories from tif into png format.")
input("Press ENTER to continue...")

success_num = 0
err_num = 0
for (dir_name, sub_dirs, file_names) in os.walk(cwd):
    print("Working in: " + dir_name)
    for file_name in file_names:
        file_path = os.path.join(dir_name, file_name)
        if ((os.path.splitext(file_path)[1].lower() == ".tif") or (os.path.splitext(file_path)[1].lower() == ".tiff")):
            print("    Converting " + file_path + "...", end="")
            with Image.open(file_path) as file:
                try:
                    file.save(os.path.splitext(file_path)[0] + ".png", "png")
                    os.remove(file_path)
                    success_num += 1
                    print("Finished.")
                except Exception:
                    err_num += 1
                    print("Error occurred.")

print("Conversion process finished. Succuss: {}. Error: {}.".format(success_num, err_num))
input("Press ENTER to quit...")
