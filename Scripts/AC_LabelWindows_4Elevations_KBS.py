##########################################
##### AC_LabelWindows_4Elevations.py #####
##########################################
## Activates Window tool, selects all, labels them, switches to the next elevation. Will Automatically label 4 elevations in a row.
## works in: Archicad 26 but Needs Custom Keyboard Shortcuts for = Window tool, Label Selected Elements, Open Elevation. Either Match the same I use, or modify them in the user defined section of the code if you have your own.
## 2023_06_05
## V1.0
## @mi_jan

import pyautogui
import time

#################### Define Delays ####################
action_delay = 0.2 # Delay between each key press
start_delay = 3 # Dalay at Start of sequence
sequence_delay = 2 # Delay between switching from one elevation to the other. If your elevations take longer to load increase this number.

#################### Define Functions ####################

''' quick description:
    different applications or systems may interpret keyboard shortcuts differently. 
    Some applications may use standard keyboard shortcuts that can be triggered by pyautogui.hotkey(), 
    while others may have specific implementation details that require a different approach.
    Below I have defined some functions that can be used in different cases.
    
    ''' # read more: 
# https://pyautogui.readthedocs.io/en/latest/keyboard.html

################################################
##### USER DEFINED FUNCTION 1: def "press_key()"

def press_key(*keys): 
    pyautogui.hotkey(*keys)
    time.sleep(action_delay)

''' quick description:
        In Python, the asterisk (*) symbol is used to perform unpacking of iterable objects, such as lists or tuples. 
        The asterisk (*) symbol before the keys parameter indicates that the function press_key can accept any number 
        of arguments and pack them into a tuple called keys. This means that when calling the press_key function, 
        you can pass multiple arguments, and they will be packed into the keys tuple within the function.
        This doesnt always work with custom keyboard shortcuts, but generally works with system keyboard shortcuts.'''
            # for example in main script see " press_key('command', 'a') "

###############################################################
##### USER DEFINED FUNCTION 2: def "label_selected_elements()"

def label_selected_elements():
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(action_delay)

''' quick description:
        In this case the custom keyboard shortcut control + K was not going propperly through the user defined function above 
        therefore I have separated it and replaced the "*keys" tuple for the actual keyboard keys that need to be pressed.
        This allows us to simplify the main script to a single line of code where we can trigger the function name 
        instead of two lines of code: "module.function" + "delay"
        '''
###############################################################
##### USER DEFINED FUNCTION 3: def "activate_window_tool()"

def activate_window_tool():
    pyautogui.keyDown('option')
    pyautogui.press('3')
    pyautogui.keyUp('option')
    time.sleep(action_delay)

''' quick description:
        In this case the custom keyboard shortcut for activating the window tool was not going propperly through the user defined 
        function 1 or 2. Therefore I had to simplify it to its basic form using "keyDown", "keyUp" and "press" functions.
        '''
##############################################
# User Defined Function 4: Repeat 1 key press.

def repeat_key_press(key, repeat_count):
    for _ in range(repeat_count):
        press_key(key)

'''
        Note that the first definded function we saw "press_key" is nested within this function, 
        therefore this function also includes the "action_delay" variable.'''
            # for example in the main script see "repeat_key_press('down', 2) "


#############################################################################################
######################################## Main script ########################################
#############################################################################################

time.sleep(start_delay)

### labels first elevation and opens the Second Elevation:
activate_window_tool() ############### presses the window tool keyboard shortcut to activate the window.
press_key('command', 'a') ############ presses command+a to select all windows.
label_selected_elements() ############ presses the label selected element keyboard shortcut to label all selected windows
press_key('command', 'option', '6') ## Open Elevation kbs - needs to be changed here if want to use different kbs
press_key('down')  ################### Down Arrow Key (1 time)
press_key('enter')  ################## Enter Key to switch to the next elevation 
time.sleep(sequence_delay) ########### Delay required while it loads the next elevation before it runs the sequence again.

### labels Second elevation and opens the third Elevation:
activate_window_tool() 
press_key('command', 'a')
label_selected_elements()
press_key('command', 'option', '6')  
repeat_key_press('down', 2)  # Down Arrow Key (2 times)
press_key('enter')  
time.sleep(sequence_delay)

### labels third elevation and opens the fourth Elevation:
activate_window_tool() 
press_key('command', 'a')
label_selected_elements()
press_key('command', 'option', '6')  
repeat_key_press('down', 3)  
press_key('enter') 
time.sleep(sequence_delay)

### labels fourth elevation
activate_window_tool()
press_key('command', 'a')
label_selected_elements()