debug = False

def cambiar_modo():
    
    global debug
    debug = not debug
    
def get_modo():
    
    return debug