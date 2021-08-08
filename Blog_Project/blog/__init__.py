import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.logger.debug('app.instance_path = %s', app.instance_path)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="$%px0vz%84j2y9ztqg^8k8_!8*-372g85z73(art-z#+5l5h1w'",
        # store the database in the instance folder
        # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    
    from blog import order,auth

    
    app.add_url_rule("/", endpoint="index")

    return app
