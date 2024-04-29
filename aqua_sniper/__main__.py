import os

from colorama import just_fix_windows_console
from pyfiglet import Figlet  # type: ignore[import-untyped]

from aqua_sniper import __app_name__, __description__, __version__
from aqua_sniper.sniper import run_sniper
from aqua_sniper.utils import color_print as print


def main() -> None:
    """Main entry point into the package."""
    os.system(f"title {__app_name__} v{__version__}")
    just_fix_windows_console()
    print(
        f"\n{Figlet(font="graffiti").renderText(__app_name__)}\n"
        f"{__app_name__} (v{__version__}) - {__description__}"
    )
    run_sniper()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("Press Enter to continue...")
