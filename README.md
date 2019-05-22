
# Scraper-Scripts
A repo containing all the self-made **Open Source** scripts related to scraping the web!

******


# 1) Flipkart Scraper (Books) 
## **EXTREMLY CUSTOMISABLE BOOK CRAWLER**

This script can be **extensively customised** and tailored to scrape ANY book collection (and any item with a bit more modifications) based on ANY genre, if you follow the instructions in the top documentation of the file.

## Requires Beautiful Soup 4 module LXML for compilation

**Installation Instructions** 

In the command prompt / terminal, type in these two commands.

``` pip install bs4 ```

*AND*

```pip install lxml```


## Instructions:

1) Add the URL of the search page containing the *collection* of books of the genre you wish to scrape, INTO the **URL.txt** file.

```
#### Eg:

The URL for Education and Professional books genre is:

https://www.flipkart.com/books/educational-and-professional-books/pr?sid=bks,enp&otracker=categorytree

```

2) Execute **master.py** to execute the script.

#### Eg:

Within the terminal, type the following commands:


```

cd <Folder Containing the repo files>
python master.py

```

#### Patch Notes

~~The code does not currently have multi-thread support.~~

**NEW:** **January 2019:** Added multi-processing functionality to scraping multiple genre at once. Each URL in URL.txt will run on a seperate process tree. Note: Very buggy for scraping more than 20 genres (which you shoudn't be doing).

### **The code will output a "Data.csv" folder containing all the assigned genres in seperate files that it scraped.**

## **Benchmark**

#### The execution time as of date is 2000 books in 20 minutes **PER** genre thread.

10 different genre threads output 20,000 books in 20 minutes.

(TESTED ON: Intel i7-7700 HQ CPU @ 2.50 GHz, 1 MB/s Network)

#### Execution time for 2000 books is 18 minutes **PER** thread.

(TESTED ON: Intel Core i5-8300H , 10MB/s network)
 
# 2) bioinf.gen.tcd.ie/ scraper

## http://bioinf.gen.tcd.ie/cgi-bin/salcom.pl?_HL 

A sraper that fetches the absolute and relative gene expression values of all gene subspecies in the Salmonella Compendium.

**NOTE: This scraper is not open source - it is a licenced and paid product that is protected and owned by the S Sandeep Pillai ©

## Dependencies

```
pip install bs4
pip install lxml
```

## Usage Instructions:

Input the gene sequence name into the input.txt file and execute main.py




