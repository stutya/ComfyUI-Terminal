from subprocess import getoutput

class Terminal:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"

    def execute(self, text):
        out = getoutput(f"{text}")
        return (out,)

    CATEGORY = "utils"
