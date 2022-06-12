import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
x,y,z = 0,0,0.5
length, width, height = 1,1,1
for i3 in range(5):
    for i2 in range(5):
        for i in range(10):
            pyrosim.Send_Cube(name="box", pos=[x,y,z] , size=[length,width,height])
            z += 1
            length = .90 * length
            width = .90 * width
            height = .90 * height
        x += 1
        z = 0.5
        length, width, height = 1,1,1
    y +=1
    x = 0
    z = 0.5
    length, width, height = 1,1,1
pyrosim.End()