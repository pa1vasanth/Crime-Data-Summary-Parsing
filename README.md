# pa1vasanth-cs5293sp22-project0
Project0
Norman Crime Data Summary
#Author: PAVAN VASANTH KOMMMINENI

#Project Summary
Our assignment in this project is to build a function that collects only the incidents. The data is accessed from City of Norman OK website(Police Department Activity Records) in form of pdf.

Python Functions:
1. Main function
2. Download the data given one incident pdf
3. Extract the incident data
4. Create an SQLite database to store the data;
5. Insert the data into the database;
6. Print each nature and the number of times it appears

Running the project :
Commandline:
pipenv run project0/main.py --incidents <url>
eg: url=""https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-21_daily_incident_summary.pdf"

The cd is cs5293sp22-Project0; I'm listing project0 for the rootpath.

It will print the list of incident nature along with frequency of occurence in the descending order of the nature count (if 2 elements has same count then alphabet order)


Required Python Packages
1. PyPDF2: For the pdf data extraction
2. Sqlite3: For the Database creation and excecution
3. Urllib: For accessing the data using url
4. Temp file: For creating the a temperory file
5. ArgParse:To convert the datatypes
6. Datetime: For sorting the Nature data  
At beginning I have used pandas because i thought of returning the data in form of Data frame later i realized returning in form of lists will be simple.

As listed above there are six functions in main.py file

Main function: main()
1. This function calls all the other functions.
2. It takes url as input.
3. It executes the flow of function.

Fetch Incidents:fetchincidents()
1. This Function takes url as input
2. I have fetched data from the webiste using urllib module with given sample header 
3. It returns the object data type

Extract Incidents: extractincidents()
1. This function takes object data as input which is returned from fetch incidents.
2. In this function a temperory file is created and data is written to temporary file.
3. Using PyPDF2 the temporary file will be open and extrach text data.
4. I have created a function which we have to input a string and it will tell whether the string is Date/Time format.
5. Using that function I'm cleaning the data, the eachdata/time interval will occur after 5 VALUES
6. The rows which are satisfying the data will include in the pdfdata 
7. This function return the lists; In the lists each list value is also a list and this  list indicates each incident row.
8. I'm facing an issue some incidents data is missing because of the logic I have used.

Sqlite Database creation: createdb()
1. This function takes lists as input.
2. Creating a database named 'normanpd.db' using sqlite3 library
3. We create and insert the table named incidents(all incident columns) into the database.
4. This Function returns the db file.

Insert data into database: populatedb()
1. This function takes input as db file and list data from the fetch incidents
2. It insert the incident data into the incident table (db file)
3. This function returns the db file with the incident data


Print each nature and the number of times it appears
1. This function takes the input as db file with loaded data
2. It print the the summary of the data Nature of incident and frequncy of incidents by  running the sql query using db.

Assumptions:
1. Intially In the incident data, some Date/Time data values are present in Nature data to overcome this error I used  Datetime module, If the value isn't in data time time format that rows will append to the data frame.
2. There is only 1 heading row in incident pdf(1st page of incident file)

Errors:
1. Faced Indentation problem, It got solved by autopep8 command
2. Faced No project0 module during in test file, It got solved by using importing the sys

Test file
1. The test_download.py file contain all the test cases.
2.When executed it runs every test case with the main file in project0 and returns the output whether it passed or failed.

References:
1. https://stackoverflow.com/questions/11542930/inserting-an-array-into-sqlite3-python
2. https://www.adamsmith.haus/python/answers/how-to-validate-a-date-string-format-in-python
3. https://docs.python.org/3.8/library/sqlite3.html

