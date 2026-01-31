# Used to fetch the Mutual Fund Data from AMFI 

import requests

AMFI_URL = "https://portal.amfiindia.com/spages/NAVOpen.txt"

class NAVFetcher:
    #@staticmethod is used to define a method that doesn't need access to the instance (self) or class (cls)
    @staticmethod
    def get_latest_nav(scheme_code):
        response = requests.get(AMFI_URL)
        for line in reponse.text.splitlines():
            if line.startswith(scheme_code + ";"):
                parts = line.split(";")
                nav = float(parts[4])
                date = parts[5]
                return nav , date
        
        return None, None
            