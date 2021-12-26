# 8kBotHack
A spammer bot for various Discord bots, including 8k Bot.

## Bots supported
* [8k Bot](https://top.gg/bot/783346270290968606)
* [Cactus](https://cactus-bot.codingcactus.codes/)
* [Cycles](https://top.gg/bot/781939317450342470)

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

| Argument                         | Meaning/function                                                                          |
| -------------------------------- | ----------------------------------------------------------------------------------------- |
| `--chromedriver`                 | Use this to specify a chromedriver file. If this argument is not present, defaults to `chromedriver96` in current folder. |
| `--chat-url` or `-c`             | Specify a Discord channel URL in which to spam. Default is [this channel](https://discord.com/channels/783422192720412694/910280045178810388). |
| `--username` or `-u`             | Specify your Discord username to autocomplete in the login.                               |
| `--verbose` or `-v`              | Print messages to the command line, telling you what's happening.                         |
| `--dont-get-daily-coins` or `-D` | Don't get the [8k Bot](https://top.gg/bot/783346270290968606) daily coins (`8k! daily`).  |
| `--cactus` or `-C`               | Spams messages like `=grow` for the [Cactus bot](https://cactus-bot.codingcactus.codes/). |
| `--cactus-daily`                 | Gets the [Cactus bot](https://cactus-bot.codingcactus.codes/) daily growth (`=daily`).    |
| `--cycles`                       | Spams messages like `&c` and `&p` for the [Cycles bot](https://top.gg/bot/781939317450342470). |
| `--cycles-daily`                 | Gets the [Cycles bot](https://top.gg/bot/781939317450342470) daily prizes (`&daily`).     |
| `--cycles-verify`                | Now and then sends `&verify 0` messages, from 0 to 10, for the [Cycles bot](https://top.gg/bot/781939317450342470). |
| `--cycles-coffee`                | Now and then sends `&use coffee` messages for the [Cycles bot](https://top.gg/bot/781939317450342470). |
| `--cycles-finger`                | Now and then sends `&use finger` messages for the [Cycles bot](https://top.gg/bot/781939317450342470). |
| `--cycles-phone`                 | Now and then sends `&use phone` messages for the [Cycles bot](https://top.gg/bot/781939317450342470). |
| `--dont-do-8kbot`                | Disables [8k Bot](https://top.gg/bot/783346270290968606) messages like `8k! beg` and `8k! work`. |
| `--8k-headset`                   | Now and then sends `8k! use headset` messages for [8k Bot](https://top.gg/bot/783346270290968606). |
| `--8k-take`                      | Now and then sends `take` messages for [8k Bot](https://top.gg/bot/783346270290968606).   |

If an argument has spaces, put double quotes around it, like this:
``` bash
python3 main.py --username "Example user"
```

## Exit codes
**Note:** Most people won't really care about this part.
**Note:** Another list of exit codes can be found in [a comment in the source code](main.py).

| Exit code | Meaning                                                                         |
| --------- | ------------------------------------------------------------------------------- |
| `2`       | User interrupted while messages where being spammed.                            |
| `3`       | User interrupted before started spamming messages.                              |
| `4`       | Error starting chromedriver. This can be caused by an incorrect value in the [`--chromedriver` argument](#arguments) |
