r_no=45
date="10-Nov-2025"
c='alice smith'
print("=" * 30)
print("Cash Recipt".capitalize().center(30))
print(f"Recipt No: RCP-{str(r_no).rjust(5,'0')}".center(30))
print(f"Date: {date}".center(30))
print(f"Customer: {c.title()}".center(30))
print("=" * 30)