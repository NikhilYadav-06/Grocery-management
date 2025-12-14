items = [] 

def get_quantity (qty_input):
    
    qty_input =qty_input.replace(" ","").lower()
    
    number = ""
    unit = ""
    
    for char in qty_input:
      
        if char.isdigit() or char ==".":
            number += char
            
        else:
            unit+= char
            
    if unit =="":
     unit = "unit"
               
    return float (number),unit
            
def add_item():
                
    name = input("Enter item name: ")
    price = int(input("Enter price per unit/kg/litre: "))
  
    qty_input =(input("Enter quantity(ex: 3kg or 2 ): "))
    qty , unit = get_quantity(qty_input)

    total = price * qty
    items.append([name, price, qty, unit, total])
    
    
    print(f"\n✔ {name} ({qty } {unit}) added successfully! Total = {total}\n")
    
    # UPDATE ITEMS !

def update_item():
    if not items:
        print("\nNo items to update!\n")
        return

    name = input("Enter item name to update: ")

    for item in items:
        if item[0].lower() == name.lower():

            print("\nWhat do you want to update?")
            print("1. Update Name")
            print("2. Update Price")
            print("3. Update Quantity")
            print("4. Update Both Price & Quantity")

            choice = input("Enter your choice: ")

            # Update Name
            
            if choice == "1":
                new_name = input("Enter new name: ")
                item[0] = new_name
                print("\n✔ Name updated!\n")

            # Update Price
            
            elif choice == "2":
                new_price = float(input("Enter new price: "))
                item[1] = new_price
                item[4] = new_price * item[2]  
                print("\n✔ Price updated!\n")

            # Update Quantity
            
            elif choice == "3":
                qty_input = input("Enter new quantity (ex: 3kg or 2): ")
                new_qty, new_unit = get_quantity(qty_input)
                item[2] = new_qty
                item[3] = new_unit
                item[4] = item[1] * new_qty
                print("\n✔ Quantity updated!\n")

            # Update both
            
            elif choice == "4":
                new_price = float(input("Enter new price: "))
                qty_input = input("Enter new quantity (ex: 3kg or 2): ")

                new_qty, new_unit = get_quantity(qty_input)

                item[1] = new_price
                item[2] = new_qty
                item[3] = new_unit
                item[4] = new_price * new_qty

                print("\n✔ Price & Quantity updated!\n")

            else:
                print("Invalid choice!")

            return

    print("\n❌ Item not found!\n")


    
# DELETED ITEMS 

def delete_item():
    
    if not items:
        print("\nNo items to delete!\n")
        return
   
    name = input("enter item name to delete")
   
    for item in items:
        
        if item[0].lower()== name.lower():
            items.remove (item)
            
            print(f"\n{name}deleted successfully!\n")
            return
       
        print("\n item not found!\n")   

# BILL STYSTEM


def show_bill():
    
    if not items:
        print("\nNo items added yet!\n")
       
        return

    print("\n==========` FINAL BILL `==========")
    grand = 0
  
    for item in items:
        
        print(f"{item[0]}  |  {item[1]} per unit x {item[2]} {item[3]}  {item[4]} ")
        grand += item[4]
 
    print("---------------------------------")
    print(f"  `Grand Total` = {grand}")
    print("=================================\n")

# items

def main():
    
    while True:
        
        print("\n===== `Grocery Management System` =====")
       
        print("1. Add Item")
        print("2. Delete item")
        print("3. Update item")
        print("4. Show Bill")
        print("5. Exit")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        
        elif choice =="2":
            delete_item()
            
        elif choice =="3":
            update_item()    
        
        elif choice == "4":
            show_bill()
        
        elif choice == "5":
            print("\n`Thank you for Visiting our Shop`!")
        
            break
        
        else:
            print("Invalid choice! Please try again.\n")


main()
