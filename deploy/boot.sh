#!/bin/sh
source python/bin/activate
pwd
ls conf
#flask db upgrade --directory portfolio-backend/portfolio_backend/application/migrations
#exec uwsgi --wsgi-file portfolio-backend/portfolio_backend/application/wsgi.py --callable backend_application --http 0.0.0.0:5000

exec uwsgi --ini conf/uwsgi.ini