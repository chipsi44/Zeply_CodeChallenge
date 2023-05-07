'''DISCLAIMER: This code is intended to demonstrate how the endpoints can be used in a simple way,
and does not represent production-level code. 
It is assumed that a web developer would ensure that users can only enter valid input, 
and appropriate error handling is not included in this code.
'''
# Importing the necessary Flask functions and endpoints to handle the different requests.
from flask import Flask, request, render_template
from endpoints import generate_address, list_address,retrieve_address

# This code creates a Flask web application.
app = Flask(__name__)

# Defines a route that is accessible at the root URL ("/"). 
@app.route("/", methods=["GET", "POST"])
def generate():

    # If the request method is "GET", the string "ALIVE" is printed and the "index.html" template is rendered.
    if request.method == "GET":
        print("ALIVE")
        return render_template("index.html")
    
    # If the request method is "POST", the action requested by the user is checked and the corresponding function is called.
    else:
        print("From Post") 
        function_to_do = request.form['action']
        
        # If the user requests to generate an address, the private key is extracted from the form data (if provided),
        # and the generate_address endpoint is called to generate the address.
        if function_to_do == 'generateAddress' :
            p_key = request.form.get('privateKey', False)
            seed,private_key,public_address = generate_address(request.form["coin"],p_key)
            return render_template("index.html", info_generate = [seed,private_key,public_address])
        
        # If the user requests to retrieve all addresses, the list_address endpoint is called to retrieve all addresses.
        elif function_to_do == 'getAllAddresses' :
            list_all_add = list_address()
            return render_template("index.html", info = list_all_add)
        
        # If the user requests to retrieve a specific address, the address ID is extracted from the form data,
        # and the retrieve_address endpoint is called to retrieve the corresponding address.
        elif function_to_do == 'retrieveAddress' :
            add_id = request.form['addressId']
            return render_template("index.html", info = retrieve_address(add_id))
        
        # If no action is specified, the "index.html" template is simply rendered again.
        else : 
            return render_template("index.html")

# Starts the Flask application.
app.run(debug=False)
