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
    def _get_insert_parameters(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_table(cls):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_dataclass(cls):
        raise NotImplementedError

    def get_id_field_name(self):
        """
        Get the ID field name (default `id`), override if necessary
        """
        return 'id'

    def insert(self, commit=False):
        """
        Insert the object model in database
        :param commit:
        :return:
        """
        sql, parameters = self._get_insert_parameters()
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
