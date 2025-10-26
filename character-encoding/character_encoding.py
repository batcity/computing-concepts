def bytes_to_binary(b):
    """Return a space-separated string of the binary representation of a bytes object."""
    return ' '.join(f'{byte:08b}' for byte in b)

# --- ASCII character example ---
ascii_char = 'a'
print(f"Character: {ascii_char}")
print(f"Unicode code point: {ord(ascii_char)}")

# Encode as ASCII
ascii_bytes = ascii_char.encode('ascii')
print(f"ASCII encoding: {ascii_bytes} (binary: {bytes_to_binary(ascii_bytes)})")

# Encode as UTF-8 (backward compatible with ASCII)
utf8_bytes = ascii_char.encode('utf-8')
print(f"UTF-8 encoding: {utf8_bytes} (binary: {bytes_to_binary(utf8_bytes)})")

print("\n--- Non-ASCII character example ---")
non_ascii_char = 'ñ'
print(f"Character: {non_ascii_char}")
print(f"Unicode code point: {ord(non_ascii_char)}")

# Encode as ASCII (will fail)
try:
    non_ascii_char.encode('ascii')
except UnicodeEncodeError:
    print("ASCII cannot encode this character")

# Encode as UTF-8
utf8_bytes = non_ascii_char.encode('utf-8')
print(f"UTF-8 encoding: {utf8_bytes} (binary: {bytes_to_binary(utf8_bytes)})")

print("\n--- Emoji example ---")
emoji_char = '😀'
print(f"Character: {emoji_char}")
print(f"Unicode code point: {ord(emoji_char)}")

# Encode as UTF-8
utf8_bytes = emoji_char.encode('utf-8')
print(f"UTF-8 encoding: {utf8_bytes} (binary: {bytes_to_binary(utf8_bytes)})")