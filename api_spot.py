import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

spots = [
    {
        'id': 0,
        'building_name': 'Yahoo Headquarters',
        'point_of_contact': 'Rob Smith',
        'building_type': 'Office',
        'zipcode': 91234,
        'address': '1234 Yahoo Avenue, San Francisco'
    },
    {
        'id': 1,
        'building_name': 'Marriott San Jose',
        'point_of_contact': 'Jeffrey Dougie',
        'building_type': 'Hotel',
        'zipcode': 91492,
        'address': '9876 Marriot Avenue, San Jose'
    },
    {
        'id':2,
        'building_name': 'Villagio Apartments',
        'point_of_contact': 'Jennifer White',
        'building_type': 'Apartment',
        'zipcode': 91239,
        'address': '1234 Villagio Avenue, San Jose'
    }, 
    {
        'id':3,
        'building_name': 'Rochester Apartments',
        'point_of_contact': 'Tiffany Nguyen',
        'building_type': 'Apartment',
        'zipcode': 91239,
        'address': '1234 Rochester Avenue, San Jose'
    },
    {
        'id':4,
        'building_name': 'Robinhood Main Office',
        'point_of_contact': 'John Adams',
        'building_type': 'Office',
        'zipcode': 91223,
        'address': '1234 Robinhood Avenue, San Francisco'
    }
]

#Code if we switch to database
"""
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
        
    return d
"""


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Spot Identifying Platform</h1>
<p>This site is a prototype API to show how we can use an api to locate a spot nearby. </p>'''



@app.route('/api/v1/locations/spots/all', methods=['GET'])
def api_all():
    return jsonify(spots)



#Code if we switch to database
"""
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('Select * FROM books;').fetchall()
    
    return jsonify(all_books)
"""



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The location could not be found </p>", 404


@app.route('/api/v1/locations/spots', methods=['GET'])
def api_id():
    
    query_parameters = request.args
    
    id = query_parameters.get('id')
    zipcode = query_parameters.get('zipcode')
    building_type = query_parameters.get('building_type')
    
    if id:
        id = int(request.args['id'])
    if zipcode:
        zipcode = int(request.args['zipcode'])
    if building_type:
        building_type = request.args['building_type']
    if not(id or zipcode or building_type):
        return page_not_found(404)
    
    # Create an empty list for our results
    results = []
    

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for spot in spots:
        if spot['id'] == id:
            results.append(spot)
        if spot['zipcode'] == zipcode:
            results.append(spot)
        if spot['building_type'] == building_type:
            results.append(spot)
            
    return jsonify(results)

#Code if we switch to database
"""
@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args
    
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')
    
    query = "SELECT * FROM books WHERE"
    to_filter = []
    
    if id:
        query+= ' id=? AND'
        to_filter.append(id)
    if published:
        query+= ' published=? AND'
        to_filter.append(published)
    if author:
        query+= ' author =? AND'
        to_filter.append(author)
    if not(id or published or author):
        return page_not_found(404)
    
    query = query[:-4] + ';'
    
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    results = cur.execute(query, to_filter).fetchall()
    
    return jsonify(results)
"""

app.run()
