import imaplib
import credentials

host = 'imap.gmail.com'
port = 993

user = 'ubirajara2018@gmail.com'
password = 'dnygokmrngbshshr'

server = imaplib.IMAP4_SSL(host, port)
server.login(user, password)
server.select("Deschamps")

status, data = server.search(None, "(UNSEEN)")

for num in data[0].split():
    status, data = server.fetch(num, "(RFC822)")
    email_msg = data[0][1]
