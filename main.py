from selenium_wrappers import *
from time import sleep
import login
import open_magazine
import download_pdf

def main(magazine, blocks: int | range | None = None, years: int | range | None = None, headless = False):
    sln_start_firefox(headless=headless)
    login.main()
    sleep(2)
    open_magazine.go_to_magazine(magazine)
    sleep(2)
    if blocks:
        block_to_download = [open_magazine.blocks()[_] for _ in blocks]
    else:
        block_to_download = open_magazine.blocks()
    block_links = [_.get_attribute("href") for _ in block_to_download]

    for block_link in block_links:
        sln_go_to(block_link)
        sleep(2)
        if years:
            data_pdfs = open_magazine.pdf_viewer_links()
            data_pdfs = [data_pdfs.blocks()[_] for _ in years]
        else:
            data_pdfs = open_magazine.pdf_viewer_links()
        for data_pdf in data_pdfs:
            download_pdf.main(data_pdf=data_pdf, headless=headless)

if __name__ == "__main__":
    main(magazine="Nepszava", blocks=range(3, 10), headless=True)