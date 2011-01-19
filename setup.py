#!/usr/bin/env python
# encoding: utf-8

#
# Copyright 2011 Daniel Foreman-Mackey
# 
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
# 
# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
#

"""

       Project: btparse
        Author: Dan Foreman-Mackey
       Purpose: This script installs a module called btparse into the
                Python search path.
         Usage: Type:
                >> sudo python setup.py install
                to compile and install the module
  Requirements: This requires the library btparse be installed in
                /usr/local/. This library can be found at
                http://www.gerg.ca/software/btOOL/

"""

from distutils.core import setup
from distutils.extension import Extension
import numpy.distutils.misc_util

btparse_dir = '/usr/local'

setup(name='btparse',
        version='0.1',
        description='btparse',
        author='Daniel Foreman-Mackey',
        author_email='danfm@nyu.edu',
        package_dir={'btparse':'btparse'},
        packages=['btparse'],
        ext_modules = [Extension(name='btparse._C_btparse', sources=['btparse/btparse.c'],
                        libraries=['btparse'],library_dirs=['%s/lib'%(btparse_dir)])],
        include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs(),
      )

