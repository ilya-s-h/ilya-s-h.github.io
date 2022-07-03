import json
from tabulate import tabulate

class TablePrinter:
    
    def __init__(self, filename='data.json'):
        self._data = []

        with open(filename) as f:
            self._data = json.load(f)
    
    
    @property
    def header(self):
        '''
        Returns list of columns headers.
        
        >>> t.header
        ['Login', 'Email', 'Active']
        '''
        header = self._data[0].keys()
        header = [h.capitalize() for h in header]
        return header
    
    
    @property
    def first(self):
        '''
        Returns first row in TSV format.
        
        >>> t.first
        'kate123\\tkate@example.com\\tTrue'
        '''
        row = [self._data[0].values()]
        return tabulate(row, tablefmt='tsv')


    def render_table(self):
        '''
        Returns rendered table.
        
        >>> type(t.render_table())
        <class 'str'>
        '''
        header = self._data[0].keys()
        header = [h.capitalize() for h in header]

        data = [d.values() for d in self._data]

        return tabulate(data, header)


if __name__ == '__main__':
    printer = TablePrinter()
    print('Table:')
    print(printer.render_table())
    print('Header:')
    print(printer.header)
    print('First row:')
    print(printer.first)
    
    import doctest
    doctest.testmod(extraglobs={'t': printer})
