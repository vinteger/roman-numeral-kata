ONE = 'I'
FIVE = 'V'
TEN = 'X'


class RomanNumerals:

    def encode(self, number):
        result = ''

        if number < 40:
            X_to_prepend = number // 10
            second_digit = number % 10

            if X_to_prepend:
                result = TEN * X_to_prepend
            result += self._second_digit_check(second_digit, result)

        return result

    def _second_digit_check(self, number, result):
        if number is 5:
            result = FIVE
        result = self._number_less_than_4(number, result)
        if number is 4:
            result = ONE + FIVE
        result = self._number_between_5_and_9(number, result)
        if number is 9:
            result = ONE + TEN
        return result

    def _number_between_5_and_9(self, number, result):
        i = 5
        if 5 < number < 9:
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
