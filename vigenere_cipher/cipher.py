"""Core Vigenere cipher logic."""

from typing import List


def _normalize_key(key: str) -> List[int]:
    """Converts a keyword into a list of shift offsets (0-25)."""
    cleaned = [k for k in key if k.isalpha()]
    if not cleaned:
        raise ValueError("Key must contain at least one alphabetic character.")
    return [ord(k.lower()) - ord("a") for k in cleaned]


def vigenere_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts plaintext using the Vigenere cipher.

    Args:
        plaintext: Text to encrypt.
        key: Alphabetic keyword (non-letters are ignored).

    Returns:
        Encrypted ciphertext.
    """
    shifts = _normalize_key(key)
    result = []
    j = 0
    for ch in plaintext:
        if ch.isalpha():
            shift = shifts[j % len(shifts)] # lặp lại key nếu key ngắn hơn plaintext
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base)) # dịch chuyển Caesar
            j += 1
        else:
            result.append(ch)
    return "".join(result)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts ciphertext using the Vigenere cipher.

    Args:
        ciphertext: Text to decrypt.
        key: Alphabetic keyword.

    Returns:
        Decrypted plaintext.
    """
    shifts = _normalize_key(key)
    result = []
    j = 0
    for ch in ciphertext:
        if ch.isalpha():
            shift = shifts[j % len(shifts)]
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base - shift) % 26 + base)) # dịch chuyển ngược Caesar
            j += 1
        else:
            result.append(ch)
    return "".join(result)
