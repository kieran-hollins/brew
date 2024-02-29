from flask import Flask
from brew import pages, posts
from flask_mysqldb import MySQL

def create_app():
    app = Flask(__name__)

    # Database Configuration - Hosted in Railway.app
    # app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST')
    # app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER')
    # app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD')
    # app.config['MYSQL_DB'] = os.environ.get('MYSQLDB')

    app.config['MYSQL_HOST'] = "roundhouse.proxy.rlwy.net"
    app.config['MYSQL_USER'] = "root"
    app.config['MYSQL_PASSWORD'] = "6caGCg56E1FghdFh-fdecdCFDC1BD2he"
    app.config['MYSQL_DB'] = "railway"

    mysql = MySQL(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    return app