from abc import abstractmethod

import src.db.manager_db as manager_db


class Base(object):

    @classmethod
    def clear_table(cls):
        sql = f'DELETE FROM {cls.get_table()};\nVACUUM;'
        cls._executescript(sql, commit=True)

    @classmethod
    def _execute(cls, sql, parameters=None, commit=False):
        db = manager_db.get_db()
        if parameters is None:
            cursor = db.execute(sql)
        else:
            cursor = db.execute(sql, parameters)
        if commit is True:
            db.commit()
        return cursor

    @classmethod
    def _executemany(cls, sql, parameters=None, commit=False):
        db = manager_db.get_db()
        if parameters is None:
            db.executemany(sql)
        else:
            db.executemany(sql, parameters)
        if commit is True:
            db.commit()

    @classmethod
    def _executescript(cls, sql_script, commit=False):
        db = manager_db.get_db()
        db.executescript(sql_script)
        if commit is True:
            db.commit()

    @classmethod
    def commit(cls):
        db = manager_db.get_db()
        db.commit()

    @abstractmethod
    def _get_insert_parameters(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_table(cls):
        raise NotImplementedError

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

    @classmethod
    def get_by_id(cls, item_id):
        sql = f'select * from {cls.get_table()} where id = ?'
        cursor = cls._execute(sql, (item_id,))
        result = cursor.fetchone()
        return None if result is None else cls(**result)

    @classmethod
    def count_rows(cls):
        sql = f'select count(*) as total from {cls.get_table()}'
        cursor = cls._execute(sql)
        result = cursor.fetchone()
        return None if result is None else result['total']
