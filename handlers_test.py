import unittest
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

import webapp2
import web


class TestHandlers(unittest.TestCase):

  def setUp(self):
    # First, create an instance of the Testbed class.
    self.testbed = testbed.Testbed()
    # Then activate the testbed, which prepares the service stubs for use.
    self.testbed.activate()
    # Create a consistency policy that will simulate the High Replication consistency model.
    self.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=0)
    # Initialize the datastore stub with this policy.
    self.testbed.init_datastore_v3_stub(consistency_policy=self.policy)

  def tearDown(self):
    self.testbed.deactivate()

  def testHello(self):
     # Build a request object passing the URI path to be tested.
     # You can also pass headers, query arguments etc.
     request = webapp2.Request.blank('/')
     # Get a response for that request.
     response = request.get_response(web.application)

     # Let's check if the response is correct.
     self.assertEqual(response.status_int, 200)
     self.assertIn('In the Cloud or Not', response.body)


if __name__ == '__main__':
  unittest.main()