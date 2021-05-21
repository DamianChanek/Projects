import re

print('Welcome to my first calculator.')
print('\nType "q" to exit.')
print('Type "c" to reset equation.')

previous = 0
run = True

def performMath():

    #take global variables into the function#

    global run
    global previous

    #create a variable for equation results#

    while True:

        #embedding the function into try block to catch inputs without any numbers without breaking the program#

        try:
            equation = ''

            # check for previous equation results and return them if applicable#

            if previous == 0:
                equation = input('Enter equation:')
            else:
                equation = input(str(previous))

            # check for quit criteria#

            if equation == 'q':
                print('Thanks for using my calculator!')
                run = False

            # check for reset equation criteria#

            elif equation == 'c':
                print('Equation has been reset.')
                previous = 0

            # remove any symbols that aren't numbers or operators #

            else:
                equation = re.sub('[a-zA-z,:()" "]', '', equation)

            # do the math, accounting for previous results #

                if previous == 0:
                    previous = eval(equation)
                else:
                    previous = eval(str(previous) + equation)


        except SyntaxError:
            print('Invalid input. Please try again.')
            continue

        else:
            break

#call the calculator function#

while run:
    performMath()
