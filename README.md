# zerodha-bhavcopy

access webapp from -> http://yashp-zerodha-bhavcopy.centralindia.cloudapp.azure.com/

## features

- Downloads the equity bhavcopy zip from BSE India every day at 18:00 IST for the current date
- Extracts and parses the CSV file in it.
- Writes the records into Redis with appropriate data structures (Fields: code, name, open, high, low, close).
- Renders a simple V̶̶̶u̶̶̶e̶̶̶J̶̶̶S̶̶̶ ̶f̶r̶o̶n̶t̶e̶n̶d̶ HTML/CSS/Bootstrap frontend with a search box that allows the stored entries to be searched by name and renders a table of results and optionally downloads the results as CSV
- The search performed on the backend using Redis

## FYI

- used HTML/CSS/Bootstrap for frontend instead of VueJS
- celery framework is used for background task to download bhavcopy everyday at 6pm
- webapp is deployed on *Microsoft Azure Cloud*
