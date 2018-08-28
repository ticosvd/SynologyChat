import config
import requests,argparse


parser=argparse.ArgumentParser(description='Sending to Synology Chat')

parser.add_argument('-s','--strings',help='The sending string',required=True)
parser.add_argument('-t','--token',help='The bot token')
args=parser.parse_args()


url = "https://"+config.serverurl+"/webapi/entry.cgi"

querystring = {"api":"SYNO.Chat.External","method":"incoming","version":"2","token":config.token}
text=args.strings

payload = 'payload='+ requests.compat.quote('{"text":"'+text+'"}')
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
response = requests.request("POST", url, data=payload, headers=headers, params=querystring,verify=False)

print(response.text)
