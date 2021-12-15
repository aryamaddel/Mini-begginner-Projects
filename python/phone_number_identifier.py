import re


# This program searches for phone number patterns in given strings.

# phone number
def phone_num(text):
    phone_num_regex = re.compile(r"\d\d\d\d\d\d\d\d\d\d")
    return phone_num_regex.findall(text)


# phone number - India
def ind_phone_num(text):
    phone_num_regex = re.compile(r"(\d\d)-(\d\d\d\d\d\d\d\d\d\d)")
    mo = phone_num_regex.search(text)
    print(phone_num_regex.findall(text))
    print(f"Area code is {mo.group(1)}")
    print(f"Phone Number is {mo.group(2)}")


# phone number - US
def us_phone_num(text):
    phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
    mo = phone_num_regex.search(text)
    print(phone_num_regex.findall(text))
    print(f"Area code is {mo.group(1)}")
    print(f"Phone Number is {mo.group(2)}")
