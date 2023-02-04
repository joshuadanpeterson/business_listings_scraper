# Business Listings Scraper
This code is a script that uses the Google Maps API to scrape business listings data. The script takes in a CSV file with location and query data, and outputs a new CSV file with the business listing information.

## Requirements
- A Google Maps API key (https://developers.google.com/maps/gmp-get-started)
- Python 3.x
- pandas library (pip install pandas)
- googlemaps library (pip install googlemaps)
  
## Usage
1. Replace 'YOUR API KEY' in the code with your own Google Maps API key.
2. The script uses the sample file 'locations_and_queries.csv' as input. Replace this file with your own data or make the necessary adjustments to the code to use a different file.
3. Run the script using python business_listings_scraper.py
4. The output file Business_Listings.csv will be created in the same directory as the script.

## Sample Data
The locations_and_queries.csv file contains sample data for demonstration purposes. The file contains four columns:

1. Query: A search term to use when querying the Google Maps API.
2. Latitude: The latitude of the location to search near.
3. Longitude: The longitude of the location to search near.
4. Radius: The search radius in meters.

## Output
The 'Business_Listings.csv' file will contain the following information for each business listing returned by the Google Maps API:

1. Location: The latitude and longitude of the search location.
2. Radius: The search radius in meters.
3. Query: The search term used to query the Google Maps API.
4. Name: The name of the business.
5 .Address: The address of the business.
6. Phone: The phone number of the business, if available.
7. Website: The website of the business, if available.





## Limitations
This script is limited by the daily usage quota of the Google Maps API and by the number of results returned by the API. The API may also return different results based on the time the script is run and the user's location.