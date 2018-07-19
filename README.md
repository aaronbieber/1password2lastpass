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
