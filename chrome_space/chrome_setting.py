import sys, os
from selenium import webdriver

sys.path.append("/usr/local/bin/chromedriver")  # mac
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/chrome_space')
chromedriver_dir = (BASE_DIR + '/chromedriver.exe') # company windows path
options = webdriver.ChromeOptions()
options.add_argument('--headless') # selenium 背后执行
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('log-level=3')
