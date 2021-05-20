from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = "123askldaskfbbaskdkasgjash0120fd17237ajkhafkas"

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.behome

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
        return f(*args, **kwargs)
    else:
        return redirect('/')
  return wrap

# Routes
import Routes.userRoutes

@app.route('/')
def home():
    session["rol"] = "invitado"
    return render_template('/views/Main/homepage.html')

@app.route('/login')
def login():
    return render_template('/views/auth/login.html')
        
@app.route('/register')
def register():
    return render_template('/views/auth/register.html')

@app.route('/mis-anuncios')
@login_required
def myAds():
    session["rol"] = "anfitrion"
    return render_template('/views/profile/misAnuncios.html')

@app.route('/añadir-anuncio', methods=["POST"])
def addNewAd():

    if request.method == "POST" and 'logged' in session:
        adTitle = request.form['adTitle']
        adImages = request.form['adImages']
        adLocation = request.form['adLocation']
        adRooms = request.form['adRooms']
        adBath = request.form['adBath']
        adMaxPeople = request.form['adMaxPeople']
        adMeters = request.form['adMeters']
        adPrice = request.form['adPrice']

        anuncio = {"title":adTitle, "Images":adImages, "Location":adLocation , "Rooms":adRooms , "Bath":adBath, "MaxPeople": adMaxPeople, "Meters": adMeters, "price":adPrice} 

    return redirect(url_for('myAds'))

@app.route('/editar-anuncio')
def editAnucements():
    return render_template('/views/auth/register.html')

# Handle User Routes

if __name__ == "__main__":
    app.run(debug=True)



