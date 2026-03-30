#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import random

class Menu:

    """
    Menu class. It handles the whole menu navigation and add_item, sell_item functions.
    It also has the read/write functions for both add_item/sell_item files, which are two separate CSVs.

    """
    
    def __init__(self):

        """
        Though it may seem unorthodox to handle it this way, the class initializer for Menu() handles the menu 
        navigation through conditional instructions. It makes sure the user prompts available menu commands 
        only and it also makes sure to return back to main menu when an user inputs "return" in any menu. 

        All user inputs are automatically converted to lowercase.

        """
        while True:
            self.choice=input("\nPlease input the name of the feature you'd like to use:").lower()
            
            if self.choice not in ["add", "stock", "sale", "profits", "help", "exit", "return","easteregg", "konami code"]:
                print("You are allowed to input the commands available through the 'help' menu only. Please retry")
            elif self.choice=="add":
                self.add_item()
            elif self.choice=="help":
                print("Here is the list of all available commands:")
                self.helpmenu()
            elif self.choice=="stock":
                print("Here is the list of all items on stock")
                self.show_inventory()
            elif self.choice=="sale":
                print("Sale feature. Please add items to the cart and then checkout when you're ready.")
                self.sell_item()
            elif self.choice in ["easteregg", "konami code"]:
                self.easteregg()
            elif self.choice=="profits":
                self.statsprinter()
            elif self.choice=="return":
                continue
            elif self.choice=="exit":
                print("Shutting down --Simple Store Manager -- Thank you for choosing our software.")
                break
        return

    def helpmenu(self):

        """
        helpmenu() function to print the "help" feature of the application. User gets a bulletlist printed
        with the desired instructions about how to use the program.

        """
        menulist=[
            "Add: add products to your stock", 
            "Stock: shows the full products inventory currently stocked", 
            "Sale: use it to access to the sale input feature", 
            "Profits: simple profits statistics tracked using products costs/sales", 
            "Help: all of the --Simple Store Manager-- features list", 
            "Return: input return in any cell to go back to main menu",
            "Exit: shut down --Simple Store Manager--"]
        for item in menulist:
            print("o\t"+item)
        print("\n")
        return

    def back_sniffer(self, input_value):

        """
        Back_sniffer function has the sole purpose to "listen" for user inputs equal to "return" in any input()
        to interrupt the current cicle and go back to the main menu

        input_value is a generic argument that has to be passed through an input(variable)

        """
        if input_value=="return":
            print("Halting execution, back to Main Menu.")
            return True
        return False

    def negativeinput(self, input_value):

        """
        negativeinput() function has a similiar scope to back_sniffer(). It is called through an if conditional under int, float inputs
        to check on user erroneously using a negative input value.

        If user input is negative it will print a warning sign in english.
        input_value is a generic argument that has to be passed through an input(variable)

        """
        if input_value<0:
            print("Input value cannot be a negative number!")
            return True
        return False
        
    def warehouse_reader(self, storage_file):

        """

        Warehouse reader has the purpose of reading the warehouse.csv file used to save and read warehouse data
        for the program. 
        It opens the file and tells the interpreter how to read the data from the csv in a storage_dict Dict{}

        Keyword arguments:
        storage_file = passed from the add_item function, it contains the item that must be read at the start
        of the add_item function

        NOTE:
        warehouse.csv sorts the products data (NAME, QUANTITY, INTERNAL BUY PRICE, SELL PRICE) thorugh a PRODUCT_ID
        code that is mapped as key to the dict values.

        """
        storage_dict={}
        with open(storage_file, "r", newline="", encoding="utf-8") as csvfile:
            reader=csv.reader(csvfile)
            for rows in reader:
                product_id=int(rows[0])
                storage_dict[product_id]= [rows[1], int(rows[2]), float(rows[3]), float(rows[4])]
            return storage_dict

    def warehouse_writer(self, storage_file, storage_dict):

        """
        Warehouse writer has the sole purpose of writing back to the file what is stored in storage_dict Dict{}
        after processing everything with the add_item function.

        Keyword arguments:
        storage_dict = the Dict() used to store the data read from warehouse writer and processed through add_item
        storage_file = the warehouse.csv used as a database to save the processed data from the storage dict

        """
        
        with open(storage_file, "w", newline="", encoding="utf-8") as csvfile:
            writer=csv.writer(csvfile)
            for key, values in storage_dict.items():
                writer.writerow([key] + values)

    def add_item(self):

        """
        add_item function is the core of the "add" feature.
        It defines and passes the storage_file to the warehouse_reader function, it then asks user input
        to define the name, quantity, internal price and sell price of a product, and it passes the data to the 
        warehouse writer function to store it in the warehouse.csv file.

        It also checks for product ID presence in csv file to edit the item quantity in case user inputs an
        existing item. 

        """
        storage_file="warehouse.csv"
        storage_update=self.warehouse_reader(storage_file)

        while True:
            product_id=input("Please add the product sequential code (i.e. 1,2,3... etc.): ")
            if self.back_sniffer(product_id):
                return
            
            try:
                product_id=int(product_id)
                if self.negativeinput(product_id):
                    continue
                break
            except ValueError:
                print("Product code can be an integer value only, please retry.")
        
        if product_id in storage_update:
            print(f"Product already in stock: {storage_update[product_id][0]}.")
            
            while True:
                qty=input(f"Adding item quantity {storage_update[product_id][0]}: ")
                if self.back_sniffer(qty):
                    return

                try:
                    qty=int(qty)
                    if self.negativeinput(qty):
                        continue
                    break
                except ValueError:
                    print("Product quantity can be an integer value only, please retry.")
            
            storage_update[product_id][1] += qty
            print(f"Updated quantity: {storage_update[product_id][1]}\n")
        else:
            while True:
                name=input("Please insert product name (20 chars max limit): ")
                if self.back_sniffer(name):
                    return
                    
                if len(name) <= 20:
                    break
                else:
                    print("Product name cannot be longer then 20 chars, please retry.")
            
            while True:
                qty=input("Adding quantity: ")
                if self.back_sniffer(qty):
                    return

                try:
                    qty=int(qty)
                    if self.negativeinput(qty):
                        continue
                    break
                except ValueError:
                    print("Quantity can be an integer value only, please retry")
            
            while True:
                
                buyprice=input("Internal buy price for this product: ")
                if self.back_sniffer(buyprice):
                    return
                sellprice=input("Retail price for this product: ")
                if self.back_sniffer(sellprice):
                    return
                
                try:
                    buyprice=float(buyprice)
                    sellprice=float(sellprice)
                    if self.negativeinput(buyprice):
                        continue
                    if self.negativeinput(sellprice):
                        continue
                    break
                except ValueError:
                    print("Company or retail price can be a decimal number only, please retry.")
                    
            storage_update[product_id]=[name, qty, buyprice, sellprice]
            print(f"Added product: {name}, \nQuantity: {qty}, \nCompany price: {buyprice}, \nRetail price {sellprice}\n")

        self.warehouse_writer(storage_file, storage_update)
        
    def show_inventory(self):

        """
        Show Inventory is at the core of the "stock" feature.
        It uses the storage_file variable for the warehouse.csv again, and passes it to the warehouse_reader()
        to generate a bullet list showing all of the items registered in the warehouse.csv database through
        key,values iteration in bulletmaker items.

        """
        storage_file="warehouse.csv"
        bulletmaker=self.warehouse_reader(storage_file)
        
        print("{:<10}\t{:<20}\t{:<20}\t{:<20}\t{:<20}".format("Product ID","Product name", "Quantity", "Company price", "Retail price"))

        for key, value in bulletmaker.items():
            name, qty, buyprice, sellprice=value 
            product_id=key
            print("- {:<10}\t{:<20}\t{:<20}\t{:<20}\t{:<20}".format(product_id, name, qty, buyprice, sellprice))
        print("\n")

    def sell_item(self):

        """
        sell_item() is at the core of the "sale" feature. It uses the storage_file warehouse.csv to read 
        the registered products database and it also defines the stats_file.csv passed to the checkout(),
        stats_reader() and update_simplestats() functions.

        sell_item() asks for user input to check which item has to be put in the cart for the checkout phase.
        It asks for product ID, warning the user that it may prompt the "stock" feature to check on stored product IDs
        and also makes sure that the user input is relative to an existing product ID.

        It then asks for the desired sale quantity and goes on to ask if another item has to be put in the cart.
        It breaks the cycle on user input "no".

        """
        storage_file="warehouse.csv"
        stats_file="stats_file.csv"
        sale_update=self.warehouse_reader(storage_file)
        cart={}

        while True:
            while True:
                product_id=input("To add an item to the cart please specify the relative product ID (i.e. 1,2,3): ")
                if self.back_sniffer(product_id):
                    return
            
                try:
                    product_id=int(product_id)
                    if self.negativeinput(product_id):
                        continue
                except ValueError:
                    print("Product ID can be an integer number only, please retry...")
                    continue 
                
                if product_id not in sale_update:
                    print("Valid product IDs allowed only. If you forgot the product ID please use the 'stock' feature to check it")
                else:
                    break
        
            if product_id in sale_update:
                product_name=sale_update[product_id][0]
                available_qty=sale_update[product_id][1]
                print(f"Selected item's name: {product_name}")
                print(f"Available in stock quantity: {available_qty}X")

                while True:
                    sale_qty=input(f"Please insert {product_name} desired quantity: ").lower()
                    if self.back_sniffer(sale_qty):
                        return

                    try:
                        sale_qty=int(sale_qty)
                        if self.negativeinput(sale_qty):
                            continue
                        if sale_qty>available_qty:
                            print(f"Selected item quantity is more then in stock quantity ({available_qty}X)!\n Please edit your in stock quantity or edit the selected item quantity.")
                        else:
                            break
                    except ValueError:
                        print("Selected item quantity can be an integer value only, please retry.")
                    
                if product_id in cart:
                    cart[product_id]["Quantity"]+=sale_qty
                else:
                    cart[product_id]={"Name":product_name, "Quantity":sale_qty, "Price":sale_update[product_id][3]}

                sale_update[product_id][1]-=sale_qty
                print(f"{product_name} quantity correctly added to customer cart: {sale_qty}X")
                print(f"Stock remaining quantity: {sale_update[product_id][1]}X")
       
            while True:
                add_more=input("Do you wish to add more items to the cart? (yes/no): ").lower()
                if self.back_sniffer(add_more):
                    return

                if add_more=="y" or add_more=="yes":
                    break
                elif add_more=="no":
                    print("Check-out phase.")
                    self.checkout(cart, sale_update, storage_file, stats_file)
                    return
                else:
                    print("Invalid command, you can either input 'yes' or 'no' only.")
    
    def checkout(self, cart, sale_update, storage_file, stats_file):
        """

        Checkout function triggered by user input "no" on add_more to cart variable.

        It reads from stats_file the current state of gross profits and total buyprice.
        It recaps all of the items added to cart in sell_item() and goes on to show subtotal for sale and
        total to pay.

        The current_revenue and current_buyprice data is then added to the total revenue and total buyprice data
        to be stored in update_simplestats() on the stats_file.csv.
        The function checkout() also updates the warehouse_writer() function to edit item quantity for each sold 
        item.

        Arguments:
        cart= dict{} from sell_item containing name, quantity, price for items in cart
        sale_update, storage_file = required to write back the quantity data do warehouse_writer() warehouse.csv
        stats_file= stats_file.csv required to read current_revenue, current_buyprice and then write back the
                    edited sale data to the same file in order to keep the "profits" feature updated.

        """
        total_revenue=0
        total_buyprice=0

        current_revenue, current_buyprice=self.stats_reader(stats_file)
        
        print("\nItems currently added to your cart: ")
        for product_id, details in cart.items():
            name=details["Name"]
            quantity=details["Quantity"]
            price=details["Price"]
            cost=sale_update[product_id][2]
            subtotal=quantity*price
            total_revenue+=subtotal
            total_buyprice+=quantity*cost
            print(f"Product: {name}\n Sold Quantity:{quantity}\n Unit Price:{price:.2f}€\n Subtotal: {subtotal:.2f}€")
        current_revenue+=total_revenue
        current_buyprice+=total_buyprice

        print(f"\n Price to pay: {total_revenue:.2f}€")

        self.update_simplestats(stats_file, current_revenue, current_buyprice)
        self.warehouse_writer(storage_file, sale_update)

    def stats_reader(self, stats_file):

        """
        Function that accepts the stats_file.csv through stats_file argument to read the current statistics 
        stored in the file.

        It also defines the total_revenue and total_buyprice variables.

        NOTE: 
        if the file is empty it sets stats to 0.0,0.0 to aviud StopIteration and FileNotFoundError exceptions.

        """
        try:
            with open(stats_file, "r", newline="") as csvfile:
                reader=csv.reader(csvfile)
                
                try:
                    simplestats=next(reader)
                    total_revenue=float(simplestats[0])
                    total_buyprice=float(simplestats[1])
                    return total_revenue, total_buyprice
                except StopIteration:
                    return 0.0, 0.0
        except FileNotFoundError:
            return 0.0, 0.0            

    def update_simplestats(self, stats_file, total_revenue, total_buyprice):

        """
        update_simplestats() accepts opens stats_file.csv to write back total_revenue and total_buyprice variables
        to the csv file, in order to save the current gross revenue and total buyprice.

        Arguments:
        stats_file: It passes the stats_file.csv. Current version opens the stats_file.csv directly, everything seems
        to work properly as it is.
        total_revenue= total gross revenue for sold items
        total_buyprice= total internal buy price. NOTE: THIS IS FOR SOLD ITEMS ONLY, NOT THE WHOLE WAREHOUSE.

        """
        with open("stats_file.csv", "w", newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([total_revenue, total_buyprice])

    def statsprinter(self):

        """

        statsprinter() has to be called from user through "profits" feature, to show the current net sales of the
        company. It uses total_revenue and total_buyprice to simply calculate the net sales, then prints the results.

        """
        stats_file="stats_file.csv"
        total_revenue, total_buyprice=self.stats_reader(stats_file)
        profit=total_revenue-total_buyprice
        
        print(f"\nTotal profits (from database creation): {profit:.2f}€\nCalculated by subtracting {total_buyprice:.2f}€ in stocked products costs from {total_revenue:.2f}€ total sales.")
    
    def easteregg(self):

        """

        This speaks for itself, for curious coders.

        """
        
        slip=["Hey i'm not linked to a cash register yet",
              "Not that advanced yet mate, i have no idea how to print a receipt slip",
              "The right man in the wrong place can make a difference in the World.",
              "Wake up, Mr. Freeman, wake up.",
              "War is when the young and stupid are tricked by the old and bitter into killing each other",
              "I mean, you could try the konami code as input, but nothing's gonna happen anyway.",
              "You should add a Jill Sandwich to your stock.",
              "What if I am just another byproduct of PATRIOTS?",
              "Snake?SNAKE?!SNAAAAKE!",
              "IT'S A ME, PYTHON!",
              "No Nintendo lawyer was harmed while developing this software.",
              "I suppose i could've used a .txt file for this but how cool it is to just randomize a list?",
              "Hey, this reminds me of that time i forgot how to sit.",
              "The cake is a lie, though i like it with cream.",
              "Please insert floppy.",
              "She'll Be Coming 'Round the Mountain!",
              "much code, such python, very nerdy, wow.",
              "r/irleastereggs, wait: is this real life though?",
             ]

        slip_randomizer=random.choice(slip)
        print(slip_randomizer+"\n")


# In[ ]:




