'''
Created on Mar 6, 2011

@author: eplaster
'''
from pyvisdk.consts import ComputeResourcesTypes, HistoryCollectorTypes
from pyvisdk.mo.consts import ManagedEntityTypes
from suds import MethodNotFound
import logging
import os.path
import suds

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class Client(object):
    '''
    The Client class acts as a proxy to the suds.client.Client class, in that it fixes the
    ManagedObjectReference objects and provides a more streamline interface specific to VISDK
    '''
    def __init__(self, server, timeout=90):
        '''
        Constructor
        '''
        wsdl_dir = os.path.abspath(os.path.dirname(__file__))
        url = "https://" + server + '/sdk'
        client = suds.client.Client("file://" + os.path.join(wsdl_dir, 'wsdl', 'vimService.wsdl'))
        client.set_options(faults=True)
        client.set_options(location=url)
        client.set_options(timeout=timeout)
        self.service = client.service
        self.url = url
        self.client = client
        self.server = server

    #
    # proxying (special cases)
    #
    def __getattribute__(self, attr):
        service = super(Client, self).__getattribute__("service")
        
        # try the service
        try:
            _attr = getattr(service, attr)
            if _attr.__class__ == suds.client.Method:
                # we need to do something about getting to the right method here...
                return _attr
            else:
                return _attr
        except (AttributeError, MethodNotFound):
            # see if it's in the client object
            try:
                client = super(Client, self).__getattribute__("client")
                _attr = getattr(client, attr)
                return _attr
            except (AttributeError, MethodNotFound):
                # if it's a member of this class...
                return super(Client, self).__getattribute__(attr)
            
    
    def typeIsA(self, searchType, foundType):
        if searchType == foundType:
            return True
        elif searchType == "ManagedEntity":
            for me in ManagedEntityTypes:
                if me == foundType:
                    return True
        elif searchType == "ComputeResource":
            for me in ComputeResourcesTypes:
                if me == foundType:
                    return True
        elif searchType == "HistoryCollector":
            for me in HistoryCollectorTypes:
                if me == foundType:
                    return True
        return False
