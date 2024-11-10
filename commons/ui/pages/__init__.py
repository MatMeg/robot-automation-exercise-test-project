from PageObjectModel import PageObjectModel
from Browser import Browser

class UiCommons(PageObjectModel, Browser):
    PageObjectModel.__init__()
    Browser.__init__()
        