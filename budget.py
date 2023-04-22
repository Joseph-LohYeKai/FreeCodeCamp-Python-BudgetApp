

class Category:

    def __init__(self,name):
        self.name=name
        self.ledger=list()

    def __str__(self):
        LengthofCat=len(self.name)
        items=""
        total=0
        title=self.name.center(30,"*")
        title=title + "\n"
        for item in self.ledger:
            name=item['description'][0:23]
            LengthofName=30-len(name)
            price=f"{item['amount']:>{LengthofName}.2f}"
            total+=item['amount']
            items+= name + price + "\n"
        output= title+items+ "Total: "+ str(total)
        return output


    #A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self,amount,description=""):
        total=0
        for items in self.ledger:
            value=items['amount']
            total+=value
        if self.check_funds(amount)==True:
            amount=-abs(amount)
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False


    def get_balance(self):
            total=0
            for items in self.ledger:
                value=items['amount']
                total+=value
            return total

    def transfer(self,amount,category):
            if self.check_funds(amount)==True:
                self.withdraw(amount,"Transfer to "+ category.name)
                category.deposit(amount,"Transfer from "+ self.name)
                return True
            else:
                return False
        
    def check_funds(self,amount):
            total=self.get_balance()
            if amount>total:
                return False
            else:
                return True


def create_spend_chart(categories):
    NameList=[]
    percentages=[]
    Withdraw_List=[]
    for category in categories:
        names=category.name
        NameList.append(names)
        Total=0
        
        
        for item in category.ledger:

            amount=item['amount']
            
            
            if amount<0:
                Total+=amount
        Withdraw_List.append(Total)
        
        
    for numbers in Withdraw_List:
        percent=round((numbers/sum(Withdraw_List))*100)
        percentages.append(percent)

    
    
    Longestword=max(NameList,key=len)
    LengthofLongestWord=len(Longestword)
    
    NewCategories=[names.ljust(LengthofLongestWord) for names in NameList]
    
    
    

        
    
    
    output="Percentage spent by category" +"\n"
    for numbers in reversed(range(0,110,10)):
        output+= f"{numbers:>3}|"
        #for each number on the left side, it would have to loop through the percentages first
        for percent in percentages:
            if percent>=numbers:
                output+= " o "
            else:
                output+="   "
        output+= " \n"
    output+= "    "+"-"*10 + "\n"
    for catergory in zip(*NewCategories):
        output+=f"{'  '.join(catergory):>12}" + '  \n'
    output=output.rstrip("\n")
    return output
                    



