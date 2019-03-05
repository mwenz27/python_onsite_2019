class AttentionError(Exception):
    raise 'AttentionError'


file = 'war_and_peace.txt'
with open(file, 'r') as fin:
    content = fin.read()

file_2 = 'crime_and_punishment.txt'
with open(file_2, 'w') as fout:
    fout.write('')

books = ['book1', 'book2', 'book3']

try:

except FileNotFoundError as fnf:
    print(fnf)
except PermissionErroras as err:

else:
    try:
        first_char = content[:100]
    except IndexError as err:
        print(err)
    else:
        if 'attention' in first_char:
            raise AttentionError
        print(first_char)

