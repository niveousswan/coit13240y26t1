def text_to_nums(text):
    nums = []
    for char in text:
        if char.isalpha():  # only process letters
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
