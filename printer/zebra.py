import subprocess

import re

import os
import sys


def clean_string(dirty_string):
    return(str(dirty_string)[13:-1])


def parse_string(zpl_commmand):
    '''
        Return zpl_command string to bytes 
    '''
    return bytes(zpl_commmand, 'utf-8')


def print_linux(byte_data):

    print('DATA TO PRINT \n')
    print(byte_data)
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    lpr.communicate(input=byte_data)


def print_win32(byte_data):
    p = win32print.OpenPrinter (printer_name)




if __name__ == "__main__":
    data = b'^XA^CFA,45^FO50,25^FDEmiliano Larrea^FS^CFA,30^FO50,80^FDProLine - CEO^FS^FO50,120^FD2644804290^FS^FO50,160^FDemiliano18796@gmail.com^FS^FO50,110^BY2,2,95^BQ,2,4^FH_^FDHM,AEmiliano Larrea/ProLine - CEO/2644804290/emiliano18796@gmail.com^FS^XZ'
    print(data)
    print_linux(data)
