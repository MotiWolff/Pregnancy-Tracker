from app import create_app, db

app = create_app()

# Create tables when app starts
if __name__ == '__main__':
    app.run()
