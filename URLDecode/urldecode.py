import sys
import urllib

query = sys.argv[1]

def urldecode(value):
    """
    URLDecodes a string
    """
    print urllib.unquote(value)

if __name__ == '__main__':
    urldecode(query)