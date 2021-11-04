import marshmallow as ma

"""
Schemas for serialization/deserialization/validation of REST API endpoint input and output
"""


class BaseListQueryArgsSchema(ma.Schema):
    """
    Base schema for list operations
    """
    page = ma.fields.Integer(missing=0, validate=lambda v: v >= 0)
    rows_per_page = ma.fields.Integer(missing=50, validate=lambda v: 1 <= v <= 200)


class BookSchema(ma.Schema):
    id = ma.fields.Integer(dump_only=True)
    isbn = ma.fields.String(required=True)
    title = ma.fields.String(required=True)
    date_of_publication = ma.fields.Date(required=True)
    created = ma.fields.DateTime(dump_only=True)


class BooksQueryArgsSchema(BaseListQueryArgsSchema):
    pass


class AuthorSchema(ma.Schema):
    id = ma.fields.Integer(dump_only=True)
    name = ma.fields.String(required=True)
    date_of_birth = ma.fields.Date(required=True)
    created = ma.fields.DateTime(dump_only=True)


class AuthorsQueryArgsSchema(BaseListQueryArgsSchema):
    isbn = ma.fields.String(description="Filter authors by book id")


class CategorySchema(ma.Schema):
    id = ma.fields.Integer(dump_only=True)
    name = ma.fields.String(required=True)
    created = ma.fields.DateTime(dump_only=True)


class CategoriesQueryArgsSchema(BaseListQueryArgsSchema):
    isbn = ma.fields.String(description="Filter categories by book id")
