import xml.etree.ElementTree as ETree
import os
import sys

def parse(xml_file_path):
    tree = ETree.iterparse(xml_file_path)
    print(tree.getroot())

parse("../enwiki-latest-pages-articles26.xml-p42567204p42663461")
