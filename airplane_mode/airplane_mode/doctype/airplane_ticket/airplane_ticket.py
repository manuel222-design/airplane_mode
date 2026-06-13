# Copyright (c) 2026, Mashuhuri Engineers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document # type: ignore
import frappe # type: ignore
import random

class AirplaneTicket(Document):

    def validate(self):
        # Remove duplicate add-ons
        unique_items = []
        seen = set()

        for addon in self.add_ons:
            if addon.item not in seen:
                seen.add(addon.item)
                unique_items.append(addon)

        self.add_ons = unique_items

        # Calculate Total Amount
        total = self.flight_price or 0

        for addon in self.add_ons:
            total += addon.amount or 0

        self.total_amount = total

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Only boarded tickets can be submitted.")

    def before_insert(self):
        seat_number = random.randint(1, 99)
        seat_letter = random.choice(["A", "B", "C", "D", "E"])

        self.seat = f"{seat_number}{seat_letter}"