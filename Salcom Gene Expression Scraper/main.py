# Author: S Sandeep Pillai
try:
    import requests
    from bs4 import BeautifulSoup
except:
    print("Please install the following modules using pip:\npip install bs4\npip install lxml")

import time # To benchmark only.


error_message = "ERROR: No data for given gene in database. Possible Reasons: \n1) Please check input.txt for " \
                "mis-spelling. \n2) Please check your internet connection / proxy settings / " \
                "firewall authorisation. \n3) Please close any of the output csv files in Excel."

def url_construct(base_url, query = "", rotation = ""):

    url = base_url
    if str(rotation) != "":
        url = url + "header_rotation=" + str(rotation) + ";"
    if query != "":
        url = url + "query=" + query + "_HL" # Check this later
    print(" Url = ", url)
    return url


def initialise_excel(URL):

    file = open("Absolute_Expression_Levels.csv", 'w')
    file.write("Name,")
    file2 = open("Relative_Expression_Levels.csv", 'w')
    file2.write("Name,")
    Relative = False

    source = requests.get(URL)
    source_code = source.text                   # BS4 module stuff, ignore.
    soup = BeautifulSoup(source_code, "lxml")
    try:
        soup.find_all("font", {"color": 'red'})[5]
    except:

        for item in soup.find_all("th", {"class": "rotate"}):

            title = item.string
            # print(title, end = " ")
            if Relative == False:
                file.write(title + ',')
            else:
                file2.write(title + ',')        #
            if title == "Nitric oxide shock (InSPI2)":      # End of Absolute-Headings. Spaghetti code I know.
                Relative = True
                # print("\n\n")

        file.write('\n')
        file2.write('\n')
        file.close()
        file2.close()
    else:
        print("Gene not found, please enter a valid first gene to load heading row.")
        exit(-1)

def scrape_gene(URL, object, delay=2):      # Method to extract info of specific gene
    source = requests.get(URL)
    source_code = source.text  # BS4 stuff, ignore.
    soup = BeautifulSoup(source_code, "lxml")
    does_gene_exist = soup.find_all("font", {"color": 'red'})

    if len(does_gene_exist) != 5: # Crude fix, checks if fifth red text "Warning" is there in html. Find better sol later.
                                  # Only 4 red font color text there if no "Warning" sign in html.
        file = open("Absolute_Expression_Levels.csv", 'a')
        file2 = open("Relative_Expression_Levels.csv", 'a')
        file.write(object + ',')
        file2.write(object + ',')
        #print("Name: " + object)

        for item in  soup.find_all("a", {"class": "nd"}):

            title = item['onmouseover'][34:].split("'")
            value = item.string.replace(",", "")

            if title[0][0:3] == "44_":                                   # Relative Expression
                #print(title[0][129:],":", value)
                file2.write(value + ",")

            else:
                #print(title[0],":", value)                              # Absolute Expression
                file.write(value + ",")

        #print("Common Name: " + object, "\nSleeping for", delay, "seconds to avoid overload. [Can be modified in code]")
        file.write('\n'); file.close(); file2.write("\n"); file2.close()
        print(object, "data found!")
        time.sleep(delay)  # Safety procedure to not overload servers. Comment out at own risk / ethics.
    else:
        print("No Results of gene:", object)
        time.sleep(delay/2)

def gene_input():

    gene_list = []
    file = open("input.txt", 'r')
    for lines in file.readlines():
        genes = lines
        gene_list.append(genes.split('\n')[0].split(', '))

    return sum(gene_list, [])       # Cute trick to flatten 2d list to 1d list

# URL = url_construct("http://bioinf.gen.tcd.ie/cgi-bin/salcom.pl?", "STM4509")
#scrape_gene(URL)



########################################################################################################################


def driver_code(delay):

    counter = 1
    url = 'http://bioinf.gen.tcd.ie/cgi-bin/salcom.pl?'
    try:
        items = list(gene_input())   # Unpack items in "input.txt" to a list.
    except:
        print("Please create a file 'input.txt' in script directory and input gene names in comma, or line seperated format!")
        exit(-1)

    try:
        initialise_excel(url_construct(url, items[0]))
        # Initialise csv file with the top headings
    except:
        print(error_message)
        exit(-2)


    for object in items:
        try:
            print("\n[", counter, ")")
            scrape_gene(url_construct(url, object), object, delay)
            counter+=1

        except:         ## Retry code incase of network failure.
            print(error_message, '\nRetrying gene 5 times:\n')
            for attempt in range(1, 6):
                try:
                    print("\n[", counter, ")")
                    scrape_gene(url_construct(url, object), object, delay*2)
                    counter += 1
                    time.sleep(7)
                    break

                except:
                    print("No data found, waiting", 7 + attempt*5, "seconds." )
                    time.sleep(5 + attempt*5)
            else:

                ch = input("Connection timed out. Press any key to manually resume by skipping gene:"+ object +"\nPress 'e' to exit")
                if ch == 'E' or ch == 'e':
                    exit(0)
                else:
                    try:
                        print("\n[", counter, ")")
                        scrape_gene(url_construct(url, object), object, delay*3)
                        counter += 1
                    except:
                        pass


        if counter % 100 == 0:
            print("Pausing scraping for 30 seconds to avoid detection")
            time.sleep(30)

if __name__ == '__main__':
    start = time.time()
    driver_code(delay = 0.5)               # Change arg at your own risk.
    print("\n\nScraping Complete!\n")
    end = time.time()
    print("TIME FOR EXECUTION == ", round(end - start, 3))

input("Press Enter to continue.")