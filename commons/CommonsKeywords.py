from commons.ui.keywords import UiCommonsKeywords
from ui.pages import UiCommons

class CommonsKeywords(UiCommonsKeywords):

    def __init__(self):
        _ui_commons = UiCommons()
        UiCommonsKeywords.__init__(_ui_commons)