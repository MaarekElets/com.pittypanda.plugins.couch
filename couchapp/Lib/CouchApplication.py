from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')

from com.pittypanda.plugins.couch.glue import CouchApplicationType

import couchapp.dispatch

class CouchApplication(CouchApplicationType, object):

    def __init__(self):
        print 'Initializing'
        pass

    def dispatch(self, args):
        return couchapp.dispatch.dispatch(args)

