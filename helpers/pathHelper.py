from customTypes.path import Path
import os


def getFilesPaths(path: Path, fileExtensionWhitelist: list[str] | None = None) -> list[Path]:
  files: list[Path] = []
  for entry in os.listdir(str(path)):
    fullPath: Path = path + entry
    if os.path.isfile(str(fullPath)):
      if fileExtensionWhitelist is None or fullPath.getSuffix() in fileExtensionWhitelist:
        files.append(fullPath)
  return files