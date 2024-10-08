from selenium_wrappers import *
import login
from selenium.webdriver.common.by import By

def go_to_magazine(magazine):
    sln_go_to(f"https://adt.arcanum.com/hu/collection/{magazine}/")

def blocks():
    block_buttons = sln_partial_find_all("btn")
    if block_buttons:
       block_buttons = block_buttons[1:]
       block_buttons = [button for button in block_buttons if button.get_attribute("href") is not None]
       block_buttons = [button for button in block_buttons if button.text != '']
    return block_buttons

def pdf_viewer_links():
    pdf_links = sln_partial_find_all("text-decoration-none")
    pdf_links = [_ for _ in pdf_links if _.get_attribute("data-pdf") is not None]
    pdf_links = [_ for _ in pdf_links if _.get_attribute("data-pdf") != ""]
    pdf_links = [_.get_attribute("data-pdf") for _ in pdf_links]
    return pdf_links

if __name__ == "__main__":
    from time import sleep
    sln_start_firefox(headless=False)
    login.main()
    sleep(2)
    from open_magazine import *
    go_to_magazine("NemzetiSport")
    sleep(1)
    print(blocks())
