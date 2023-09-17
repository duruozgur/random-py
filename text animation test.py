import time

print('?')
print("")


def pprint(text, sleep):
    for letter in text:
        time.sleep(sleep)
        print(letter, end='')


pprint('Loading...', 0.07)

time.sleep(2)

a = """
Loading completed.
"""

pprint(a, 0.09)

time.sleep(0.5)
print("")

desc = """
Item #: SCP-048

Object Class: None (see description)

Special Containment Procedures: The designation SCP-048 is to be retired from the SCP catalog. No future SCPs are to be assigned this number.

Description: SCP-048 has long been considered the "cursed SCP number" by SCP staff: any items given this designation tend to be destroyed, decommissioned, stolen, or otherwise lost to the Foundation, usually through no fault of any individual person. In addition, personnel assigned to SCP-048 in its various incarnations have had a 50% higher rate of turnover due to death, dismemberment, and disciplinary action.

Whether or not the number 048 actually has any supernatural qualities is unknown, but given the superstition around this number, the designation has been removed from the catalog in order to help maintain employee morale.
"""
pprint(desc, 0.05)
