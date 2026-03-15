# englishcipher.py
# Module for converting between English letters and numbers

# Convert a string of letters into a list of numbers (0 = a, 25 = z)
def text_to_nums(text):
    nums = []
    for char in text:
        if char.isalpha():  # only process letters
            nums.append(ord(char.lower()) - ord('a'))
    return nums

# Convert a list of numbers back into letters
def nums_to_text(nums):
    text = ""
    for n in nums:
        # ensure the number is within 0-25
        n_mod = n % 26
        text += chr(n_mod + ord('a'))
    return text

# Optional: Caesar cipher helper for single letter
def shift_letter(letter, key):
    if not letter.isalpha():
        return letter
    num = ord(letter.lower()) - ord('a')
    shifted = (num + key) % 26
    return chr(shifted + ord('a'))

# Optional: Encrypt text with Caesar cipher directly
def caesar_encrypt(text, key):
    result = ""
    for c in text:
        result += shift_letter(c, key)
    return result

# Optional: Decrypt text with Caesar cipher directly
def caesar_decrypt(text, key):
    result = ""
    for c in text:
        result += shift_letter(c, -key)
    return result

# Example usage when run directly
if __name__ == "__main__":
    test_text = "BelGium"
    key = 9

    nums = text_to_nums(test_text)
    print("Text to numbers:", nums)

    back_to_text = nums_to_text(nums)
    print("Numbers to text:", back_to_text)

    encrypted = caesar_encrypt(test_text, key)
    print("Caesar encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, key)
    print("Caesar decrypted:", decrypted)
