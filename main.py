import fileinput
import re
import json
import base64
import zlib


def int_to_char(i: int) -> str:
    pos = i + 45
    return chr(pos)


def decode_decimal_encoding(data: str) -> str:
    pairs = re.findall('[0-9]{2}', data)
    ints = map(int, pairs)
    chars = map(int_to_char, ints)
    return ''.join(chars)


def decode_header(head: str) -> dict:
    decoded = base64.urlsafe_b64decode(f'{head}==')
    return json.loads(decoded)


def decode_body(head: dict, body: str) -> dict:
    body_bytes = base64.urlsafe_b64decode(f'{body}==')
    zip_head = head['zip']
    if zip_head != 'DEF':
        raise ValueError(f'Expected "zip" header to be "DEF": {zip_head}')
    json_body = zlib.decompress(body_bytes, -15)
    return json.loads(json_body)


def decode_smart_health_card(data: str):
    jwt = decode_decimal_encoding(data)
    parts = jwt.split('.')
    head = decode_header(parts[0])
    print('Head:')
    print(json.dumps(head, indent=2, sort_keys=True))
    body = decode_body(head, parts[1])
    print('Body:')
    print(json.dumps(body, indent=2, sort_keys=True))
    sign = parts[2]
    print(f'Sign: {sign}')


if __name__ == '__main__':
    decode_smart_health_card(fileinput.input().readline())
