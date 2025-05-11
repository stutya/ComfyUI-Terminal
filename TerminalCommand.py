import subprocess

class Terminal:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
            "optional": {
                "encoding": ("STRING", {"default": "utf-8"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"

    def execute(self, text, encoding="utf-8"):
        try:
            out = subprocess.check_output(f"{text}", shell=True, stderr=subprocess.STDOUT).decode(encoding, errors="replace")
            return (out,)
        except subprocess.CalledProcessError as e:
            error_output = e.output.decode(encoding, errors="replace") if e.output else f"Command failed with exit code {e.returncode}"
            return (f"ERROR: {error_output}",)

    CATEGORY = "utils"
