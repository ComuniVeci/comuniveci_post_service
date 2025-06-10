import mongoengine as me
from datetime import datetime

class Post(me.Document):
    title = me.StringField(required=True, max_length=200)
    description = me.StringField()
    latitude = me.FloatField()
    longitude = me.FloatField()
    address = me.StringField()
    contact_email = me.EmailField()
    images = me.ListField(me.URLField())
    is_approved = me.BooleanField(default=False)
    created_at = me.DateTimeField(default=datetime.utcnow)
