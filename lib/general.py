from __future__ import annotations
import time
from typing import Any, Dict, Optional, TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from account import Account

BASE_URL = "https://mobile.southwest.com/api/"


def make_request(
    method: str, site: str, account: Account, info: Dict[str, str]
) -> Optional[Dict[str, Any]]:
    url = BASE_URL + site

    # In the case that your server and the Southwest server aren't in sync,
    # this requests multiple times for a better chance at success when checking in
    attempts = 0
    while attempts < 20:
        if method == "POST":
            response = requests.post(url, headers=account.headers, json=info)
        elif method == "GET":
            response = requests.get(url, headers=account.headers, params=info)
        else:
            print(f"\033[91mError: Method {method} not known\033[0m")
            return

        if response.status_code == 200:
            return response.json()

        attempts += 1
        time.sleep(0.5)

    print(f"Failed to retrieve reservation. Reason: {response.reason} {response.status_code}")
    # TO-DO: Kill thread without killing other threads or the main process
    # The thread does not exit at the moment, it instead continues even after failing
