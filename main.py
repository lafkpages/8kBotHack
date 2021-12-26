import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from argupy import STR, Args


'''
EXIT CODES:
3  - User interrupted before start (Ctrl + C)
2  - User interrupted while running
'''


def debug(*args, **kwargs):
  if VERBOSE:
    print(*args, **kwargs)

def get_way_too_spicy_button():
  return DRIVER.find_element_by_css_selector(
    'div div > div > div > form > div > button[type=submit][class*=button-] > div'
  )

def enter_the_chill_zone():
  try:
    # Get the "Enter the chill zone" button
    btn = get_way_too_spicy_button()

    # Click it
    btn.click()

    # Send the message that is currently in the message box
    send_message('')

    return True
  except:
    return False

def get_message_box():
  return DRIVER.find_element_by_css_selector(
    'div div > main form div > div > div[contenteditable=true] > div > span > span > span'
  )

def send_message(msg, clear=False):
  try:
    inp = get_message_box()

    if clear:
      # Clear the message box
      inp.clear()
    else:
      # Send the current message
      # in the message box
      inp.send_keys(Keys.ENTER)

    inp.send_keys(msg + Keys.ENTER)

    enter_the_chill_zone()

    time.sleep(0.01)

    return True
  except:
    return True

def send_message_forced(*args, **kwargs):
  has_succeded = False

  while not has_succeded:
    has_succeded = send_message(*args, **kwargs)

def exit_spammer(code=0, msg=True):
  if msg:
    debug('Quitting...')

  DRIVER.quit()

  exit(code)


DEFAULT_CHAT_URL = 'https://discord.com/channels/783422192720412694/910280045178810388'

args = Args()
args.setarg('--chat-url', STR, DEFAULT_CHAT_URL, '-c')
args.setarg('--username', STR, '', '-u')
args.setarg('--verbose', short='-v')
args.setarg('--dont-get-daily-coins', short='-D')
args.setarg('--cactus', short='-C')
args.setarg('--cactus-daily')
args.setarg('--cycles')
args.setarg('--cycles-daily')
args.setarg('--cycles-verify')
args.setarg('--cycles-coffee')
args.setarg('--cycles-finger')
args.setarg('--cycles-phone')
args.setarg('--dont-do-8kbot')
args.setarg('--8k-headset')
args.setarg('--8k-take')

CHAT_URL    = args.arg('--chat-url')
USERNAME    = args.arg('--username')
VERBOSE     = args.arg('--verbose')
NODAILY     = args.arg('--dont-get-daily-coins')
DOCACTUS    = args.arg('--cactus')
CACTUSDAILY = args.arg('--cactus-daily')
DOCYCLES    = args.arg('--cycles')
CYCLESDAILY = args.arg('--cycles-daily')
CYCLESVERIF = args.arg('--cycles-verify')
CYCLESCOFFE = args.arg('--cycles-coffee')
CYCLESFINGR = args.arg('--cycles-finger')
CYCLESPHONE = args.arg('--cycles-phone')
DONTDO8K    = args.arg('--dont-do-8kbot')
DO8KHEADSET = args.arg('--8k-headset')
DO8KTAKE    = args.arg('--8k-take')


debug('Starting chromedriver...')

DRIVER = webdriver.Chrome('./chromedriver96')
DRIVER.set_window_position(0, 0)
DRIVER.set_window_size(1120, 1080)

debug('Started chromedriver.')

DRIVER.get(CHAT_URL)

debug('Doing login...')

# Autocomplete username
# if specified in args
if USERNAME != '':
  time.sleep(1)

  debug('Autofilling username...')

  DRIVER.find_element_by_css_selector(
    'div > form > div div > input[name=email]'
  ).send_keys(USERNAME + Keys.TAB)

  debug('Autofill done.')

# Wait for the user to login
# (wait until exits login page)
while True:
  if not '://discord.com/login' in DRIVER.current_url:
    break

debug('Login completed.\nWaiting for a channel...')

# Wait until Discord redirects
# the user to a channel
while True:
  if '://discord.com/channels/' in DRIVER.current_url:
    break

debug('Channel found.\nBots to spam:')
if not DONTDO8K:
  debug(' - 8k Bot')
if DOCACTUS:
  debug(' - Cactus')
if DOCYCLES:
  debug(' - Cycles')

time.sleep(1)

try:
  input('Press enter to start spamming, or Ctrl + C to quit')
except (KeyboardInterrupt, EOFError):
  exit_spammer(3, False)

time.sleep(1)

debug('Bots to get daily prizes:')

# 8k Bot daily coins
if NODAILY:
  pass
elif not DONTDO8K:
  debug(' - 8k Bot')

  send_message_forced('8k! daily')

# Cactus daily growth
if CACTUSDAILY:
  debug(' - Cactus')

  send_message_forced('=daily')
else:
  debug('Skipped Cactus daily growth.')

# Cycles daily prize
if CYCLESDAILY:
  debug(' - Cycles')

  send_message_forced('&daily')

try:
  i = 10

  while True:
    message = []

    # If user didn't say not to
    # do 8k Bot, beg, and
    # take money from the floor
    if not DONTDO8K:
      message.append('8k! beg')

      if DO8KTAKE:
        message.append('take')

    # If enough time has passed,
    # reset the counter and
    # do the commands that
    # have longer cooldowns
    if i >= 11:
      if not DONTDO8K:
        message.append('8k! work')

        if DO8KHEADSET:
          message.append('8k! use headset')
      if DOCYCLES:
        for i in range(11): # 0 to 10
          message.append(f'&verify {i}')

        message.append('&post')

        if CYCLESCOFFE:
          message.append('&drink coffe')

        if CYCLESFINGR:
          message.append('&use finger')

        if CYCLESPHONE:
          message.append('&use phone')

      i = 0

    # If user said to do Cactus
    # bot, grow
    if DOCACTUS:
      message.append('=grow')

    # If user said to do
    # Cycles bot, code
    if DOCYCLES:
      message.append('&c')

    # Send messages
    for msg in message:
      try:
        send_message(msg)
      except:
        pass

    time.sleep(10)

    # Increment counter
    i += 1
except KeyboardInterrupt:
  print('')

  exit_spammer(2)
