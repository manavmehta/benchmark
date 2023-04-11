
def LTMS(ltms):

    data_nginx = {}

    for i in ltms.index:
        if ltms["api"][i] not in data_nginx:
            data_nginx[ltms["api"][i]] = []
        
        data_nginx[ltms["api"][i]].append(ltms["duration"][i])
    return data_nginx

def LVAG(lvag):

    data_nginx = {}

    for i in lvag.index:
        RPP = lvag["revProxyPath"][i]
        if RPP.find("streamer/addIceCandidate") != -1:
            RPP = "streamer/addIceCandidate"
        elif RPP.find("streamer/getIceCandidate") != -1:
            RPP = "streamer/getIceCandidate"
        elif RPP.find("video/stop") != -1:
            RPP = "video/stop"
        elif RPP.find("video/start") != -1:
            RPP = "video/start"
        elif RPP.find("streamer/video") != -1:
            RPP = "streamer/video"
        elif RPP.find("streamer/hangup") != -1:
            RPP = "streamer/hangup"
        elif RPP.find("system/browser") != -1:
            RPP = "system/browser"
        elif RPP.find("system/dir") != -1:
            RPP = "system/dir"
        if RPP not in data_nginx:
            data_nginx[RPP] = []
        
        data_nginx[RPP].append(float(lvag["duration"][i][0:-2:]))
    return data_nginx

# ltms_dc_csv.drop(['_messagetimems', '_messagetime', 'ip', 'z', 'zz', 'zzz', 'zzzz', '_raw'], axis=1, inplace=True)
