#!/usr/bin/python3
""" UTF-8 Validation"""
import codecs


def validUTF8(data):
    """ This function checkes where the passed
    list of integers are correct utf8 values"""

    # convert list of data to bytes
    if len(data) == 0:
        return False
    try:
        dataBytes = bytes(data)
        # decode the bytes using utf8 encoding
        decodedData = dataBytes.decode('utf-8')
        return True
    except Exception as e:
        return False
