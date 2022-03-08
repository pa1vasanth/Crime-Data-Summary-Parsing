import sys
sys.path.append('..')
import pytest
import project0
from project0 import main
import sqlite3
def test_fetchincidents():
    url="https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"
    data=main.fetchincidents(url)
    assert data is not None

def test_extractincidents():
    url="https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"
    data=main.fetchincidents(url)
    incidentdata=main.extractincidents(data)
    assert incidentdata is not None

def test_createdb():
    db=main.createdb()
    assert db=='normanpd.db'

def test_populatedb():
    url=r"https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"
    fetchdata=main.fetchincidents(url)
    incidentdata=main.extractincidents(fetchdata)
    db=main.createdb()
    db_base=main.populatedb(db,incidentdata)
    con=sqlite3.connect(db)
    cur=con.cursor()
    cur.execute('SELECT count(*) from incidents;')
    s=cur.fetchone()
    assert s  is not None

def test_status():
    db='normanpd.db'
    status=main.status(db)
    assert status is not None


