import xml.etree.ElementTree as ET
root_node = ET.parse('http://www.cbr.ru/scripts/XML_daily.asp').getroot()
# for tag in root_node.findall('Valute/CharCode'):
#     value = tag.text
#     if value == 'AZN':
#         tag1 = root_node.find('Valute/Value')
#          # cost = tag1[4]
#         print(tag1.text)
#         break
fl = 0
value = ''
for tag in root_node.getchildren():
    for val in tag.getchildren():
        if val.tag == 'CharCode' and val.text == "AZN":
            fl = 1
        if fl and val.tag == 'Value':
            value = val.text
            fl = 0
            print(value)
    if value != '':
        break




