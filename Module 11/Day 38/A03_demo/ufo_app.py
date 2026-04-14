import csv
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """

def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings

@app.route('/ufo-sightings', methods=['GET'])
def get_sightings():
    country = request.args.get('country', '') # '' is passing in a blank value; like * in SQL
    page = int(request.args.get('page', 1)) # default 1
    per_page = int(request.args.get('per_page', 10)) # default 10
    
    scrubbed_sightings = load_ufo_data('data/scrubbed.csv')

    # Make a copy of our data
    filtered_sightings = scrubbed_sightings.copy() # copy makes a new copy of our list in memory so they're independent

    # Loop through the original data and remove any sightings that don't match the country filter
    for sighting in scrubbed_sightings:
        if country and sighting['country'].lower() != country.lower():
            filtered_sightings.remove(sighting)

    # Implement pagination
    start = (page - 1) * per_page # offsets our start point depending on which page we're on
    end = start + per_page # select our end result based on our starting point

    paginated_sightings = filtered_sightings[start:end] # just returns the data we want to see on our page

    return jsonify(paginated_sightings)

@app.route('/research-stations', methods=['GET'])
def get_research_stations():
    stations = []

    with open('data/research_stations.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            stations.append(row)
    
    return jsonify(stations)

# POST requests send data to our "backend"
@app.route('/add-research-station', methods=['POST'])
def add_research_station():
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')

    if not name or not location: # if name or location are None
        return jsonify({'error': 'Name and location are required'}), 400 # returns a 400 - Bad Request error if we're missing data
    
    # If we have all the data we need, add it to the csv file
    with open('data/research_stations.csv', mode='a', newline='') as file: # opens in 'a'ppend mode
        fieldnames = ['name', 'location'] # sets up our keys
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow({'name': name, 'location': location}) # writes our data to the csv as a new row
    
    return jsonify({'message': 'Research station added successfully'}), 201 # 201 - Success code