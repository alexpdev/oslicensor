import json
import os
from setuptools import setup, find_packages

def get_info():
    project = os.path.dirname(__file__)
    info = json.load(open(os.path.join(project, 'package.json')))
    with open(os.path.join(project, 'README'), 'rt', encoding='utf-8') as readme:
        info['long-description'] = readme.read()
    with open(os.path.join(project, 'LICENSE'), 'rt', encoding='utf-8') as lic:
        info['license'] = lic.read()
    info['package'] = os.path.join(project, 'licensor')
    return info

INFO = get_info()

setup(
    name=INFO.get('name'),
    version=INFO.get('version'),
    author=INFO.get('author'),
    author_email=INFO.get('author_email'),
    description=INFO.get('description'),
    long_description=INFO.get('long-description'),
    long_description_content_type="text/markdown",
    include_package_data=True,
    license=INFO.get('license'),
    url=INFO.get('url'),
    keywords=INFO.get('keywords'),
    entry_points={'console_scripts': ["osslicenser = osslicenser.__main__:main"]},
    packages=find_packages(include=['osslicenser']),
    package_data={
        'osslicenser': ['assets/*.txt']
    },
    zip_safe=False
)
