from flask import Flask
from config import Config
from models import db, init_db
from flask_login import LoginManager
from views.auth import auth_bp
from views.customer import customer_bp
from views.farm import farm_bp
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

init_db(app)
login_manager.init_app(app)
migrate = Migrate(app, db)
    
app.register_blueprint(auth_bp)
app.register_blueprint(customer_bp, url_prefix='/customer')
app.register_blueprint(farm_bp, url_prefix='/farm')



@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

if __name__ == '__main__':
 
    app.run(host='0.0.0.0', port=5000, debug=True)