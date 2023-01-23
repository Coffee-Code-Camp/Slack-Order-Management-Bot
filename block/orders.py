from random import randint


def generate_oder(customer, customer_email, products, created_at, description, status):
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Order for customer:\n*<mailto:{customer_email}|{customer}>*"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*Products:*\n{str(products)}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*When:*\n{created_at}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Description:*\n{description}"
                }
            ]
        }
    ]

    if status == 0:
        blocks.append({
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Approve"
                    },
                    "style": "primary",
                    "action_id": "accept_order",
                    "value": str(randint(1, 30))
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Deny"
                    },
                    "style": "danger",
                    "action_id": "reject_order",
                    "value": str(randint(1, 30))
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Send Invoice"
                    },
                    "action_id": "send_invoice",
                    "value": str(randint(1, 30))
                }
            ]
        })

    return blocks
