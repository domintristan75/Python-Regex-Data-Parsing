import random

emails = [
    "client.alpha@domain.com",
    "buyer.hero@yahoo.com",
    "tcg.collector99@gmail.com",
    "store.owner@business-mail.org"
]
skus = ["TCG-BLU-402", "TCG-RED-109", "TCG-WHT-551", "TCG-GLD-007"]
noise_lines = [
    "[INFO] System heartbeat OK. CPU load at 12%.",
    "[DEBUG] Database connection pool refreshed successfully.",
    "[WARNING] High memory usage detected on worker node 4.",
    "[INFO] User session expired for guest token #8832.",
    "[ERROR] Failed to load asset image: card_back_v2.png"
]

with open("raw_system_logs.txt", "w") as f:
    for i in range(1000):
        line_type = random.choice(["order", "noise", "order"])

        if line_type == "noise":
            f.write(f"[2026-10-17 14:{random.randint(10, 59)}:{random.randint(10, 59)}] {random.choice(noise_lines)}\n")
        else:
            email = random.choice(emails)
            sku = random.choice(skus)
            order_id = f"ORD-{random.randint(10000, 99999)}"
            tracking = f"1Z{random.randint(1000000000000000, 9999999999999999)}"

            log_entry = (
                f"[2026-10-17 14:{random.randint(10, 59)}:{random.randint(10, 59)}] "
                f"ORDER_SUCCESS: Customer ({email}) purchased Item SKU: {sku}. "
                f"Ref: {order_id}. ShipTrack: {tracking}.\n"
            )
            f.write(log_entry)

with open("raw_system_logs.txt", "r") as file:
    log_content = file.read()
    print(log_content)