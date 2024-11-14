import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

_default_browser = 'chrome'
_default_headless = False

_current_directory_path = os.getcwd()

_project_path=os.path.dirname(_current_directory_path)
_default_chrome_path = f'{_project_path}\\resources\\browser\\GoogleChrome.exe'
_default_chrome_driver_path = f'{_project_path}\\resources\\browser\\driver\\chromedriver.exe'
_default_firefox_path = f'{_project_path}\\resources\\browser\\Firefox.exe'
_default_firefox_driver_path = f'{_project_path}\\resources\\browser\\driver\\geckodriver.exe'
_default_screenshot_allowed = True

BROWSER = f'{"Headless" if os.environ.get("HEADLESS", _default_headless) else ""}{os.environ.get("BROWSER", _default_browser).lower()}'

CHROME_PATH = os.environ.get('CHROME_PATH', _default_chrome_path)
CHROME_DRIVER_PATH = os.environ.get('CHROME_DRIVER_PATH', _default_chrome_driver_path)
_chrome_options = ChromeOptions()
_chrome_options.add_argument('disable-notifications')
_chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
#_chrome_options.binary_location = CHROME_DRIVER_PATH

FIREFOX_PATH = os.environ.get('FIREFOX_PATH', _default_firefox_path)
FIREFOX_DRIVER_PATH = os.environ.get('FIREFOX_DRIVER_PATH', _default_firefox_driver_path)
_firefox_options = FirefoxOptions()
#_firefox_options.binary_location = FIREFOX_DRIVER_PATH

if 'chrome' in BROWSER:
    DRIVER_PATH = os.environ.get('DRIVER_PATH', CHROME_DRIVER_PATH)
    BROWSER_PATH = os.environ.get('BROWSER_PATH', CHROME_PATH)
    BROWSER_OPTIONS = _chrome_options
    #BROWSER_OPTIONS = f'add_argument("--disable-popup-blocking"); add_argument("--disable-notifications"); add_experimental_option("excludeSwitches", "disable-popup-blocking")'
elif 'firefox' in BROWSER:
    DRIVER_PATH = os.environ.get('DRIVER_PATH', FIREFOX_DRIVER_PATH)
    BROWSER_PATH = os.environ.get('BROWSER_PATH', FIREFOX_PATH)
    BROWSER_OPTIONS = _firefox_options.to_capabilities()
else:
    DRIVER_PATH = os.environ.get('DRIVER_PATH', '')
    BROWSER_PATH = os.environ.get('BROWSER_PATH', '')
    BROWSER_OPTIONS = {"browserName" : BROWSER,
                           "binary" : DRIVER_PATH}

SCREENSHOT_ALLOWED=os.environ.get('SCREENSHOT_ALLOWED', _default_screenshot_allowed)

AUTOMATION_EXERCISE_URL='http://automationexercise.com'