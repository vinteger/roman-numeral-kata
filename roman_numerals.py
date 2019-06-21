class RomanNumerals:

    def encode(self, number):
        result = ''
        one = 'I'
        five = 'V'
        ten = 'X'

        if number is 5:
            result = five

        if number is 10:
            result = ten

        i = 0
        if number < 4:
            while i < number:
                result += one
                i += 1

        if number is 4:
            result = one + five

        if 5 < number < 9:
            i = 5
            result = five
            while i < number:
                result += one
                i += 1

        if number is 9:
            result = one + ten

        return result
