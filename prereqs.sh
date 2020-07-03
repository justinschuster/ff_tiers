curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
rm get-pip.py
pip install --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv env 
pip install requests
pip3 install beautifulsoup4
pip install lxml
pip install -U pytest
pip install pandas
pip install -U scikit-learn
pip install -U matplotlib
