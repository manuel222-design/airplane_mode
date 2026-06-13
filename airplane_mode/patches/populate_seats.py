import frappe
import random

def execute():
    tickets = frappe.get_all(
        "Airplane Ticket",
        fields=["name", "seat"]
    )

    for ticket in tickets:
        if not ticket.seat:
            seat_number = random.randint(1, 99)
            seat_letter = random.choice(["A", "B", "C", "D", "E"])

            frappe.db.set_value(
                "Airplane Ticket",
                ticket.name,
                "seat",
                f"{seat_number}{seat_letter}"
            )