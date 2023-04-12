import stats

NGINX, DC, MS = "NGINX:", "DC:", "ms"

def printf(key, nginx, dc, service):
    if service == "LTMS":
        printLTMS(key, nginx, dc)
    else:
        printLVAG(key, nginx, dc)
    
def printLTMS(key, nginx, dc):
    print(key)
    print("min - ", NGINX, min(nginx[key]), DC, min(dc[key]))
    print("p10 - ", NGINX, stats.p10(nginx[key]), DC, stats.p10(dc[key]))
    print("avg - ", NGINX, stats.mean(nginx[key]), DC, stats.mean(dc[key]))
    print("p50 - ", NGINX, stats.p50(nginx[key]), DC, stats.p50(dc[key]))
    print("p90 - ", NGINX, stats.p90(nginx[key]), DC, stats.p90(dc[key]))
    print("max - ", NGINX, max(nginx[key]), DC, max(dc[key]))
    print()

def printLVAG(key, nginx, dc):
    print(key)
    print("min - ", NGINX, min(nginx[key]), MS, DC, min(dc[key]), MS)
    print("p10 - ", NGINX, stats.p10(nginx[key]), MS, DC, stats.p10(dc[key]), MS)
    print("avg - ", NGINX, stats.mean(nginx[key]), MS, DC, stats.mean(dc[key]), MS)
    print("p50 - ", NGINX, stats.p50(nginx[key]), MS, DC, stats.p50(dc[key]), MS)
    print("p90 - ", NGINX, stats.p90(nginx[key]), MS, DC, stats.p90(dc[key]), MS)
    print("max - ", NGINX, max(nginx[key]), MS, DC, max(dc[key]), MS)
    print()
