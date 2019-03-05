'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''


def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    try:
        with open(source, 'r') as fin:
            lines = fin.readlines()

    except FileNotFoundError as pl:
        print(f'File not found {pl}')

    new_string = ''
    for line in lines:
        new_string += line.replace(pattern, replace)

    with open(dest, 'w') as fir:
        fir.write(new_string)

    return print('code finished')


file = 'rename_file_test'
file2 = 'modified_file_test'

sed('a', 'AAAAA', file, file2)
