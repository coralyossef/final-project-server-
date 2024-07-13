from app import create_app, db
from app.models import Customer, Service

app = create_app()

def create_initial_data():
    with app.app_context():
        services = [
            Service(name='Home Network Setup', description='Setting up and securing home networks', icon='https://static.thenounproject.com/png/3615869-200.png', customer_type='private', price=100.00),
            Service(name='Personal Tech Support', description='Offering on-demand tech support for various personal technology issues', icon='https://fivotechnology.com/wp-content/uploads/2024/01/24-hours.png', customer_type='private', price=50.00),
            Service(name='Cloud Backup Services', description='Providing secure cloud storage solutions for personal data backup', icon='https://fivotechnology.com/wp-content/uploads/2024/02/migration.png', customer_type='private', price=75.00),
            Service(name='IT Consulting', description='Providing expert advice on IT strategy and implementation', icon='https://fivotechnology.com/wp-content/uploads/2024/02/full-stack.png', customer_type='business', price=200.00),
            Service(name='Managed IT Services', description='Comprehensive IT management including monitoring, maintenance, and support', icon='https://fivotechnology.com/wp-content/uploads/2024/01/management-1.png', customer_type='business', price=150.00),
            Service(name='Cloud Solutions', description='Implementing and managing cloud services such as AWS, Azure, and Google Cloud', icon='https://fivotechnology.com/wp-content/uploads/2024/02/migration.png', customer_type='business', price=250.00),
            Service(name='Cybersecurity Services', description='Protecting business data and networks from cyber threats', icon='https://fivotechnology.com/wp-content/uploads/2024/02/management-1.png', customer_type='business', price=300.00),
            Service(name='Government IT Solutions', description='Offering IT services tailored for government agencies', icon='https://fivotechnology.com/wp-content/uploads/2024/02/front-end.png', customer_type='institutional', price=400.00),
            Service(name='Research IT Support', description='Providing specialized IT support for research and development projects', icon='https://fivotechnology.com/wp-content/uploads/2024/02/team.png', customer_type='institutional', price=350.00)
        ]
        db.session.bulk_save_objects(services)
        db.session.commit()

        customers = [
            Customer(first_name='Alice', last_name='Smith', user_name='alice', password='password', email='alice@example.com', customer_type='private', user_type="default"),
            Customer(first_name='Bob', last_name='Johnson', user_name='bob', password='password', email='bob@example.com', customer_type='business', user_type="default"),
            Customer(first_name='Carol', last_name='Williams', user_name='carol', password='password', email='carol@example.com', customer_type='institutional', user_type="default")
        ]
        db.session.bulk_save_objects(customers)

        db.session.commit()

if __name__ == '__main__':
    create_initial_data()
