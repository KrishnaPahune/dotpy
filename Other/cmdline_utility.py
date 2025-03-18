import argparse
import requests
import os 

# For passing and displaying output on command line
parser = argparse.ArgumentParser()

parser.add_argument("url",help="url of the file to be downloaded")
# parser.add_argument("output",help="name by which you want to save the file")
parser.add_argument("-o","--output",help="name by which you want to save the file",default=None)

args = parser.parse_args()

if args.output:
    filename = args.output
else: 
    filename = os.path.basename(args.url)
print(f"Downoading from {args.url}")
print(f"Saving as {filename}")


# Code to download image using url

# # Send a GET request to the image URL
response = requests.get(args.url, stream=True)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    with open(filename, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    print("Image downloaded successfully!")
else:
    print("Failed to download image.")
