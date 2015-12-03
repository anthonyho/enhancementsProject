# Last update 12/3/2015
"""Library of parsing tools"""

def standardizeCharge(charge):
    # Remove all white spaces in charge
    newCharge = charge.replace(' ', '')
    # Add parenthesis to the number at the end if there
    # isn't one already
    newCharge_s = newCharge.split(')')
    if newCharge_s[-1].isdigit():
        newCharge = ''.join(newCharge_s[0:-1])+')('+newCharge_s[-1]+')'
    return newCharge

