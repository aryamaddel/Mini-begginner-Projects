import smtplib

# This automation can send and check your email inbox

# conn is a connection object
# for the smtp server that is the domain name of your email pass "smtp.<DOMAIN NAME>.com"as argument
# and pass the port number for your smtp server
conn = smtplib.SMTP("smtp.gmail.com", 587)

# ehlo() establishes connection with the server and returns a connections status tuple
connection = conn.ehlo()
# if the tuple has 250 as the first integer then the connection has been established correctly
print(connection)

# starttls() encrypts the passwords which should be done before logging in
data_encryption = conn.starttls()
# if the tuple has 220 as the first integer then the encryption is successful
print(data_encryption)
