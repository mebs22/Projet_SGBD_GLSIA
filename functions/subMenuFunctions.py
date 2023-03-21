
SUBCOMPONENT = None

def loadSubComponents(element):
    # Get the parent
    elementRoot = element.get_parent()
    # print(f"element {element} \nParent {elementRoot}")

    # Remove the current child
    elementRoot.remove(element)
    
    # Attach component and re-render
    elementRoot.attach(SUBCOMPONENT, 0, 1, 1, 1)
    elementRoot.show_all()