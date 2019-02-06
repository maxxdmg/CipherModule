import string

'''
Vigenere's Cipher methods
maxdmg 2/6/19
'''

def vigenere_encrypt(plaintext, key):
	encryption = ""
	for i in range(len(plaintext)):
		key_index = ord( key[i % len(key)] ) - 97
		plaintext_index = ord( plaintext[i] ) - 97
		encrypted_numeric = (key_index + plaintext_index) % 26
		encrypted_letter = chr(encrypted_numeric + 97)
		encryption += encrypted_letter
	return encryption

def vigenere_decrypt(encryption, key):
	decryption = ""
	for i in range(len(encryption)):
		key_index = ord( key[i % len(key)] ) - 97
		encryption_index = ord( encryption[i] ) - 97
		decrypted_numeric = (encryption_index - key_index + 26) % 26
		decrypted_letter = chr(decrypted_numeric + 97)
		decryption += decrypted_letter
	return decryption