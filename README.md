# Links

A shortlink aggregator for the LCSC to use for QR codes and other semi-permanent links that cannot be easily changed.

Project Lead: Andy

Stack: Flask

The code should be self documenting, please see main.py for details

The code can be edited by anyone where needed.

Dev:
- create a virtual environment and install `requirements.txt`
- run `main.py -dev`

Production:
- `docker build -t flask-app .`
- `docker run -p 5000:5000 flask-app`