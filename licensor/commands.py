import sys
import os
import shutil
from licensor.markdown_converter import convert, convert_folder

def convert_command(args):
    path = args.path
    if os.path.isfile(path):
        convert(path)
    elif os.path.isdir(path):
        convert_folder(path)

def get_command(args):
    lic = args.license
    path = os.path.join(ASSETS, lic + ".txt")
    shutil.copy(path, './LICENSE')

def choose_command(*_):
    titles = []
    codes = {}
    counter = 1
    for k,v in LICENSES.items():
        titles.append(str(counter) + ". " + v)
        codes[counter] = k
        counter += 1
    print('\n'.join(titles))
    chosen = input("Choose the number of the corresponding license.")
    if chosen.isdigit():
        lic = codes[int(chosen)]
        path = os.path.join(ASSETS, lic + ".txt")
        shutil.copy(path, './LICENSE')
    else:
        response = input(f"Incorrect input {chosen}. Try again? (Y/N) ")
        if response.upper() == "Y":
            choose_command(_)
        else:
            sys.exit()

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

LICENSES = {
    'agpl':               'GNU AFFERO GENERAL PUBLIC LICENSE',
    'apache':             'Apache License 2.0',
    'artistic':           'The Artistic License 2.0',
    'bsd1':               'BSD(1 clause) License',
    'bsd2':               'BSD(2 clause) License',
    'bsd3':               'BSD(3 clause) License',
    'cc4':                'Creative Commons Attribution 4.0 Public License',
    'cc1':                'Creative Commons Attribution 1.0 Universal',
    'commons-clause':     '“Commons Clause” License Condition v1.0',
    'eclipse1':           'Eclipse Public License 1.0',
    'eclipse2':           'Eclipse Public License 2.0',
    'gpl1':               'GNU GENERAL PUBLIC LICENSE v1',
    'gpl2':               'GNU GENERAL PUBLIC LICENSE v2',
    'gpl3':               'GNU GENERAL PUBLIC LICENSE v3',
    'hyppocratic':        'Hyppocratic Public License',
    'isc':                'ISC License',
    'ldap':               'The OpenLDAP Public License',
    'lgpl2':              'GNU LESSER GENERAL PUBLIC LICENSE v2.1',
    'lgpl3':              'GNU LESSER GENERAL PUBLIC LICENSE v3',
    'mit':                'MIT License',
    'mozilla':            'Mozilla Public License v2',
    'unlicense':          'Unlicense Licenese',
    'upl':                'Universal Public License',
    'zope':               'Zope Public License (ZPL) Version 2.1'
}