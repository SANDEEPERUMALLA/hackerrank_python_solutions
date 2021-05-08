import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    attr_count = len(node.attrib)
    for child in node:
        attr_count += get_attr_number(child)
    return attr_count


if __name__ == '__main__':

    xml = ''
    n = int(input())
    while n > 0:
        xml += input() + "\n"
        n -= 1

    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
