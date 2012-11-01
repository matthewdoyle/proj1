from joy import *
from socket import socket, AF_INET, SOCK_STREAM, error as SocketError
from json import loads as json_loads

class SensorPlan( Plan ):
  """
  SensorPlan is a concrete Plan subclass that uses the self.app's
  remote plan to read and decode WayPoint Task sensor and waypoint
  updates.
  """
  def __init__( self, app, peer, *arg, **kw ):
    Plan.__init__(self, app, *arg, **kw )
    self.sock = None
    self.peer = peer
    self.lastSensorReading = None
 
  def _connect( self ):
    s = socket(AF_INET, SOCK_STREAM)
    try:
       s.connect( self.peer )
    except SocketError, se:
       progress("Failed to connect: "+str(se))
       return
    s.setblocking(0)
    self.sock = s

  def stop( self ):
    if self.sock is not None:
      self.sock.close()
    self.sock = None

  def behavior( self ):
    while True:
      # if not connected --> try to connect
      if self.sock is None:
        self._connect()
      # if not connected --> sleep for a bit
      if self.sock is None:
        yield self.forDuration(0.1)
        continue
      # receive an update / skip
      try:
        msg = self.sock.recv(1024)
      except SocketError, se:
        # If there was no data on the socket --> not a real error, else
        if se.errno != 11:
          progress("Connection failed: "+str(se))
          self.sock.close()
          self.sock = None
        yield
        continue
      ts = self.app.now
      dic = json_loads(msg)
      self.lastSensorReading = (ts, dic['f'], dic['b'])
      #assert type(dic) is dict
      #dic = dic.items()
      #dic.sort()
      #progress("Message received at: " + str(ts))
      #for k,v in dic:
      #  progress("   %s : %s" % (k,repr(v)))
      yield self.forDuration(0.3)

class WaypointSensorApp( JoyApp ):
  def onStart( self ):
    # Set up the sensor receiver plan
    self.sensor = SensorPlan(self,("67.194.202.70",8080))
    self.sensor.start()
    
  def onEvent( self, evt ):
    # Punt to superclass
    # this is here to remind you to override it
    if evt.type is KEYDOWN and evt.key is K_p:
      progress('Sensor :'+str(self.sensor.lastSensorReading))
    return super( WaypointSensorApp, self ).onEvent(evt)
  
  def onStop( self ):
    self.sensor.stop()
    return super( WaypointSensorApp, self ).onStop()
      
if __name__=="__main__":
  print """
  Running the waypoint sensor demo
  
  Connects to waypoint application and reads sensor.
  
  The waypoint sensor send JSON maps with keys:
  'f', 'b' : front and back sensor values
  'w' : list of lists. Each sub-list is of length 2. List of waypoint
    coordinates, including the next waypoint. Each time the next 
    waypoint changes, it means the previous waypoint was reached.
  """
  #app=WaypointSensorApp()
  #app.run()


'''
su - hrb-team2 # team user
'''
class myApp( JoyApp ):
	"""HelloJoyApp

		 The "hello world" of JoyApp programming.
		 This JoyApp pipes the y coordinate of mouse positions (while left
		 button is pressed) to a specified setter. By default this setter is
		 given by "#output " -- i.e. it is a debug message. 
		 
		 See JoyApp.setterOf() for a specification of possible outputs
	"""
def __init__(self,spec,*arg,**kw):
		# This is a "constructor". It initializes the JoyApp object.
		# Because we added an additional parameter, we extend the 
		# JoyApp constructor. The first step is to call the superclass
		# constructor so that we'll have a valid JoyApp instance.
	JoyApp.__init__(self,robot={'count':4}, *arg,**kw)
		# Store output specifier for later use
	self.spec = spec

def onStart(self):
		# This function is called when the JoyApp is ready to start up,
		# i.e. after all PyGame devices have been activated, robot Cluster
		# is populated, scratch interface is live, etc.
	self.sensor = SensorPlan(self,("67.194.202.70",8080))
	self.sensor.start()
	self.output = self.setterOf(self.spec)

def onEvent(self,evt):
		# All unknown events --> punt to superclass
		#if evt.type != MOUSEMOTION or evt.buttons[0] == 0:
			#return JoyApp.onEvent(self,evt)
	if (evt.type != KEYDOWN and evt.type != KEYUP):
		return JoyApp.onEvent(self,evt)
	progress('Sensor :'+str(self.sensor.lastSensorReading))
	speed = 0.1
		#  0  , 1 up on dpad
		#  0  ,-1 down on dpad
		# -1  , 0 left on dpad
		#  1  , 0 right on dpad

		#GO RIGHT
	if (evt.key == K_RIGHT):
		progress('right')
		self.robot.at.left.go_slack()
		self.robot.at.right.go_slack()
		self.robot.at.front.set_torque(speed)
		self.robot.at.back.set_torque(-speed)

		#GO LEFT
	if (evt.key == K_LEFT):
		progress('left')
		self.robot.at.left.go_slack()
		self.robot.at.right.go_slack()
		self.robot.at.back.set_torque(speed)
		self.robot.at.front.set_torque(-speed)
		#GO FORWARD
	if (evt.key == K_UP):
		progress('fwd')
		self.robot.at.front.go_slack()
		self.robot.at.back.go_slack()
		self.robot.at.left.set_torque(speed)
		self.robot.at.right.set_torque(-speed)
		#GO BACKWARD
	if (evt.key == K_DOWN):
		progress('bwd')
		self.robot.at.front.go_slack()
		self.robot.at.back.go_slack()
		self.robot.at.left.set_torque(-speed)
		self.robot.at.right.set_torque(speed)
	if (evt.type == KEYUP):
		progress('nothing')

		self.robot.at.left.set_torque(0.0)
		self.robot.at.back.set_torque(0.0)
		self.robot.at.front.set_torque(0.0)
		self.robot.at.right.set_torque(0.0)

def onStop( self ):
	self.sensor.stop()
  
app = myApp("#output ")
app.run()


