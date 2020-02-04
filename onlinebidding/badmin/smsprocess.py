def smsprocess(contact,message):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=" + message + "&language=english&route=p&numbers=" + contact
    headers = {
        'authorization': "YJ2kOT4mqauNWUleypHgdXvx510GcCbhViFfQrRLztDPSA9w3IJ5tV06wOZqMFDb8H2ckrnoh4TflNPa",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    s1 = response.text
    return s1