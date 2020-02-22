# SQLAlchemy Challenge

Climate analysis and data exploration for Hawaiii temperature and temperature station data. This analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* [Overview](#overview)
* [Technologies Used](#technologies)

##  <a name="overview"></a>Overview

This repository includes a data analysis of Hawaii climate data, which is stored in a sqlite database. The analysis is split up into two parts:

* [Climate Analysis and Exploration](#exploration)
* [Climate Flask App](#app)

### <a name="exploration"></a>Climate Analysis and Exploration

To start, I used Python and SQLAlchemy to do a climate analysis and data exploration of the climate database. All of the analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

The analysis was done inside a jupyter notebook file, which can be found [here](./climate.ipynb). In this file, I used SQLAlchemy `create_engine` to connect to the sqlite database and then used SQLAlchemy `automap_base()` to reflect the tables into classes. References to those classes are saved as variables and are called Station and Measurement.

After setting up the database, I did an analysis on the precipitation data. Specifically, I designed a query to retrieve the last 12 months of precipitation data. To do this, I used a package called `dateutil.relativedelta` to calculate the date 1 year ago from the last point in the database. I then stored the date and precipitation values from the query into a Pandas dataframe so that I could plot the results as a bar chart using Matplotlib. Images of the visualizations for this analysis can be found [here](./Images).

After analyzing precipitation data, I did a quick analysis of the station data. Specifically, I designed a query to show how many stations are available in this dataset. After that, I created another query to find the most active station (i.e., the station with the highest number of temperature observations.). Using the results from this query, I was able to calculate the lowest temperature recorded, the highest temperature recorded, and the average temperature of the most active station. Finally, I took the last 12 months of temperature observation data for the most active station and plotted the results as a histogram with `bins=12`. Images of the visualizations for this analysis can be found [here](./Images).

### <a name="app"></a>Climate Flask App

After completing the initial data analysis, I designed a Flask API based on the queries I developed previously.

To run the app:

1. Clone or download this repository to a local directory on your computer.
2. Change directory to the root directory (`sqlalchemy-challenge`) of this repository.
3. Run `python app.py` from the root directory (`sqlalchemy-challenge`). The app starts up at `localhost:5000` by default.

In the app, here are the available routes/endpoints you can hit:

* `/`
  * This route is the home route. It lists all the routes that are available.
* `/api/v1.0/precipitation`
  * This route queries the database, retrieves the last 12 months of precipitation data, and returns the results.
  * The format of the results is a JSON representation of a dictionary using the date as the key and the precipitation as the value.
* `/api/v1.0/stations`
  * This route returns a JSON list of stations from the dataset.
* `/api/v1.0/tobs`
  * This route queries for the dates and temperature observations from a year from the last data point.
  * It returns a JSON list of temperature observations (tobs) for the previous year.
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * This route return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * The endpoint accepts dates using the YYYY-MM-DD date format (e.g., 2012-02-28).
  * If you only specify a start date, the endpoind calculates the minimum, average, and maximum temperature for all dates greater than and equal to the start date.
  * If you specify both a start and an end date, the endpoint calculates the minimum, average, and maximum temperature for dates between the start and end date inclusive.
  * If the date(s) you specify aren't in range of the dataset, you wlll get a 404 like message that no temperature data was found for that date range.

##  <a name="technologies"></a>Technologies Used

* SQLAlchemy
* Jupyter Notebook
* Python
* Matplotlib
* Pandas
* Flask
* datetime
* dateutil.relativedelta
