# Character Encoding

Character encoding is a system that maps **characters** (letters, digits, symbols, emojis) to **numeric values**, allowing computers to store and transmit text.  
Not all encoding standards support non-English characters, which is crucial for **internationalization**.

---

## Popular Character Encoding Standards

### ASCII
- **Size**: 7 bits → 2⁷ = 128 characters  
- **Coverage**: Only English characters, digits, and basic symbols — **not suitable for internationalization**  
- **Types of characters**:
  - **Printable**: Uppercase and lowercase letters, digits, punctuation marks  
  - **Control**: 33 non-printable characters that manage device functions (e.g., carriage return, bell)  

**Example:**
| Character | Decimal | Binary   |
|-----------|---------|----------|
| `'A'`     | 65      | 01000001 |
| `'a'`     | 97      | 01100001 |

---

### Unicode
- **Purpose**: Designed to represent **all characters from all languages**, plus emojis and symbols.  
- **Coverage**: Over **1.1 million code points** (0–0x10FFFF)  
- **Representation**: Uses **code points** (numeric values) like `U+0041` for `'A'` or `U+1F600` for 😀  
- **Encodings**: Unicode itself is a character set; encodings like **UTF-8, UTF-16, UTF-32** define how to store these code points as bytes.

---

### UTF-8 (Unicode Transformation Format – 8-bit)
- **Variable-length encoding**: 1–4 bytes per character  
- **Backward compatible with ASCII**: ASCII characters use 1 byte in UTF-8  
- **Efficient for internationalization**: Handles emojis, accented characters, and non-Latin scripts seamlessly  

**Byte usage by character range:**
| Unicode Range        | UTF-8 Bytes | Example |
|---------------------|------------|---------|
| U+0000 – U+007F      | 1 byte     | `'A'` |
| U+0080 – U+07FF      | 2 bytes    | `'ñ'` |
| U+0800 – U+FFFF      | 3 bytes    | `'ह'` |
| U+10000 – U+10FFFF   | 4 bytes    | `'😀'` |

---

## Key Takeaways
1. **ASCII** → 7-bit, English-only, limited coverage.  
2. **Unicode** → Universal character set for all languages and symbols.  
3. **UTF-8** → The most common Unicode encoding, variable-length, ASCII-compatible, and ideal for modern applications.  

---

### References / Further Reading
- [Unicode Consortium](https://home.unicode.org/)  
- [UTF-8 on Wikipedia](https://en.wikipedia.org/wiki/UTF-8)  
- [Python `str.encode()` Documentation](https://docs.python.org/3/library/stdtypes.html#str.encode)
