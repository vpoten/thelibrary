import marshmallow as ma


class BookSchema(ma.Schema):
    isbn = ma.fields.String(required=True)
    title = ma.fields.String(required=True)
    date_of_publication = ma.fields.Date(required=True)
    authors = ma.fields.List(ma.fields.Integer, required=True)
    categories = ma.fields.List(ma.fields.Integer, required=True)


class BookQueryArgsSchema(ma.Schema):
    # TODO
    pass


class AuthorSchema(ma.Schema):
    id = ma.fields.Integer(required=True)
    name = ma.fields.String(required=True)
    date_of_birth = ma.fields.Date()


class AuthorQueryArgsSchema(ma.Schema):
    # TODO
    pass


class CategorySchema(ma.Schema):
    id = ma.fields.Integer(required=True)
    name = ma.fields.String(required=True)


class CategoryQueryArgsSchema(ma.Schema):
    # TODO
    pass
