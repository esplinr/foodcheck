foodcheck
=========

Copyright
---------
Web applictaion to display health report information for local eateries.
Copyright (C) 2013
Timothy James Austen
Eileen Qiuhua Lin
Richard Esplin <richard-oss@esplins.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Overview
--------
Display health report information for local eateries.

Hosted at http://Foodcheck.us

Target Market: Restaurant connoisseurs who want to see the health report for local eateries.

Business Model: Civic awareness funded by cities and donations. Code for America has expressed an interest in having this application in their directory.

Minimum Functionality and Scope:
* Touch friendly web UI
* Read data for San Francisco: https://data.sfgov.org/Public-Health/Restaurant-Scores/stya-26eb
* Allow the data to be browsed against OpenStreetMap data.
* Goal is to submit the application to Code for America (http://codeforamerica.org/apps/)
* AGPL License hosted at Github

Out of Scope Future Features:
* Add other cities (need to research who has data available)
* Analytics on historical data, on a per location or per city basis
* Mobile native UI

Relevant Technologies:
* Source control: Git / Github (https://github.com/esplinr/foodcheck)
* Language: Python 2.7
* Web Framework: Django
* PaaS: RedHat OpenShift
* Data Store: MongoDB
* Mapping Data: OpenStreetMap, exposed through Leaflet
