# In his name

# Title: Flat file documentation generator
# Description: Converts a collection of MarkDown files to MarkUp output
# Author: MohammadReza Tayyebi

# Libraries

# Name: MarkDown2 by @trentm (Github)
# print(markdown2.markdown("*boo!*"))
import markdown2
import stringbuilder
import os.path

#Read the header
# Create instances of StringBuilder
header = stringbuilder.stringbuilder()
footer = stringbuilder.stringbuilder()
doc = stringbuilder.stringbuilder() # For each file

# Read header file line by line
for l in open('master/header.txt').readlines():
    header.Append(l)

# Read footer file line by line
for l in open('master/footer.txt').readlines():
    footer.Append(l)

# Read each file based on nav.md
directory = None
document = None
for t in open('nav.md').readlines():
    if t.startswith('-'):
        directory = t[2:-1] + '/'
        continue;
    elif t.startswith('    1.'):
        document = t[7:-1]
    
        # Read the file
        doc.Cls()
        path = 'content/' + directory + document + '.md';
        if not os.path.exists(path):
            continue;
        for l in open(path).readlines():
            doc.Append(l)
    print (doc)