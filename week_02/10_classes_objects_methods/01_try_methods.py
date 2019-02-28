'''
We've learned about strings earlier. Looking at string methods from the
perspective of "everything is an object in python" explains the syntax
that we encountered there.

Now take a second look at the documentation of the string methods at:
http://docs.python.org/3/library/stdtypes.html#string-methods.

Demonstrate 3 interesting string methods of your choice and explain why
they are invoked like this: str.method()


'''

# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional
# arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

string1 = 'Walking on this path will open new'
string2 = 'pa'
x = string1.find(string2)
print(string1[x])


# str.partition(sep)

# containing the part before the separator,
# the separator itself, and the part after the separator.
# If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

a = "this is a test is testing what is a test in this "
print('method 2a', a.partition("test")) # Split the string at the first occurrence of sep, and return a 3-tuple
print('method 2b', a.partition("s"))

# str.splitlines([keepends])
# Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
#
# This method splits on the following line boundaries. In particular, the boundaries are a superset of universal newlines.
#
# Representation	Description
# \n	Line Feed
# \r	Carriage Return
# \r\n	Carriage Return + Line Feed
# \v or \x0b	Line Tabulation
# \f or \x0c	Form Feed
# \x1c	File Separator
# \x1d	Group Separator
# \x1e	Record Separator
# \x85	Next Line (C1 Control Code)
# \u2028	Line Separator
# \u2029	Paragraph Separator
# \v Vertical Tab, 0x0b
# \f ASCII 0x0c, a.k.a. “new page”

a = " 324\x859r\f3u\x1cjdjf\n\r\v\u2028"
print('method 3', a.splitlines()) #creating a list without the \ as mentioned above