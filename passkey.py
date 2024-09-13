import string
import random
def build_passkey(length):
    if length < 6:
        raise ValueError("Passkey length should be at least 6 or more to include all character types.")

    ll= string.ascii_lowercase
    ul= string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation 

    passkey = [
        random.choice(ll),
        random.choice(ul),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_characters = ll+ ul+ digits + special_chars
    passkey += [random.choice(all_characters) for _ in range(length - 6)]

    random.shuffle(passkey)
    return ''.join(passkey)

def main():
    try:
        length = int(input("Enter the desired length of the passkey:"))

        passkey = build_passkey(length)
        print("Generated Passkey:", passkey)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
