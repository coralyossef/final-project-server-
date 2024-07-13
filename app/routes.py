from flask import request, jsonify, make_response
from app import db
from app.models import Customer, Service, customer_services
from functools import wraps

# Decorator to require authentication and role check
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username):
            return

        user = Customer.query.filter_by(user_name=auth.username).first()
        if user.user_type != 'operator':
            return make_response('Unauthorized access!', 403)

        return f(*args, **kwargs)
    return decorated

# Function to verify username and password
def check_auth(username):
    # Here you should check the username and password with the ones stored in your database
    # For example, let's assume we have a table User with columns username and password
    user = Customer.query.filter_by(user_name=username).first()
    if user:  # Assuming you have a method to verify password
        return True
    return False

def init_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        customer = Customer(
            first_name=data['first_name'],
            last_name=data['last_name'],
            user_name=data['username'],
            password=data['password'],
            email=data['email'],
            phone=data['phone'],
            customer_type=data['customer_type'],
            user_type="customer"
        )
        db.session.add(customer)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201

    @app.route('/login', methods=['POST'])
    def login():
        print(request)
        data = request.get_json()
        customer = Customer.query.filter_by(user_name=data['username']).first()
        if not customer or customer.password != data['password']:
            return jsonify({'message': 'Could not verify'}), 401
        print(customer.to_dict())
        return jsonify({'message': 'Login successful', 'user': customer.to_dict()})

    @app.route('/services', methods=['POST'])
    def add_service():
        data = request.get_json()
        service = Service(
            name=data['name'],
            description=data.get('description', ''),
            icon=data.get('icon', ''),
            price=data['price'],
            customer_type=data['customer_type']
        )
        db.session.add(service)
        db.session.commit()
        return jsonify({'message': 'Service added successfully'})

    @app.route('/customers', methods=['GET'])
    def get_customers():
        customers = Customer.query.all()
        result = [customer.to_dict() for customer in customers]
        return jsonify(result)

    @app.route('/services', methods=['GET'])
    def get_services():
        services = Service.query.all()
        result = [service.to_dict() for service in services]
        return jsonify(result)

    @app.route('/customers/<int:customer_id>', methods=['GET'])  # Fixed HTTP method name
    def get_profile(customer_id):
        customer = Customer.query.get_or_404(customer_id)
        return jsonify(customer.to_dict())
    
    @app.route('/services/<int:id>', methods=['GET'])  # Fixed HTTP method name
    def get_service(id):
        service = Service.query.get_or_404(id)
        return jsonify(service.to_dict())

    @app.route('/customers/<int:customer_id>/services', methods=['GET'])
    def get_customer_services(customer_id):
        customer = Customer.query.get_or_404(customer_id)
        services = Service.query.join(customer_services).filter(customer_services.c.customer_id == customer.id).all()
        return jsonify([service.to_dict() for service in services])
    
    @app.route('/customers/<int:id>', methods=['POST'])
    @requires_auth
    def edit_customer(id):
        data = request.json
        customer = Customer.query.get_or_404(id)

        customer.first_name = data['first_name']
        customer.last_name = data['last_name']
        customer.user_name = data['user_name']
        customer.email = data['email']
        customer.phone = data["phone"]
        customer.customer_type = data['customer_type']
        customer.user_type = data['user_type']

        db.session.commit()

        return jsonify({
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'user_name': customer.user_name,
            'email': customer.email,
            'phone': customer.phone,
            'customer_type': customer.customer_type,
            'user_type': customer.user_type
        }), 200

    @app.route('/customers/<int:customer_id>', methods=['DELETE'])
    @requires_auth
    def delete_customer(customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404

        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted successfully'})

    @app.route('/services/<int:id>', methods=['POST'])
    @requires_auth
    def edit_service(id):
        data = request.json
        service = Service.query.get_or_404(id)

        service.name = data['name']
        service.description = data['description']
        service.icon = data['icon']
        service.price = data['price']
        service.customer_type = data['customer_type']

        db.session.commit()

        return jsonify({
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'icon': service.icon,
            'price': service.price,
            'customer_type': service.customer_type
        }), 200

    @app.route('/services/<int:id>', methods=['DELETE'])
    @requires_auth
    def delete_service(id):
        service = Service.query.get(id)
        if not service:
            return jsonify({'error': 'Service not found'}), 404

        db.session.delete(service)
        db.session.commit()
        return jsonify({'message': 'Service deleted successfully'})
