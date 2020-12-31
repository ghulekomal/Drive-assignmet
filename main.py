import time
from typing import List, Any, Union

dictionary = {}
def create_dictionary(keypair, valuepair, tout=0):
    if keypair in dictionary:
        return "error: this keypair alread_dictionaryy exists" # error message1
    else:
        if (keypair.isalpha()):
            if len(dictionary) < (1024 * 1020 * 1024) and valuepair <= int(16 * 1024 * 1024):  # constraints for file size less than 1GB and Jasonobject valuepair less than 16KB
                if tout == 0:
                    l = [valuepair, tout]
                else:

                    l = [int(valuepair), time.time() + tout]
                if len(keypair) <= 32:  # constraints for input keypair_name capped at 32chars
                    dictionary[keypair] = l
            else:
                return "error: Memory limit exceeded!! "  # error message2
        else:
            return "error: Invalind keypair_name!! keypair_name must contain only alphabets and no special characters or numbers"  # error message3

def read_dictionary(keypair):
    if keypair not in dictionary:
        return "error: given keypair does not exist in database. Please enter a valid keypair"  # error message4
    else:
        b = dictionary[keypair]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the present time with expiry time
                stri = str(keypair) + ":" + str(
                    b[0])  # to return the valuepair in the format of JasonObject i.e.,"keypair_name:valuepair"
                return stri
            else:
                return "error: time-to-live of", keypair, "has expired"  # error message5
        else:
            stri = str(keypair) + ":" + str(b[0])
            return stri

def delete_dictionary(keypair):
    if keypair not in dictionary:
        print("error: given keypair does not exist in database. Please enter a valid keypair")  # error message4
    else:
        b = dictionary[keypair]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the current time with expiry time
                del dictionary[keypair]
                print("keypair is successfully delete_dictionaryd")
            else:
                print("error: time-to-live of", keypair, "has expired")  # error message5
        else:
            del dictionary[keypair]
            print("keypair is successfully delete_dictionaryd")


def modify_dictionary(keypair, valuepair):
    b = dictionary[keypair]
    if b[1] != 0:
        if time.time() < b[1]:
            if keypair not in dictionary:
                print("error: given keypair does not exist in database. Please enter a valid keypair")  # error message6
            else:
                l = []
                l.append(valuepair)
                l.append(b[1])
                dictionary[keypair] = l
        else:
            print("error: time-to-live of", keypair, "has expired")  # error message5
    else:
        if keypair not in dictionary:
            print("error: given keypair does not exist in database. Please enter a valid keypair")  # error message6
        else:
            l = []
            l.append(valuepair)
            l.append(b[1])
            dictionary[keypair] = l


