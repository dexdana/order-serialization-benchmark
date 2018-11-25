from pickle import dumps as pickle_dumps
from json import dumps as json_dumps
from rapidjson import dumps as rapidjson_dumps
from eth_abi import encode_abi

from hexbytes.main import HexBytes

ORDER = [
    "0x8d12a197cb00d4747a1fe03395095ce2a5cc6819",  # contractAddress: Address,
    "0x0000000000000000000000000000000000000000",  # tokenGet: Address,
    390954796113878994,  # amountGet: int,
    "0x12b306fa98f4cbb8d4457fdff3a0a0a56f07ccdf",  # tokenGive: Address,
    200489639032758458461,  # amountGive: int,
    6787057,  # expires: int,
    1061676627,  # nonce: int,
    "0xf8536CA7a25CBF70DF754fA310079aDa4c6114C2",  # user: Address,
    27,  # v: int,
    "0x34ed0a28bb3c0a6f57d22327b2f20cbbb715958886563f8e321ae7a52314008e",  # r: bytes,
    "0x02625bed4feb95f86168412cb38a65a133225ba90518fd0368ffb09830500c4f"  # s: bytes
]

ORDER_KEYS = [
    "contractAddress", "tokenGet", "amountGet", "tokenGive", "amountGive",
    "expires", "nonce", "user", "v", "r", "s"
]
ORDER_HASH = {k: ORDER[idx] for (idx, k) in enumerate(ORDER_KEYS)}

ORDER_WITH_BYTES = [
    "0x8d12a197cb00d4747a1fe03395095ce2a5cc6819",  # contractAddress: Address,
    "0x0000000000000000000000000000000000000000",  # tokenGet: Address,
    390954796113878994,  # amountGet: int,
    "0x12b306fa98f4cbb8d4457fdff3a0a0a56f07ccdf",  # tokenGive: Address,
    200489639032758458461,  # amountGive: int,
    6787057,  # expires: int,
    1061676627,  # nonce: int,
    "0xf8536CA7a25CBF70DF754fA310079aDa4c6114C2",  # user: Address,
    27,  # v: int,
    b"4\xed\n(\xbb<\noW\xd2#'\xb2\xf2\x0c\xbb\xb7\x15\x95\x88\x86V?\x8e2\x1a\xe7\xa5#\x14\x00\x8e",  # r: bytes,
    b'\x02b[\xedO\xeb\x95\xf8ahA,\xb3\x8ae\xa13"[\xa9\x05\x18\xfd\x03h\xff\xb0\x980P\x0cO'  # s: bytes
]

ORDER_ABI = [
    'address',
    'address',
    'uint',
    'address',
    'uint',
    'uint',
    'uint',
    'address',
    'uint8',
    'bytes32',
    'bytes32',
]


def test_serialize_pickle(benchmark):
    print(benchmark(pickle_dumps, ORDER))


def test_serialize_pickle_with_keys(benchmark):
    print(benchmark(pickle_dumps, ORDER_HASH))


def test_serialize_json(benchmark):
    print(benchmark(json_dumps, ORDER))


def test_serialize_json_with_keys(benchmark):
    print(benchmark(json_dumps, ORDER_HASH))


def test_serialize_rapidjson(benchmark):
    print(benchmark(rapidjson_dumps, ORDER))


def test_serialize_rapidjson_with_keys(benchmark):
    print(benchmark(rapidjson_dumps, ORDER_HASH))


def test_serialize_ethabi(benchmark):
    print(benchmark(encode_abi, ORDER_ABI, ORDER_WITH_BYTES))
