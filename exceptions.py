# Exceptions are special objects created by python to handle errors
# mor euser friendly to include these than traceback errors that python will through back


try:
    print(5/0)
except ZeroDivisionError: #this is an exception created by python that will show in the temrinal
    print('You cannot divide by zero')

# ifg the try and except is passed, an additional else block can be created to host what depends on the try

try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print('You cannot divide by zero')
else:
    print(answer)

# another exception that can be raised us a FileNotFoundError 


# to fail silently, put nothing in the except block 

# except FileNotFoundError:
#     pass