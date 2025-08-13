from lxml import etree
import os

def process_large_xml(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    context = etree.iterparse(file_path, events=("end",), tag="article")
    
    for event, elem in context:
        title = elem.find("title")
        if title is not None:
            print(f"Found title: {title.text}")
        # Clear memory
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]

# try:
#     process_large_xml("dblp.xml")
# except etree.XMLSyntaxError as e:
#     print(f"XML parsing error: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")

with open("dblp.xml", "r") as f:
    print(f.read(1000))