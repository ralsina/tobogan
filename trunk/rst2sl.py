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

import docutils.core
import docutils.io
import sourcecode 

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass


def rst2sl(source, source_path=None, source_class=docutils.io.StringInput,
                  destination_path=None,
                  reader=None, reader_name='standalone',
                  parser=None, parser_name='restructuredtext',
                  writer=None, writer_name='slwriter',
                  settings=None, settings_spec=None,
                  settings_overrides=None, config_section=None,
                  enable_exit_status=None):
    """
    Set up & run a `Publisher`, and return a dictionary of document parts.
    Dictionary keys are the names of parts, and values are Unicode strings;
    encoding is up to the client.  For programmatic use with string I/O.

    For encoded string input, be sure to set the 'input_encoding' setting to
    the desired encoding.  Set it to 'unicode' for unencoded Unicode string
    input.  Here's how::

        publish_parts(..., settings_overrides={'input_encoding': 'unicode'})

    Parameters: see `publish_programmatically`.
    """
    output, pub = docutils.core.publish_programmatically(
        source=source, source_path=source_path, source_class=source_class,
        destination_class=docutils.io.StringOutput,
        destination=None, destination_path=destination_path,
        reader=reader, reader_name=reader_name,
        parser=parser, parser_name=parser_name,
        writer=writer, writer_name=writer_name,
        settings=settings, settings_spec=settings_spec,
        settings_overrides=settings_overrides,
        config_section=config_section,
        enable_exit_status=enable_exit_status)
    return pub.writer.parts['whole'],pub.document.reporter.max_level

if __name__ == "__main__":
    import docutils.core
    docutils.core.publish_cmdline(writer_name='slwriter')

    
