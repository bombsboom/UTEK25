# UTEK25 Team 13 Submission
The disaster scenario chosen was the earthquake scenario. The communication focus area is damage reporting. The files provided are a demo featuring what would make up an effective damage reporting tool for civilians to communicate to emergency response. Civilians will install an app which allows them to report damage, and emergency response teams will have their own app that allows them to view areas with the most impact on people. The demo is not a complete full stack app due to time restriction, and it could be implemented in real life as a server with django. Flask, React and many other front end tools could be used to create a more user-friendly civilian and emergency response app. The database could also be replaced with an actual SQL database as a better practice. The area of Los Angeles was selected as a test case, but this program can easily be adapted to any region.

## Libraries Used

The following libraries were used for the project and must be installed first in order for the project to run:

   1.  pandas
   2.  folium
   3.  geopy

## Files in Directory

There will be 4 files in the directory:


   1.  client.py
  
       This file is the app used by civilians to report damage caused by earthquakes and send it to the database.


   2.  reports.csv
  
       This file saves all the damage reports. It contains the latitude and longitude of the location the damage was reported and the nature of the damage as per the user's report, as well as the zip code. This file would be stored on the server.


   2.  magnitude.csv
  
       This file is stored on the server and compiles the number of reports in each LA zip code.


   3.  backend.py


       This file runs on the server and uses the reports.csv to create magnitude.csv.


   4.  ems.py
	
	This file is the app used by emergency services to locate where repairs are needed. It displays every report on a map, which has togglable layers to view each type of repair independently. It also shows how many reports have been reported in each zip code, allowing emergency services to identify the areas most damaged by the earthquake.

## Installation & Execution

1. Install python3

2. Install pandas by entering the following in the command line shell:
  
   pip install pandas

3.  Install folium by entering the following in the command line shell:
  
   pip install folium

4.  Install geopy by entering the following in the command line shell:
  
   pip install geopy

5.  To run client app to report damage, use the command-line shell to open the directory where the files are kept and enter:

   python3 client.py

6. To run back end to calculate damnage in each zip code, use the command-line shell to open the directory where the files are kept and enter:

   python3 backend.py

7. To open the emergency services end app, open the directory where the files are kept and enter:

   python3 ems.py


