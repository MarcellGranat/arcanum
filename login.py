from selenium_wrappers import *
from dotenv import load_dotenv
from time import sleep
import os
load_dotenv()

def main():
    sln_go_to("https://adt.arcanum.com/hu/accounts/login/?next=/hu/")
    sleep(2)  
    
    username = os.getenv("arcanum_username")
    password = os.getenv("arcanum_password")
    sln_find_by_id("id_username").send_keys(username)
    sln_find_by_id("id_password").send_keys(password)
    sln_partial_find("btn-primary").click()
    sleep(3)
    
if __name__ == "__main__":
    sln_start_firefox()
    main()
