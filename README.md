# ticket-viewer

Ticket Viewer accesses tickets from a Zendesk account and displays them in a readable format.

## Installation

**Dependencies**: Python 2.7, Python Requests library, Python Tabulate library, Python Mock library (for testing)

**Installing Python 2.7**

Recent versions of Mac OS X should already have Python 2.7 installed. If you're not sure what version of Python you have installed, follow [this guide](http://docs.python-guide.org/en/latest/starting/install/osx/).

For installing Python 2.7 on Windows, see [this guide](http://docs.python-guide.org/en/latest/starting/install/win/).

**Installing Python Requests, Tabulate and Mock libraries**

Installing Python's [Requests](https://pypi.python.org/pypi/requests/) library is as easy as running `pip install requests` from the terminal. Likewise, installing [Tabulate](https://pypi.python.org/pypi/tabulate) just involves running `pip install tabulate`.

Python's [Mock](https://pypi.python.org/pypi/mock) library is only used for testing purposes - if you just want to run the viewer and ignore tests.py, you don't need to install it. If you do want to install it, run `pip install mock` from the terminal.

If for some reason you don't have pip installed, [this link](http://docs.python-guide.org/en/latest/starting/install/osx/#install-osx) will talk you through it.

## Usage

To use Ticket Viewer, run `python viewer.py` from the command line.

You can page through your total tickets, or view details on an individual ticket.

When finished, exit from the main menu. Alternatively, `Ctrl+C` will exit from anywhere.

## Testing

To test Ticket Viewer, run `python tests.py` from the command line.
