# mike stiers
# mike.stiers@gmail.com

# code wallet pro from like 1999 / 2000 did not have the greatest improt export feature.
# when I decided to move to keepass2, i was left with the inability to import the data
# this will take the default txt export option of code wallet pro and turn it into a KeePass2 formatted CSV


import os
import re

pwfile = os.getenv('HOME')+'/k.txt'

category_regex = re.compile(r"^Category: Passwords.*")
card_regex = re.compile(r"^Card: .*")
website_regex = re.compile(r"^Web site: .*")
userid_regex = re.compile(r"^User ID: .*")
password_regex = re.compile(r"^Password: .*")
notes_regex = re.compile(r"^Notes:.*")
entry_list = []

filename = open(pwfile, 'r')

for line in filename:
    print(line)
    if category_regex.match(line):
        category_line = line.split(':', 1)
        category = category_line[1]
    elif card_regex.match(line):
        card_line = line.split(':', 1)
        card = card_line[1]
    elif website_regex.match(line):
        website_line = line.split(':', 1)
        website = website_line[1]
    elif userid_regex.match(line):
        userid_line = line.split(':', 1)
        userid = userid_line[1]
    elif password_regex.match(line):
        password_line = line.split(':', 1)
        password = password_line[1]
    elif notes_regex.match(line):
        entry_list.append([category, card, website, userid, password])
        print('list added')
    else:
        print('not a password category')

while i < len(entry_list):
    print(entry_list[i])
    i += 1
    
    
    
    
