#!/usr/bin/env python
#coding:utf-8

# refer: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='ubuntu', database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(2018, 2, 27)
hire_end = datetime.date(2018, 2, 28)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()

