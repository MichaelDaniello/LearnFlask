import os
 
# General Flask app settings
DEBUG = os.environ.get('DEBUG', True)
SECRET_KEY = os.environ.get('SECRET_KEY', None)
 
# Redis connection
REDIS_SERVER = os.environ.get('REDIS_SERVER', None)
REDIS_PORT = os.environ.get('REDIS_PORT', None)
REDIS_DB = os.environ.get('REDIS_DB', None)
 
# Twilio API credentials
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', 'AC014eb7304ef3ce9954e4dc457f736d45')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', '6cccbfafd3717dbe2691251b9d6375c5')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', '15085072546')
