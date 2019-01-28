
# Scraper-Scripts
A repo containing all the scripts related to scraping the web!


# 1) Flipkart Scraper (Books) 
## **EXTREMLY CUSTOMISABLE BOOK CRAWLER**

This script can be **extensivly customised** and tailored to search ANY book (and any item with a bit more modifications) based on ANY genre, if you follow the instructions in the top documentation of the file.

## Requires Beautiful Soup 4 module for compilation

In the command prompt / terminal, type in these two commands.

``` pip install bs4 ```

*AND*

```pip install lxml```



~~The code does not currently have multi-thread support.~~
**NEW:** Added multi-processing functionality to scraping multiple genre at once. Each URL in URL.txt will run on a seperate process tree.

### **The code will output a "Data.csv" file containing all the books that it scraped.**

## **Benchmark**

#### The execution time as of date is 2000 books in 20 minutes **PER** genre thread.

10 different genre threads output 20,000 books in 20 minutes.

(TESTED ON: Intel i7-7700 HQ CPU @ 2.50 GHz, 1 MB/s Network)

#### Execution time for 2000 books is 18 minutes **PER** thread.

(TESTED ON: Intel Core i5-8300H , 10MB/s network)
 
