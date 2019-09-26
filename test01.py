import vrep

if __name__ == '__main__':
    clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to V-REP
    if clientID!=-1:
        print ('Connected to remote API server')

        # control loop
        emptyBuff = bytearray()
        pose = [0.]*16
        pose[0] = 1.0; pose[5] = 1.0; pose[10] = 1.0
        pose[12] = 0.1; pose[13] = 0.2; pose[14] = 0.3; pose[15] = 1.
        for i in range(10):
            res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,'ABB_IRB52', \
                vrep.sim_scripttype_childscript,'hapPose',[],pose,[],emptyBuff, \
                vrep.simx_opmode_blocking)
            if res==vrep.simx_return_ok:
                print ('hapPose #%d'%i)
            '''    
            res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,'ABB_IRB52', \
                vrep.sim_scripttype_childscript,'hapForce',[],[],[],emptyBuff, \
                vrep.simx_opmode_streaming)
            if res==vrep.simx_return_ok:
                print ('hapForce #%d'%i)
            '''    

        # Now close the connection to V-REP:
        vrep.simxFinish(clientID)
