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
menu = stringbuilder.stringbuilder()
doc = stringbuilder.stringbuilder() # For each file

# Read header file line by line
for l in open('master/header.txt').readlines():
    header.Append(l)

# Read footer file line by line
for l in open('master/footer.txt').readlines():
    footer.Append(l)

# Get files and build menu
index = {} # This will store file names
directory = None # This will switch directoy foreach sub located file
i = 0;

menu.Append('<ul class="navigation">');
for t in open('nav.md').readlines(): # Reads each file based on nav.md
    if t.startswith('-'):
        directory = t[2:-1] + '/'
        menu.Append('<li class="grp">' + directory + '</li>')
        continue;
    elif t.startswith('    1.'):
        document = t[7:-1]
        i += 1
        # File name
        n = names.names() # Create an instance of Names PY
        filename = 'content/' + directory + document + '.md'
        n.Generate(filename)
        newfilename = "a_" + str(n)[:-2] + '.html';
        # Add to dictionary
        index[filename] = newfilename
        menu.Append('<li><a href="' + newfilename + '">' + filename + '</a></li>');
menu.Append('</ul>');

# Read each file content
i = -1;
while i < len(index) - 1:
    i += 1 # Because of `continue` we have to do ++ here
    print(index.keys()[i])
    doc.Cls()
    if not os.path.exists(index.keys()[i]):
        continue;
    with io.open(index.keys()[i], 'r', encoding='utf8') as f:
        doc.Append(markdown2.markdown(f.read()))
    with io.open(index.values()[i],'w',encoding='utf8') as f:
        f.write(unicode(header))
        f.write(unicode(menu))
        f.write(unicode(doc))
        f.write(unicode(footer))