from reader import TablePrinter
import pytest

def test_printer_1():
    printer = TablePrinter()
    table = printer.render_table()
    assert isinstance(table, str)


def test_printer_2():
    printer = TablePrinter()
    row = printer.first
    assert row == 'kate123\tkate@example.com\tTrue'


def test_printer_3():
    printer = TablePrinter()
    row = printer.first
    assert isinstance(row, str)


def test_printer_4():
    printer = TablePrinter()
    head = printer.header
    assert head == ['Login', 'Email', 'Active']


def test_printer_5():
    printer = TablePrinter()
    head = printer.header
    assert isinstance(head, list)
    
    
@pytest.fixture()
def test_file(tmp_path):
    import json
    data = [
        {
            'name': 'John',
            'mail': 'john@mailserver.org'
        }
    ]
    filename = tmp_path / 'data.json'
    with open(filename, 'w') as f:
        json.dump(data, f)
    return filename


def test_printer_newfile_1(test_file):
    printer = TablePrinter(test_file)
    row = printer.first
    assert row == 'John\tjohn@mailserver.org'
    
    
def test_printer_newfile_2(test_file):
    printer = TablePrinter(test_file)
    head = printer.header
    assert head == ['Name', 'Mail']


if __name__ == '__main__':
    test_printer_1()
    test_printer_2()
    test_printer_3()
    test_printer_4()
    test_printer_5()
