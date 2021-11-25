import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from argupy import *


def debug(*args, **kwargs):
  if VERBOSE: print(*args, **kwargs)

def get_message_box():
  global driver

  return driver.find_element_by_css_selector('div div > main form div > div > div[contenteditable=true] > div > span > span > span')

def send_message(msg, clear=False):
  global driver

  inp = get_message_box()

  if clear: inp.clear()
  
  inp.send_keys(msg + Keys.ENTER)

  return inp


DEFAULT_CHAT_URL = 'https://discord.com/channels/783422192720412694/910280045178810388'

args = Args()
args.setarg('--chat-url', STR, DEFAULT_CHAT_URL, '-c')
args.setarg('--username', STR, '', '-u')
args.setarg('--verbose', short='-v')
args.setarg('--dont-get-daily-coins', short='-D')

CHAT_URL = args.arg('--chat-url')
USERNAME = args.arg('--username')
VERBOSE  = args.arg('--verbose')
NODAILY  = args.arg('--dont-get-daily-coins')


debug('Starting chromedriver...')

driver = webdriver.Chrome('./chromedriver96')
driver.set_window_position(0, 0)
driver.set_window_size(1120, 1080)

debug('Started chromedriver.')

driver.get(CHAT_URL)

debug('Doing login...')

if USERNAME != '':
  time.sleep(1)

  debug('Autofilling username...')

  driver.find_element_by_css_selector('div > form > div div > input[name=email]').send_keys(USERNAME + Keys.TAB)

  debug('Autofill done.')

while True:
  if not '://discord.com/login' in driver.current_url: break

debug('Login completed.\nWaiting for a channel...')

while True:
  if '://discord.com/channels/' in driver.current_url: break

debug('Channel found.')

time.sleep(5)

if NODAILY:
  debug('Skipped daily coins.')
else:
  debug('Getting daily coins...')

  send_message('8k!daily')

  debug('Done')

try:
  i = 10

  while True:
    message = '8k!beg'
    if i >= 11:
      message = '8k!work'

      i = 0

    try:
      send_message(message)
    except (NoSuchElementException, ElementNotInteractableException):
      continue

    time.sleep(11)

    i += 1
except KeyboardInterrupt:
  print('')

debug('Quitting...')

driver.quit()