from flask import render_template
import config
from models import Profile

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    people = Profile.query.all()
    return render_template("home.html", Profile=Profile)
