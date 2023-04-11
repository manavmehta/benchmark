import stats

NGINX, DC, MS = "NGINX:", "DC:", "ms"

def printf(key, nginx, dc):
    print(key)
    print("min - ", NGINX, min(nginx[key]), MS, DC, min(dc[key]), MS)
    print("p10 - ", NGINX, stats.p10(nginx[key]), MS, DC, stats.p10(dc[key]), MS)
    print("avg - ", NGINX, stats.mean(nginx[key]), MS, DC, stats.mean(dc[key]), MS)
    print("p50 - ", NGINX, stats.p50(nginx[key]), MS, DC, stats.p50(dc[key]), MS)
    print("p90 - ", NGINX, stats.p90(nginx[key]), MS, DC, stats.p90(dc[key]), MS)
    print("max - ", NGINX, max(nginx[key]), MS, DC, max(dc[key]), MS)
    print()


# for key in lvag_nginx_data:
#     print(key)
#     print("min - ", NGINX, min(lvag_nginx_data[key]), DC, min(lvag_dc_data[key]))
#     print("p10 - ", NGINX, stats.p10(lvag_nginx_data[key]), DC, stats.p10(lvag_dc_data[key]))
#     print("avg - ", NGINX, stats.mean(lvag_nginx_data[key]), DC, stats.mean(lvag_dc_data[key]))
#     print("p50 - ", NGINX, stats.p50(lvag_nginx_data[key]), DC, stats.p50(lvag_dc_data[key]))
#     print("p90 - ", NGINX, stats.p90(lvag_nginx_data[key]), DC, stats.p90(lvag_dc_data[key]))
#     print("max - ", NGINX, max(lvag_nginx_data[key]), DC, max(lvag_dc_data[key]))
#     print()


# for key in ltms_nginx_data:
#     print(key)
#     print("min - ", NGINX, min(ltms_nginx_data[key]), DC, min(ltms_dc_data[key]))
#     print("p10 - ", NGINX, stats.p10(ltms_nginx_data[key]), DC, stats.p10(ltms_dc_data[key]))
#     print("avg - ", NGINX, stats.mean(ltms_nginx_data[key]), DC, stats.mean(ltms_dc_data[key]))
#     print("p50 - ", NGINX, stats.p50(ltms_nginx_data[key]), DC, stats.p50(ltms_dc_data[key]))
#     print("p90 - ", NGINX, stats.p90(ltms_nginx_data[key]), DC, stats.p90(ltms_dc_data[key]))
#     print("max - ", NGINX, max(ltms_nginx_data[key]), DC, max(ltms_dc_data[key]))
#     print()

