from sqlalchemy import create_engine, MetaData, Text, ForeignKey
from sqlalchemy import Table, Column, Integer, String, SmallInteger, Boolean, insert
from secrets3 import config
import json
from pprint import pprint

username = config['host']['username']
DATABASE_URI = f'postgres+psycopg2://{username}@localhost:5432/speedforce'

# print(DATABASE_URI)

engine = create_engine(DATABASE_URI, echo=True)
connection = engine.connect()
metadata = MetaData()

messages = Table('messages', metadata, autoload=True, autoload_with=engine)

with open('slack_jason_dump.json', 'r') as f:
    list_of_messages = json.load(f)

pprint(list_of_messages)

for msg in list_of_messages:
    if 'comments' in msg:
        del msg['comments']
#
pprint(list_of_messages)

#
# query = insert(messages)
# connection.execute(query, list_of_messages)


