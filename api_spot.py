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
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.row_factory = dict_factory
    return jsonify(c.execute("SELECT * FROM Spots").fetchall())

@app.route('/api/v1/locations/restaurants/all', methods=['GET'])
def api_allR():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.row_factory = dict_factory
    return jsonify(c.execute("SELECT * FROM restaurants").fetchall())

@app.route('/api/v1/locations/customers/all', methods=['GET'])
def api_allC():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.row_factory = dict_factory
    return jsonify(c.execute("SELECT * FROM Customers").fetchall())

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The location could not be found </p>", 404


@app.route('/api/v1/locations/restaurants', methods=['GET'])
def api_id():
    
    query_parameters = request.args
    
    spot_id = query_parameters.get('id')
    address = query_parameters.get('Address')
    phone= query_parameters.get('Phone')
    
    query = "SELECT * FROM restaurants WHERE"
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
    
    conn = sqlite3.connect('data.db')
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
    
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    results = cur.execute(query, to_filter).fetchall()
    
    return jsonify(results)
    
    # Create an empty list for our results
    
    

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
  
            
    


app.run()
