import marshmallow as ma


class GroupSchema(ma.Schema):
    id = ma.fields.Integer(required=True, validate=lambda v: v > 0)
    people = ma.fields.Integer(required=True, validate=lambda v: 1 <= v <= 6)


class GroupIdSchema(ma.Schema):
    ID = ma.fields.Integer(required=True, validate=lambda v: v > 0)


class CarSchema(ma.Schema):
    id = ma.fields.Integer(required=True, validate=lambda v: v > 0)
    seats = ma.fields.Integer(required=True, validate=lambda v: 4 <= v <= 6)
