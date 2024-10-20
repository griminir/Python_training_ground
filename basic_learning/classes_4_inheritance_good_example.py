# abc = abstract base class
from abc import ABC, abstractmethod


# good example use of inheritance
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed')
        self.opened = False

    # making a method abstract means each class that inherits from this clas needs to implement it
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('reading data from a file')


class NetworkStream(Stream):
    def read(self):
        print('reading data from a network')


class MemoryStream(Stream):
    def read(self):
        print('reading data from a memory stream')


stream = MemoryStream()
