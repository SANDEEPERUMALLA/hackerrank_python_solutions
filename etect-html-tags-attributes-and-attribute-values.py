from html.parser import HTMLParser


def printAttrs(attrs):
    for attr in attrs:
        print('-> {0} > {1}'.format(attr[0], attr[1]))
    pass


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag.strip())
        printAttrs(attrs)

    def handle_startendtag(self, tag, attrs):
        print(tag.strip())
        printAttrs(attrs)


n = int(input())
parser = MyHTMLParser()
htmlString = ''
for i in range(n):
    htmlString += input() + '\n'

parser.feed(htmlString)
