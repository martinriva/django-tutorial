import logging


class MiMiddleware(object):

    def process_request(self, request):
          
        logging.critical("[Miidleware] request. %s" % request.META['PATH_INFO'])
                    
        return None
    
    def process_response(self, request, response):
        
        logging.critical("[Miidleware] response")
                    
        return response