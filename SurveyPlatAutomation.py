#-------------------------------------------------------------------------------
# Name:        SurveyPlatAutomation
# Purpose:  {Brief description of what this script}
# 
# Author:      sgambrel@bouldercounty.gov, mlauer@bouldercounty.gov
#
# Created:     05/16/2024
#-------------------------------------------------------------------------------
import csv
from datetime import date, datetime, timedelta
import os
import time

import arcpy
import pypyodbc

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

accela_connection_string = ()

def main():

    # start
    start_time = time.time()

    # GET REPORT FROM ACCELA WITH THESE FIELDS:  PARCEL NUMBER, SURVEY ID, SUMMARY, DESCRIPTION, SURVEY YEAR
    
    # CODE FROM MODELBUILDER:  SELECT PARCELS BY PARCEL NUMBER.  SELECT, COPY, PASTE TO SURVEY PLAT LAYER.  ENTER ATTRIBUTES FROM ACCELA TABLE.  SAVE EDITS.
    
    # LOOP THROUGH ALL, PASS SURVEYS WITH NO PARCEL ID
    
    # COPY PDF FROM PLANSCAN FODLER TO SURVEYS FOLDER.  RENAME.
    
    # MARK MAPPED IN ACCELA
    
    # EMAIL REPORT OF WHAT WAS PROCESSED AND WHAT WAS NOT (AND NEEDS DONE MANUALLY)

    # end
    end_time = time.time()
    run_time = end_time - start_time
    print(f'Runtime: {run_time:.2f} seconds')

################################################################################
## END MAIN
################################################################################

def query_accela(connection_string, query):
    # set parameters if needed
    db = pypyodbc.connect(connection_string)
    cursor = db.cursor()
    cursor.execute(query)
    query_results = [dict(zip([column[0] for column in cursor.description],
                              row)) for row in cursor.fetchall()]
    # close connection
    cursor.close()
    db.close()
    return query_results[0]
    

################################################################################
## END OF ALL FUNCTIONS
################################################################################

if __name__ == '__main__':
    main()