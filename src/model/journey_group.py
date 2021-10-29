from datetime import datetime

from src.model.base import Base


class JourneyGroup(Base):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.people = kwargs.get('people')
        self.created = kwargs.get('created', datetime.utcnow())
        self.car_id = kwargs.get('carId')
        self.registered = kwargs.get('registered')
        self.drop_off = kwargs.get('dropOff')

    @classmethod
    def get_table(cls):
        return 'JourneyGroup'

    def _get_insert_parameters(self):
        sql = f'insert into {self.get_table()} (id, people, created) values (?, ?, ?)'
        return sql, (self.id, self.people, self.created)

    def register(self, car_id):
        self.car_id = car_id
        self.registered = datetime.utcnow()

        sql = f'update {self.get_table()} set carId=?, registered=? where id=?'
        self._execute(sql, (self.car_id, self.registered, self.id), commit=True)

    def dropoff(self):
        self.car_id = None
        self.drop_off = datetime.utcnow()

        sql = f'update {self.get_table()} set carId=?, dropOff=? where id=?'
        self._execute(sql, (self.car_id, self.drop_off, self.id), commit=True)

    @classmethod
    def get_first_waiting(cls, available):
        sql = f'select * from {cls.get_table()} where people <= ? and registered is NULL order by created asc'
        cursor = cls._execute(sql, (available,))
        result = cursor.fetchone()
        return None if result is None else cls(**result)
