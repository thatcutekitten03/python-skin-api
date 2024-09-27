import urllib.request
import PIL 
from PIL import Image

print("\n"*50)
print("py-skin-api | https://https://github.com/thatcutekitten03/python-skin-api//")
print("\n\n\nHow to use:\n - skin <minecraft user name>")

def skin(name):
    urllib.request.urlretrieve("https://mineskin.eu/download/"+name, name+".png")

while True:
    cmd = input ("> ")
    if cmd.startswith("skin "):
        new_cmd = cmd.split("skin ")
        skin(new_cmd[1])
        print("\nDownloaded Skin for "+new_cmd[1]+"\n")
    if cmd.startswith("c"):
        break
    
