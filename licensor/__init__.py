import sys
import argparse

from licensor.commands import choose_command, convert_command, get_command


def execute(args=None):
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog='licensor',
        description=('CLI tool that generates the most commonly used software '
                     'license files in one command.'),
        prefix_chars='-'
        )

    parser.add_argument(
        '-l',
        '--list',
        help='show the list of available licenses to choose from.',
        action='store_true',
        dest='list'
    )
    subs = parser.add_subparsers(title="Commands", metavar='<command>')
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
    convert_parser = subs.add_parser(
        'convert',
        help='convert plain-text license file to markdown, if path argument is a directory, it will convert all files with .txt extension to markdown.'
    )
    convert_parser.add_argument(
        'path',
        metavar='<path>',
        action='store',
        help='path to the plain-text file.'
    )
    choose_parser = subs.add_parser(
        'choose',
        help='choose license from a list of options.'
    )
    choose_parser.set_defaults(func=choose_command)
    convert_parser.set_defaults(func=convert_command)
    get_parser.set_defaults(func=get_command)
