# import functions from custom python package
from calc.calculator import Calculator
from object.state import StateAvgTuitionRow
# declare global variable
global avg_tuition, state_list

# make the global variable a list
avg_tuition = []
# make a state list
state_list = []
# read the csv file
with open("us_avg_tuition.csv") as csv_file:
    # skip the first row
    next(csv_file)
    # fill the list with data from csv file
    for row in csv_file:
        # fill the state_list with state names
        state = row.split(',')
        state_list.append(state[0].lower())
        # fill the avg_tuition with numbers from CSV
        data = row.replace("\"", '').replace(" \n", '').replace(" ,", '').split('$')
        avg_tuition.append(StateAvgTuitionRow(int(data[1].replace(",", "")), \
        int(data[2].replace(",", "")), \
        int(data[3].replace(",", "")), \
        int(data[4].replace(",", "")), \
        int(data[5].replace(",", "")), \
        int(data[6].replace(",", "")), \
        int(data[7].replace(",", "")), \
        int(data[8].replace(",", "")), \
        int(data[9].replace(",", "")), \
        int(data[10].replace(",", "")), \
        int(data[11].replace(",", "")), \
        int(data[12].replace(",", ""))))

# declare main loop function
def main():
    options = input('\nPlease select your query.\n\n1. For whole US data, enter "USA"\n2. For data for a specified US state, enter state\'s name. e.g. "California" or "Alabama" \n3. To exit program, enter "Exit"\n')
    while options.lower() != "exit":
        # user enters USA
        if options.lower() == "usa":
            print("National average tuition rise between 2004-2016: $" + str(Calculator.national_avg_rise(avg_tuition)))
            Calculator.rise_each_year(avg_tuition)
            print("One-year prediction: $" + str(Calculator.national_avg_rise(avg_tuition)))
            print("Two-year prediction: $" + str(Calculator.national_avg_rise(avg_tuition) * 2))
            # restart the program
            main()
        # check if the user's input is in the state_list
        if options.lower() in state_list:
            print("\nSelected state: " + options.title())
            state_index = state_list.index(options.lower())
            print("Sate average tuition rise between 2004-2016: $" + str(Calculator.state_avg_rise(avg_tuition[state_index])))
            print("One-year prediction: $" + str(Calculator.state_avg_rise(avg_tuition[state_index])))
            print("Two-year prediction: $" + str(Calculator.state_avg_rise(avg_tuition[state_index]) * 2))
            # restart the program
            main()
        # error handler for wrong input
        if options.lower() not in state_list and options.lower() != "usa":
            print("\n\nERROR: Please enter a correct state name. US territories and districts are not supported.\n")
            # restart the program
            main()
        
    # terminate program
    print("See you again")
    exit()
# execute main() loop function        
main()
