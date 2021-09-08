import json, falcon

class ObjRequstClass:
    def on_get(self, req, resp):
        content= {
            'name':'Sami',
            'age' :'21',
            'country' :'India',
        }

        resp.body=json.dumps(content)
         

app=falcon.App()
app.add_route('/test', ObjRequstClass())
