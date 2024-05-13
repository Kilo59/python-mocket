from __future__ import annotations

import typing

___all__ = ["SupportsRead"]


@typing.runtime_checkable
class SupportsRead(typing.Protocol):
    def read(self) -> bytes: ...
