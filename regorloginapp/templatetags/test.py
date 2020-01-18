from django import template
register = template.Library()
@register.filter

def do_calculation_final(Name, Age, Occupation, Purchase_Price,Deposit_Paid,Bond_Term,Fixed_Interest_Rate):
    Const1 =100
    Loan_Amount= (self.Purchase_Price*(((Const1 - self.Deposit_Paid)))-(X-Interest)) 
    Bond_Term1=(12*Bond_Term)
    R=1+float(Fixed_Interest_Rate)*(0.12)
    X=(Purchase_Price*((1-Deposit_Paid)*0.01))*(R**Bond_Term1)*(1-R)/(1-R**Bond_Term1)
    Monthly_Interest=[]
    Monthly_Balance=[]
    for i in range(1,Bond_Term1+1):
        Interest=(Purchase_Price*((1-Deposit_Paid)*0.01))*(R-1)
        Loan_Amount=(Purchase_Price*((1-(Deposit_Paid)*0.01))-(X-Interest))
        Monthly_Interest =np.append(Monthly_Interest,Interest)
        Monthly_Balance =np.append(Monthly_Balance,Loan_Amount)

#     Monthly_Interest =np.append[Monthly_Interest,Interest]
#     Monthly_Balance =np.append(Monthly_Balance,Loan_Amount)

    solution=do_calculation(Purchase_Price,Deposit_paid,Bond_Term,Fixed_Interest_Rate)
    # Produce Visualization of Monthly Loan Balance and Interest
    plt.plot(range(1,Bond_Term1+1),Monthly_Interest,'r',lw=2)
    plt.xlabel('month')
    plt.ylabel('monthly interest ($)')
    plt.show()
    plt.savefig('Monthly Loan interest.png')
    plt.plot(range(1,Bond_Term1+1),Monthly_Balance,'b',lw=2)
    plt.xlabel('month')
    plt.ylabel('monthly loan balance ($)')
    plt.show()
    plt.savefig('Monthly Loan Balance.png')
   
    return self.solution, self.Monthly_Interest, self.Monthly_Balance
    def __str__(self):
        return self.Name, self.Purchase_Price, self.Deposit_Paid, self.Monthly_Interest, self.Monthly_Balance,self.Monthly_Interest, self.Monthly_Balance 

