import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True





def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
        
    return d



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Spot Identifying Platform</h1>
<p>This site is a prototype API to show how we can use an api to locate a spot nearby. </p>'''



@app.route('/api/v1/locations/spots/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('datav2.db')
    c = conn.cursor()
    c.row_factory = dict_factory
    return jsonify(c.execute("SELECT * FROM Spots").fetchall())
"""
Old version
@app.route('/api/v1/locations/spots/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('datav2.db')
    c = conn.cursor()
    c.row_factory = dict_factory
    return jsonify(c.execute("SELECT * FROM Spots").fetchall())
"""
@app.route('/api/v1/locations/restaurants/all', methods=['GET'])
def api_allR():
    conn = sqlite3.connect('datav2.db')
    c = conn.cursor()
    c.row_factory = dict_factory
    return jsonify(c.execute("SELECT * FROM Restaurants").fetchall())

@app.route('/api/v1/locations/customers/all', methods=['GET'])
def api_allC():
    conn = sqlite3.connect('datav2.db')
    c = conn.cursor()
    c.row_factory = dict_factory
    return jsonify(c.execute("SELECT * FROM Customers").fetchall())

@app.route('/api/v1/orders/all', methods=['GET'])
def api_allO():
    conn = sqlite3.connect('datav2.db')
    c = conn.cursor()
    c.row_factory = dict_factory
    return jsonify(c.execute("SELECT * FROM Orders").fetchall())

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The location could not be found </p>", 404


@app.route('/api/v1/locations/restaurants', methods=['GET'])
def api_id():
    
    query_parameters = request.args
    
    spot_id = query_parameters.get('id')
    address = query_parameters.get('Address')
    phone= query_parameters.get('Phone')
    
    query = "SELECT * FROM Restaurants WHERE"
    to_filter = []
    
    if spot_id:
        query+= ' id=? AND'
        to_filter.append(spot_id)
    if address:
        query+= ' Address=? AND'
        to_filter.append(address)
    if phone:
        query+= ' Phone=? AND'
        to_filter.append(address)

    if not(phone or address or spot_id):
        return page_not_found(404)
    
    query = query[:-4] + ';'
    
    conn = sqlite3.connect('datav2.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    results = cur.execute(query, to_filter).fetchall()
    
    return jsonify(results)

@app.route('/api/v1/locations/spots', methods=['GET'])
def api_idh():
    
    query_parameters = request.args
    
    spot_id = query_parameters.get('id')
    address = query_parameters.get('Address')
    
    query = "SELECT * FROM Spots WHERE"
    to_filter = []
    
    if spot_id:
        query+= ' id=? AND'
        to_filter.append(spot_id)
    if address:
        query+= ' Address=? AND'
        to_filter.append(address)
    if not(address or spot_id):
        return page_not_found(404)
    
    query = query[:-4] + ';'
    
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    results = cur.execute(query, to_filter).fetchall()
    
    return jsonify(results)

@app.route('/api/v1/locations/customers', methods=['GET'])
def api_idq():
    
    query_parameters = request.args
    
    spot_id = query_parameters.get('id')
    name = query_parameters.get('Name')
    address=query_parameters.get('Address')
    
    query = "SELECT * FROM customers WHERE"
    to_filter = []
    
    if spot_id:
        query+= ' id=? AND'
        to_filter.append(spot_id)
    if address:
        query+= ' Address=? AND'
        to_filter.append(address)
    
    if name:
        query+= ' name=? AND'
        to_filter.append(address)

    if not(name or address or spot_id):
        return page_not_found(404)
    
    query = query[:-4] + ';'
    
    conn = sqlite3.connect('datav2.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    results = cur.execute(query, to_filter).fetchall()
    
    return jsonify(results)
    
    # Create an empty list for our results
    
    

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
  
            
    


app.run()

"""
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
"""
