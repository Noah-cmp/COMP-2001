from flask import render_template
import config
from models import Profile

app = config.connex_app
app.add_api(config.basedir / "swagger.yaml")

@app.route("/")
def home():
    people = Profile.query.all()
    return render_template("home.html", Profile=Profile)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
