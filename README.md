htmltable.py
============

A small HTML parser to extract tables from HTML files.

## Usage

    html = open('sample.html').read()
    extractor = HTMLTableExtractor()
    tables = extractor.get_tables(html)

'tables' will be a list of tables. Each table is represented as a list of list.

## Notes

* There is no external dependency. It works with the standard Python library.
* It may incorrectly work against HTML files.
