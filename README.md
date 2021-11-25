# AthenaClubClone
Reproduction of webpage for technical assessment purposes. Uses a Flask API to provide the frontend with data. Frontend built using Vue.js and Bootstrap.

## Setup

Python version used: 3.9.6

1. Create a virtual environment for the project to live in. Instructions to do so can be found here: https://docs.python.org/3/tutorial/venv.html
2. Once in the virtual environment, download the dependencies.
   - It should be sufficient to execute only this command in order to gather all the dependencies needed: 
   ```
   pip install Flask flask-restful
   ```
   - Alternatively, dependencies can be downloaded via the requirements.txt file. *Assuming use of venv for the creation of virtual environments.
      - Windows: 
      ```
      python -m pip install -r requirements.txt
      ```
      - Unix/MacOS: 
      ```
      python3 -m pip install -r requirements.txt
      ```

## Running API and Viewing the Webpage

1. Run the api that will give the frontend the data for all the products. No products will be displayed if this step is ignored.
   ```
   python api.py
   ```
2. Open index.html in the browser of your choosing.

