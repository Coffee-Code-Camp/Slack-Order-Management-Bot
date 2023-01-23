from block.orders import generate_oder
from datetime import datetime


def fake_orders():
    orders = []
    for i in range(3):
        orders.append({
            "customer": f"Customer number {i}",
            "customer_email": "info@coffeecodecamp.ir",
            "products": ["MacBook Air", "Galaxy Tab 7"],
            "created_at": datetime.now(),
            "description": f"Description number {i}",
            "status": i % 2
        })
    return orders


def list_orders(ack, respond, command):
    if command['text'] == "new":
        print("listing new orders")

    final_blocks = []
    for o in fake_orders():
        final_blocks.extend(generate_oder(**o))
    ack()
    respond(
        blocks=final_blocks,
        text="Orders list",
    )
