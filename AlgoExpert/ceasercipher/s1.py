def caesarCipherEncryptor(string, key):
    # Write your code here.
	cipher_text = []
	newKey = key % 26
	print(newKey)
    for i in range(len(string)):
		if ord(string[i])+newKey <= ord('z'):
			cipher_text.append(chr(ord(string[i])+newKey))
		else:
			newLetter = ord(string[i])+key
			cipher_text.append(chr(96+newLetter%122))
		
	return "".join(cipher_text)
