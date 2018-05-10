import falcon
from FETCHER import OPwithID
import json
class fetch:
    def on_get(self, req, resp):
        if req.get_param("id"):
            if req.get_param("day"):
                day = req.get_param("day")
            else:
                day = 0
            print "[" + req.get_param("id") + "] received get"
            quote = OPwithID().Fetch(req.get_param("id"), day)
            if quote == "ConnectionError":
                resp.status = falcon.HTTP_503
                print "[" + req.get_param("id") + "] ConnectionError"
                resp.body = json.dumps("PRONOTE unreachable")
            elif quote == "BadID":
                resp.status = falcon.HTTP_404
                print "[" + req.get_param("id") + "] BadID"
                resp.body = json.dumps("Invalid ID or not associated with PRONOTE")
            else:
                quote = json.dumps(quote) 
                resp.status = falcon.HTTP_200
                resp.body = quote
                print "[" + req.get_param("id") + "] Courses fetched"

class store:
    def on_post(self, req, resp):
        print "[" + req.get_param("id") + "] received post"
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps('Stream unreadable')
        if req.get_param("id"):
            if req.get_param("pw"):
                try:
                    result = json.loads(raw_json, encoding='utf-8')
                    if type(result) == list or type(result) == tuple:
                        if len(result) == 2:
                            resultat = OPwithID().Store(req.get_param("id"), req.get_param("pw"), result)
                            if resultat == "BadID":
                                resp.status = falcon.HTTP_404
                                print "[" + req.get_param("id") + "] BadID"
                                resp.body = json.dumps("Invalid ID or PW or not associated with PRONOTE")      
                            else:
                                resp.status = falcon.HTTP_200
                                resp.body = json.dumps('Credits Saved')
                        else:
                            resp.status = falcon.HTTP_400
                            resp.body = json.dumps('List need 2 parameters')
                    else:
                        resp.status = falcon.HTTP_400
                        resp.body = json.dumps('Posted resource need to be a list or tuple')
                except ValueError:
                    falcon.HTTPError(falcon.HTTP_400,'Invalid JSON','Could not decode the request body. The ''JSON was incorrect.')
            else:
                resp.status = falcon.HTTP_400
                resp.body = json.dumps("Need PW parameter")
        else:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps("Need ID parameter")


api = falcon.API()
api.add_route('/fetch', fetch())
api.add_route('/store', store())
