# SQLAlchemy Challenge

Climate analysis and data exploration for Hawaii temperature and temperature station data. If you are thinking about taking a vacation to Honolulu, Hawaii (I'm not), this might be interesting to you. This analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* [Overview](#overview)
* [Technologies Used](#technologies)

##  <a name="overview"></a>Overview

This repository includes a data analysis of Hawaii climate data, which is stored in a [sqlite database](./Resources/hawaii.sqlite). The analysis is split up into the following parts:

* [Climate Analysis and Exploration](#exploration)
* [Climate Flask App](#app)
* [Temperature Analysis I](#temp_analysis_i)
* [Temperature Analysis II](#temp_analysis_ii)

### <a name="exploration"></a>Climate Analysis and Exploration

To start, I used Python and SQLAlchemy to do a climate analysis and data exploration of the [climate database](./Resources/hawaii.sqlite). All of the analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

#### Reflect Tables into SQLAlchemy ORM

The analysis was done inside a jupyter notebook file, which can be found [here](./climate.ipynb). In this file, I used SQLAlchemy `create_engine` to connect to the sqlite database and then used SQLAlchemy `automap_base()` to reflect the tables into classes. References to those classes are saved as variables and are called **Station** and **Measurement**.

#### Exploratory Climate Analysis

After setting up the database, I did an analysis on the precipitation data. Specifically, I designed a query to retrieve the last 12 months of precipitation data. To do this, I used a package called `dateutil.relativedelta` to calculate the date 1 year ago from the last point in the database. I then stored the date and precipitation values from the query into a Pandas dataframe so that I could plot the results as a bar chart using Matplotlib. Images of the visualizations for this analysis can be found [here](./Images).

#### Station Analysis

After analyzing precipitation data, I did a quick analysis of the station data. Specifically, I designed a query to show how many stations are available in this dataset. After that, I created another query to find the most active station (i.e., the station with the highest number of temperature observations.). Using the results from this query, I was able to calculate the lowest temperature recorded, the highest temperature recorded, and the average temperature of the most active station. Finally, I took the last 12 months of temperature observation data for the most active station and plotted the results as a histogram with `bins=12`. Images of the visualizations for this analysis can be found [here](./Images).

### <a name="app"></a>Climate Flask App

After completing the initial data analysis, I designed a Flask API based on the queries I developed previously.

To run the app:

1. Clone or download this repository to a local directory on your computer.
2. Change directory to the root directory (`sqlalchemy-challenge`) of this repository.
3. Run `python app.py` from the root directory (`sqlalchemy-challenge`). The app starts up at `localhost:5000` by default.

In the app, here are the available routes/endpoints you can hit:

| Route       | Description    
| :------------- | :----------: |
|  `/` | This route is the home route. It lists all the routes that are available.  | 
| `/api/v1.0/precipitation`   | This route queries the database, retrieves the last 12 months of precipitation data, and returns the results. The format of the results is a JSON representation of a dictionary using the date as the key and the precipitation as the value.|
| `/api/v1.0/stations`   | This route returns a JSON list of stations from the dataset. |
| `/api/v1.0/tobs`   |  This route queries for the dates and temperature observations from a year from the last data point for the most active station. It returns a JSON list of temperature observations (tobs) for the previous year. |
| `/api/v1.0/<start>` | This route return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date. If you only specify a start date, the endpoint calculates the minimum, average, and maximum temperature for all dates greater than and equal to the start date. The endpoint accepts dates using the YYYY-MM-DD date format (e.g., 2012-02-28). If the date you specify isn't in range of the dataset, you will get a 404 like message that no temperature data was found for that date range. |
| `/api/v1.0/<start>/<end>` | This route return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range. If you specify both a start and an end date, the endpoint calculates the minimum, average, and maximum temperature for dates between the start and end date inclusive. The endpoint accepts dates using the YYYY-MM-DD date format (e.g., 2012-02-28). If the date you specify isn't in range of the dataset, you wlll get a 404 like message that no temperature data was found for that date range. |

### <a name="temp_analysis_i"></a>Temperature Analysis I

Hawaii is reputed to enjoy mild weather all year. So, I wanted to determine if there is a meaningful difference between the temperature in, for example, June and December. To do this, I used SQLAlchemy to query the temperatures in June at all stations across all available years in the dataset. I also did the same query for December.

After querying for the temperature data, I identified the average temperature for June and December, plotted the temperature values on a scatter plot to show the distribution of the values, and plotted those values on a histogram to show the difference in means. Just looking at the histogram, there appears to be a difference in the means for June and December.

I decided to do an independent t-test. An independent t-test compares the means of 2 independent populations (June temperatures in Hawaii and December temperatures in Hawaii). We want to use an independent t-test (unpaired) rather than a paired t-test because we want to compare the means of two independent populations. A paired t-test (one sample t-test) looks at comparing the sample to the population, which we don't want in this case. Assumptions include data are normally distributed, data are independent, and data are homogenous (the standard deviations are roughly equal).

The independent t-test was calculated using `scipy.stats.ttest_ind` from the scipy package. After calculating the results, it was determined that there is a statistically significant difference in means (p-value of less than 0.05). In other words, the p-value is a very small value, so the means of these two populations are significantly different, and there is a lower probability that the difference is random. As a result, we can reject the null hypothesis, which is that there is no meaningful difference between the temperature in June and December in Hawaii.

### <a name="temp_analysis_ii"></a>Temperature Analysis II

Inside the jupyter notebook file, there is a function called `calc_temps`, which accepts a start date and end date in the format `%Y-%m-%d` and returns the minimum, average, and maximum temperatures for that range of dates. Using the `calc_temps` function, I calculated the min, avg, and max temperatures for my trip using the matching dates from the previous year. I then plotted the min, avg, and max temperature from the previous query as a bar chart. I used the average temperature as the bar height and used the peak-to-peak (tmax-tmin) value as the y error bar (yerr). An image of the bar chart can be found [here](./Images).

I also calculated the rainfall per weather station using the previous year's matching dates and stored the results in a pandas dataframe. Then, using the `daily_normals` function, I calculated the daily normals (the averages for the min, avg, and max temperatures for each day) and plotted the results using a pandas area plot. An image of the area chart can be found [here](./Images).

##  <a name="technologies"></a>Technologies Used

* SQLAlchemy
* Jupyter Notebook
* Python
* Matplotlib
* Pandas
* Flask
* datetime
* dateutil.relativedelta
* Scipy
