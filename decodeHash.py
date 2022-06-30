import hashlib


def decode():
    open_password_textFile = open("Password List.txt", "r") #open password file
    open_salt_open_password_textFile = open("Salt List.txt", "r")# open salt file
    pass_code = "Pass Code Not Found... Mission Failed"


    password_lst = []
    salt_lst = []

    # loop though the password file, strip the lines (done as a precaution)
    # and store each line in the list
    for line in open_password_textFile:
        stripped_line = line.strip()
        password_lst.append(stripped_line)

    # loop though the password file, strip the lines (done as a precaution)
    # and store each line in the list
    for line in open_salt_open_password_textFile:
        stripped_line = line.strip()
        salt_lst.append(stripped_line)

    #close files
    open_password_textFile.close()
    open_salt_open_password_textFile.close()

    #loop through password list
    for i in password_lst:
        #loop through salt list
        for j in salt_lst:
            test_string = i+j #cocatenate strings
            test_hash = hashlib.sha256(test_string.encode("ascii")) #hash the string
            if test_hash.hexdigest() == "6572c665a765e849c5d54fc357cb8d7f8308cfeffebc685db1a9259e9df2d533": #compare to hash given
                pass_code = "Pass code is: "+i + "\n"+"Salt used is: " + j
                pass

    print(pass_code)
    



if __name__ == "__main__":
    decode()
