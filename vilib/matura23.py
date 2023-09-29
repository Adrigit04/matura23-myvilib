# matura23 some vars and util functions
class Matura23Utils(object):

    @staticmethod
    def isMatura23Model(model_path=""):
        if "matura23" in model_path.lower():
            return True 
        else:
            return False