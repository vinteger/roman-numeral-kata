class RomanNumerals:

    def encode(self, number):
        result = ''
        five = 'V'
        i = 0
        if number < 4:
            while i < number:
                result += 'I'
                i += 1
        if number is 4:
            result = 'I' + five
        if number is 5:
            result = five
        if number > 5:
            result = five + 'I'
        return result
