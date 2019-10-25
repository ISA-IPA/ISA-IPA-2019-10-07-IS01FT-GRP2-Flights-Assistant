from datetime import datetime as dt
import DB_Functions as dbf
from skyscanner_flight_search import flight_search

def batch_search():
    #set Batch Job Run Date
    batchRunDate = dt.now()

    print(f'Batch Job Run Date: {batchRunDate}')
    ReqDoc = dbf.retrieve_FlightRequest()

    for row in ReqDoc:
        print(row)
        request_id = row['Request_ID']
        info = row['Request_Details']
        outFile = flight_search(row)
        print(outFile)

if __name__ == '__main__':
    batch_search()











