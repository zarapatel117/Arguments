def total_calc (bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total_amount=round(total,2)
    print(f"please pay {total_amount} ")
total_calc(150,20)    
    