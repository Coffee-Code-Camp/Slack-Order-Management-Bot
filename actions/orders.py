def reject_order(ack, body, client, respond):
    ack()
    respond(f"Order {body['actions'][0]['value']} rejected")


def accept_order(ack, body, client, respond):
    ack()
    respond(f"Order {body['actions'][0]['value']} accepted")


def send_invoice(ack, body, client, respond):
    ack()
    respond(f"Order {body['actions'][0]['value']} invoice sent")
