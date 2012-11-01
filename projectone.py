#w: 2 dimensional list
#dict key w, f, b


for x in range(0,3):
    placer=dic["w"]
    current_x=dic["w"][x][0]
    current_y=dic["w"][x][1]
    next_x=dic["w"][x+1][0]
    next_y=dic["w"[x+1][1]
    if(len(placer)>0):
        distancex=current_x-next_x
        distancey=current_y-next_y
        starting_length=len(placer)
        if(0<distancex<.25 and .25<distancey or -.25<distancex<0 and .25<distancey ): #up only
           while(len(placer)==starting_length):
               #robot.front.at.set_torque(.25)
               #robot.back.at.set_torque(.25)
           continue
         elif(0<distancex<0.25 and .-25<distancey or -.25<distancex<0 and -.25<distancey ): #down only
           while(len(placer)==starting_length):
               #robot.front.at.set_torque(-.25)
               #robot.back.at.set_torque(-.25)
            continue
         elif(0<distancey<.25 and .25<distancex or -.25<distancey<0 and .25<distancex ):
            while(len(placer)==starting_length): #rihgt only
               #robot.right.at.set_torque(.25)
               #robot.left.at.set_torque(.25)
            continue
         elif(0<distancey<0.25 and .-25<distancex or -.25<distancey<0 and -.25<distancex):            #left only
           while(len(placer)==starting_length):
               #robot.right.at.set_torque(-.25)
               #robot.left.at.set_torque(-.25)
            continue
          elif(distancey>0.25 and distancex>0.25):  #right diagnol Northeast movement
            while(len(placer)==starting_length):
               while(dict["f"]>50):
                  #robot.front.at.set_torque(.25)
                  #robot.back.at.set_torque(.25)
               while(dict["f"]-dict["b"]>10 or dict["f"]-dict["b"]<-10):
                  #robot.right.at.set_torque(.25)
                  #robot.left.at.set_torque(.25)
             continue
           elif(distancey<-0.25 and distancex<-0.25): #down left diagnlo Southwest movemnt
            while(len(placer)==starting_length):
               while(dict["f"]>50):
                  #robot.front.at.set_torque(-.25)
                  #robot.back.at.set_torque(-.25)
               while(dict["f"]-dict["b"]>10 or dict["f"]-dict["b"]<-10):
                  #robot.right.at.set_torque(-.25)
                  #robot.left.at.set_torque(-.25)
             continue
            elif(distancey>0.25 and distancex<-0.25): #Northwest movement
            while(len(placer)==starting_length):
               while(dict["f"]>50):
                  #robot.front.at.set_torque(.25)
                  #robot.back.at.set_torque(.25)
               while(dict["f"]-dict["b"]>10 or dict["f"]-dict["b"]<-10):
                  #robot.right.at.set_torque(-.25)
                  #robot.left.at.set_torque(-.25)
              continue
            elif(distancey<-0.25 and distancex>0.25): #south east movement
            while(len(placer)==starting_length):
               while(dict["f"]>50):
                  #robot.front.at.set_torque(-.25)
                  #robot.back.at.set_torque(-.25)
               while(dict["f"]-dict["b"]>10 or dict["f"]-dict["b"]<-10):
                  #robot.right.at.set_torque(-.25)
                  #robot.left.at.set_torque(-.25)
              continue 
      else:
         break


