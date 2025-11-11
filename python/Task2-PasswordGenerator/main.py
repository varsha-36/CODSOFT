# CODSOFT – Python Task 2: Password Generator
# Uses cryptographically secure randomness (secrets)

import string
import secrets

SIMILAR = set("Il1O0")
AMBIGUOUS = set("{}[]()/\\'\"`~,;:.<>")

def build_charset(use_lower=True, use_upper=True, use_digits=True, use_symbols=True,
                  exclude_similar=True, exclude_ambiguous=True):
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*_-+=?:"
    # remove confusing characters
    if exclude_similar:
        chars = "".join(c for c in chars if c not in SIMILAR)
    if exclude_ambiguous:
        chars = "".join(c for c in chars if c not in AMBIGUOUS)
    return chars

def generate_password(length=12, **opts):
    if length < 4:
        raise ValueError("Length must be at least 4")
    charset = build_charset(**opts)
    if not charset:
        raise ValueError("No characters available. Enable at least one set.")
    return "".join(secrets.choice(charset) for _ in range(length))

def yes_no(prompt, default=True):
    d = "Y/n" if default else "y/N"
    ans = input(f"{prompt} ({d}): ").strip().lower()
    if not ans:
        return default
    return ans in {"y", "yes"}

def get_int(prompt, default):
    raw = input(f"{prompt} [{default}]: ").strip()
    if not raw:
        return default
    try:
        n = int(raw)
        return n
    except ValueError:
        print("Please enter a number.")
        return get_int(prompt, default)

def main():
    print("=== CODSOFT | Task 2: Password Generator ===")
    length = get_int("Password length", 12)

    use_lower = yes_no("Include lowercase (a-z)?", True)
    use_upper = yes_no("Include uppercase (A-Z)?", True)
    use_digits = yes_no("Include digits (0-9)?", True)
    use_symbols = yes_no("Include symbols (!@#$...)?", True)
    exclude_similar = yes_no("Exclude similar characters (I, l, 1, O, 0)?", True)
    exclude_ambiguous = yes_no("Exclude ambiguous symbols ({ } [ ] / \\ etc.)?", True)

    try:
        pwd = generate_password(
            length=length,
            use_lower=use_lower,
            use_upper=use_upper,
            use_digits=use_digits,
            use_symbols=use_symbols,
            exclude_similar=exclude_similar,
            exclude_ambiguous=exclude_ambiguous,
        )
    except ValueError as e:
        print("Error:", e)
        return

    print("\nYour password:\n", pwd)
    print("\nTip: Run again to generate a different password.")

if __name__ == "__main__":
    main()
