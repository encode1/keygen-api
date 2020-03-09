"""
KeyGenerator uses the RSA keys to encrypt the email
"""
import os
import re
import rsa
import pickle
from base64 import b64encode, b64decode


class KeyGenerator(object):
    _pubkey = pickle.loads(b64decode(os.getenv('PUB_KEY')))
    _privkey = pickle.loads(b64decode(os.getenv('PRIV_KEY')))

    def __init__(self, email):
        print(self._pubkey)
        print(self._privkey)
        self.email = email

    def _validate_email(self):
        """
        validates email format using regex
        :return Boolean:
        """
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if (re.search(email_regex, self.email)):
            return True

    def generate(self):
        """
        Generate the key by signing key with a private Key
        :return: str
        """
        if not self._validate_email():
            return False

        signature = rsa.sign(self.email.encode('utf-8'), self._privkey, 'SHA-1')
        key = b64encode(signature).decode('ascii')
        return key

    def validate(self, key):
        if not self._validate_email():
            return False
        signature = b64decode(key)
        try:
            rsa.verify(self.email.encode('utf-8'), signature, self._pubkey)
        except rsa.VerificationError:
            return '{0} : Invalid'.format(key)
        else:
            return '{0} : valid'.format(key)
