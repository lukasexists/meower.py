python3 -m build
python3 -m twine upload --repository tpypi dist/*
pip3 install --upgrade meower
