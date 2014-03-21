import sys
import urllib

query = sys.argv[1]

def urlencode(value):
    """
    URLEncodes a string
    """
    print urllib.quote(value)

if __name__ == '__main__':
    urlencode(query)