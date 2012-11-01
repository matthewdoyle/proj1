from joy import *

class HelloJoyApp( JoyApp ):
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
    JoyApp.__init__(self, robot={'count':4},*arg,**kw)
    # Store output specifier for later use
    self.spec = spec
    
  def onStart(self):
    # This function is called when the JoyApp is ready to start up,
    # i.e. after all PyGame devices have been activated, robot Cluster
    # is dpopulated, scratch interface is live, etc.
    self.output = self.setterOf(self.spec)

  def onEvent(self,evt):
    # All unknown events --> punt to superclass
    #if evt.type != MOUSEMOTION or evt.buttons[0] == 0:
      #return JoyApp.onEvent(self,evt)
	if (evt.type != KEYDOWN) and (evt.type != KEYUP):
		return JoyApp.onEvent(self,evt)
	self.robot.at.left.set_mode(1)
	self.robot.at.right.set_mode(1)
	self.robot.at.back.set_mode(1)
	self.robot.at.front.set_mode(1)
	speed = 0.3
#  0  , 1 up on dpad
#  0  ,-1 down on dpad
# -1  , 0 left on dpad
#  1  , 0 right on dpad

#GO RIGHT
	if (evt.key == 275):
		progress('right')
		self.robot.at.front.set_torque(speed)
		self.robot.at.back.set_torque(-speed)
		self.robot.at.left.go_slack
		self.robot.at.right.go_slack()
#GO LEFT
	if (evt.key == 276):
		progress('left')
		self.robot.at.left.go_slack()
		self.robot.at.right.go_slack()
		self.robot.at.back.set_torque(speed)
		self.robot.at.front.set_torque(-speed)
#GO FORWARD
	if (evt.key == 273):
		progress('fwd')
		self.robot.at.front.go_slack()
		self.robot.at.back.go_slack()
		self.robot.at.left.set_torque(speed)
		self.robot.at.right.set_torque(-speed)
#GO BACKWARD
	if (evt.key == 274):
		progress('bwd')
		self.robot.at.front.go_slack()
		self.robot.at.back.go_slack()
		self.robot.at.left.set_torque(-speed)
		self.robot.at.right.set_torque(speed)
	if (evt.type == KEYUP):
		progress('nothing')
#		self.robot.at.left.go_slack()
		self.robot.at.left.set_torque(0)
#		self.robot.at.back.go_slack()
#		self.robot.at.front.go_slack()
		self.robot.at.back.set_torque(0)
		self.robot.at.front.set_torque(0)
		self.robot.at.right.set_torque(0)
#		self.robot.at.right.go_slack()
  
app = HelloJoyApp("#output ")
app.run()
