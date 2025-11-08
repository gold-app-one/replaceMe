import os

class Path:
  PATH_SEPERATOR: str = '/'
  def __init__(self, path: str) -> None:
    self.__path: str = path
  def getPath(self) -> str:
    return self.__path
  def __sanitizePath(self, path: str) -> str:
    return path.strip(' '+Path.PATH_SEPERATOR)
  def getSuffix(self) -> str:
    return os.path.splitext(self.__path)[1]
  def __add__(self, other: "Path | str") -> "Path":
    path1: str = self.__sanitizePath(self.getPath())
    path2: str = self.__sanitizePath(other.getPath() if isinstance(other, Path) else other)
    return Path(path1 + Path.PATH_SEPERATOR + path2)
  def __str__(self) -> str:
    return self.__path