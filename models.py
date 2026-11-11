from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

def zimbabwe_now():
    harare_tz = pytz.timezone("Africa/Harare")
    return datetime.now(harare_tz)

# USER MODEL
class User(UserMixin, db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  
    created_at = db.Column(db.DateTime, default=zimbabwe_now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# RISK PREDICTION MODEL
class RiskPrediction(db.Model):
    __tablename__ = "risk_predictions"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Inputs
    product = db.Column(db.String(150))
    unit = db.Column(db.String(50))
    production_cost = db.Column(db.Float)
    wholesale_price = db.Column(db.Float)
    retail_price = db.Column(db.Float)
    operational_costs = db.Column(db.Float)
    usd_inflation_rate = db.Column(db.Float)
    gdp_growth_rate = db.Column(db.Float)
    stock_out_rate = db.Column(db.Float)
    purchasing_frequency = db.Column(db.Float)
    dollarization_policy_usd = db.Column(db.Float)
    dollarization_policy_zwl = db.Column(db.Float)
    demand_rate = db.Column(db.Float)

    # Outputs
    predicted_risk = db.Column(db.String(100))
    all_risks_with_scores = db.Column(db.JSON)      
    profit_risk_data = db.Column(db.JSON)           
    created_at = db.Column(db.DateTime, default=zimbabwe_now)


# DEMAND FORECAST MODEL

class DemandForecast(db.Model):
    __tablename__ = "demand_forecasts"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Inputs
    product = db.Column(db.String(150))
    unit = db.Column(db.String(50))
    production_cost = db.Column(db.Float)
    retail_price = db.Column(db.Float)
    demand_rate = db.Column(db.Float)

    # Outputs
    forecasted_demand = db.Column(db.Float)
    model_used = db.Column(db.String(50)) 
    rmse = db.Column(db.Float)
    mae = db.Column(db.Float)
    r2 = db.Column(db.Float)

    created_at = db.Column(db.DateTime, default=zimbabwe_now)

# PROFIT OPTIMIZATION MODEL
class ProfitOptimization(db.Model):
    __tablename__ = "profit_optimizations"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Inputs
    product = db.Column(db.String(150))
    unit = db.Column(db.String(50))
    production_cost = db.Column(db.Float)
    operational_costs = db.Column(db.Float)
    retail_price = db.Column(db.Float)

    # Outputs
    suggested_units = db.Column(db.Integer)        
    estimated_profit = db.Column(db.Float)         
    suggested_retail_price = db.Column(db.Float)   

    created_at = db.Column(db.DateTime, default=zimbabwe_now)

# RETAIL PRICE FORECAST MODEL

class RetailPriceForecast(db.Model):
    __tablename__ = "retail_price_forecasts"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Inputs
    product = db.Column(db.String(150))
    unit = db.Column(db.String(50))
    production_cost = db.Column(db.Float)
    operational_costs = db.Column(db.Float)
    wholesale_price = db.Column(db.Float)

    # Outputs
    predicted_price = db.Column(db.Float)
    volatility_index = db.Column(db.Float)
    confidence_interval = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, default=zimbabwe_now)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        #db.drop_all() 
