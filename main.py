import pandas as pd
import stats
import parse
import printer

print("LVAG:")
lvag_nginx_csv = pd.read_csv("lvag-nginx.csv")
lvag_dc_csv = pd.read_csv("lvag-dc.csv")
lvag_nginx_data = parse.LVAG(lvag_nginx_csv)
lvag_dc_data = parse.LVAG(lvag_dc_csv)

for key in lvag_nginx_data:
    printer.printf(key, lvag_nginx_data, lvag_dc_data, service="LVAG")

print("LTMS:")
ltms_nginx_csv = pd.read_csv("ltms-nginx.csv")
ltms_dc_csv = pd.read_csv("ltms-dc.csv")
ltms_nginx_data = parse.LTMS(ltms_nginx_csv)
ltms_dc_data = parse.LTMS(ltms_dc_csv)

for key in ltms_nginx_data:
    printer.printf(key, ltms_nginx_data, ltms_dc_data, service="LTMS")
