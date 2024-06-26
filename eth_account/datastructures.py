from typing import (
    NamedTuple,
)

from hexbytes import (
    HexBytes,
)


def __getitem__(self, index):
    try:
        return tuple.__getitem__(self, index)
    except TypeError:
        return getattr(self, index)


class SignedTransaction(NamedTuple):
    raw_transaction: HexBytes
    hash: HexBytes
    r: int
    s: int
    v: int

    def __getitem__(self, index):
        return __getitem__(self, index)


class SignedMessage(NamedTuple):
    message_hash: HexBytes
    r: int
    s: int
    v: int
    signature: HexBytes

    def __getitem__(self, index):
        return __getitem__(self, index)
