
MAX_LINE=3
MIN_BET=1
MAX_BET=1000



def deposit():
    while True:
      amount=int(input("please enter the amount of deposit"))
      if amount > 0:
            break
      else: 
         print("please enter the valid number")
    
    return amount
def  get_number_of_lines ():
     while True:
          lines = int(input("choose the number of lines you want up to 3"))
          if 1<=lines<=MAX_LINE:
             break
          else: 
               print("plese enter valid no.of lines")
  
     return lines
def get_bet():
     while True:
         bet=(f"pleasse enter between ${MIN_BET} to ${MAX_BET} for betting")
         if MIN_BET<bet<MAX_BET:
             bet=int(bet)
             break
         else:
             print("please choose valid amount")

       

def main():
     balance =deposit()
     lines =get_number_of_lines() 
     print(balance,lines) 
  
main() 

   