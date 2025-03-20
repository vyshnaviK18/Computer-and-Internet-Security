def rail_fence_encrypt(plaintext, rails):
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    row, step = 0, 1
    
    for i, char in enumerate(plaintext):
        fence[row][i] = char
        row += step
        if row == 0 or row == rails - 1:
            step = -step
    
    return ''.join(''.join(row) for row in fence)

def rail_fence_decrypt(ciphertext, rails):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    row, step = 0, 1
    
    for i in range(len(ciphertext)):
        fence[row][i] = '*'
        row += step
        if row == 0 or row == rails - 1:
            step = -step
    
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*' and index < len(ciphertext):
                fence[r][c] = ciphertext[index]
                index += 1
    
    plaintext = []
    row, step = 0, 1
    for i in range(len(ciphertext)):
        plaintext.append(fence[row][i])
        row += step
        if row == 0 or row == rails - 1:
            step = -step
    
    return ''.join(plaintext)

# Example usage
plaintext = "HELLO WORLD"
rails = 3
ciphertext = rail_fence_encrypt(plaintext.replace(" ", ""), rails)
decrypted_text = rail_fence_decrypt(ciphertext, rails)

print("Original Text:", plaintext)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
