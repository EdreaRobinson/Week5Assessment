log_file = open("um-server-01.txt")
# this opens the .txt file that contains the data


def sales_reports(log_file): #defines the function
    for line in log_file:    #defines the variable for the loop and initiates it
        line = line.rstrip() #removes any white spaces at the end of the string
        day = line[0:3]      #defines the variable as the first 3 characters of each line
        if day == "Mon":     #tests a logical condition
            print(line)      #if the condition is met, it returns this variable


sales_reports(log_file)

print(sales_reports)
