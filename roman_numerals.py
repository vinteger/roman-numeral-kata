class RomanNumerals:

    def encode(self, number):
        result = ''
        i = 0
        if number < 4:
            while i < number:
                result += 'I'
                i += 1
        if number is 4:
            result = 'IV'
        return result
