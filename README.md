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

## Developing

Oh, you want to help me out? Hey, that'd be swell. You can use `setuptools` to
get yourself up and running for development. Here's how!

First create a virtualenv. If you use the great `virtualenvwrapper` you can
simply run `mkvirtualenv some_env_name`. If you do not, then creating the
virtualenv is left as an exercise for the reader.

Activate the virtualenv (this is very important), and then install the script
for development with:

```
$ pip install -e '.[dev]'
```

Note that `.[dev]` only needs to be quoted in zsh; it does not need to be quoted
in bash. But you really should use zsh because it is awesome.

Congratulations, you now have `1password2lastpass` on your path. Verify that it
is installed in your virtualenv with `which 1password2lastpass`, which should
give you a value similar to `~/.virualenvs/some_env_name/bin/1password2lastpass`.

The bracketed `dev` specification tells `pip` to also install `flake8`, for
which I have provided a simple config in `.flake8`.

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
