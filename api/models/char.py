from mongoengine import Document, StringField, IntField, ReferenceField

from models.user import User


class Char(Document):
    meta = {'collection': 'chars'}
    name = StringField(required=True, max_length=20)
    attribute = IntField(required=True, min_value=2, max_value=5)
    user = ReferenceField(User)
    adventure = StringField(required=True)
    color = StringField(required=True)

    def create_char(data, _user, _adventure):
        if data.get('is_npc', False):
            return Char(name=data['name'], attribute=data['attribute'], user=_user,
                        adventure=_adventure, color='#000000').save()
        return Char(name=data['name'], attribute=data['attribute'], user=_user,
                    adventure=_adventure, color=data['color']).save()

    
    def get_char(_name, _adventure):
        return Char.objects(name=_name, adventure=_adventure).first()

    def list_char_user(_user):
        return Char.objects(user=_user)
