class Color:
    blue = "\033[94m"
    bold = "\033[1m"
    end = "\033[0m"
    red = "\033[31m"
    start = blue + "::" + end

    @staticmethod
    def make_bold(text):
        return f"{Color.bold}{text}{Color.end}"

    @staticmethod
    def make_red(text):
        return f"{Color.red}{text}{Color.end}"
