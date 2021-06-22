from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import hashlib


def couchdb_password_hash(password, user, iterations=10):
    bsalt = hashlib.sha1(user.encode())
    hexbsalt = bsalt.hexdigest()
    password_hash = hashlib.pbkdf2_hmac('sha1', password.encode(), hexbsalt.encode(), iterations)
    print(password_hash.hex())

    couchdb_hash = "-pbkdf2-" + password_hash.hex() + "," + hexbsalt + "," + str(iterations)

    return(couchdb_hash)


class FilterModule(object):
    def filters(self):
        return {
            'couchdb_password_hash': couchdb_password_hash,
        }
