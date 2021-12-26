# 8kBotHack
A spammer bot for various Discord bots, including 8k Bot.

## Bots supported
* 8k Bot
* Cactus
* Cycles

## How to use
To use this tool:

1. Click on the green button that says _Code_, and then click _Download ZIP_
2. Once downloaded, extract the ZIP into another folder
3. If you are on Mac
     1. Just use the `chromedriver96` file that comes with this
4. If you are not on Mac
     1. Go to the [chromedriver downloads site](https://chromedriver.chromium.org/downloads) and download chromedriver version 96
     2. If the download is a ZIP, extract it, and it should result in one unique file called `chromedriver`
     3. Rename it to `chromedriver96` and put it in the same folder as the previous download, replacing the other `chromedriver96`
5. If you don't have Python 3 installed, go to [the Python website](https://python.org) and follow their instructions on downloading the most recent version of Python 3
     - To check if you have Python 3 installed, open a command line and type `python` and press enter. If you get an error saying something like _command not found_, try typing `python3` and pressing enter. If you still get _command not found_ then you don't have Python 3 installed. If you did not get an error running either of those commands, check for a line that says the version of Python installed. If it is not Python 3.x.x, you must install Python 3
6. Open a command line (Terminal on Mac, PowerShell on Windows)
7. Change to the folder from the first ZIP (`cd`)
     - If the folder is called `8kBotHack-main` and is in your Downloads folder, do `cd ~/Downloads/8kBotHack-main/`
     - If the folder is called `lol` and is in your home folder, do `cd ~/lol/` (you get the point)
     - If you are on Windows, you might want to use a backslash (`\`) insead of normal forward slashes (`/`)
8. Run the Python script: `python3 main.py`
     - If you get an error similar to `python3: command not found`, try the same as above but with just `python`, without the three
     - To spam other bots, and other options, check the [arguments](#arguments) section

## Arguments
There are some extra arguments you can pass to the program for it to do different things.
A table with all the arguments can be found here.

| Argument                        | Meaning/function                                                          |
| ------------------------------- | ------------------------------------------------------------------------- |
| `--chromedriver`                | Use this to specify a chromedriver file. If this argument is not present, defaults to `chromedriver96` in current folder. |
| `--chat-url` or `-c`            | Specify a Discord channel URL in which to spam.                           |
| `--username` or `-u`            | Specify your Discord username to autocomplete in the login.               |
| `--verbose` or `-v`             | Print messages to the command line, telling you what's happening.         |
| `` |  |

If an argument has spaces, put double quotes around it, like this:
``` bash
python3 main.py --username "Example user"
```
