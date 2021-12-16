import xml.etree.ElementTree as ET
from xml.etree import ElementTree, ElementInclude
tree = ET.parse('country_data.xml')
root = tree.getroot()

print(root.tag)


print(root.attrib)


for child in root:
    print(child.tag, child.attrib)



print(root[0][1].text)


for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)



for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
    # print(country)



for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('output.xml')


# Element.remove

for country in root.findall('country'):
    # using root.findall() to avoid removal during traversal
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')



# SubElement

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
print(ET.dump(a))



xml_text ='''<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>'''
print("canonicalize",ET.canonicalize(xml_text))

root = ET.fromstring(xml_text)
for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)


root = tree.getroot()

# Top-level elements
print(root.findall("."))

print(root.findall("./country/neighbor"))

# Nodes with name='Singapore' that have a 'year' child
print(root.findall(".//year/..[@name='Singapore']"))


# 'year' nodes that are children of nodes with name='Singapore'
print("year nodes",root.findall(".//*[@name='Singapore']/year"))

# All 'neighbor' nodes that are the second child of their parent
print(root.findall(".//neighbor[2]"))






# tree1 = ElementTree()
tree = ET.parse("document.xhtml")

p = tree.find("body/p")     # Finds first occurrence of tag p in body
print("p   ",p)

links = list(p.iter("a"))   # Returns list of all links
print(links)

for i in links:             # Iterates through all found links
    i.attrib["target"] = "blank"
tree.write("output.xhtml")


