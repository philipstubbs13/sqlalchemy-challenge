import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt
from dateutil.relativedelta import relativedelta


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

# Reflect an existing database into a new model.
Base = automap_base()
# Reflect the tables.
Base.prepare(engine, reflect=True)

# Save reference to the tables.
Measurement = Base.classes.measurement
Station = Base.classes.station
# print(Base.classes.keys())

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Query to retrieve the last 12 months of precipitation data and return the results."""
    # Create our session (link) from Python to the DB.
    session = Session(engine)

    # Calculate the date 1 year ago from the last data point in the database.
    last_measurement_data_point_tuple = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    (latest_date, ) = last_measurement_data_point_tuple
    latest_date = dt.datetime.strptime(latest_date, '%Y-%m-%d')
    latest_date = latest_date.date()
    date_year_ago = latest_date - relativedelta(years=1)

    # Perform a query to retrieve the data and precipitation scores.
    data_from_last_year = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date_year_ago).all()

    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value.
    all_precipication = []
    for date, prcp in data_from_last_year:
        if prcp != None:
          precip_dict = {}
          precip_dict[date] = prcp
          all_precipication.append(precip_dict)

    # Return the JSON representation of dictionary.
    return jsonify(all_precipication)

@app.route("/api/v1.0/tobs")
def tobs():
    """Query for the dates and temperature observations from a year from the last data point."""
    # Create our session (link) from Python to the DB.
    session = Session(engine)

    # Calculate the date 1 year ago from the last data point in the database.
    last_measurement_data_point_tuple = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    (latest_date, ) = last_measurement_data_point_tuple
    latest_date = dt.datetime.strptime(latest_date, '%Y-%m-%d')
    latest_date = latest_date.date()
    date_year_ago = latest_date - relativedelta(years=1)

    # Perform a query to retrieve the data and temperature scores.
    data_from_last_year = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= date_year_ago).all()

    session.close()

    # Convert the query results to a dictionary using date as the key and temperature as the value.
    all_temperatures = []
    for date, temp in data_from_last_year:
        if temp != None:
          temp_dict = {}
          temp_dict[date] = temp
          all_temperatures.append(temp_dict)
    # Return the JSON representation of dictionary.
    return jsonify(all_temperatures)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query for stations.
    stations = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    # Convert the query results to a dictionary.
    all_stations = []
    for station, name, latitude, longitude, elevation in stations:
      station_dict = {}
      station_dict["station"] = station
      station_dict["name"] = name
      station_dict["latitude"] = latitude
      station_dict["longitude"] = longitude
      station_dict["elevation"] = elevation
      all_stations.append(station_dict)

    # Return the JSON representation of dictionary.
    return jsonify(all_stations)

if __name__ == '__main__':
    app.run(debug=True)