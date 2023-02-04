import csv
import googlemaps
import pandas as pd

# Your API key
API_KEY = 'YOUR API KEY'

# Create a client object
gmaps = googlemaps.Client(key=API_KEY)

# Import the data from the CSV file
filename = 'locations_and_queries.csv'
df = pd.read_csv(filename)

# Read lat/long and query data from the file
with open("locations_and_queries.csv", "r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    lat_long_data = []
    for row in reader:
        lat = float(row[1])
        long = float(row[2])
        query = row[0]
        radius = int(row[3])
        lat_long_data.append((lat, long, query, radius))

# Open a new CSV file for writing
output_filename = 'Business_Listings.csv'
with open(output_filename, 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['Location', 'Radius', 'Query', 'Name', 'Address', 'Phone', 'Website'])

    for lat_long in lat_long_data:
        # Call the Place Search API
        location = f'{lat_long[0]}, {lat_long[1]}'
        query = lat_long[2]
        radius = lat_long[3]
        result = gmaps.places(query=query, location=location, radius=radius)

        # Write the results to the CSV file
        for place in result['results']:
            place_id = place['place_id']
            place_details = gmaps.place(place_id=place_id).get('result', {})
            phone = place_details.get('formatted_phone_number', '')
            website = place_details.get('website', '')
            writer.writerow([location, radius, query, place['name'], place['formatted_address'], phone, website])

print(f'Data exported to {output_filename}.')
