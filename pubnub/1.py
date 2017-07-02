from pubnub import Pubnub

pubnub = Pubnub(
 #   publish_key = "publish_key_here",
#subscribe_key = "subscribe_key_here")


#pnconf = PNConfiguration()

	publish_key = "pub-c-df8834de-1092-41eb-bff8-29f753a7184b",
	subscribe_key = "sub-c-077eca30-340d-11e7-81b3-02ee2ddab7fe")
#pubnub = PubNub(pnconf)
channel = "Channel1",
message="A mesage"

print "dainth"
print 'connected'

pubnub.publish(
	channel=channel,
	message="A message")
