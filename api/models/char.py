from mongoengine import Document, StringField, IntField, ReferenceField

from models.user import User


class Char(Document):
    meta = {'collection': 'chars'}
    name = StringField(required=True, max_length=20)
    attribute = IntField(required=True, min_value=2, max_value=5)
    user = ReferenceField(User)
    adventure = StringField(required=True)

    def create_char(_name, _attribute, _user, _adventure):
        return Char(name=_name, attribute=_attribute, user=_user,
                    adventure=_adventure).save()
    
    def get_char(_name, _user, _adventure):
        return Char.objects(name=_name, user=_user, adventure=_adventure).first()

    def list_char_user(_user):
        return Char.objects(user=_user)

