#dominos clone
import random
class dominos:
    menu={
        "veg":{"margerita":129,"chee_and_corn":149,"farmhouse":199,"peppy_paneer":229,"tomato_basil":99},
        "nonveg":{"chicken_tikka":249,"pepper_barbeque":299,"chicken_sausage":199,"chicken_supreme":349},
        "snacks":{"garlic_bread":99,"chicken_wings":199,"potato_wedges":149},
        "desserts":{"choco_lava_cake":149,"brownie":129,"ice_cream":99},
        "drinks":{"coke":49,"pepsi":49,"sprite":49}
    }

    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False #to validate login state
        self.cart={} #to store ordered items

        #MAIN PROGRAM
        while True:
            if not self.login_status:
                print("--------------------WELCOME TO DOMINOS APP🍕🍕-------------------")
                print("LOGIN💌")
                ch=input("Do you want to login? (y/n):😊 ").lower()
                if ch=='y':
                    self.login()
            
            if self.login_status:
                print("USER 👤:",self.name)
                print("ENTER 1: TO VIEW MENU📃")
                print("ENTER 2: TO VIEW CART🛒")
                print("ENTER 3: TO LOGOUT😔")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    self.order()
                elif choice==2:
                    self.view_cart()
                elif choice==3:
                    self.logout()
                else:
                    print("Invalid choice.❌")
    @staticmethod
    def validate_otp(value):
        while True:
            print("--------------------------")
            og_otp=random.randint(1000,9999)
            print("an otp has been sent to the",value)
            print("your dominos otp is:",og_otp)
            otp=int(input("enter the otp: "))
            if otp==og_otp:
                print("LOGIN SUCCESSFUL✅")
                return True
            print("incorrect otp enter correct opt😟")


    def login(self):
        print("enter 1: to log in with phone number📲")
        print("enter 2: to log in with email📩")
        ch=int(input("Enter your choice: "))
        if ch==1:
            phno=int(input("enter phno📞")) #phno validation
            if phno==self.phno:
                state=self.validate_otp(phno)
                self.login_status=state
            else:
                print("invalid phno🤔")

        elif ch==2:
            email=input("enter email id📨") #email validation
            if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state
            else:
                print("invalid email id🤔")
        else:
            print("Invalid choice❌")


    def order(self):
        print("--------------------MENU--------------------")
        for category in dominos.menu:
            print(f"---{category.upper()}---")
        cat=input("enter category you want to order from: 👇")
        if cat in dominos.menu:
            d=dominos.menu[cat]
            for item in d:
                print(f"{item}:{d[item]}")
            item=input("enter item you want to order: 😋")
            if item in d:
                q=int(input("enter quantity: ❔"))
                print(item,"added to cart✅🛒")
                if item in self.cart:
                    self.cart[item]+=d[item]*q
                else:
                    self.cart[item]=d[item]*q 
                print(f"{item} added to cart")
                print(self.cart)
            else:
                print("item not found😟")
        else:
            print("invalid category❌")
         


    def view_cart(self):
        print("---------DOMINOS CART🛒---------")
        if self.cart !={}:
            for item in self.cart:
                print(f"{item}:{self.cart[item]}")
            total=sum(self.cart.values())
            print("------------------------")
            print(f"➡️total amount:{total}⬅️")
            print("------------------------")
        else:
            print("cart is empty😟")
        
        ch=input("do you want to checkout? (y/n):🤔").lower()
        if ch=='y':
            print("order placed successfully✅")
            print("you will receive your order soon🍕🍕")
            print("----------------------------------------")
            self.cart={} 


    def logout(self):
        ch=input("are you sure you want to logout? (y/n):🤔 ").lower()
        if ch=='y':
            self.login_status=False
            print("logged out successfully👍")

ob=dominos("Mahisha","mahisharajesh6@gmail.com",1234567890)
'''print(ob.menu)'''



