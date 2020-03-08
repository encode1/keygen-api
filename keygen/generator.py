"""
KeyGenerator is a random character generator that generates
20 Alphanumeric character in group of 4 separated by '-'.
The sum of each unicode point of each character in the email string
provided is used to determine the random character for each group
"""
import random
import re


class KeyGenerator(object):

    def __init__(self, email):
        self.email = email
        self.email_score = self._calculate_score(email.upper())


    def _validate_email(self):
        """
        validates email format using regex
        :return Boolean:
        """
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if (re.search(email_regex, self.email)):
            return True

    def _calculate_score(self, text):
        """
        Calculate score of the text by summing unicode point of each character
        :param text: str
        :return: Returns int
        """
        score = 0
        for char in text:
            score += ord(char)
        return score

    def _verify(self, key):
        """
        checks if the score of the individual groups is
        equal to the score of the email
        :param key:
        :return: Boolean
        """
        score = 0
        chunks = key.split('-')
        for chunk in chunks:
            if len(chunk) != 4:
                return False
            score += self._calculate_score(chunk)
        if score == 1772:
            return True
        return False

    def generate(self):
        """
        Generate the key by randomizing the sequence
        :return: str
        """
        if not self._validate_email():
            return False
        key = ''
        chunk = ''
        seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        while True:
            while len(key) < 25:
                char = random.choice(seq)
                key += char
                chunk += char
                if len(chunk) == 4:
                    key += '-'
                    chunk = ''
            key = key[:-1]
            if self._verify(key):
                return key
            else:
                key = ''

    def validate(self, key):
        if not self._validate_email():
            return False

        valid = 'Invalid'
        if self._verify(key):
            valid = 'Valid'
        return '{0} : {1}'.format(key, valid)


