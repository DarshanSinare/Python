import calender as cal
print("calender program in python\n");
print("Enter 'x' for exit");
y=input("ENTER THE YEAR");
if y=='x':
    exit();
else:
    m=input("enter the month:");
yy=int(y);
mm=int(m);
print("\n",cal.month(yy,mm))