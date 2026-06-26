print("===================================")
print(" UNIVERSITY ELECTION VOTING SYSTEM ")
print("===================================")

import json
import os
import getpass

CANDIDATE_FILE = "candidates.json"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def load_candidates():

    if os.path.exists(CANDIDATE_FILE):

        try:

            with open(CANDIDATE_FILE, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []

    return []