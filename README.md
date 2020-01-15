# locust_influx

Send information about [locust](https://locust.io/) requests 
to [TimescaleDB](https://www.timescale.com/) 
and follow the progress through [Grafana](https://grafana.com/) charts.

## Test and taste it locally

Start an TimescaleDB container locally:

`docker run -d --name timescaledb -d -p 5432:5432 timescale/timescaledb:1.5.1-pg11-bitnami`

Start a Grafana container locally:

`docker run -d --name grafana -d -p 3000:3000 grafana/grafana`

Crete a new [python virtual environment](https://docs.python.org/3/tutorial/venv.html) and install `locust_influx`:

`pip install locust-timescaledb`

Run the example locustfile contained in this repo (Change the host to point to desired one):

`locust -f ./locustfile.py --no-web --clients 10 --hatch-rate 1 --run-time 60s --host http://localhost:8080`

Open your local Grafana in the browser at [http://localhost:3000/](http://localhost:3000/)

Import the example dashboard from `locust_dashboard.json` file.

![Locust dashboard in TimescaleDB](https://raw.githubusercontent.com/smenateam/locust-timescaledb/master/dashboard.png)
