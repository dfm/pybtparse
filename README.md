#PyBTParse

This is a Python wrapper around Greg Ward's "btparse" library.  So far, it only has one function:
```python
btparse.load(filename)
```
that loads and parses a .bib file and returns a list of dictionaries of the entries.

##NOTE

This is pre-alpha software.  Use at your own risk.

##LICENSE

Nominally released under GPL version 2 (see LICENSE).

##AUTHOR

Daniel Foreman-Mackey

##INSTALLATION

First you must install "btparse" from http://www.gerg.ca/software/btOOL/

Type
```python
>>> sudo python setup.py install
```
to compile and install the module "btparse" in the Python search path.

##USAGE

```python
>>> import btparse
>>> bib = btparse.load('biblio.bib')
>>> print bib[0]['title']
Title of zero-th entry in biblio.bib
>>> print bib[10]['abstract']
This is the abstract of the 10th entry in biblio.bib...
```
