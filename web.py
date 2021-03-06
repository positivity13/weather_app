from assignment_3 import company_by_number, company_profile
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# access_token = os.environ.get('ACCESS_TOKEN')
# #create search object
# s = Search(access_token=access_token)

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	details = None
	profile = None
	co_no = None
	name = request.values.get('name')
	co_no = request.values.get('cono')
	if name == None:
		pass
	else:
		details = company_by_number(name)
	if co_no == None:
		pass
	else:
		profile = company_profile(co_no)
	return render_template('index.html', name=name, co_no=co_no, details=details, profile=profile)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	# city = request.values.get('city')
	# weather = get_weather(city, api_key)
	return render_template('contact.html')

if __name__ == "__main__":
	app.run()
