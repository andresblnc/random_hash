import secrets

def find_hash_with_leading_zeros():
	for i in range(1000):
		hash_str = secrets.token_hex(16)
		if hash_str.startswith('00'):
			print(f"Found hash after {i+1} tries: {hash_str}")
			return True
	print("No hash starting with two zeros found in 1000 tries.")
	return False


find_hash_with_leading_zeros()