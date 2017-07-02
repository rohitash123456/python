import time
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import Pubnub
#import serial

#ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=5)
#while True:
   # print s
  #  pnconf = PNConfiguration()
    pnconf.subscribe_key = "sub-c-077eca30-340d-11e7-81b3-02ee2ddab7fe"
    pnconf.publish_key = "pub-c-df8834de-1092-41eb-bff8-29f753a7184b"
    pubnub = PubNub(pnconf)
    channel = "Channel1"
    print "dainth"
    print 'connected'
    pubnub.publish().channel(channel).message({'TEMEPARATURE': t[:3], 'HEARTBEAT': h[:3], 'ACC':a[:3]}).sync()
    #result = my_listener.wait_for_message_on(channel)
    #print(result.message)
