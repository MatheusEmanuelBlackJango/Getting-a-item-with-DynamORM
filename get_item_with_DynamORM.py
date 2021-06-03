# Marshmallow example
import os
from pprint import pprint
from dynamorm import DynaModel
from marshmallow import fields, validate, validates, ValidationError

class Thing(DynaModel):
    class Table:
        name = '-things'.format(env=os.environ.get('ENVIRONMENT', 'dev'))
        hash_key = 'id'
        read = 5
        write = 1

    class Schema:
        id = fields.String(required=True)
        name = fields.String()
        color = fields.String(validate=validate.OneOf(('purple', 'red', 'yellow')))
       
        @validates('name')
        def validate_name(self, value):
            if os.name.lower() == 'evan':
                raise ValidationError("No Evan's allowed")

    def say_hello(self):
        print("Hello.  {name} here.  My ID is {id} and I'm colored {color}".format(
        id=self.id,
        name=self.name,
        color=self.color
        ))

if __name__ == '__main__':
    things = Thing.get(id="id")
    if things:
        print("Get Table succeeded:")
        pprint(things.say_hello(), sort_dicts=False)

