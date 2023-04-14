# happy3.py

#Kyle Nabors

#creates a dictonary of countries and happiness index and then lets the user lookup a country and see the happiness index

def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()
    
    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    #print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)



def make_happy_dict():
    happy_dict = {} #create a dictonary 

    infile = open("happiness.csv")#open the refrence csv file 

    heading = infile.readline()#skips the header of the csv file

    for line in infile: #loops for every line in file
        line = line.strip() #removes empty space from each line
        line = line.split(',')#splits the lines at the ,
        
        country = line[0] #pulls country the first data collum in the csv file
        happiness_index = line[2]#pulls happiness index from the third data collum of the csv file 
        happy_dict[country] = happiness_index #stores the lists as key values and pairs them in the dictonary 
         
    infile.close()#closes the file 
    
    return happy_dict #return the happy dictonary 

def read_gdp_data(happy_dict):
    return

def lookup_happiness_by_country(happy_dict):
    while True: #loops section 
        query = input("Enter a country to lookup or 'done' to exit:")#gets country name from user
        if query == 'done':#ends program if user enters done
            return
        if query in happy_dict:
            lookup = happy_dict[query]#looks up country based on user input 
            print(lookup)
        else:
            print(query, "not found")#if country not found in database tell user country not found
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}): # if there is an error is the dictonary or no dictonary prints out a error message 
        print("Dictionary not found")
        return
   # print("Contents of dictionary sorted by key.")
  #  print("Key","Value")
   # for key in sorted(D.keys()):#loops for the number of keys 
    #    print(key, D[key]) #prints out the dictonary 
        
main()
