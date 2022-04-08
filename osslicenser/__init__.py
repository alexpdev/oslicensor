#! /usr/bin/python3

#############################################################################
#  Copyright 2022 alexpdev
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#############################################################################

import sys
import argparse

from osslicenser.commands import choose_command, convert_command, get_command, LICENSES


def execute(args=None):
    """
    Execute function for parsing command line arguments.

    Parameters
    ----------
    args : list
        Command line arguments.
    """
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog='osslicenser',
        description=('CLI tool that generates the most commonly used software '
                     'license files in one command.'),
        prefix_chars='-'
    )

    parser.add_argument(
        '-l',
        '--list',
        help='Show the list of available licenses to choose from.',
        action='store_true',
        dest='list'
    )

    subs = parser.add_subparsers(title="Commands")

    convert_parser = subs.add_parser(
        'convert',
        help='Converts the text file(s) into Markdown.'
    )

    convert_parser.add_argument(
        'path',
        metavar='<path>',
        action='store',
        help='Path to the plain-text file or directory containing text files.'
    )

    choose_parser = subs.add_parser(
        'choose',
        help='Choose license from a list of options.'
    )

    get_parser = subs.add_parser(
        'get',
        help='Get the license file indicated by license argument'
    )

    get_parser.add_argument(
        'license',
        metavar='<license>',
        action='store',
        help='The abbreviated title representation of the desired license.'
    )

    choose_parser.set_defaults(func=choose_command)

    convert_parser.set_defaults(func=convert_command)

    get_parser.set_defaults(func=get_command)

    if not args:
        args = ['-h']
    namespace = parser.parse_args(args)

    if namespace.list:
        print("\n".join(
            [k + ((" ")* (11 - len(k) + 10)) + v for k,v in LICENSES.items()]
        ))
        return

    namespace.func(namespace)
