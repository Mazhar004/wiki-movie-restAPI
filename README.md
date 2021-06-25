# Cefalo Assignment Mazhar

## Environment Setup (Linux)
### Virtual Environment
- Python == 3.8
- `sudo apt-get install python3.8`
- `sudo apt-get install python3.8-venv`
- Virtual Environment Create
    - `python3.8 -m venv venv`
- Activate Virtual Environment
    - `source venv/bin/activate`
### Library Installation
- `pip install --upgrade pip`
- `pip install --upgrade setuptools`
- `pip install -r requirements.txt`

### Database Setup
- `sudo apt-get install mongodb`
- Go to project root folder **cefalo_assignment_mazhar**
    - `mkdir -p data/db`
    - Run command `mongod --dbpath data/db`


## Run the Program
### Data Parsing
- `python application.py parse`



