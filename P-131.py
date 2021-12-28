import pandas as pd
import csv
import plotly.express as px

rows = []

with open("scraper300.csv")as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
headers[0] = "row_num"

temp_star_data_rows = list(star_data_rows)
for star_data in temp_star_data_rows:
    star_mass = star_data[3]
    star_radius = star_data[4]

#gravity = (float(star_mass[index])*1.989e+30)/(float(star_radius[index])*float(star_radius[index])*6.957e+8)*6.674e-11
#gravity = (float(star_mass[index])*5.972e+24)/(float(star_radius[index])*float(star_radius[index])*6371000*6371000)*6.674e-11
#gravity = (star_mass[index]*5.972e+24)/(star_radius[index]*star_radius[index]*6371000*6371000)*6.674e-11

star_gravity = []
for index, name in enumerate(star_mass):
  gravity = (float(star_mass[index])*5.972e+24)/(float(star_radius[index])*float(star_radius[index])*6371000*6371000)*6.674e-11
  star_gravity.append(gravity)

with open("scraper300.csv", "w")as f:
  csvwriter = csv.writer(f)
  csvwriter.writerow(star_gravity)