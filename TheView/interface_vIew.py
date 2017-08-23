from abc import ABCMeta, abstractmethod


class IView:
    __metaclass__ = ABCMeta

    @abstractmethod
    def say(self, message): raise NotImplementedError
