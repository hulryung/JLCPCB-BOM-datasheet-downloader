# this program is download the datasheet from the JLCPCB "CART" page
# the part number for URL is from the BOM file. the BOM file is read from the
# argument of the program
# the datasheet is saved in the current directory
# the datasheet file name is the same as the part number

# We can find the part number from the BOM file
# the BOM file is a csv file
# You can find the component detail from the JLCPCB "CART" page using below URL
# https://cart.jlcpcb.com/shoppingCart/smtGood/getComponentDetail?componentCode={part_number}

# author: Daekeun Kang
# date: 2023-12-27
# version: 1.0.0

import requests
import json
import csv
import sys
import os

# the current directory
current_dir = os.getcwd()

# the BOM file is read from the argument of the program
# if the argument is not provided, the program will load
# the default BOM file name. it starts with "bom" or "BOM" and ends with ".csv"
# the BOM file is a csv file
if len(sys.argv) > 1:
    bom_file = sys.argv[1]
else:
    # find the BOM file name in the current directory
    bom_file = ""
    for file in os.listdir(current_dir):
        if file.lower().startswith("bom") and file.lower().endswith(".csv"):
            bom_file = file
            break
    if bom_file == "":
        print("BOM file not found")
        exit()

# load the BOM file
bom = []
with open(bom_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        bom.append(row)

# the part number is 4th column in the BOM file
part_number = []
for row in bom:
    part_number.append(row["LCSC"])

# looking for the datasheet URL from the JLCPCB "CART" page
# the part number for URL is from the BOM file
# the datasheet URL is in the "datasheet" field
for part in part_number:
    url = "https://cart.jlcpcb.com/shoppingCart/smtGood/getComponentDetail?componentCode=" + part
    r = requests.get(url)
    data = json.loads(r.text)
    # peel off the "data" layer
    data = data["data"]
    # the datasheet URL is in the "dataManualUrl" field
    # if the field is empty, the datasheet is not found.
    try:
        datasheet_url = data["dataManualUrl"]
    except:
        pass
    # if the datasheet is found, download it
    if datasheet_url != "":
        # get the file name from the URL
        datasheet_file = datasheet_url.split("/")[-1]
        if os.path.isfile(datasheet_file):
            print("skip " + datasheet_file)
        else:
            # download the datasheet
            print("download " + datasheet_file)
            r = requests.get(datasheet_url)
            with open(datasheet_file, 'wb') as f:
                f.write(r.content)
    else:
        print("datasheet not found for " + part)

    # now, download the images
    # the image URL is in the "imageList" field
    imageList = ""
    try:
        imageList = data["imageList"]
    except:
        pass
    # if the image is found, download it
    if imageList != "":
        for image_dict in imageList:
            image_url = image_dict["productBigImage"]
            # get the file name from the URL
            image_file = image_url.split("/")[-1]
            if os.path.isfile(image_file):
                print("skip " + image_file)
            else:
                # download the image
                print("download " + image_file)
                r = requests.get(image_url)
                with open(image_file, 'wb') as f:
                    f.write(r.content)

print("done")
