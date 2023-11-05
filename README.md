# SacHacks 2023 Project: "Derk's Group"

### Brief
This will be our project for the SacHacks 2023 hackathon with IBM as the event sponsor. In this project, we will create a city driving advisory web application powered by a ML model running on an IBM mainframe computer for the event. The road advisor will take into account factors like traffic flow and collisions.

### Dev. Notes
 - Update README with general notes.
 - All Flask files are in the `flaskr` directory.
 - Create an `instance` directory in `flaskr`. This will store a `config.py` file with just: `DEBUG = False`. The setting here should be set to `False` for production, but `True` for local testruns.
 - Running:
    - Normal: `flask --app flaskr run`
    - Debug: `flask --app flaskr run --debug` only if `DEBUG = True` is in the config.

### To Do:
 - ~~Integrate static data from MLM into the Flask app.~~
 - ~~Get Google Maps API Key~~
 - ~~Refactor map JS to accept server JSON as arguments.~~

### References: Frontend
 - [Sample Palette 1](https://colorpalettes.net/color-palette-155/)
 - [Sample Palette 2](https://colorpalettes.net/color-palette-2075/)

### References: Backend
 - [Flask Layout Doc](https://flask.palletsprojects.com/en/3.0.x/tutorial/layout/)
 - [Flask Quick Refresher](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
 - Google Maps API Documentation
