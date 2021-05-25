#! python3

# rudimentary address lookup using maps.google
# prior to using must install pyperclip :: pip3 install pyperclip

# mapIt.py - use google maps to find an address either from the cli or clipboard (pyperclip)

import webbrowser, sys, pyperclip

# look for an address on the cli
if len(sys.argv) > 1:
    # join address as an array of strings :: ' ' denotes a space between each argument
    address = ' '.join(sys.argv[1:])

    # if no arguments are passed check clipboard for contents
else:
    address = pyperclip.paste()

# open default webbrowser with contents of address
webbrowser.open_new('https://www.google.com/maps/place/' + address)
