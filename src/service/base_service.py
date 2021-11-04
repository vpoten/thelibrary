from src.repository.base_repository import BaseRepository


class BaseService(object):
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def create(self, data):
        return self.repository.insert(self.repository.get_dataclass()(**data), True)

    def retrieve(self, item_id):
        return self.repository.get_by_id(item_id)

    def update(self, item_id, data):
        entity = self.repository.get_dataclass()(**data)
        # force entity id
        setattr(entity, self.repository.get_id_field_name(), item_id)
        self.repository.update(entity, True)
        return self.retrieve(item_id)

    def list(self, page=0, rows_per_page=100):
        return self.repository.list(page=page, rows_per_page=rows_per_page)

    def delete(self, item_id):
        self.repository.delete_by_id(item_id, True)
