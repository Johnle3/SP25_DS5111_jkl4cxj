# Declare phony targets
.PHONY: default env update ygainers.html ygainers.csv wjsgainers.html wjsgainers.csv lint

# Default action is to show the contents of the Makefile
default:
	@cat Makefile

# Target to create and prepare the virtual environment
env:
	python3 -m venv env
	. env/bin/activate && pip install --upgrade pip

# Target to update the virtual environment with required packages
update: env
	. env/bin/activate && pip install -r requirements.txt

# Target to fetch HTML content for Yahoo gainers
ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

# Target to convert HTML to CSV for Yahoo gainers
ygainers.csv: ygainers.html
	. env/bin/activate && python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

# Target to fetch HTML content for WSJ gainers
wjsgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 'https://www.wsj.com/market-data/stocks/us/movers' > wjsgainers.html

# Target to convert HTML to CSV for WSJ gainers
wjsgainers.csv: wjsgainers.html
	. env/bin/activate && python -c "import pandas as pd; raw = pd.read_html('wjsgainers.html'); raw[0].to_csv('wjsgainers.csv')"

# Running Pylint
lint:
	@echo "Running Pylint..."
	@. env/bin/activate; pylint bin/normalize_csv.py
