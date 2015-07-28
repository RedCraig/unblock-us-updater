#!/usr/bin/python3
#
# Unblock-Us Update-Script
#
# This script automatically sends your current IP adress to the Unblock-Us api.
# It can be used to update your IP adress via cron.
#
# Author:       Timo Schlueter
# Mail:         me@timo.in
# Web:          www.timo.in
# Twitter:      twitter.com/tmuuh
#
# Version:      0.3
# Date:         19-12-2014
#
# Notes:        I am not affiliated with Unblock-Us
#

import argparse
import sys

from urllib.request import urlopen

# TODO: Check that this url actually updates the ip address, it looks like it
#       only checks if the current address is the active one.
APIURL = "https://api.unblock-us.com/login"


def main(email, password):
    request = urlopen(APIURL + "?" + email + ":" + password)
    response = request.read()
    request.close()

    if (response == bytes('active', 'UTF-8')):
        print("IP address is active. You are good to go!")
        sys.exit(0)
    elif (response == bytes('bad_password', 'UTF-8')):
        print("Wrong username or password.")
        sys.exit(1)
    elif (response == bytes('not_found', 'UTF-8')):
        print("Username not found.")
        sys.exit(1)
    else:
        print("Unknown error. Check api url or documentantion.")
        print('%s' % response)
        sys.exit(1)


def setup_arg_parser():
    """Create the arg parser Unblock-Us credentials args."""
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="Unblock-Us email.")
    parser.add_argument("password", help="Unblock-Us password.")
    return parser


if __name__ == '__main__':
    parser = setup_arg_parser()
    args = parser.parse_args()
    main(args.email, args.password)
