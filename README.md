# unidays-code-farmer

Made by @johndoe01274 / John Doe [ES]#7592
If you would like to stay up to date regarding any updates, feel free to follow me on [Twitter](https://twitter.com/johndoe01274).

## Before running

1. Make sure you have Python (preferably 3.8.2) installed
2. download & unzip this the zip you donwloaded, open your CMD/Terminal and `cd` to this folder.
3. run `pip install -r requirements.txt`
4. Add your info into `setting.json`

## To run

open your terminal, change your directory to this folder/repo and run:

- on Mac: `python3 main.py`

- on Widnows: `py main.py`

## Common errors

1. `No module named XXX` = you don't have some of the dependencies installed. Make sure you did everything in [Before running](https://github.com/Alexvec00/unidays-code-farmer#before-running). If that doesn't help, try running:
     - on Windows `py -m pip install -r requirements.txt`
     - on Mac `python3 -m pip install -r requirements.txt`

2. `'pip' is not recognized as an internal or external command, operable program or batch file.` or anything related to this -> you probably don't have Python in your PATH variable (`setx PATH "%PATH%;C:\Python38\Scripts"` - ONLY IF YOU'RE ON WINDOWS). If that doesn't help, try running:
     - on Windows `py -m pip install -r requirements.txt`
     - on Mac `python3 -m pip install -r requirements.txt`
3. Anything related to a `keyerror XXX` = There is something wrong with your `account.json` file. Make sure it's filled in like this:

```json
{
    "email":"password"
}
```

## Where do I find generated code?

- If everything goes smoothly, accounts should be in the **codes folder** in the respective .txt file.


## FAQ

- What is `cd` and how do I use it?
  - From [wikipedia](https://en.wikipedia.org/wiki/Cd_(command)): "the `cd` command is a command-line shell command used to change the current working directory" -  so what you need to do is change your working directory, to the Folder (or directory) of this script.
- How do I install Python?
  - [This should help you](https://realpython.com/installing-python/)
- I am getting `[ERROR] -> Bad request. Satus code 403` or `[ERROR] -> Encountered CloudFare...` all the time, what do I do?
  - Keep trying and or switch proxies. This also happens frequently when the site is under a heavy load (When a restock/drop happens etc.)
