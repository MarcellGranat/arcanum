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
       blocks = [button for button in block_buttons if button.text != '']
    titles = sln_texts(block_buttons)
    links = [block.get_attribute("href") for block in blocks]
    return titles, links

def go_to_block(title):
    titles, links = blocks()
    found = False
    for i in range(len(titles)):
        if titles[i] == title:
            found = True
            sln_go_to(links[i])
            break
    if not found:
      print("Block not found")

def yield_pdf_viewer_links():
    pdf_links = sln_partial_find_all("text-decoration-none")
    pdf_links = [_ for _ in pdf_links if _.get_attribute("data-pdf") is not None]
    pdf_links = [_ for _ in pdf_links if _.get_attribute("data-pdf") != ""]
    pdf_links = [_.get_attribute("data-pdf") for _ in pdf_links]
    return pdf_links
