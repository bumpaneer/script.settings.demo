import copy
import sys
import xbmcgui

getLocalizedString = sys.modules['__main__'].getLocalizedString

class GUI(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 13]
        
        # get control ids
        self.control_id_button_category = 10
        self.control_id_grouplist_main = 3
        
        # translation ids
        self.translation_id_system = 32002
        self.translation_id_about = 32196
        
        #set templates
        self.button_category = self.getControl(self.control_id_button_category)
        self.button_category.setVisible(False)
        
        # set actions
        self.button_test1 = copy.deepcopy(self.getControl(self.control_id_button_category))
        self.button_test1.setPosition(100, 250)
        self.button_test1.setVisible(True)
        self.button_test2 = copy.deepcopy(self.button_category)
        self.button_test2.setPosition(100, 320)
        self.button_test2.setVisible(True)
        
        # translate buttons
        self.button_test1.setLabel(getLocalizedString(self.translation_id_system))
        self.button_test2.setLabel(getLocalizedString(self.translation_id_about))
        
        #add to grouplist
        #self.getControl(self.control_id_grouplist_main).add(self.button_test2)
        self.addControl(self.button_test1)
        self.addControl(self.button_test2)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.closeDialog()

    def onFocus(self, controlId):
        pass

    def onClick(self, controlId):
        if controlId == self.control_id_button_action:
            self.doAction()
        elif controlId == self.control_id_button_exit:
            self.closeDialog()

    def doAction(self):
        pass

    def closeDialog(self):
        self.close()
