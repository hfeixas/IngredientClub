import mongoengine as mongo

db = mongo.connect(
    'test', # This will be the name of your database
    host='192.168.1.14',
    port=27017,
    username='user',
    password='pass'
)