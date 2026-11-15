# Simple Billing System
PRODUCTS = {"Rice": 50, "Sugar": 40, "Oil": 120}
GST_RATE = 0.05

def add_item(bill, name, qty):
    """Validate the product and quantity, then add the item to the bill list."""
    name = name.strip().capitalize()
    if name not in PRODUCTS:
        print("Invalid product. Available: " + ", ".join(PRODUCTS))
        return False
    if qty < 1:
        print("Quantity must be at least 1.")
        return False
    amount = PRODUCTS[name] * qty
    bill.append({"name": name, "qty": qty, "amount": amount})
    print(f"{name} x{qty} added | Amount: {amount}")
    return True

def calculate_totals(bill):
    subtotal = sum(item["amount"] for item in bill)
    gst = subtotal * GST_RATE
    return subtotal, gst, subtotal + gst

def build_bill(customer, bill):
    subtotal, gst, grand = calculate_totals(bill)
    lines = []
    if customer:
        lines.append(f"Customer: {customer}")
    lines.append(" | ".join(f"{i['name']} x{i['qty']} = {i['amount']}" for i in bill))
    lines.append(f"Subtotal: {subtotal:g} | GST (5%): {gst:.2f}")
    lines.append(f"Grand Total: {grand:.2f}")
    return "\n".join(lines)

def generate_bill(customer, bill):
    if not bill:
        print("No items added yet.")
        return
    text = build_bill(customer, bill)
    print(text)
    with open("bill.txt", "w") as f:
        f.write(text + "\n")
    print("Bill saved to bill.txt")

def main():
    customer = input("Customer name: ").strip()
    bill = []
    while True:
        print("\n1. Add item  2. View bill  3. Generate bill  4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Add item: ")
            try:
                qty = int(input("Quantity: "))
            except ValueError:
                print("Quantity must be at least 1.")
                continue
            add_item(bill, name, qty)
        elif choice == "2":
            print(build_bill(customer, bill) if bill else "No items added yet.")
        elif choice == "3":
            generate_bill(customer, bill)
            break
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()