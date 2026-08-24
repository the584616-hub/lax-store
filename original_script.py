"""
Calculates discounts and generates invoice summary
"""
import time

def main():
    print("=== Super Invoice Calculator ===")
    customer_name = input("Enter Customer Name: ")
    item_price = float(input("Enter Item Price ($): "))
    discount_pct = float(input("Enter Discount Percentage (%): "))

    print(f"\nProcessing invoice for {customer_name}...")
    time.sleep(0.5)

    discount_amount = item_price * (discount_pct / 100.0)
    final_total = item_price - discount_amount

    print("--------------------------------")
    print(f"Customer:        {customer_name}")
    print(f"Original Price:  ${item_price:,.2f}")
    print(f"Discount:        -${discount_amount:,.2f} ({discount_pct}%)")
    print(f"FINAL TOTAL:     ${final_total:,.2f}")
    print("--------------------------------")
    print("Thank you for your business! 🎉")

if __name__ == "__main__":
    main()
