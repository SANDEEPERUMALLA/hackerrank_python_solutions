import xml.etree.ElementTree as etree

maxdepth = 0


def depth_internal(elem, level):
    global maxdepth
    global maxdepth
    maxdepth = max(maxdepth, level)

    for child in elem:
        depth_internal(child, level + 1)


def depth(elem, level):
    depth_internal(elem, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
