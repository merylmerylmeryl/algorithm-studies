class CaesarCipher:
    """A class for converting a message into a secret message."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        """Return string reprsenting encrypted message."""
        return self._transform(message, self._forward)

    def decrypt(self, message):
        """Return string representing decrypted message."""
        return self._transform(message, self._backward)

    def _transform(self, message, coder):
        tempList = list(message)
        for i in range(len(tempList)):
            if message[i].isupper():
                pos = ord(message[i]) - ord('A')
                tempList[i] = coder[pos]
        return ''.join(tempList)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message: ', answer)
