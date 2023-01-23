from actions.orders import reject_order, accept_order, send_invoice

actions_registry = {
    "reject_order": reject_order,
    "accept_order": accept_order,
    "send_invoice": send_invoice
}
