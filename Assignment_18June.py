#Ans.  1.
"""The 'else' block in a try-except statement is an optional block that is executed when no exceptions are raised within the 'try' block.
Its purpose is to provide a section of code to run if the 'try' block completes successfully, without any exceptions being raised."""
"""try:
    num1=int(input("Enter first number:- "))
    num2=int(input("Enter second number:- "))
    result=num1/num2

except ZeroDivisionError:
    print("Error : Zero division error")

except ValueError:
    print("Error: Value error")

else:
    print(result)"""

print("")

# Ans.  2
"""Yes, a try-except block can be nested inside another try-except block. This is known as nested exception handling.
Nested exception handling allows for more granular and specific handling of exceptions.
It allows you to handle different types of exceptions at different levels of your code, providing more fine-grained control over error handling."""
"""try:
   try:
       num1=int(input("Enter first number:- "))
       num2=int(input("Enter second number:- "))
       result=num1/num2
   
   except ZeroDivisionError:
       print("Error : Zero division error")
   
   except ValueError:
       print("Error: Value error")
   
   else:
       print(result)

except Exception as e :
    print("Error: ",e)"""

print("")

# Ans.  3.
"""To create a custom exception class in Python, you can define a new class that inherits from the built-in Exception class or any of its subclasses.
 This allows you to define your own exception type with specific behaviors and attributes."""

class CustomError(Exception):
    def __init__(self,message):
        self.message=message

    def __str__(self):
        return f"Custom message :{self.message}"
    
def divide_num(num1,num2):
    if num2==0:
        raise CustomError("Cannot divide by zero")
    else:
        return num1/num2
    

try:
    num1=int(input("Enter first number:- "))
    num2=int(input("Enter second number:- "))
    result= divide_num(num1,num2)
    print(f"The result is {result}")

except CustomError as e:
    print(e)


print("")


# Ans.  6.
"""The purpose of log levels in Python logging is to categorize log messages based on their severity or importance.
Each log level corresponds to a specific level of severity, and developers can choose the appropriate level for each log message to control which messages should be recorded and displayed.
The Python logging module provides the following log levels in increasing order of severity:"""

# 1. DEBUG: Detailed information, typically used for debugging and development. These messages are usually only relevant to developers during the development phase and are not included in the production logs.

import logging

logging.basicConfig(level=logging.DEBUG)

def add(x, y):
    logging.debug('Adding variables %s and %s', x, y)
    return x + y

print(add(10, 20))

# 2. INFO: General information about the program's execution. These messages are helpful for understanding the program's flow and providing insights into its behavior during runtime.

import logging

logging.basicConfig(level=logging.INFO)

def login(Admin):
    logging.info("We are inside the login function with admin as %s",Admin)

login("Ashish")

# 3. WARNING: An indication that something unexpected happened or a potential issue was encountered. The program is still running as expected, but it may require attention.

import logging

logging.basicConfig(level=logging.WARNING)

def weather(temperature):
    if temperature>45:
        logging.warning("The temperature is %s above 45,avoid outside exposure !",temperature)

weather(49)

# 4. ERROR: Indicates an error that caused the program to fail to perform a specific operation or task.

import logging

logging.basicConfig(level=logging.ERROR)

def divide(x,y):
    try:
        R=x/y
    except ZeroDivisionError:
        logging.error("Error : Division by zero ,not allowed ")
    else:
        print(R)
    
divide(5,0)

# CRITICAL: Indicates a critical error or failure that could lead to the program's termination.

import logging

logging.basicConfig(level=logging.CRITICAL)

def system_check(sys):
    if sys != "OK":
        logging.critical("System failure: %s",sys)

system_check("You need to handle the bug")

# Ans.  7.
"""In Python logging, log formatters are objects responsible for specifying the layout and structure of the log messages.
They define how the log records are formatted into a string representation before being emitted to the output destination, such as a log file or the console."""

"""The Python logging module provides a built-in Formatter class that you can customize to define your desired log message format.
The Formatter class uses placeholders to represent different components of the log record, such as the log level, timestamp, log message, etc."""

import logging

# Create a Formatter object with the desired log message format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

# Create a logger and set its log level
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a handler and set the formatter
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

# Log messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


# Ans.  10

import logging

logging.basicConfig(filename="app.log",level=logging.INFO)

message="Hello World!"

logging.info("%s",message)

# Ans.  11.

import datetime

def main():
    # Set up logging configuration
    logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        filename='error.log',
                        filemode='a')

    try:
        # Your main program code goes here
        # For demonstration purposes, let's raise a sample exception
        result = 10 / 0
    except Exception as e:
        # Log the error message to console and the "errors.log" file
        error_message = f'Exception type: {type(e).__name__}, Timestamp: {datetime.datetime.now()}'
        logging.exception(error_message)
        print("An error occurred. Check 'error.log' for details.")

if __name__ == "__main__":
    main()