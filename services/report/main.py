from http.server import BaseHTTPRequestHandler, HTTPServer
import json,os,urllib.request
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  try:
   if self.path=='/health': body={'ok':True,'service':'python-report'}
   else:
    with urllib.request.urlopen(os.environ.get('ADAPTER_URL','http://adapter:8092')+'/ledger',timeout=10) as r: data=json.load(r)
    body={'service':'python-report','adapter':data,'total':sum(x['amount'] for x in data['entries'])}
   self.send_response(200)
  except Exception as error: self.send_response(502);body={'error':str(error),'service':'python-report'}
  self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(json.dumps(body).encode())
HTTPServer(('0.0.0.0',int(os.environ.get('PORT','8091'))),Handler).serve_forever()
