#! python3


# mapIt.py - use google maps to find an address either from the cli or clipboard (pyperclip)

import webbrowser, sys, pyperclip


# look for an address on the cli 
if len(sys.argv) > 1:
    # join address as an array of strings
    address = ''.join(sys.argv[1:])

    # if no arguments are passed check clipboard for contents
else:
    address = pyperclip.paste()

# open default webbrowser with contents of address
webbrowser.open('https://www.google.com/maps/place/' + address)




