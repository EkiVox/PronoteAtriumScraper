import falcon
from FETCHER import OPwithID
import json
class fetch:
    def on_get(self, req, resp):
        if req.get_param("id"):
            print "[" + req.get_param("id") + "] received get"
            quote = json.dumps(OPwithID().Fetch(req.get_param("id")))
            if quote == '"IDError"':
                resp.status = falcon.HTTP_503
                print "[" + req.get_param("id") + "] IDError"
            else:   
                resp.status = falcon.HTTP_200
                resp.body = quote
                print "[" + req.get_param("id") + "] Courses fetched"

class store:
    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

        if req.get_param("id"):
            if req.get_param("pw"):
                try:
                    result = json.loads(raw_json, encoding='utf-8')
                    OPwithID().Store(req.get_param("id"), req.get_param("pw"), result)
                    resp.body = 'CREDITS SAVED'
                except ValueError:
                    falcon.HTTPError(falcon.HTTP_400,'Invalid JSON','Could not decode the request body. The ''JSON was incorrect.')
        print "[" + req.get_param("id") + "] received post"

api = falcon.API()
api.add_route('/fetch', fetch())
api.add_route('/store', store())
