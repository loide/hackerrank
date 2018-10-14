"""
Think Python by Allen B. Downey
http://thinkpython.com

Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces sso that the last letter of the
string is in column 70 of the display.

Example:
>>> right_justify('allen')
                                                                 allen
"""
def right_justify(s):
    parameter_size = len(s)
    column_size = 70
    remaining_columns = column_size - parameter_size
    output_string = ' ' * remaining_columns + s
    print (output_string)

def main():
    s = input("give a string: ")
    right_justify(s)

if __name__ == '__main__':
    main()
