import logging


class ExtraLog(object):

    def process_request(self, request):
        
        agent = request.META.get('HTTP_USER_AGENT', "unknown")
        logging.critical(agent)
                    
        return None