# FAA Technical Operations - Aircraft Parts Requisition System

# --- Input Section ---
# Gather part details and convert numeric inputs to appropriate types
part_number = input("Enter Part Number (P/N): ")
part_description = input("Enter Part Description: ")
unit_cost = float(input("Enter Unit Cost ($): "))
quantity_requested = int(input("Enter Quantity Required: "))
expedite_fee = float(input("Enter Freight/Expedite Fee ($): "))

# --- Calculations Section ---
# Calculate base parts subtotal
parts_subtotal = unit_cost * quantity_requested

# Calculate FAA Form 8130-3 airworthiness certification surcharge (5%)
cert_fee_rate = 0.05
cert_surcharge = parts_subtotal * cert_fee_rate

# Calculate total requisition cost
total_requisition_cost = parts_subtotal + cert_surcharge + expedite_fee

# --- Output Section ---
print("\n" + "=" * 50)
print("     FAA TECH OPS - REQUISITION SUMMARY")
print("=" * 50)
print(f"Part Number:             {part_number}")
print(f"Description:             {part_description}")
print(f"Quantity Requested:      {quantity_requested}")
print(f"Unit Cost:               ${unit_cost:,.2f}")
print("-" * 50)
print(f"Base Parts Subtotal:     ${parts_subtotal:,.2f}")
print(f"FAA Cert Surcharge (5%): ${cert_surcharge:,.2f}")
print(f"Freight/Expedite Fee:    ${expedite_fee:,.2f}")
print("-" * 50)
print(f"Total Requisition Cost:  ${total_requisition_cost:,.2f}")
print("=" * 50)
