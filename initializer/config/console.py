from terminology import in_green, in_red, in_blue, in_yellow
from emoji import emojize


class Console:

    success_emoji = emojize(':raising_hands:', language='alias')
    error_emoji = emojize(":cross_mark:", language='alias')
    warning_emoji = emojize(":warning:", language='alias')
    info_emoji = emojize(":information:", language='alias')

    @staticmethod
    def success(text: str, emoji: bool = True) -> None:
        if emoji:
            print(in_green(text=f"{Console.success_emoji} {text}").in_bold())
        else:
            print(in_green(text=text).in_bold())

    @staticmethod
    def error(text: str, emoji: bool = True) -> None:
        if emoji:
            print(in_red(text=f"{Console.error_emoji} {text}").in_bold())
        else:
            print(in_red(text=f"{text}").in_bold())

    @staticmethod
    def info(text: str, emoji: bool = True) -> None:
        if emoji:
            print(in_blue(text=f"{Console.info_emoji}  {text}").in_bold())
        else:
            print(in_blue(text=f"{text}").in_bold())

    @staticmethod
    def warning(text: str, emoji: bool = True) -> None:
        if emoji:
            print(in_yellow(text=f"{Console.warning_emoji}  {text}").in_bold())
        else:
            print(in_yellow(text=f"{text}").in_bold())
