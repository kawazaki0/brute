from abc import ABC
from abc import abstractmethod


class Game(ABC):
  def __init__(self, init):
    pass

  @abstractmethod
  def clone(self):
    pass

  @abstractmethod
  def move(self, op):
    pass

  @abstractmethod
  def completed(self):
    pass

