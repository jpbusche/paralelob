from mongoengine import Document, StringField


class Adventure(Document):
    meta = {'collection': 'adventures'}
    name = StringField(required=True)

    def list_adventures():
        return Adventure.objects

    def get_adventure(_name):
        return Adventure.objects(name=_name).first()

    def create_adventure(_name):
        return Adventure(name=_name).save()