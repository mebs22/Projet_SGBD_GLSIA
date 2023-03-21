TEXT_SIZE = 250
from components.constants import MAIN

# Stack functions
def goBack(stack):
    stack.set_visible_child_name(MAIN)

def changePage(stack, page):
    stack.set_visible_child_name(page)


def insertComponentName(string: str)->str:
    return f"""<span size="{TEXT_SIZE}%"> <b> <u>{string}</u> </b> </span>"""