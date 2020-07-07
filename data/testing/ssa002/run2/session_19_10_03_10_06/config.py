# Copyright (c) 2007-2012, Michael J. Kahana.
#
# This file is part of PandaEPL.
#
# PandaEPL is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Alec Solway
# URL: http://memory.psych.upenn.edu/PandaEPL

## notes for set-up:
# to change environment models loaded by TboyLite_multienv.py, don't touch anything EXCEPT the numbers in the environs vector in this file


##########################
# Core PandaEPL settings.#
##########################

FOV = 70

# Movement.
linearAcceleration  = 100 # set >= fullForward speed for ~"instant" acceleration
fullForwardSpeed    = 4.25
fullBackwardSpeed   = 0 # set to 0 for no backward motion 
turningAcceleration = 300
fullTurningSpeed    = 35
turningLinearSpeed  = 0.25 # Factor

maxTurningLinearSpeed          = 7.0
minTurningLinearSpeedReqd      = 1.0
minTurningLinearSpeed          = 1.5
minTurningLinearSpeedIncrement = 0.5 


# Starting Position.

# (PER ENV).
#newstartPos = [,,,,,,,,,,]
initialPos = Point3(0,0,0) #this is a "dummy" position, we will immediate replace with one of the positions below
initialPos1 = Point3(4,20,0.8)
initialPos2 = Point3(44,24,0.8)
initialPos3 = Point3(20,16,0.8)
initialPos4 = Point3(16,44,0.8)
initialPos5 = Point3(4,8,0.8)
initialPos6 = Point3(28,0,0.8)
initialPos7 = Point3(32,-4,0.8)
initialPos8 = Point3(20,36,0.8)
initialPos9 = Point3(4,8,0.8)
initialPos10 = Point3(28,20,0.8)
initialPos11 = Point3(52,20,0.8)
initialPos12 = Point3(16,20,0.8)

# (PER ENV).
#initialHead = [,,,,,,,,,,,]
initialHead1 = [[270.0]]
initialHead2 = [[0.0]]
initialHead3 = [[0.0]]
initialHead4 = [[90.0]]
initialHead5 = [[0.0]]
initialHead6 = [[180.0]]
initialHead7 = [[270.0]]
initialHead8 = [[180.0]]
initialHead9 = [[180.0]]
initialHead10 = [[270.0]]
initialHead11 = [[180.0]]
initialHead12 = [[270.0]]


avatarRadius = 0.5
cameraPos    = Point3(0, 0, 0.8)
friction     = 0.4
movementType = 'walking' # car | walking

# Not being used. Leave anyway just in case.
#second positions within envs
laterPos = [Point3(52,26,0.8),Point3(4,46,0.8), Point3(34,4,0.8),Point3(18,4,0.8),Point3(42,52,0.8),Point3(28,12,0.8),Point3(6,46,0.8),Point3(50,46,0.8),Point3(14,50,0.8),Point3(10,30,0.8),Point3(44,46,0.8),Point3(12,50,0.8)]#Env avatar reposition locs
#laterPos = [Point3(-5,-31,0.5),Point3(-41,-5,0.5)]#Env avatar reposition locs
laterHead = [[-90.0],[-90.0],[-90.0],[-90.0],[-90.0],[-90.0],[-90.0],[-90.0],[-90.0],[-90.0],[-90.0],[-90.0]]


# Instructions.
instructSize    = 0.075
#instructFont    = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'; # Linux
#instructFont    = '/Library/Fonts/Microsoft/Times New Roman.ttf';    # Mac OS X
instructFont    = '/c/Windows/Fonts/times.ttf';                      # Windows
instructBgColor = Point4(0, 0, 0, 1)
instructFgColor = Point4(1, 1, 1, 1)
instructMargin  = 0.06
instructSeeAll  = False

################################
# Experiment-specific settings.#
###############################

# Shops
shopDir = '../../../../models/stores/'
shopLocs = [[100,23,90],[100,-13,90],[100,14,90]]
shopZ    = 0.11
numShops = len(shopLocs)

# Stores ~ these are goal items, not necessarily stores
#storeDir  = './models/stores/'
storeDir  = '../../../../models/goals/SSAgoals/'


