#!/usr/bin/env python3

import argparse
import os
import time


# Define account and password
facebook = "yourfbpassword"
instagram = "yourigpassword"
twitter = "yourtwitterpassword"

#set up argparse
parser = argparse.ArgumentParser(description="!WARNING! Since this script handles sensitive data, make sure you have FileVault turned on. This file should be saved as a hidden file somewhere in the /root/ directory. The permissions should be set like so: 'sudo chown root:root <THIS_FILES_NAME>' and 'sudo chmod 700 <THIS_FILES_NAME>' This script must be run inside the macos 'terminal' Application. If not it will not work. Edit this file and set your password in the 'Define account and password' section above. Neither myself nor github will be held responsible for improper use of this script.")
parser.add_argument("account")
args = parser.parse_args()

#Close terminal window after password has been printed for 3 seconds
def close_session():
    osa = """osascript -e 'tell application "Terminal" to close first window' & exit"""
    print("Exiting session in 3 seconds!")
    time.sleep(3)
    os.system(osa)

def main():
    if args.account == "facebook":
        print(facebook)
    elif args.account == "instagram":
        print(instagram)
    elif args.account == "twitter":
        print (twitter)
    else:
        print("none")

if __name__ =="__main__":
    main()
    close_session()
