from typing import Callable
from constants.paths import WHATSAPP_CHATS_PATH
from customTypes.chatTypes import ChatType, Chats
from customTypes.platform import Platform
from handlers.chatConversionHandler import ChatConversionHandler

class ChatsHandler:
  def __init__(self, nameList: dict[Platform, str]) -> None:
    self.__chats: list[ChatType] = []
    self.__conversion: ChatConversionHandler = ChatConversionHandler(WHATSAPP_CHATS_PATH)
    getChatFunctions: dict[Platform, Callable[[str], Chats]] = {
      Platform.WHATSAPP: self.__getWhatsAppChats
    }
    for platform, getChats in getChatFunctions.items():
      ownName: str = nameList[platform]
      self.__chats.extend(getChats(ownName))

  def __getWhatsAppChats(self, ownName: str) -> Chats:
    whatsappChats: Chats = []
    self.__conversion.getChats(WHATSAPP_CHATS_PATH, Platform.WHATSAPP, ownName)
    return whatsappChats