from config import db, ma

class Profile(db.Model):
    __tablename__ = "Profile"
    __table_args__ = {"schema": "CW2"}

    email = db.Column(db.String(30), primary_key=True)
    username = db.Column(db.String(30), nullable=False)

    aboutme = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    language = db.Column(db.String(30), nullable=True)

    password = db.Column(db.String(30), nullable=False)

    role = db.Column(db.String(5), nullable=False, default="User")  

class Activity(db.Model):
    __tablename__ = "Activity"
    __table_args__ = {"schema": "CW2"}

    activity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    activity = db.Column(db.String(30), nullable=False, unique=True)


class FavouriteActivity(db.Model):
    __tablename__ = "FavouriteActivity"
    __table_args__ = {"schema": "CW2"}

    email = db.Column(db.String(30), db.ForeignKey("CW2.Profile.email"), primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("CW2.Activity.activity_id"), primary_key=True)



class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        load_instance = True
        sqla_session = db.session
class ActivitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Activity
        load_instance = True
        sqla_session = db.session

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)


class FavouriteActivitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FavouriteActivity
        load_instance = True
        sqla_session = db.session
        include_fk = True

fav_schema = FavouriteActivitySchema()
favs_schema = FavouriteActivitySchema(many=True)
profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)




