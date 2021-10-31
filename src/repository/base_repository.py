from abc import abstractmethod

import src.db.manager_db as manager_db


class BaseRepository(object):

    def __init__(self, db=None):
        self._db = manager_db.get_db() if db is None else db

    def get_db(self):
        return self._db

    def clear_table(self):
        sql = f'DELETE FROM {self.get_table()};\nVACUUM;'
        self._executescript(sql, commit=True)

    def _execute(self, sql, parameters=None, commit=False):
        db = self.get_db()
        if parameters is None:
            cursor = db.execute(sql)
        else:
            cursor = db.execute(sql, parameters)
        if commit is True:
            db.commit()
        return cursor

    def _executemany(self, sql, parameters=None, commit=False):
        db = self.get_db()
        if parameters is None:
            db.executemany(sql)
        else:
            db.executemany(sql, parameters)
        if commit is True:
            db.commit()

    def _executescript(self, sql_script, commit=False):
        db = self.get_db()
        db.executescript(sql_script)
        if commit is True:
            db.commit()

    def commit(self):
        db = self.get_db()
        db.commit()

    @abstractmethod
    def _get_insert_parameters(self, entity):
        """
        Build a tuple with the sql query for insertion and the column values to insert
        :param entity:
        :return: a pair tuple (insert_sql, values)
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_table(cls):
        """
        Get table name, to override
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_dataclass(cls):
        """
        Get repository entity class, to override
        """
        raise NotImplementedError

    def get_id_field_name(self):
        """
        Get the ID field name (default `id`), override if necessary
        """
        return 'id'

    def insert(self, entity, commit=False):
        """
        Insert the object model in database
        :param entity: a `@dataclass` entity
        :param commit:
        :return:
        """
        sql, parameters = self._get_insert_parameters(entity)
        self._execute(sql, parameters)
        if commit is True:
            self.commit()

    def get_by_id(self, item_id):
        """
        Get an entity by its id
        :param item_id:
        :return:
        """
        sql = f'select * from {self.get_table()} where {self.get_id_field_name()} = ?'
        cursor = self._execute(sql, (item_id,))
        result = cursor.fetchone()
        return None if result is None else self.get_dataclass()(**result)

    def delete_by_id(self, item_id):
        """
        Delete an entity by its id
        :param item_id:
        :return:
        """
        sql = f'delete from {self.get_table()} where {self.get_id_field_name()} = ?'
        self._execute(sql, (item_id,))

    def count_rows(self):
        """
        Count rows in table
        :return: {int}
        """
        sql = f'select count(*) as total from {self.get_table()}'
        cursor = self._execute(sql)
        result = cursor.fetchone()
        return None if result is None else result['total']

    def list(self, page=0, rows_per_page=100):
        """
        List entities with pagination
        :param page: page to retrieve, zero indexed
        :param rows_per_page: rows per page
        :return: list of instances of class `self.get_dataclass()`
        """
        if rows_per_page == -1:
            sql = f'select * from {self.get_table()}'
        else:
            sql = f'select * from {self.get_table()} limit {rows_per_page} offset {page * rows_per_page}'

        cursor = self._execute(sql)
        items = [self.get_dataclass()(**row) for row in cursor]
        return items
