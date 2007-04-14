# Author: Roberto Alsina
# Contact: ralsina@kde.org
# Copyright: This module has been placed in the public domain
# Largely based on the S5 writer by Chris Liechti and David Goodger

"""
Mootools fancy HTML/Javascript slide writer
"""

__docformat__ = 'reStructuredText'


import docutils
from docutils import frontend, nodes, utils
from docutils.writers import html4css1
from docutils.parsers.rst import directives


class Writer(html4css1.Writer):

    settings_default_overrides = {'toc_backlinks': 0}
    config_section_dependencies = ('writers', 'html4css1 writer')

    def __init__(self):
        html4css1.Writer.__init__(self)
        self.translator_class = SLHTMLTranslator

class SLHTMLTranslator(html4css1.HTMLTranslator):

    doctype = (
        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"'
        ' "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')


    extra_head = '''\
<script type="text/javascript" charset="utf-8" src="mootools.js" ></script>
<link rel="stylesheet" type="text/css" href="code.css">
<link rel="stylesheet" type="text/css" href="murphy.css">
<link rel="stylesheet" type="text/css" href="slides.css">
<script src="mootools.js"></script>'''

    layout_template = '''\

    <script type="text/javascript">

    slides=[%(sections)s];
    transitions=['slide_bottom','slide_left','slide_bottom','slide_left','slide_bottom','slide_left','slide_bottom','slide_left','slide_bottom','slide_left'];

    var current=-1;
    var numPages=%(numPages)s;
    var delay=750;
    var pw=0;
    var ph=0;
    var topMargin=0;
    var leftMargin=0;
    var effects;
    
    function controls_in() {

        var eff=$('controlBox').effect('top',{
                duration: 100
        });
        eff.start(0);
    }

    function controls_out() {
        var eff=$('controlBox').effect('top',{
                duration: 100
        });
        eff.start(-100);
    }
    
    function adjustSlides(){


        var pres=$('__presentation');
        pres.setStyle('width',window.getWidth());
        pres.setStyle('height',window.getHeight());

        var size=pres.getSize();
        pw=size['size']['x'];
        ph=size['size']['y'];
        topMargin=ph*.05;
        leftMargin=pw*.05;
        var sl_h=ph*.9;
        var sl_w=pw*.9;

        effects={   'slide_bottom': ['top',topMargin+'px',ph+'px'],
                    'slide_left': ['left',leftMargin+'px',pw+'px'],
                    'fade': ['left',leftMargin+'px',pw+'px']
                };
                
        for (var i=0;i<numPages;i++)
        {            
            slide=$(slides[i]);
            if (slide) {
                slide.setStyle('visibility','hidden');
                slide.setStyle('top',topMargin+'px');
                slide.setStyle('left',leftMargin+'px');
                slide.setStyle('width',sl_w+'px');
                slide.setStyle('height',sl_h+'px');
            }
        }
    };
    
    window.addEvent('domready', adjustSlides );
    window.addEvent('resize', adjustSlides );

    window.addEvent('load',function() {
        current=-1;
        next();
    });


    function slide_out() {
        if ( current > -1 && current < numPages )
        {
            var slide=$(slides[current]);
            var trans=effects[transitions[current*2]];
            var eff1=slide.effect(trans[0],{
                    duration: delay
            });
            eff1.start(trans[1],trans[2]).chain (function () {
                slide.setStyle(trans[0],trans[1]);
                slide.setStyle('visibility','hidden');
                });
        }
    }

    function slide_in() {
        if ( current > -1 && current < numPages )
        {
            var slide=$(slides[current]);
            var trans=effects[transitions[current*2+1]];
            var eff1=slide.effect(trans[0],{
                    duration: delay});
            slide.setStyle(trans[0],trans[2]);
            slide.setStyle('visibility','visible');
            eff1.start(trans[2],trans[1]);
        }
    }

    function next() {
        if (current < numPages-2)
        {
            slide_out();
            current=current+1;
            slide_in.delay(delay);
        }
    };

    function prev() {
        if (current > 0)
        {
            slide_out();
            current=current-1;
            slide_in.delay(delay);
        }
    }


    </script>


    <div id="controlBox" class="sl_control" onMouseOver="controls_in(); " >
            <span id="prev" onClick="if (current > 0 ) {prev();}">&lt;&lt;&nbsp;</span>
            <span id="next" onClick="if (current <numPages-1) { next();}">&nbsp;&gt;&gt;</span>
    </div>
    <div class="sl_cover" onMouseOver="controls_out();" onClick="if (current <numPages-1) { next();}"></div>
    <div id="header" class="sl_header">
    %(header)s
    </div>
    <div id="footer" class="sl_footer">
    %(title)s%(footer)s
    </div>\n
    '''

    def __init__(self, *args):
        html4css1.HTMLTranslator.__init__(self, *args)
        self.section_count = 0
        self.sl_header=[]
        self.sl_footer=[]
        self.stylesheet.append(self.extra_head)
        self.sections=[]

    def depart_document(self, node):
        header = ''.join(self.sl_header)
        footer = ''.join(self.sl_footer)
        title = ''.join(self.html_title).replace('<h1 class="title">', '').replace('</h1>','')
        layout = self.layout_template % {'header': header,
                                         'title': title,
                                         'footer': footer,
                                         'numPages': self.section_count+1,
                                         'sections': "'slide0','"+"','".join(self.sections)+"'"
                                         }
        self.fragment.extend(self.body)
        self.body_prefix.append('<div id="__presentation" class="sl_presentation">\n')
        self.body_prefix.extend(layout)
        self.body_prefix.append(
            self.starttag({'classes': ['sl_slide'], 'ids': ['slide0']}, 'div'))
        if not self.section_count:
            self.body.append('</div>\n')
        self.body_suffix.insert(0, '</div>\n')
        self.body_suffix.insert(0,'''
            <script type="text/javascript">
                /*next();*/
            </script>''')
        # skip content-type meta tag with interpolated charset value:
        self.html_head.extend(self.head[1:])
        self.html_body.extend(self.body_prefix[1:] + self.body_pre_docinfo
                              + self.docinfo + self.body
                              + self.body_suffix[:-1])

    def visit_section(self, node):
        if not self.section_count:
            self.body.append('\n</div>\n')
        self.section_count += 1
        self.section_level += 1
        if self.section_level > 1:
            # dummy for matching div's
            self.body.append(self.starttag(node, 'div', CLASS='section'))
        else:
            self.body.append(self.starttag(node, 'div', CLASS='sl_slide'))


    def depart_section(self, node):
        if self.section_level ==1:
            self.sections.append(node['ids'][0])
        html4css1.HTMLTranslator.depart_section(self,node)


    def depart_footer(self, node):
        start = self.context.pop()
        self.sl_footer.append('<div id="footer">')
        self.sl_footer.extend(self.body[start:])
        self.sl_footer.append('</div>')
        del self.body[start:]

    def depart_header(self, node):
        start = self.context.pop()
        header = ['<div id="header">\n']
        header.extend(self.body[start:])
        header.append('\n</div>\n')
        del self.body[start:]
        self.sl_header.extend(header)

    def visit_subtitle(self, node):
        if isinstance(node.parent, nodes.section):
            level = self.section_level + self.initial_header_level - 1
            if level == 1:
                level = 2
            tag = 'h%s' % level
            self.body.append(self.starttag(node, tag, ''))
            self.context.append('</%s>\n' % tag)
        else:
            html4css1.HTMLTranslator.visit_subtitle(self, node)

    def visit_title(self, node):
        html4css1.HTMLTranslator.visit_title(self, node)
