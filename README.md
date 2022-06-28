# meower.py
Python library for interacting with the Meower API
## Commands
- `meower.repairMode()` - Checks if the server is in repair mode
- `meower.scratchDeprecated()` - Checks if Scratch clients are now deprecated
- `meower.find_post(num)` - Downloads home, then finds the post number
- `meower.get_home()` - Downloads home
- `meower.home_len()` - Shows the number of posts on home
- `meower.get_post(str)` - Gets the specified post, and shows in `username: post` format
- `meower.page_len()` - Shows the number of home pages
- `meower.current_page()` - Returns the current page number
- `meower.change_page(num)` - Changes the page
- `meower.ping()` - "Pings" the Meower API, by timing `requests` to fetch the root 
- `meower.argoTunnel()` - Checks if there is a Argo Tunnel error on the API
## Installing
`meower.py` is now on [PyPI](https://pypi.org/project/meower/) (Python Package Index)! That means that you can use `pip3`, or `pip` to install it now!
```
pip3 install meower
```
## Usage
For some reason (maybe because of the lack of a class), you can't use the traditional `import meower` method. Instead, use:
```python
from meower import meower
```
## Building
Before you build, you'd might want to double-check that you have all of the dependencies:
```
pip3 install -r requirements.txt
```
Now, you can use the following commands corresponding to your OS:
### Linux
```
python3 -m build
```
### Windows
```
py -m build
```
## Upgrading
`meower.py` is a ongoing project, so you'd might want to check for updates regularly. You can update the package like this:
```
pip3 install --upgrade meower
```
