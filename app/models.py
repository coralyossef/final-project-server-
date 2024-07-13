from . import db

# Define the Customer model to store customer data
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    first_name = db.Column(db.String(255), nullable=False)  # Customer's first name
    last_name = db.Column(db.String(255), nullable=False)  # Customer's last name
    user_name = db.Column(db.String(255), unique=True, nullable=False)  # Unique username
    password = db.Column(db.String(255), nullable=False)  # Password
    email = db.Column(db.String(255), unique=True, nullable=False)  # Unique email
    phone = db.Column(db.String(50), nullable=True)  # Optional phone number
    customer_type = db.Column(db.String(50), nullable=False)  # Customer type (private, business, institutional)
    user_type = db.Column(db.String(50), nullable=False, default='default')  # User type (default, manager, admin)
    services = db.relationship('Service', secondary='customer_services', backref='customers')

    # Convert the customer object to a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'user_name': self.user_name,
            'email': self.email,
            'phone': self.phone,
            'customer_type': self.customer_type,
            'user_type': self.user_type,
            'services': [service.to_dict() for service in self.services]
        }

# Define the Service model to store service data
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(255), nullable=False)  # Service name
    description = db.Column(db.String(255), nullable=True)  # Optional service description
    icon = db.Column(db.String(255), nullable=True)  # URL to an icon image
    price = db.Column(db.Float, nullable=False)  # Add price field
    customer_type = db.Column(db.String(50), nullable=False)  # Customer type (private, business, institutional)

    # Convert the service object to a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon': self.icon,
            'price': self.price,
            'customer_type': self.customer_type
        }

# Relationship table to associate customers with services
customer_services = db.Table('customer_services',
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'), primary_key=True)
)
