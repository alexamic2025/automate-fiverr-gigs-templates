from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class DashboardMetrics(db.Model):
    __tablename__ = 'dashboard_metrics'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    revenue = db.Column(db.Float, nullable=False, default=0.0)
    orders = db.Column(db.Integer, nullable=False, default=0)
    customers = db.Column(db.Integer, nullable=False, default=0)
    conversion_rate = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'revenue': self.revenue,
            'orders': self.orders,
            'customers': self.customers,
            'conversion_rate': self.conversion_rate,
            'created_at': self.created_at.isoformat()
        }

class SalesCategory(db.Model):
    __tablename__ = 'sales_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    revenue = db.Column(db.Float, nullable=False, default=0.0)
    percentage = db.Column(db.Float, nullable=False, default=0.0)
    color = db.Column(db.String(7), nullable=False, default='#3B82F6')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'category_name': self.category_name,
            'revenue': self.revenue,
            'percentage': self.percentage,
            'color': self.color,
            'created_at': self.created_at.isoformat()
        }

class ServicePackage(db.Model):
    __tablename__ = 'service_packages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # market_research, bi_dashboard, data_analysis
    tier = db.Column(db.String(20), nullable=False)  # basic, standard, premium
    price = db.Column(db.Float, nullable=False)
    features = db.Column(db.Text, nullable=False)  # JSON string of features
    delivery_days = db.Column(db.Integer, nullable=False)
    is_popular = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'tier': self.tier,
            'price': self.price,
            'features': json.loads(self.features) if self.features else [],
            'delivery_days': self.delivery_days,
            'is_popular': self.is_popular,
            'created_at': self.created_at.isoformat()
        }

class ContactSubmission(db.Model):
    __tablename__ = 'contact_submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    company = db.Column(db.String(100), nullable=True)
    service_type = db.Column(db.String(50), nullable=True)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='new')  # new, contacted, converted, closed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'company': self.company,
            'service_type': self.service_type,
            'message': self.message,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

