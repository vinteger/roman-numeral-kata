class RomanNumerals:

    def encode(self, number):
        result = ''
        i = 0
        while i < number:
            result += 'I'
            i += 1
        return result
