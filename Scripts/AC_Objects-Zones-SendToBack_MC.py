##########################################
##### AC_objects-Zones-SendToBack.py #####
##########################################
# Selects all objects and zones and sends them back
# 2023_06_03
# V1.1
# @mi_jan
# Cursor Coordinates work only if using Screen Resolution: 1728 x 1117 (default resolution for Mac Book Pro 16”)

import pyautogui
import time

### Set delay in seconds
action_delay = 0.2
start_delay = 3

### set the variables for each cursor coordinate

position1 = (281, 17) #Design
position2 = (573, 51) #Architectural Tools
position3 = (690, 530) #Object Tool
position4 = (690, 459) #Zone Tool
position5 = (183, 17) #Edit
position6 = (240,415) #Display Order
position7 = (570,487) #Send to back

#############################################################################################
######################################## Main script ########################################
#############################################################################################

time.sleep(start_delay)

#### Activate the Object Tool, and Press Select All to select all visible objects ####
# Move cursor & click: Design Menu
pyautogui.moveTo(position1[0], position1[1])
pyautogui.click()
time.sleep(action_delay)

# Move cursor: Architectural Tools
pyautogui.moveTo(position2[0], position2[1])
time.sleep(action_delay)

# Move cursor & click: Object Tool
pyautogui.moveTo(position3[0], position3[1])
pyautogui.click()
time.sleep(action_delay)

##### Press Key sequence/Keyboard shortcut for: Select All
# Note: keys will be pressed in order, and released in reverse order #
pyautogui.hotkey('command', 'a')
time.sleep(action_delay)

#### Activate the Zone Tool, and Press Select All to select all visible zones ####
# Move cursor & click: Design Menu
pyautogui.moveTo(position1[0], position1[1])
pyautogui.click()
time.sleep(action_delay)

# Move cursor: Architectural Tools
pyautogui.moveTo(position2[0], position2[1])
time.sleep(action_delay)

# Move cursor & click: Zone Tool
pyautogui.moveTo(position4[0], position4[1])
pyautogui.click()
time.sleep(action_delay)

##### Press Key sequence/Keyboard shortcut for: Select All
# Note: keys will be pressed in order, and released in reverse order #
pyautogui.hotkey('command', 'a')
time.sleep(action_delay)


#### Send To back all selected elements ####
# Move cursor & click: Edit
pyautogui.moveTo(position5[0], position5[1])
pyautogui.click()
time.sleep(action_delay)

# Move cursor: Display Order
pyautogui.moveTo(position6[0], position6[1])
time.sleep(action_delay)

# Move cursor & click: Send to back
pyautogui.moveTo(position7[0], position7[1])
pyautogui.click()
time.sleep(action_delay)

##### Press Key: Escape
pyautogui.hotkey('esc')
pyautogui.hotkey('esc')
