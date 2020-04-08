from flask insert render_template
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/get/animal', methods = ['GET', 'POST']
def animal():
    animal = requests.get('http://app-2:5001/animal/name')
    noise = requests.post('http://app-2:5001/animal/noise', data=animal.text)
    return render_template('animals.html', title='Animals', animal=animal.text, noise=noise.text)




