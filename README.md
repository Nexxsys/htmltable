htmltable.py
============

A small Python HTML parser to extract tables from HTML files.

## Features

* Extracts all tables from an HTML file. Nested tables (tables in a table) are also supported
* Flattens HTML tables into plain-text tables

## Usage

    html = open('sample.html').read()
    extractor = HTMLTableExtractor()
    tables = extractor.get_tables(html)

'tables' will be a list of tables. Each table is represented as a list of list.

## Notes

* There is no external dependency. It works with the standard Python library.
* It may incorrectly work against broken HTML files.
