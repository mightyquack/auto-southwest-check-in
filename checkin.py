#!/usr/bin/env python3
import sys

from lib.account import Account


if __name__ == "__main__":
    arguments = sys.argv
    confirmation_number = arguments[1]
    first_name = arguments[2]
    last_name = arguments[3]

    account = Account(first_name=first_name, last_name=last_name)
    account.get_checkin_info(confirmation_number)
