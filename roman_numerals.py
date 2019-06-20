class RomanNumerals:

    def encode(self, number):
        result = ''
        one = 'I'
        five = 'V'

        if number is 5:
            result = five

        i = 0
        if number < 4:
            while i < number:
                result += one
                i += 1

        if number is 4:
            result = one + five

        if number > 5:
            i = 5
            result = five
            while i < number:
                result += one
                i += 1

        return result
