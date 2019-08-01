def phone_word(phone_number):
    """Return all possible phonewords respective to a phone number.
    :param phone_number: str
    :return list of str with all phonewords
    """
    digit_to_chars = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    n = len(phone_number)

    def phone_word_rec(previous_result, cursor):
        if cursor == n:
            return previous_result
        digit = phone_number[cursor]
        result = []
        for char in digit_to_chars[digit]:
            result.extend(
                prev_result + char for prev_result in previous_result)
        return phone_word_rec(result, cursor + 1)

    return phone_word_rec([''], 0)


print(phone_word(''))  # ['']
print(phone_word('7'))  # ['p','q', 'r', 's']
print(phone_word('73'))  # ['pd','qd', 'rd', 'sd', 'pe', 'qe', ...]
print(phone_word('736'))  # [...,'ren','sen', ...]
