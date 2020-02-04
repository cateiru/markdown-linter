import io
import re

from setuptools import find_packages, setup

with open('README.md', encoding='utf-8', mode='r') as f:
    readme = f.read()

with io.open("src/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

install_requires = [
    'click',
    'bs4'
]

setup(
    name='md-analysis',
    version=version,
    description='Performs static code analysis on Markdown files.',
    author='yuto51942',
    url='https://github.com/yuto51942/md-linter',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['src/analysis', 'src/md_error', 'src/lint'],
    long_description=readme,
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points={
        'console_scripts': [
            'md-lint=src.lint:main'
        ],
    }
)
