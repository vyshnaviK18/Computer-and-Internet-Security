import numpy as np

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def hill_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext_numbers = text_to_numbers(plaintext)
    
    while len(plaintext_numbers) % n != 0:
        plaintext_numbers.append(0)  # Padding with 'A'
    
    plaintext_matrix = np.array(plaintext_numbers).reshape(-1, n)
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    ciphertext = numbers_to_text(ciphertext_matrix.flatten())
    
    return ciphertext

def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * adjugate) % modulus

def hill_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    ciphertext_numbers = text_to_numbers(ciphertext)
    ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, n)
    key_inverse = mod_inverse(key_matrix, 26)
    
    decrypted_matrix = np.dot(ciphertext_matrix, key_inverse) % 26
    plaintext = numbers_to_text(decrypted_matrix.flatten())
    
    return plaintext

# Example usage
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
plaintext = "ACT"
ciphertext = hill_encrypt(plaintext, key_matrix)
decrypted_text = hill_decrypt(ciphertext, key_matrix)

print("Original Text:", plaintext)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
