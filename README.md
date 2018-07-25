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
$ 1password-to-lastpass /path/to/your/export.1pif/data.1pif
```

The above command would generate a LastPass CSV at
`/path/to/your/export.1pif/data.csv`.

## GNU GPLv3

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
