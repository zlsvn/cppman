#-*- coding: utf-8 -*-
# 
# Environ.py
#
# Copyright (C) 2010 -  Wei-Ning Huang (AZ) <aitjcize@gmail.com>
# All Rights reserved.
#
# This file is part of manpages-cpp.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import os.path
import sys

home = os.path.expanduser('~')

# If launched from source directory
if not sys.argv[0].startswith('/usr/bin'):
    prefix = os.path.dirname(os.path.abspath(sys.argv[0]))
    man_dir = home + '/.local/share/man/man3/'
    index_db = prefix + '/../lib/index.db'
    viewer = prefix + '/../lib/viewer.sh'
else:
    man_dir = home + '/.local/share/man/man3/'
    index_db = '/usr/lib/cppman/index.db'
    viewer = '/usr/lib/cppman/viewer.sh'
