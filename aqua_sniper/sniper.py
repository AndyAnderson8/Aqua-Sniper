import time

from aqua_sniper.items import RareItem
from aqua_sniper.utils import color_print as print
from aqua_sniper.utils import load_authenticated_users


def run_sniper() -> None:
    """Snipe new rare items."""
    users = []
    rares: list[RareItem] = []

    loop_iterations = 0
    while True:
        if loop_iterations % 86400 == 0:  # Refresh users once a day
            print("\nAuthenticating users...")
            users = load_authenticated_users()
            print(f"{len(users)} users authenticated and ready for sniping.\n")

        print(f"Checking for new rares... ({loop_iterations})", True)
        old_rare_ids = {old_rare.item_id for old_rare in rares}
        rares = users[loop_iterations % len(users)].get_rares()
        for new_rare in rares:
            if new_rare.item_id not in old_rare_ids and loop_iterations != 0:
                print(f"New rare found!\n{new_rare}")

                for user in users:
                    print(f"Purchasing rare on user '{user.username}'...")
                    try:
                        user.buy_item(new_rare.item_id)
                        print("Purchase successful!")
                    except ValueError:
                        raise ValueError("Purchase failed!")

        time.sleep(1)
        loop_iterations += 1
