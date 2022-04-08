import os
import re

class PathError(Exception):
    """
    The path provided was not found.
    """

def convert(path):
    """
    Convert the plain-text license file to a markdown file.

    Parameters
    ----------
    path : str
        The relative or absolute path to the plain-text file.

    Returns
    -------
    str :
        The relative or absolute path to the markdown file.
    """
    ol = re.compile(r'^\s*?[0-9]+?[.)]?(\s+?\w+?)+?$')
    headers = re.compile(r'^\s*?(\w+?\s*?){1,3}$')
    blank = re.comile(r'^\s*?$')
    lic = None
    if os.path.exists(path):
        with open(path, 'rt', encoding='utf-8') as textfile:
            lic = textfile.read()
    if not lic:
        raise PathError
    lines = lic.split('\n')
    while len(lines[0].strip()) == 0:
        del lines[0]
    first = ''.join(['## ', lines[0].strip()])
    out = [first, '\n']
    for line in lines[1:]:
        if ol.match(line):
            new = line.strip()
            out.append(new)
        elif blank.match(line):
            out.append('\n')
        elif headers.match(line):
            new = '### ' + line.strip()
            out.append(line)
    base = os.path.splitext(path)[0]
    outpath = base + '.md'
    with open(outpath, 'wt', encoding='utf-8') as outfile:
        outfile.write('\n'.join(out))
    return outpath


def convert_folder(path):
    """
    Convert all plain-text license files in directory path to a markdown files.

    Parameters
    ----------
    path : str
        The path to the directory containing plain-text files.
    """
    if os.path.exists(path) and os.path.isdir(path):
        for item in os.listdir(path):
            full = os.path.join(path, item)
            if os.path.isfile(full) and full.lower().endswith('.txt'):
                convert(full)
