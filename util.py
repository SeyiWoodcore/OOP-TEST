import pandas as pd
from database import Database
from datetime import datetime
from env import Secrets
from report import ActiveCustomersReportsQuery
from report import ActiveLoansQuery
import logging


#This is where i plan to do everything, my excel and all

# class ActiveCustomersReports:
#     def __init__(self) -> None:
#         pass
#     #def active_customers_report(self):
#         CUSTOMERS = []
#         sql = ActiveCustomers(
#             branch=self.get_branches(),
#             start_date=self.start_date,
#             end_date=self.end_date,
#         ).script()
#         for customer in pd.read_sql(
#             sql, Database.connection(self.schema_name), chunksize=CHUNK_SIZE
#         ):
#             CUSTOMERS.append(customer)
#         df = pd.concat(CUSTOMERS)
#         df.columns = df.columns.str.upper()
#         return df
#     #call the function that would return the active customers query report
#     #lets call it Activecustomerrsreports = script(
#     # self.Branch = Branch
#        # self.start_date = start_date
#       #  self.end_date = end_date
# #)
# #Activecustomersreports.ActiveReports()
# class ActiveLoansReports:
#     def __init__(self) -> None:
#         pass
#     def active_customers_report(self):
#         CUSTOMERS = []
#         sql = ActiveCustomers(
#             branch=self.get_branches(),
#             start_date=self.start_date,
#             end_date=self.end_date,
#         ).script()
#         for customer in pd.read_sql(
#             sql, Database.connection(self.schema_name), chunksize=CHUNK_SIZE
#         ):
#             CUSTOMERS.append(customer)
#         df = pd.concat(CUSTOMERS)
#         df.columns = df.columns.str.upper()
#         return df
#     def manage(self):
#         writer = pd.ExcelWriter(
#             self.reportName,
#             engine="xlsxwriter",
#             engine_kwargs={"options": {"strings_to_numbers": False}},
#         )
#         workbook = writer.book
#      #####  REPORT START  ####
#         start_row = 6
#         df = self.active_customers_report()
#         df.index = np.arange(1, len(df) + 1)
#         df.to_excel(
#             writer,
#             sheet_name="ACTIVE CUSTOMERS",
#             index=True,
#             startrow=start_row,
#             startcol=0,
#             header=True,
#         )