from typing import TypeAlias

JSONPrimitive: TypeAlias = str | int | float | bool | None

JSONItem: TypeAlias = JSONPrimitive | dict[str, "JSONItem"] | list["JSONItem"]

JSONDict: TypeAlias = dict[str, JSONItem]

JSONList: TypeAlias = list[JSONItem]

JSONType: TypeAlias = JSONDict | JSONList