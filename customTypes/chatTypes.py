from typing import TypeAlias
from typing import TypedDict
from datetime import datetime

class ChatMessage(TypedDict):
  sender: str
  content: str
  timestamp: datetime

class ChatType:
  def __init__(self, messages: list[ChatMessage], ownName: str, othersName: str) -> None:
    self.__messages: list[ChatMessage] = messages
    self.__ownName: str = ownName
    self.__othersName: str = othersName

Chats: TypeAlias = list[ChatType]