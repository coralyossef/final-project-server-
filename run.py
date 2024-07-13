from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Test")
    app.run(host='127.0.0.1', port=8000)  # Change 8000 to your desired port
