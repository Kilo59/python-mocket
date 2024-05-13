from __future__ import annotations

import codecs
import os
import shlex
from typing import Final

ENCODING: Final[str] = os.getenv("MOCKET_ENCODING", "utf-8")

text_type = str
byte_type = bytes
basestring = (str,)


def encode_to_bytes(s: str | bytes, encoding: str = ENCODING) -> bytes:
    if isinstance(s, text_type):
        s = s.encode(encoding)
    return byte_type(s)


def decode_from_bytes(s: str | bytes, encoding: str = ENCODING) -> str:
    if isinstance(s, byte_type):
        s = codecs.decode(s, encoding, "ignore")
    return text_type(s)


def shsplit(s: str | bytes) -> list[str]:
    s = decode_from_bytes(s)
    return shlex.split(s)


def do_the_magic(lib_magic, body):  # pragma: no cover
    if hasattr(lib_magic, "from_buffer"):
        # PyPI python-magic
        return lib_magic.from_buffer(body, mime=True)
    # file's builtin python wrapper
    # used by https://www.archlinux.org/packages/community/any/python-mocket/
    _magic = lib_magic.open(lib_magic.MAGIC_MIME_TYPE)
    _magic.load()
    return _magic.buffer(body)
