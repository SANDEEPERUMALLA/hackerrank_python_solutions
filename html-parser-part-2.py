from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if len(data.split('\n')) != 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.replace("\r", "\n"))

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


n = int(input())
parser = MyHTMLParser()
htmlString = ''
for i in range(n):
    htmlString += input() + '\n'

parser.feed(htmlString)
