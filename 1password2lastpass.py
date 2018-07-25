#!/usr/bin/env python

from pprint import pprint
import click
import csv
import json
import sys
import os.path


def loadDataFromExportFile(filename):
    with open(filename, 'r') as fp:
        rawLines = fp.read().splitlines()

    jsonLines = filter(lambda l: l[0] != '*', rawLines)
    rawJson = '[' + ','.join(jsonLines) + ']'
    data = json.loads(rawJson)

    return data


def looksLike1PasswordFile(lines):
    """
    Given a list of lines from some file, see if it looks like it's
    a 1Password export data file.
    """
    guidLines = filter(lambda l: l[0] == '*', lines)
    dataLines = filter(lambda l: l[0] == '{', lines)

    return len(guidLines) == len(dataLines)


def filterDictsByKeyVal(dicts, key, val):
    return filter(lambda d: key in d.keys() and d[key] == val, dicts)


def getValueForName(dicts, name):
    """
    Return the 'value' field from the dict in a list of dicts whose
    'name' field equals NAME.
    """

    def keyFilter(item):
        return 'name' in item and \
            item['name'] == name and \
            'value' in item and \
            len(item['value'])

    try:
        target = filter(keyFilter, dicts['secureContents']['fields'])
    except KeyError:
        return None

    if len(target):
        try:
            return target[0]['value']
        except KeyError:
            return None

    return None


def extractFieldFromEntry(entry, field):
    if field in entry['secureContents']:
        return entry['secureContents'][field]
    else:
        try:
            fieldEntry = filterDictsByKeyVal(entry['secureContents']['fields'],
                                             'designation',
                                             field)
            if len(fieldEntry):
                return fieldEntry[0]['value']
        except KeyError:
            return None


def extractFieldsFromSource(data, quiet=False):
    """
    Extract the username, password, and URL fields that are
    occasionally found in different locations within the export data
    structure. We can only make educated guesses here, but these
    fields are NOT always at the top level of the data structure.
    """
    completeEntries = 0
    cleanData = []
    for site in data:
        title = site['title']

        try:
            url = site['location']
        except KeyError:
            if 'typeName' in site and \
               ('wallet' in site['typeName'] or
                'securenote' in site['typeName']):

                if not quiet:
                    click.echo('-', nl=False)
                continue

        username = getValueForName(site, 'username')

        if username is None:
            username = extractFieldFromEntry(site, 'username')

        if username is None or not len(username):
            username = 'Unknown'

        password = getValueForName(site, 'password')

        if password is None:
            password = extractFieldFromEntry(site, 'password')

        if password is None:
            password = ''
            pprint(site)

        cleanSite = {
            'source': site,
            'url': url,
            'name': title,
            'username': username,
            'password': password
        }
        cleanData.append(cleanSite)
        completeEntries += 1
        click.echo('.', nl=False)

    click.echo('\n')
    click.echo('Processed {} entries.'.format(len(data)))
    click.echo(
        'Found {} complete entries (url, username, and password extracted).'
        .format(completeEntries))
    percentSuccess = int(round((float(completeEntries) / len(data)) * 100, 0))
    click.echo('{}% success rate.'.format(percentSuccess))
    return cleanData


def writeCSV(data, filename):
    """
    Write an array of dicts into a CSV in the format LastPass expects.
    """
    fieldnames = ['url',
                  'username',
                  'password',
                  'name']

    with open(filename, 'w') as csvFile:
        csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
        csvWriter.writeheader()

        for site in data:
            csvWriter.writerow({'url': site['url'],
                                'username': site['username'],
                                'password': site['password'],
                                'name': site['name']})


@click.command()
@click.argument('filename')
def main(filename):
    """
    Convert a 1Password data file, FILENAME, into a LastPass CSV
    import file.

    FILENAME should be the full path to a data.1pif file found within
    a *.1pif directory resulting from exporting your passwords from
    1Password.
    """
    if not os.path.isfile(filename):
        click.echo('Cannot find {}, is it a real file?'.format(filename))
        sys.exit(1)

    print('Reading data from {}...'.format(filename))
    data = loadDataFromExportFile(filename)
    cleanData = extractFieldsFromSource(data)
    outputFilename = os.path.join(os.path.dirname(filename), 'data.csv')
    writeCSV(cleanData, outputFilename)
    click.echo('\nData written to {}.'.format(outputFilename))
