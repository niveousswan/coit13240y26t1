# Import module that converts between English characters and numbers
import englishcipher 

# Caesar encrypt: input key and plaintext; output ciphertext
def encrypt(key, plaintext):
	# Convert plaintext text to numerical values in list
	plaintext_list = englishcipher.text_to_nums(plaintext)

	# initialise ciphertext list
	ciphertext_list = []

	# for each letter in the list, perform Caesar encrypt math
	for p in plaintext_list:
		c = (p + key) % 26 # Caesar encrypt operation
		ciphertext_list.append(c) # append ciphertext to list


	# convert ciphertext numerical values back to text
	ciphertext = englishcipher.nums_to_text(ciphertext_list)

	return ciphertext

def decrypt(key, ciphertext):
	ciphertext_list = englishcipher.text_to_nums(ciphertext)
	plaintext_list = []
	for c in ciphertext_list:
		p = (c - key) % 26
		plaintext_list.append(p)
	plaintext = englishcipher.nums_to_text(plaintext_list)
	return plaintext

# Test caesar encrypt
p1 = "belgium"
k1 = 9
c1 = encrypt(k1, p1)
print(p1)
print(k1)
print(c1)

c2 = "knuprdv"
k2 = 9
p2 = decrypt(k2, c2)
print(p2)
