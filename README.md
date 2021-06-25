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
    - Run database
        - `mongod --dbpath data/db`
        - **MONGODB_PORT may be vary, You can find it in terminal & replace it in follwing file**
        - **.env**


## Run the Program
### Data Parsing
- `python application.py parse`
### RestFul API
- Run the API server
    - `python application.py server`
- You can call the api by following get method from directly browser
    - **Port number may be vary from your side, You can find it in terminal**
    - [http://localhost:5000/movie/12](http://localhost:5000/movie/12)
        - Where last value 12 is the movie id (Starts with 1 to length of movie list available in database)
    - [http://localhost:5000/movie?count=11&page=2](http://localhost:5000/movie?count=11&page=2)
        - count = Number of movie data will show on per page
        - page = Page Number
        - Example:
            - Suppose we have total 40 movie data in our database
            - [http://127.0.0.1:5000/movie?count=25&page=1](http://127.0.0.1:5000/movie?count=25&page=1)
            - First page show movie data from 1-25
            - [http://127.0.0.1:5000/movie?count=25&page=2](http://127.0.0.1:5000/movie?count=25&page=2)
            - Second page show movie data from 26-40




