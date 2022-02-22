# In settings.json first activate computer vision mode: 
# https://github.com/Microsoft/AirSim/blob/master/docs/image_apis.md#computer-vision-mode

import airsim
import cv2
import numpy as np

c = airsim.VehicleClient()
# Get a list of existing objects in the environment
'''
#object_list = sorted(c.simListAssets())
object_list = sorted(c.simListSceneObjects())
for object_name in object_list:
  print(object_name)
'''

# For landscapemountains environment
found = c.simSetSegmentationObjectID("[\w]*", 0, True);
print("Done: %r" % (found))

compact_object_list = np.loadtxt("landscapemountains_objectlist.txt", dtype=str)
print(compact_object_list)
i = 1
for object_name in compact_object_list:
    found = c.simSetSegmentationObjectID(object_name+"[\w]*", i, True)
    if found:
        print("%s %i" % (object_name, i))
        i += 1
