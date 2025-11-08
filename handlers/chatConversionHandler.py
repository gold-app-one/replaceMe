from re import compile
from customTypes.chatTypes import ChatType, ChatMessage, Chats
from datetime import datetime
from customTypes.path import Path
from customTypes.platform import Platform
from helpers.pathHelper import getFilesPaths

class ChatConversionHandler:
  def __init__(self, folderPath: Path) -> None:
    self.__folderPath: Path = folderPath
  def getChats(self, path: Path, platform: Platform, ownName: str) -> Chats:
    chats: Chats = []
    for filePath in getFilesPaths(self.__folderPath):
      chat = self.getChat(filePath, platform, ownName)
      if chat:
        chats.append(chat)
    return chats
  def getChat(self, path: Path, platform: Platform, ownName: str) -> ChatType | None:
    chat: ChatType | None = None
    match platform:
      case Platform.WHATSAPP:
        chat = self.__txtPathToChat(path, Platform.WHATSAPP, ownName)
      case Platform.INSTAGRAM:
        pass # TODO: implement instagram chat conversion
      case Platform.DISCORD:
        pass # TODO: implement discord chat conversion
      case Platform.MAIL:
        pass # TODO: implement mail conversion

    return chat
  def __openTxt(self, path: Path, platform: Platform) -> list[str]:
    if platform == Platform.WHATSAPP:
      pattern = compile(r"^\d{1,2}\.\d{1,2}\.\d{2}, \d{1,2}:\d{2} - ")

      messages: list[str] = []
      currentMessage: list[str] = []

      with open(str(path), "r", encoding="utf-8") as file:
        for line in file:
          line = line.rstrip("\n")

          if pattern.match(line):
            if currentMessage:
              messages.append(" ".join(currentMessage))
              currentMessage = []
            currentMessage.append(line)
          else:
            if currentMessage:
              currentMessage.append(line)
            else:
              currentMessage = [line]

        if currentMessage:
          messages.append("\n".join(currentMessage))
      return messages
    else:
      return [] # HACK

  def __convertTimestamp(self, timeText: str) -> datetime:
    timestamp: datetime = datetime.strptime(timeText, "%d.%m.%y, %H:%M")
    return timestamp

  def __lineToMessage(self, line: str) -> ChatMessage:
    splitLineForTime = line.split(" - ", 1)

    timeStr: str = splitLineForTime[0]

    restStr: str = splitLineForTime[1] if len(splitLineForTime) > 1 else ''

    splitLineForSenderAndMessage: list[str] = restStr.split(": ", 1)

    senderStr: str = splitLineForSenderAndMessage[0]
    timestamp: datetime = self.__convertTimestamp(timeStr)
    messageStr: str = splitLineForSenderAndMessage[1] if len(splitLineForSenderAndMessage) > 1 else ''

    message: ChatMessage = {'sender': senderStr, 'timestamp': timestamp, 'content': messageStr}
    return message

  def __txtPathToChat(self, txtPath: Path, platform: Platform, ownName: str) -> ChatType:
    lines: list[str] = self.__openTxt(txtPath, platform)
    messages: list[ChatMessage] = []
    for line in lines:
      message = self.__lineToMessage(line)
      messages.append(message)
    othersName: str = 'Them' # FIXME
    return ChatType(messages=messages, ownName=ownName, othersName=othersName)