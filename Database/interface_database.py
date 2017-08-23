# KRIS LITTLE

from abc import ABCMeta, abstractmethod


class IDatabase:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute_sql(self, sql): raise NotImplementedError

    @abstractmethod
    def close_connection(self): raise NotImplementedError

    @abstractmethod
    def commit(self): raise NotImplementedError

    @abstractmethod
    def setup(self): raise NotImplementedError

    @abstractmethod
    def reset(self): raise NotImplementedError

    @abstractmethod
    def display_data(self): raise NotImplementedError

    @abstractmethod
    def write_to_database(self, data): raise NotImplementedError

    @abstractmethod
    def backup_database(self): raise NotImplementedError
