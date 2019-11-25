from datetime import date
import sqlite3


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
t = ('chris',)
c.execute('SELECT * FROM auth_user')
users = c.fetchall()

profiles = []
for user in users:
    user_id = (user[0],)
    c.execute('SELECT * FROM users_profile WHERE user_id=?', user_id)
    profiles += c.fetchall()

#print(profiles)

mailing_list = []

for user in users:
    for prof in profiles:
        if user[0] == prof[2] and None not in prof:
            mailing_list += [{'first_name':user[5], 'email':user[6], 'zipcode':prof[1]}]

print(mailing_list)

def getDate():
    return str(date.today())

def getName(name):
    return name