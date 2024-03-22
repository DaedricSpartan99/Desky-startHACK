# Desky-startHACK
Connect remote workers and digital nomads to farms.

Interface Wwoofing for remote workers willing to sustain farmers and promote Co-Working in farms and everywhere.

This is a prototype embedding our idea and impact.


## Installation and run 

Install [**python**](https://www.python.org/) (version **3.11.8**).

Open a terminal and create a dedicated environment:

`python -m venv desky-env`

Activate it:

`source desky-env/bin/activate`

Install dependencies:

`pip install -r requirements.txt`

Run the server:

`python manage.py runserver`

Access through the browser to the local server: [http://localhost:8000/](http://localhost:8000/)

## API documentation

### Search farms and co-working API in Italy
In order to search in the database we scraped perform a GET http request tothe address:

`http://localhost:8000/booking/search/?keyword=<keyword>`

where `<keyword>` must be replaced by which location or name you are looking for.

### Access [Syngenta](https://www.syngenta.com/en)'s weather forecast
Send an e-mail to a user about the wheater in a specific zone.

Send a http POST request to the following address:

`http://localhost:8000/emailrequest/send-email/`

with a json body of the form:

```
{
    "recipient" : <email address>,
    "latitude" : <latitude>,
    "longitude" : <longitude>
}
```

The recipient e-mail address will receive a .csv file containing the weather informations in the specified latitude and longitude coordinates.

## External database and webscrapting

### Data scraping with Selenium
There are three scripts exploiting [Python Selenium](https://www.selenium.dev/) responsible of the collection of data present in the `external` directory:

* `coworking_scraping.ipynb`: collect information about coworking spaces located in Milan (Italy).
* `coworking_milan.ipynb`: collect information about coworking spaces located in Rome (Italy).
* `wwoof_scraping.ipynb`: collect information about farms interfaced by [Wwof](https://wwoof.net/).

### Interfacing weather forecast of Syngenta
People travelling around the world and remote workers will decide their target location also considering the weather in that locality and sometimes it can be determinant for the decision process. So we decided to fournish an instrument that gives an idea it.
Syngenta offers an API for the retrieval of meteorogical data in a specificplace and the script `syngenta_weather.ipynb` exploits this possibility implementing an e-mail notification about the forecast. In a future version of our portal, this functionality can be useful to show to our users the weather forecast after one day, one week or two weeks as they decide to visit a farm or a city. 


