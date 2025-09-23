class BlockTranspositionCipher:
    def __init__(self, text, key, decrypt=False):
        self.text = str(text) if text is not None else ""
        self.decrypt = bool(decrypt)
        self.key = self._validate_key(key)
        self.key_order = self._get_key_order()
        self.block_size = len(self.key)
        self.current_index = 0

    def _validate_key(self, key):
        if key is None:
            raise ValueError("Ключ не может быть None")

        if not isinstance(key, str):
            try:
                key = str(key)
            except:
                raise ValueError("Ключ должен быть строкой")

        if not key:
            raise ValueError("Ключ не может быть пустой строкой")

        key_lower = key.lower()

        for char in key_lower:
            if not 'a' <= char <= 'z':
                raise ValueError(f"Ключ должен содержать только английские буквы. Невалидный символ: '{char}'")

        if len(set(key_lower)) != len(key_lower):
            raise ValueError("Все символы в ключе должны быть уникальными (регистр не учитывается)")

        return key_lower

    def _get_key_order(self):
        char_positions = [(char, idx) for idx, char in enumerate(self.key)]

        sorted_chars = sorted(char_positions, key=lambda x: x[0])

        order_mapping = {}
        for new_pos, (char, orig_pos) in enumerate(sorted_chars):
            order_mapping[orig_pos] = new_pos

        if self.decrypt:
            decrypt_order = [0] * len(self.key)
            for orig_pos, new_pos in order_mapping.items():
                decrypt_order[new_pos] = orig_pos
            return decrypt_order
        else:
            return [order_mapping[i] for i in range(len(self.key))]

    def _process_block(self, block):
        if len(block) < self.block_size:
            block += ' ' * (self.block_size - len(block))

        if self.decrypt:
            result = [''] * self.block_size
            for new_pos, orig_pos in enumerate(self.key_order):
                if new_pos < len(block):
                    result[orig_pos] = block[new_pos]
        else:
            result = [block[pos] for pos in self.key_order]

        return ''.join(result)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.text):
            raise StopIteration

        block = self.text[self.current_index:self.current_index + self.block_size]
        self.current_index += self.block_size

        processed_block = self._process_block(block)

        if self.decrypt and self.current_index >= len(self.text):
            processed_block = processed_block.rstrip()

        return processed_block


#Тестирование
if __name__ == "__main__":
    print("=== ТЕСТИРОВАНИЕ ===")

    #Пример 1: Шифрование с явной итерацией по блокам
text = "HELLOWORLD"
key = "bAc"
print("Процесс шифрования по блокам:")
cipher = BlockTranspositionCipher(text, key)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")


    #Пример 2: Полное шифрование
cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")

    #Пример 3: Дешифрование с итерацией
print("\nПроцесс дешифрования по блокам:")
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
for i, decrypted_block in enumerate(decipher, 1):
    print(f"Блок {i}: '{decrypted_block}'")

    #Пример 4: Полное дешифрование с обрезкой пробелов
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'")




