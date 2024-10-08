from selenium_wrappers import *
from selenium.webdriver.common.keys import Keys
from time import sleep
from tqdm import tqdm
from selenium.webdriver.common.action_chains import ActionChains
from logger_config import get_logger

logger = get_logger()

def subheaders():
    return sln_partial_find_all(pattern="MuiTreeItem-label")

def titles_to_txt(filename: str="titles.txt"):
    titles = [_.text for _ in subheaders()]
    with open(filename, "w") as f:
        f.write("\n".join(titles))

    logger.success(filename + " created")

def n_pages():
  n = sln_partial_find_all("MuiInputAdornment-root MuiInputAdornment-positionEnd MuiInputAdornment-outlined MuiInputAdornment-sizeMedium")[1]
  n = int(n.text[2:]) # remove: '/ '
  return n

def current_page():
    return int(sln_partial_find_all(pattern="uiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd")[1].get_attribute("value"))

def overwrite_field(field, value):
    field.send_keys(Keys.COMMAND, 'a')
    field.send_keys(Keys.BACKSPACE)
    sleep(.5)
    field.send_keys(value)

def sendesc():
    ActionChains(sln_get_browser()).send_keys(Keys.ESCAPE).perform()

def close_pdf_window() -> None:
    browser = sln_get_browser()
    windows = browser.window_handles
    while len(windows) > 1:
        browser.switch_to.window(windows[1])
        sleep(.5)
        if browser.current_url.endswith(".pdf"):
            browser.close()
            break
        else: # if it is not a pdf window
            logger.error("A new window is opened.")
            break
    windows = browser.window_handles
    browser.switch_to.window(windows[0])
    sleep(.2)
    sendesc()
    sleep(.2)

def download_pdf(pages_from: int = 1, pages_to: int = 10) -> None:
    """
    Download a range of pages from the current document.

    Clicks the "Oldalak mentése" button, then sets the start and end page fields
    to the provided values, and finally clicks the "MENT S" button.

    :param from: The first page to download (inclusive)
    :param to: The last page to download (inclusive)
    """
    sln_find_by_xpath("//span[@aria-label='Oldalak mentése']").click()
    sleep(1)
    start_field = sln_find_by_id("first page")
    overwrite_field(start_field, str(pages_from))
    sleep(.3)
    last_field = sln_find_by_id("last page")
    overwrite_field(last_field, str(pages_to))
    save_button = [_ for _ in sln_partial_find_all("MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium") if _.text == "MENTÉS"][0]
    save_button.click()
    sleep(2)

    logger.info(f"Downloaded pages {pages_from}-{pages_to}")

def download_in_batches(on_error, msg = "Downloading"):
    prev_page_nmr = 1
    n_subheaders = len(subheaders())
    # for subheader in tqdm(subheaders()[1:], "Downloading"):
    for i in tqdm(range(1, n_subheaders), msg):
        while True:
            try:
                subheader = subheaders()[i]
                subheader.click()
                current_page_nmr = current_page()
                download_pdf(prev_page_nmr, current_page_nmr - 1)
                sleep(3)
                close_pdf_window()
                prev_page_nmr = current_page_nmr
                break
            except Exception as e:
                on_error(e)

    # download the last page
    download_pdf(prev_page_nmr, n_pages())
    sleep(3)
    close_pdf_window()

def start_batch(data_pdf):  
    data_link = f"https://adt.arcanum.com{data_pdf}?pg=0&layout=s"
    txt_filename = data_folder() + "/" + data_pdf.split("/")[3] + ".txt"
    sln_go_to(data_link)
    sleep(2)
    titles_to_txt(txt_filename)

def default_on_error(error, url_to_restart, **kwargs):
    logger.error(error)
    sln_start_firefox(**kwargs)
    sln_go_to(url_to_restart)
    sleep(15)
    sln_refresh()

def main(data_pdf, **kwargs):
    start_batch(data_pdf=data_pdf)
    def custom__on_error(error):
        default_on_error(error, data_pdf, **kwargs)

    download_in_batches(on_error=custom__on_error, msg=data_pdf)
    logger.success(data_pdf + "Done!")

if __name__ == "__main__":
    import login
    import open_magazine
    sln_start_firefox(headless=False)
    login.main()
    sleep(2)
    open_magazine.go_to_magazine("NemzetiSport")
    sleep(1)
    sln_go_to(open_magazine.link_for_block(0))
    sleep(1)
    data_pdf = open_magazine.pdf_viewer_links()[0]
    sleep(3)
    main(data_pdf=data_pdf)
