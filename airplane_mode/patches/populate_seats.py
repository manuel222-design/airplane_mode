import frappe
import random

def execute():
    tickets = frappe.get_all("Airplane Ticket", fields=["name"])

    for ticket in tickets:
        doc = frappe.get_doc("Airplane Ticket", ticket.name)

        if not doc.seat:
            seat_number = random.randint(1, 99)
            seat_letter = random.choice(["A", "B", "C", "D", "E"])

            doc.seat = f"{seat_number}{seat_letter}"
            doc.save()