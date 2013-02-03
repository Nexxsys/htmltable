#!/usr/bin/env python

from HTMLParser import HTMLParser

class HTMLTableExtractor(HTMLParser):
    STATE_OUTTER    = 0
    STATE_IN_TABLE  = 1
    STATE_IN_ROW    = 2
    STATE_IN_CELL   = 3

    def handle_starttag(self, tag, attrs):
        if self.state == self.STATE_IN_CELL:
            self.cell_data += '<%s %s>' % (tag, 
                    ' '.join(['%s=%s' % (name, value) for name, value in attrs]))
        elif tag == 'table':
            if self.state != self.STATE_OUTTER:
                raise Exception('Nested table found')
            self.state = self.STATE_IN_TABLE
            self.tables.append([])
        elif tag == 'tr':
            if self.state != self.STATE_IN_TABLE:
                raise Exception('<tr> found outside a table')
            self.state = self.STATE_IN_ROW
            self.tables[-1].append([])
        elif tag in ('td', 'th'):
            if self.state != self.STATE_IN_ROW:
                raise Exception('<%s> found outside a table' % tag)
            self.state = self.STATE_IN_CELL
            self.cell_data = ''

    def handle_endtag(self, tag):
        if self.state == self.STATE_IN_CELL:
            if tag in ('td', 'th'):
                self.state = self.STATE_IN_ROW
                self.tables[-1][-1].append(self.cell_data)
            else:
                self.cell_data += '</%s>' % tag
        elif tag == 'table' and self.state == self.STATE_IN_TABLE:
            self.state = self.STATE_OUTTER
        elif tag == 'tr' and self.state == self.STATE_IN_ROW:
            self.state = self.STATE_IN_TABLE

    def handle_data(self, data):
        if self.state == self.STATE_IN_CELL:
            data = data.strip()
            self.cell_data += data

    def get_tables(self, html):
        self.tables = []
        self.state = self.STATE_OUTTER

        self.feed(html)
        return self.tables

if __name__ == '__main__':
    html = open('sample.html').read()
    extractor = HTMLTableExtractor()
    tables = extractor.get_tables(html)

    for i, table in enumerate(tables):
        print 'Table %d/%d' % (i + 1, len(tables))
        print '-' * 78
        for row in table:
            print '|',
            for cell in row:
                print cell, '|',
            print
        print '-' * 78
        print