# Goal Coordinates (PER ENV).
#environment 1
storeLocs1 = [[12,20,270],[36,8,270],[4,44,180]] # [x, y, orientation] B(face),A(animal),C(other)
#environment 2
storeLocs2 = [[44,42,90],[20,4,90],[33.5,50,90]]
#environment 3
storeLocs3 = [[50,50,90],[4,46,90],[44,28,90]]
#environment 4
storeLocs4 = [[22,44,90],[52,34,90],[12,22,90]]
#environment 5
storeLocs5 = [[4,20,0],[44,20,90],[28,36,270]]
#environment 6
storeLocs6 = [[52,30,90],[42,6,90],[42,44,90]]
#environment 7
storeLocs7 = [[52,28,90],[20,8,90],[28,36,90]]
#environment 8
storeLocs8 = [[52,16,180],[40,52,270],[12,20,90]]
#environment 9
storeLocs9 = [[4,18,90],[20,6,90],[28,46,90]]
#environment 10
storeLocs10 = [[36,52,270],[12,32,0],[52,16,180]]
#environment 11
storeLocs11 = [[40,36,90],[36,20,270],[12,36,90]]
#environment 12
storeLocs12 = [[36,4,90],[52,48,180],[20,28,0]]


# Finish Lines (PER ENV).
custLocs1 = [[4,24,180]]#location of custom goal for, e.g., training
custLocs2 = [[12,52,90]]#location of custom goal for, e.g., training
custLocs3 = [[20,52,270]]#location of custom goal for, e.g., training
custLocs4 = [[4,12,180]]#location of custom goal for, e.g., training
custLocs5 = [[4,4,0]]#location of custom goal for, e.g., training
custLocs6 = [[52,14,0]]#location of custom goal for, e.g., training
custLocs7 = [[52,32,0]]#location of custom goal for, e.g., training
custLocs8 = [[24,36,90]]#location of custom goal for, e.g., training
custLocs9 = [[36,20,180]]#location of custom goal for, e.g., training
custLocs10 = [[28,24,180]]#location of custom goal for, e.g., training
custLocs11 = [[48,20,270]]#location of custom goal for, e.g., training
custLocs12 = [[12,20,270]]#location of custom goal for, e.g., training
custZ = 0.2

storeZ    = 0.5 #z (vertical) coordinate shared by all stores
numStores = len(storeLocs1)

# Height of objects above
storeZ    = 0.5 #z (vertical) coordinate shared by all stores
numStores = len(storeLocs1)

# Finish Line Barrier
barrLocs1 = [[4,23.5,180]]
barrLocs5 = [[4,4.5,0]]
barrLocs8 = [[23.5,36,90]]
barrLocs10 = [[28,23.5,180]]
barrLocs11 = [[48.5,20,270]]
barrLocs12 = [[12.5,20,270]]
barrZ = 0.2

# Buildings.
buildingDir  = '../../../../models/buildings/'    
#environment 1
buildingLocs = [[-50,50],[-50,41],[-32,50],[-32,41],[-50,23],[-50,14],[-32,23],[-32,14]]#bldg7 #[31,23],

buildingZ    = 0.25 #z (vertical) coordinate shared by all buildings
numBuildings = len(buildingLocs)


# Barriers.
barrierDir  = '../../../../models/barriers/'   
#10-unit barriers (1 building size)
barrier1Locs = [[-50,37],[-32,37],[-41,53],[-50,27],[-32,27],[-41,10],[-55,32],[-27,32]]
numBarriers1 = len(barrier1Locs)
#20-unit barriers
barrier2Locs = [[-46,45.5],[-36,45.5],[-46,18.5],[-36,18.5]]
numBarriers2 = len(barrier2Locs)
#etc..
barrier3Locs = []
numBarriers3 = len(barrier3Locs)

barrier4Locs = []
numBarriers4 = len(barrier4Locs)

barrier5Locs = []
numBarriers5 = len(barrier5Locs)

barrierZ    = 0 #z (vertical) coordinate shared by all buildings


