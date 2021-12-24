from mongoengine import Document, StringField, ListField, DateTimeField, IntField, BooleanField, EmbeddedDocument, EmbeddedDocumentField
from datetime import datetime


class Result(EmbeddedDocument):
    result = IntField(min_value=1, max_value=6)
    success = StringField(required=True)

    def create_result(_result, _success):
        return Result(result=_result, success=_success)

class Roll(Document):
    meta = {'collection': 'rolls'}
    results = ListField(EmbeddedDocumentField(Result), required=True)
    adventure = StringField(required=True)
    char_name = StringField(required=True, max_length=20)
    created = DateTimeField(default=datetime.now())

    def create_roll(_results, _adventure, _char_name):
        return Roll(results=_results, adventure=_adventure, char_name=_char_name).save()
    
    def list_rolls_adventure(_adventure):
        return Roll.objects(adventure=_adventure)