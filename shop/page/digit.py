import re


def has_digit(text):
  if re.search("\d", text):
    return True
  return False