# Terrain, sky.
terrainModel1  = '../../../../models/SST_towns/town1_v1.bam'
terrainModel2  = '../../../../models/SST_towns/town2_v1.bam'
terrainModel3  = '../../../../models/SST_towns/town3_v1.bam'
terrainModel4  = '../../../../models/SST_towns/town4_v1.bam'
terrainModel5  = '../../../../models/SST_towns/town5_v1.bam'
terrainModel6  = '../../../../models/SST_towns/town6_v1.bam'
terrainModel7  = '../../../../models/SST_towns/town7_v1.bam'
terrainModel8  = '../../../../models/SST_towns/town8_v1.bam'
terrainModel9  = '../../../../models/SST_towns/town9_v1.bam'
terrainModel10  = '../../../../models/SST_towns/town10_v1.bam'
terrainModel11  = '../../../../models/SST_towns/town11_v1.bam'
terrainModel12  = '../../../../models/SST_towns/town12_v1.bam'

#terrainModel  = './models/towns/simpletown1_11x11.egg'
#terrainModel1  = './town1_1stpass.egg'
#terrainModel2 = '../models/building_blox/arena2_11x11.egg'
##terrainModel3 = '../models/building_blox/arena3_11x11.egg'
terrainCenter = Point3(0,0,0)
skyModel      = '../../../../models/sky/sky.bam'
skyScale      = 1.6


# Gameplay (CHANGE ENV ORDER).
deliveries = [0] # number of delivs per town e.g. [0, 1] for two delivs
#numDeliveries  = 24 #2 per env
environs = [1,11,8]
shockenvs = [0,0,0] # #which envs have shocks? 1 = yes
shockwarns = [0,0,0] # #which envs have shock warnings? All? Only true shock towns? 1 = yes
startingScore  = 0
deliveryBonus  = 50
scoreIncrement = 1
scoreIncrementInterval = 1000 # in ms


# Heads-up display.
fixationflag = 1 #if zero, code will display town shock status text instead of a fixation during ITI

scorePos   = Point3(0.83,0,1)
scoreSize  = 0.1
scoreColor = Point4(1,0,0,1)


# HUD assignment position.
assignmentPos   = Point3(-1,0,1)
assignmentSize  = 0.1
assignmentColor = Point4(1,0,0,1)


# Assignment cue screen position.
assignmentscreenPos   = Point3(-0.33,0,0.1)


# Victory screen position.
victoryscreenPos   = Point3(-0.52,0,0.1)

shockPos   = Point3(-0.85,0,0.1) # these coords roughly center the shock warning
shockSize  = 0.125
shockColor = Point4(1,1,0,1)

fixPos   = Point3(-0.03,0,0.1) # these coords roughly center the fixation
fixSize  = 0.25
fixColor = Point4(1,1,0,1)


# Command Keys (non-default).
keyboard = Keyboard.getInstance()
keyboard.bind("exit", ["escape", "q"])
keyboard.bind("toggleDebug", ["escape", "d"])
keyboard.bind("toggleFog", "f")
keyboard.bind("toggleLighting", "l")
keyboard.bind("recordSound", "r")
keyboard.bind("playSound", "p")
keyboard.bind("stopSound", "s")

joystick = Joystick.getInstance()
joystick.bind("toggleDebug", "joy_button0")


# Instructions.
instructionFile        = './instructions.txt'
deliveryMadeText       = 'You completed the route'
assignmentText         = 'navigate the route'
experimentCompleteText = 'Run finished'
shockWarning = '* SHOCK POSSIBLE in this environment *'
noshockWarning = '* safe environment *'
fixation = '+'


# Lighting.
initialLightingScheme   = 0
darkAmbientLightColor   = Point3(0.2,0.2,0.2)
brightAmbientLightColor = Point3(0.8,0.8,0.8)
directionalLightColor   = Point3(1,1,1)
directionalLightOrient  = Point3(270,0,0)
pointLightColor         = Point3(0.8,0.8,0.8)
pointLightPos           = initialPos
pointLightAttenuation   = Point3(0,0,0.01)
spotlightColor          = Point3(0.8,0.8,0.8)
spotlightPos            = initialPos
spotlightFallof         = 0.01 
spotlightHorzFov        = 50


# Fog.
initialFogScheme  = 0
expFogColor       = Point3(0.4,0.4,0.4)
expFogDensity     = 0.04
