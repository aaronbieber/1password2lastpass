# 1Password to LastPass Converter

So, you want to export all of your sites from 1Password and import them into
LastPass, do you? Well you're in luck, because LastPass supports importing a
variety of formats. Unfortunately, their 1Password importer doesn't understand
1Password 6+ export format, which occasionally buries the username and password
fields in layers of JSON.

Never fear, this converter will attempt (key word here: attempt) to extract as
much of that information as I could figure out by eyeballing the data for a
couple of days.

NB: this is a best-effort thing. It only handles sites right now, it won't do
secure notes or credit cards or driver's licenses or anything else. Just sites.

## Usage

This script assumes that you have `setuptools`, which you should already have if
you have `pip`. To start from square one, [follow these
instructions](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line)

Install the program by running:

```
$ python setup.py install
```

Actually run the script like this:

```
$ 1password-to-lastpass.py /path/to/your/export.1pif/data.1pif
```

The above command would generate a LastPass CSV at
`/path/to/your/export.1pif/data.csv`.

## License

This program is provided AS IS with no warranty of any kind and even though it
works for me I would not be surprised in the slightest if it does not work for
you. Feel free to do as you wish with this program. Change it, share it, sell it
(good luck), I don't care. If you do make improvements, I will be happy to
review PRs!
