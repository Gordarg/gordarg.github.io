# In his name
# Title: Flat file documentation generator
# Description: Converts a collection of MarkDown files to MarkUp output
# Author: MohammadReza Tayyebi

# Libraries
# Name: MarkDown2 by @trentm (Github)
import markdown2
# Name: StringBuilder by @tayyebi (Github)
import stringbuilder
# Name: Names PY by @tayyebi (Github)
import names
# Name: OS
import os.path
# Name: IO
import io

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

# Get files
index = [] # This will store file names
directory = None # This will switch directoy foreach sub located file
for t in open('nav.md').readlines(): # Reads each file based on nav.md
    if t.startswith('-'):
        directory = t[2:-1] + '/'
        continue;
    elif t.startswith('    1.'):
        document = t[7:-1]
        index.append('content/' + directory + document + '.md')

# Build menu
# TODO

# Read each file content
i = -1;
while i < len(index) - 1:
    i += 1 # Because of `continue` we have to do ++ here
    doc.Cls()
    if not os.path.exists(index[i]):
        continue;
    with io.open(index[i], 'r', encoding='utf8') as f:
        doc.Append(markdown2.markdown(f.read()))
    # File name
    n = names.names() # Create an instance of Names PY
    n.Generate(index[i])
    with io.open("a_" + str(n) + '.html','w',encoding='utf8') as f:
        f.write(unicode(header))
        f.write(unicode(doc))
        f.write(unicode(footer))