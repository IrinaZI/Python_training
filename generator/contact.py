from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "date\\contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(prefix, maxlen):
    symbols = string.punctuation + "" + string.digits*40
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(Firstname=random_string("First", 10), Middlename=random_string("Middle", 10),
                         Lastname=random_string("Last", 10),
                         Nickname=random_string("Nick", 8), Title=random_string("Title", 15),
                         Company=random_string("Company", 20),
                         Address=random_string("Address", 40), Home=random_number("", 8), Mobile=random_number("", 10),
                         Work=random_number("", 10), Fax=random_number("", 10), Email=random_string("mail@", 15),
                         Email2=random_string("mail2@", 15), Email3=random_string("mail", 15),
                         Homepage=random_string("www.", 15),
                         Bday="3", Bmonth="March", Byear="1979",
                         Aday="10", Amonth="September", Ayear="2017",
                         Address2=random_string("Address", 40), Phone2=random_number("", 12),
                         Notes=random_string("Address", 70))
                 for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
