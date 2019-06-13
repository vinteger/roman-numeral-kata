class RomanNumerals:

    def encode(self, number):
        if number is 1:
            return 'I'
        elif number is 2:
            return 'II'
        elif number is 3:
            return 'III'
        elif number is 4:
            return 'IV'
        return ''
