from __future__ import annotations

def find_all_occurrences(text: str, pattern: str) -> list[int]:
    """Return all starting indices where pattern appears in text."""
    if not pattern:
        return list(range(len(text) + 1))

    text_len = len(text)
    pattern_len = len(pattern)
    if pattern_len > text_len:
        return []

    matches: list[int] = []
    for start in range(text_len - pattern_len + 1):
        for offset in range(pattern_len):
            if text[start + offset] != pattern[offset]:
                break
        else:
            matches.append(start)
    return matches


if __name__ == '__main__':
    examples = [
        ('abcabcabc', 'abc'),
        ('aaaaa', 'aa'),
        ('hello', 'xyz'),
    ]

    for text, pattern in examples:
        print(f'find_all_occurrences({text!r}, {pattern!r}) -> {find_all_occurrences(text, pattern)}')
