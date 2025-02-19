from app import create_app, db
import logging
from logging.handlers import RotatingFileHandler
import os

app = create_app()

# Set up logging
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/pregnancy_tracker.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Pregnancy Tracker startup')

# Create tables
with app.app_context():
    try:
        db.create_all()
        app.logger.info('Database tables created successfully')
    except Exception as e:
        app.logger.error(f'Error creating database tables: {str(e)}')

if __name__ == '__main__':
    app.run()
