import sys

# Project for computX by Sai Madhavan G IMT2021101

# Initialising a few global counters and dictionaries to be used later
varaddress = 16
variables = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4, "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4,
             "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15,
             "SCREEN": 16384, "KBD": 24576}
instructCount = 0

# File handling
fileName = sys.argv[1]
srcfile = open(fileName, "r")
destFileName = fileName[:len(fileName)-3] + "hack"
destFile = open(destFileName, "w")
lines = srcfile.readlines()

# Iterating through each line of the source file
for line in lines:
    line = line.strip()  # Geting rid of whitespaces
    if(line == ''):     # Skipping empty lines
        continue
    if(line[0:2] == "//"):  # Skipping comments
        continue
    if line[0] == '(':  # Looking for all labels and adding them to variables dictionary with their instruction count
        label = line[1:-1]
        variables[label] = instructCount
        continue
    instructCount += 1

# Iterating through each line of the source file
for line in lines:
    if '//' in line:  # Getting rid of comments
        line = line[:line.index('//')]
    line = line.strip()  # Getting rid of whitespaces
    if(line == ''):  # Skipping empty lines
        continue
    if(line[0:2] == "//"):  # Skipping comments
        continue

    # Handling A type instructions
    elif(line[0] == "@"):
        value = line[1:]
        try:
            value = int(value)  # Checking if the given value is a integer
            value = bin(value)[2:]
        except:
            # If the given value is not an integer, checking if it is an existing variable, else creating a new variable
            if value not in variables:
                variables[value] = varaddress
                value = bin(varaddress)[2:]
                varaddress += 1
            else:
                value = bin(variables[value])[2:]
        # Converting the A instruction to binary and writing to destination file
        opline = "0" + (15-len(value))*"0" + value + "\n"
        destFile.write(opline)
    # Skipping labels
    elif line[0] == '(':
        pass
    # Dealing with C type instructions
    else:
        equalPos = -1
        n = semiPos = len(line)
        dest = ""
        jmpLabel = ""
        # Getting the destination, computation and jump strings from te line
        if "=" in line:
            equalPos = line.index('=')
            dest = line[:equalPos]
        if ";" in line:
            semiPos = line.index(';')
            jmpLabel = line[semiPos+1:].strip()
        comp = line[equalPos+1:semiPos].strip()
        # Calculating binary string for destination field
        destString = ['0', '0', '0']
        if 'A' in dest:
            destString[0] = '1'
        if 'M' in dest:
            destString[2] = '1'
        if 'D' in dest:
            destString[1] = '1'
        destString = "".join(destString)
        # Calculating binary string for a and computation field
        if comp == '0':
            a = '0'
            compString = "101010"
        elif comp == '1':
            a = '0'
            compString = "111111"
        elif comp == '-1':
            a = '0'
            compString = "111010"
        elif comp == 'D':
            a = '0'
            compString = "001100"
        elif comp == 'A':
            a = '0'
            compString = "110000"
        elif comp == 'M':
            a = '1'
            compString = "110000"
        elif comp == '!D':
            a = '0'
            compString = "001101"
        elif comp == '!A':
            a = '0'
            compString = "110001"
        elif comp == '!M':
            a = '1'
            compString = "110001"
        elif comp == '-D':
            a = '0'
            compString = "001111"
        elif comp == '-A':
            a = '0'
            compString = "110011"
        elif comp == '-M':
            a = '1'
            compString = "110011"
        elif comp == 'D+1':
            a = '0'
            compString = "011111"
        elif comp == 'A+1':
            a = '0'
            compString = "110111"
        elif comp == 'M+1':
            a = '1'
            compString = "110111"
        elif comp == 'D-1':
            a = '0'
            compString = "001110"
        elif comp == 'A-1':
            a = '0'
            compString = "110010"
        elif comp == 'M-1':
            a = '1'
            compString = "110010"
        elif comp == 'D+A':
            a = '0'
            compString = "000010"
        elif comp == 'D+M':
            a = '1'
            compString = "000010"
        elif comp == 'D-A':
            a = '0'
            compString = "010011"
        elif comp == 'D-M':
            a = '1'
            compString = "010011"
        elif comp == 'A-D':
            a = '0'
            compString = "000111"
        elif comp == 'M-D':
            a = '1'
            compString = "000111"
        elif comp == 'D&A':
            a = '0'
            compString = "000000"
        elif comp == 'D&M':
            a = '1'
            compString = "000000"
        elif comp == 'D|A':
            a = '0'
            compString = "010101"
        elif comp == 'D|M':
            a = '1'
            compString = "010101"
        # Calculating binary string for jump field
        jmpString = "000"
        if jmpLabel == "JGT":
            jmpString = "001"
        elif jmpLabel == "JEQ":
            jmpString = "010"
        elif jmpLabel == "JGE":
            jmpString = "011"
        elif jmpLabel == "JLT":
            jmpString = "100"
        elif jmpLabel == "JNE":
            jmpString = "101"
        elif jmpLabel == "JLE":
            jmpString = "110"
        elif jmpLabel == "JMP":
            jmpString = "111"
        # Making the C type instruction binary string and writing to the file
        opline = "111" + a + compString + destString + jmpString + '\n'
        destFile.write(opline)

# Flushing both the files
srcfile.close()
destFile.close()
