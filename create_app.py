from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)


def create_app():

    # initalise the database
    db.init_app(app)

    # import the files
    from register.views import register_app
    from login.views import login_app
    from users.views import user_app
    from profile.views import profile_app
    from follow.views import follow_app
    from tweets.views import tweets_app
    from logout.views import logout_app

    # register the blueprints
    app.register_blueprint(register_app)
    app.register_blueprint(login_app)
    app.register_blueprint(user_app)
    app.register_blueprint(profile_app)
    app.register_blueprint(follow_app)
    app.register_blueprint(tweets_app)
    app.register_blueprint(logout_app)
    return app


