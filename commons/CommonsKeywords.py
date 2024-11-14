import sys
sys.path.append('./commons/ui/keywords')
from UiCommonsKeywords import UiCommonsKeywords
sys.path.append('./commons/ui/pages')
from UiCommons import UiCommons

class CommonsKeywords(UiCommonsKeywords):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        super().__init__(UiCommons())
        