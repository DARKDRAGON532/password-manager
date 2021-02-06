import secrets
import string
import json
import argparse


def gen_pass(l: int):
    p = ""
    for _ in range(l):
        p += secrets.choice(alphabets)
    return p


def delete(n):
    global passwords
    try:
        del passwords[n]
    except (KeyError):
        print(f'No keyword "{n}" found')
        return
    if input("Are you sure? (Y/n): ").lower() != "y":
        print("Cancelled")
        return
    with open("passwords.json", "w") as f:
        f.write(json.dumps(passwords))
    print("Deleted")


def add(n, l: int, s="None"):
    global passwords
    p = gen_pass(l)
    passwords[n] = {"site": s, "password": p, "name": n}
    with open("passwords.json", "w") as f:
        f.write(json.dumps(passwords))
    print(f"Name: {n} Password: {p} Site: {s}")


def display(n=None):
    global passwords
    if n:
        for x in passwords.values():
            if n.lower() in x["name"].lower():
                print(
                    f"Name: {x['name']} Password: {x['password']} Site: {x['site']}")
                break
    else:
        for x in passwords.values():
            print(
                f"Name: {x['name']} Password: {x['password']} Site: {x['site']}")


alphabets = string.ascii_letters + string.digits + string.punctuation
parser = argparse.ArgumentParser(prog="Password Manager")
parser.add_argument("option", help="Choose display | d for displaying all passwords or add | a for adding new password or del | delete for removing password", choices={
                    "d", "display", "a", "add", "del", "delete"})
parser.add_argument(
    "-n", "--name", help="Name for password / password to search for / password to delete")
parser.add_argument("-l", "--length", help="Length for password", type=int)
parser.add_argument("-site", "--site", help="Site for password (Optional)")
args = parser.parse_args()

try:
    with open("passwords.json", "r") as f:
        passwords = json.load(f)
except:
    with open("passwords.json", "w") as f:
        f.write("{}")

    with open("passwords.json", "r") as f:
        passwords = json.load(f)

if args.option == "d" or args.option == "display":
    if not args.name:
        display()
    else:
        display(args.name)
elif args.option == "del" or args.option == "delete":
    if args.name:
        delete(args.name)
    else:
        print("Missing argument name")
else:
    if args.name and args.length:
        if args.site:
            add(args.name, args.length, args.site)
        else:
            add(args.name, args.length)
    else:
        argument = ""
        if not args.length:
            argument += "length "
        if not args.name:
            argument += "name"

        print(f"Missing argument {argument}")