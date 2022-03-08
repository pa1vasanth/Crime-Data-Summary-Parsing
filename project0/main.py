import argparse
import urllib.request
import PyPDF2
import tempfile
import sqlite3
from datetime import datetime

def main(url):
    # Download data
    incident_data = fetchincidents(url)

    # Extract data
    incidents = extractincidents(incident_data)

    # Create new database
    db = createdb()

    # Insert data
    populatedb(db,incidents)

    # Print incident counts
    status(db)

def fetchincidents(url):

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return data

def extractincidents(incident_data):
    fp = tempfile.TemporaryFile()
    fp.write(incident_data)
    fp.seek(0)
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    page_count =  pdfReader.getNumPages()
    pdf_data = []
    def time(string):
        string=str(string)
        format="%m/%d/%Y %H:%M"
        try:
            res = bool(datetime.strptime(string, format))
        except ValueError:
            res = False
        return res
    for i in range(page_count):
        page_data = pdfReader.getPage(i).extractText()
        page_data = page_data.replace(" \n"," ")
        page_data=page_data.split('\n')
        if(i==0):
            page_data=page_data[5:-3]
        if(i==(page_count-1)):
            page_data=page_data[:-2]
        else:
            page_data=page_data[:-1]

        for j in range(0, (len(page_data)-5), 5):
            if(((time(page_data[j])==True)) and ((time(page_data[j+5])==True))):
                    row_data = page_data[j:j+5]
                    pdf_data.append(row_data)
        if(time(page_data[-5])==True):
            row_data=page_data[-5:]
            pdf_data.append(row_data)
                    


    print(pdf_data)
    return pdf_data


def createdb():
    db="normanpd.db"
    con=sqlite3.connect(db)
    cur=con.cursor()
    cur.execute('''Drop Table if exists incidents''')
    cur.execute(''' CREATE TABLE incidents ( incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT)''')
    con.commit()
    con.close()
    return db

def populatedb(db,incidents):
    con = sqlite3.connect(db)
    cur = con.cursor()
    statmt = """ INSERT INTO incidents (incident_time,incident_number,incident_location,nature,incident_ori) VALUES (?,?,?,?,?)"""
    cur.executemany(statmt,incidents)
    con.commit()
    con.close()


def status(db):
     con = sqlite3.connect(db)
     cur = con.cursor()
     cur.execute('''SELECT nature ||'|'|| count(*) FROM incidents GROUP BY nature ORDER BY count(nature) DESC, nature ASC''')
     result = cur.fetchall()
     for row in result:
        print(row[0])
     cur.close()
     return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, help="Incident summary url.")
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)


