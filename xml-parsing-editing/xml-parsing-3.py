from lxml import html

tree = html.parse("exampleData.xml")

for elem in tree.findall(".//country/gdppc"):
    print(elem.text)
