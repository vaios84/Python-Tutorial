from lxml import html

tree = html.parse("dblp.xml")

for elem in tree.findall(".//article/title"):
    print(elem.text)
