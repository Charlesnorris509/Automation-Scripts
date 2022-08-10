#!/usr/bin/python

import re, pyperclip

URLRegex = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)

txt = str(pyperclip.paste())
matches = []
for groups in URLRegex.findall(txt):
  matches.append(groups[:])
  
if len(matches) > 0:
  pyperclips.copy('\n'.join(matches))
  print('URL Copied to the Clipboard')
  print('\n'.join(matches))
else:
  print('No URL was found')
