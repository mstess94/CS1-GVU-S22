# balance_table.py
# Print table of account balances earning interest.

def balance(p, r, t):
    """Return new balance using compound annual interest. """
    return p*(1 + r)**t
    
def main():
    print("Calculates compound interest over time.")
    
main()
