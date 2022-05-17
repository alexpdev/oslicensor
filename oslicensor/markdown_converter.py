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
    ol = re.compile(r"^\s*?[0-9]+?[.)]?(\s+?\w+?)+?$")
    headers = re.compile(r"^\s*?\w+.{0,70}$")
    blank = re.compile(r"^\s*?$")
    lic = None
    if os.path.exists(path):
        with open(path, "rt", encoding="utf-8") as textfile:
            lic = textfile.read()
    if not lic:
        raise PathError
    lines = lic.split("\n")
    while len(lines[0].strip()) == 0:
        del lines[0]
    out = []
    for i, line in enumerate(lines):
        if i == 0:
            first = "".join(["## ", lines[0].strip()])
            out.append(first)
        elif ol.match(line):
            new = line.strip()
            out.append(new)
        elif blank.match(line):
            out.append("")
        elif headers.match(line):
            if i == len(lines) - 1:
                out.append(line)
            elif blank.match(lines[i - 1]) and blank.match(lines[i + 1]):
                new = "### " + line.strip()
                out.append(new)
            else:
                out.append(line)
        else:
            out.append(line)
    base = os.path.splitext(path)[0]
    outpath = base + ".md"
    with open(outpath, "wt", encoding="utf-8") as outfile:
        outfile.write("\n".join(out))
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
            if os.path.isfile(full) and full.lower().endswith(".txt"):
                convert(full)
