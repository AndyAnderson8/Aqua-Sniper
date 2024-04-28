from pyfiglet import Figlet  # type: ignore[import-untyped]

from aqua_sniper import __app_name__, __description__, __version__
from aqua_sniper.sniper import run_sniper
from aqua_sniper.utils import color_print as print


def main() -> None:
    """Main entry point into the package."""
    run_sniper()


if __name__ == "__main__":
    print(
        f"\n{Figlet(font="graffiti").renderText(__app_name__)}\n"
        f"{__app_name__} (v{__version__}) - {__description__}"
    )
    main()
