from datetime import datetime

from src.model.base import Base


class Car(Base):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.seats = kwargs.get('seats')
        self.created = kwargs.get('created', datetime.utcnow())
        self.available = kwargs.get('available', self.seats)

    @classmethod
    def insert_many(cls, cars: list):
        """
        Insert many cars in database
        :param cars: list of cars
        :return:
        """
        if len(cars) == 0:
            return
        insert_sql = f'insert into {cls.get_table()} (id, seats, available, created) values (?, ?, ?, ?)'
        created = datetime.utcnow()
        parameters = [(car['id'], car['seats'], car['seats'], created) for car in cars]
        cls._executemany(insert_sql, parameters)
        cls.commit()

    @classmethod
    def get_table(cls):
        return 'Car'

    def _get_insert_parameters(self):
        sql = f'insert into {self.get_table()} (id, seats, available, created) values (?, ?, ?, ?)'
        return sql, (self.id, self.seats, self.available, self.created)

    @classmethod
    def get_by_availability(cls, people: int):
        """
        Get the first car with enough room for the requested number of people
        :param people: {int}
        :return: a Car instance or None
        """
        sql = f'select * from {cls.get_table()} where available >= ?'
        cursor = cls._execute(sql, (people,))
        result = cursor.fetchone()
        return None if result is None else Car(**result)

    def update_availability(self, amount: int):
        """
        Update the availability of a car
        :param amount: {int} value to add/decrease
        :return:
        """
        self.available += amount
        sql = f'update {self.get_table()} set available=? where id=?'
        self._execute(sql, (self.available, self.id), commit=True)
