#!/usr/bin/python

import re, pyperclip

EmailRe = re.compile(r'''(
                     [a-zA-Z0-9._%+-]+
                     @
                     [a-zA-Z0-9.-]+
                     (\.[a-zA-Z]{2,4})
                     )''',re.VERBOSE)

txt = str(pyperclip.paste())

matches = []
for group in EmailRe.findall(txt):
  matches.append(group[0])
  
if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('Copied')
  print('\n'.join(matches))
else:
  print("No Email Addresses Found in this text")
        
        
