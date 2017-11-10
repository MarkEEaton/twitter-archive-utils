#encoding: utf-8

import json
import codecs
import sys
import os

if len(sys.argv) < 2:
    sys.exit('Usage: python filter.py <file>')

if not os.path.exists(sys.argv[1]):
    sys.exit('Error: File %s not found' % sys.argv[1])

# UTF8Writer = codecs.getwriter('utf8')
# sys.stdout = UTF8Writer(sys.stdout)
	
i = 0

with open(sys.argv[1], 'r') as f:
    content = f.readlines()
    for line in content:
        i += 1
        try:
            fulltweet = json.loads(line)
            username = fulltweet['user']['screen_name'].encode(encoding='UTF-8')
            name = fulltweet['user']['name'].encode(encoding='UTF-8')
            print("\n" + str(username) + " (" + str(name) + ")")
            print(fulltweet.get('created_at'))
            print(fulltweet.get('text').encode('utf-8'))
        except:
            pass
        

#print ('\nTotal number of tweets:')
#print (i)
