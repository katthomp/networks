# File: CheckTags.py

"""
This program checks that tags are properly matched in an HTML file.
This version of the program runs in Python; the checktags version runs
directly from the command line.
"""

import html.parser
import urllib.request
import urllib.error

def CheckTags():
    """Reads a URL from the user and then checks it for tag matching."""
    url = input("URL: ")
    checkURL(url)

def checkURL(url):
    """Checks whether the tags are balanced in the specified URL."""
    try:
        response = urllib.request.urlopen(url)
        print(type(response))
        parser = HTMLTagParser()
        parser.checkTags(response.read().decode("UTF-8"))
    except urllib.error.URLError:
        print("Something went wrong")


class HTMLTagParser(html.parser.HTMLParser):

    """
    This class extends the standard HTML parser and overrides the
    callback methods used for start and end tags.
    """

    def __init__(self):
        """Creates a new HTMLTagParser object."""
        html.parser.HTMLParser.__init__(self)
        self._link_stack=[]
    def brokenLinks(self):
        for url in self._link_stack:
            try:
                response=urllib.request.urlopen(url)
                self.checkTags(response.read().decode("UTF-8"))
            except urllib.error.URLError:
                print("Link doesn't work")
    def checkTags(self, text):
        """Checks that the tags are balanced in the supplied text."""
        try:
            self._stack = [ ]
            self.feed(text)
            while len(self._stack) > 0:
                startTag,startLine = self._stack.pop()
                print("Missing </" + startTag + "> for <" + startTag +
                    "> at line " + str(startLine))
        except urllib.error.URLError:
            print("something didn't work")

    def handle_starttag(self, startTag, attributes):
        """Overrides the callback function for start tags."""
        try:
            startLine,_ = self.getpos()
            self._stack.append((startTag, startLine))
            print(attributes)
            self._link_stack = [x[1] for x in attributes if 'href' in attributes or 'src' in attributes]
        except urllib.error.URLError:
            print("nope")



    def handle_endtag(self, endTag):
        """Overrides the callback function for end tags."""
        try:
            endLine,_ = self.getpos()
            if len(self._stack) == 0:
                print("No <" + endTag + "> for </" + endTag +
                    "> at line " + str(endLine))
            else:
                while len(self._stack) > 0:
                    startTag,startLine = self._stack.pop()
                    if startTag == endTag:
                        break;
                    print("Missing </" + startTag + "> for <" + startTag +
                        "> at line " + str(startLine))
        except urllib.error.URLError:
            print("bad")
'''
I need to make this code be able to handle broken links in the html page



'''
# Startup code

if __name__ == "__main__":
    CheckTags()
