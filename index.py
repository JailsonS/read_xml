import xml.etree.ElementTree as ET
import os, csv

dir = 'data'
out = 'output.csv'
data = []

for filename in os.listdir(dir):
    tree = ET.parse(os.path.join(dir, filename))
    root = tree.getroot()
    # print(root[1][0].text)

    
    # make dict
    for i in root[1][1]:
        dict = {}
        dict['name'] = root[1][0].text
        dict['lat'] = i.attrib['lat']
        dict['lng'] = i.attrib['lon']

        # add to list
        data.append(dict)


with open(out, mode='w', newline='', encoding='utf-8') as outputfile:
	wr = csv.DictWriter(outputfile, fieldnames=['name', 'lat', 'lng'])
	wr.writeheader()

	for item in data:
    		wr.writerow(item)
