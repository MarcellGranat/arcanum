from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import tempfile
import webbrowser

browser = None

def sln_start_firefox(headless = False):
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    options = Options()
    if headless:
        options.add_argument('-headless')
    global browser
    browser = webdriver.Firefox(capabilities=firefox_capabilities, options=options)
    if headless:
      print("Firefox started in headless mode")
    else:
      print("Firefox started")
    
def sln_get_browser():
    return browser

def sln_go_back():
    browser.back()

def sln_refresh():
    browser.refresh()

def sln_partial_find(pattern):
    """Find elements on a website opened with selenium, 
    where the id contains the given input string.
    """
    pattern = "//*[contains(@class, '" + pattern + "')]"
    elements = browser.find_element("xpath", pattern)
    return elements

def sln_partial_find_all(pattern):
    """Find elements on a website opened with selenium,
    where the id contains the given input string.
    """
    pattern = "//*[contains(@class, '" + pattern + "')]"
    elements = browser.find_elements("xpath", pattern)
    return elements

def sln_find_by_xpath(xpath):
    return browser.find_element("xpath", xpath)

def sln_find_all_by_xpath(xpath):
    return browser.find_elements("xpath", xpath)

def sln_find_by_id(id):
    return browser.find_element("id", id)

def sln_find_all_by_id(id):
    return browser.find_elements("id", id)

def sln_go_to(url):
    print("Going to " + url)
    browser.get(url)
    
def sln_texts(elements):
    return [element.text for element in elements]
    
def sln_click(element):
  try:
    element.click()
    return True
  except:
    return False

def sln_current_url():
    return browser.current_url

def sln_quit():
    browser.quit()
    
def sln_partial_find_w_label(pattern, label):
    """Find elements on a website opened with selenium,
    where the id contains the given input string and the text a label.
    """
    pattern = "//*[contains(@class, '" + pattern + "')]"
    elements = browser.find_elements("xpath", pattern)
    element = [element for element in elements if element.text == label]
    if len(element) > 0:
      return element[0]
    else:
      return None
    
def sln_page():
    return browser.page_source
  

def sln_view_html(xml_obj):
    # Create a temporary file with .html extension
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as temp_file:
        # Write the XML object content as a string to the file
        temp_file.write(str(xml_obj).encode('utf-8'))
        # Get the file path
        temp_file_path = temp_file.name
    
    # Open the HTML file in the default web browser
    webbrowser.open(f"file://{temp_file_path}")
    
def sln_view_page():
    sln_view_html(sln_page())
    

