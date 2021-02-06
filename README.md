# Password Manager CLI

This is a password manager that works in the CLI.
I made this as a small project so I would recommend you to use DashLane or LastPass or any other password manager to keep your passwords safe and secure since this is probably not the best way of storing it.

# Usage
```
usage: Password Manager [-h] [-n NAME] [-l LENGTH] [-site SITE] {add,delete,del,a,d,display}

positional arguments:
  {add,delete,del,a,d,display}
                        Choose display | d for displaying all passwords or add | a for adding new password or del | delete for removing password

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name for password / password to search for / password to delete
  -l LENGTH, --length LENGTH
                        Length for password
  -site SITE, --site SITE
                        Site for password (Optional)
```