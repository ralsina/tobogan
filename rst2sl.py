#!/usr/bin/python

# Author: Chris Liechti
# Contact: cliechti@gmx.net
# Revision: $Revision: 4156 $
# Date: $Date: 2005-12-08 05:43:13 +0100 (Thu, 08 Dec 2005) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML slides using
the S5 template system.
"""

import BartleBlog.rst

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates slideshow documents from standalone '
               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer_name='slwriter', description=description)
