import xml.etree.ElementTree as ET

try:
	xmlp = ET.XMLParser(encoding="iso-8859-1")
	mytree = ET.parse('dblp.xml', parser=xmlp)
	myroot = mytree.getroot()
	print(myroot)
except ET.ParseError:
    print("data format failure")

