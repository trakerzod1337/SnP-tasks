class BlockTranspositionCipher:
    def __init__(self, text, key, decrypt=False):
        self.text = str(text) if text is not None else ""
        self.decrypt = bool(decrypt)
        self.key = self._validate_key(key)
        self.block_size = len(self.key)
        self.current_index = 0

        char_positions = [(char, idx) for idx, char in enumerate(self.key)]
        sorted_chars = sorted(char_positions, key=lambda x: x[0])
        
        self.encrypt_order = [0] * self.block_size
        for new_pos, (char, orig_pos) in enumerate(sorted_chars):
            self.encrypt_order[orig_pos] = new_pos

        self.decrypt_order = [0] * self.block_size
        for new_pos, (char, orig_pos) in enumerate(sorted_chars):
            self.decrypt_order[new_pos] = orig_pos

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

    def _process_block(self, block):
        if len(block) < self.block_size:
            block += ' ' * (self.block_size - len(block))

        result = [''] * self.block_size
        if self.decrypt:
            for i, orig_pos in enumerate(self.decrypt_order):
                result[orig_pos] = block[i]
        else:
            for orig_pos, new_pos in enumerate(self.encrypt_order):
                result[new_pos] = block[orig_pos]

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
        
