class Color:
    blue = "\033[94m"
    bold = "\033[1m"
    end = "\033[0m"
    red = "\033[31m"
    start = blue + "::" + end

    @staticmethod
    def format_error(text):
        return f"{Color.red}error{Color.end}: {text}"

    @staticmethod
    def format_start(text):
        return f"{Color.start} {Color.bold}{text}{Color.end}"
