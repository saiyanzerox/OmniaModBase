# Omnia Example Python Mod
import omnia

enablePython = False

def OnTogglePython(val):
    global enablePython
    enablePython = (val > 0.5) # Change the value to boolean (1 or 0)
    omnia.Logger.Success("ExampleMod", f"Python Logic {'Active' if enablePython else 'Inactive'}")

def Settings():
    # This Function is Just For Mod Settings...
    global enablePython
    omnia.UI.Label("Example Mod - Python")
    enablePython = omnia.UI.Checkbox("Enable Python", enablePython, OnTogglePython)

def Boot():
    # This Function Will be Called Only Once...
    pass

def Loop():
    # This Function Will be Called Every Game Ticks...
    pass

def Kill():
    # This Function Will be Called on Mod Disable or Game Shutdown...
    pass