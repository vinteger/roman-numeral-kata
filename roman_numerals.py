ONE = 'I'
FIVE = 'V'
TEN = 'X'


class RomanNumerals:

    def encode(self, number):
        result = ''

        if number is 5:
            result = FIVE

        if number is 10:
            result = TEN

        result = self._number_less_than_4(number, result)

        if number is 4:
            result = ONE + FIVE

        result = self._number_between_5_and_9(number, result)

        if number is 9:
            result = ONE + TEN

        result = self._number_between_10_and_14(number, result)

        return result

    def _number_between_5_and_9(self, number, result):
        if 5 < number < 9:
            i = 5
            result = FIVE
            while i < number:
                result += ONE
                i += 1
        return result

    def _number_less_than_4(self, number, result):
        i = 0
        if number < 4:
            while i < number:
                result += ONE
                i += 1
        return result

    def _number_between_10_and_14(self, number, result):
        if 10 < number < 14:
            i = 10
            result = TEN
            while i < number:
                result += ONE
                i += 1
        return result

