ONE = 'I'
FIVE = 'V'
TEN = 'X'


class RomanNumerals:
    result = ''

    def encode(self, number):

        if number < 40:
            if number < 10:
                return self._rightmost_digit_check(number)

            X_to_prepend = number // 10
            rightmost_digit = number % 10

            if X_to_prepend:
                self.result = TEN * X_to_prepend

                self.result += self._rightmost_digit_check(rightmost_digit)

        return self.result

    def _rightmost_digit_check(self, number):
        rightmost_digit = ''

        if 0 < number < 5:
            rightmost_digit = self._rightmost_less_than_4(number)

        if number is 4:
            rightmost_digit = ONE + FIVE

        if number is 5:
            rightmost_digit = FIVE

        if 5 < number < 9:
            rightmost_digit = self._rightmost_between_5_and_9(number)

        if number is 9:
            rightmost_digit = ONE + TEN

        return rightmost_digit

    def _rightmost_less_than_4(self, number):
        digit = ''
        i = 0
        while i < number:
            digit += ONE
            i += 1
        return digit

    def _rightmost_between_5_and_9(self, number):
        digit = FIVE
        i = 5
        if 5 < number < 9:
            while i < number:
                digit += ONE
                i += 1
        return digit
