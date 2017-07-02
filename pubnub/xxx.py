import time
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconf = PNConfiguration()
pnconf.subscribe_key = "sub-c-49b1aafe-19f4-11e7-894d-0619f8945a4f"
pnconf.publish_key = "pub-c-860897e3-bc4e-4d19-9e11-dfaeee7284b3"
pubnub = PubNub(pnconf)
channel = "pidemo"

###reading raw data from 8051###
while True:
 t=45
 hb=12
 x=12
 y=13
 z=15  
 pubnub.publish().channel(channel).message({'TEMP':str(t),'HB':str(hb),'X':str(x),'Y':str(y),'Z':str(z)}).sync()
    


