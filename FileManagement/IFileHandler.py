from abc import ABCMeta, abstractmethod


class IFileHandler:
    __metaclass__ = ABCMeta

    @abstractmethod
    def load_file(self, file): raise NotImplementedError

    @abstractmethod
    def write_file(self, file, data): raise NotImplementedError

    @abstractmethod
    def validate_data(self, data): raise NotImplementedError

    @abstractmethod
    def pack_pickle(self, graphs): raise NotImplementedError

    @abstractmethod
    def unpack_pickle(self, file): raise NotImplementedError

    @abstractmethod
    def pickle_all(self, data): raise NotImplementedError
