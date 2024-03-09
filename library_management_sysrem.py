#-------------------------------------------------------#
##LIBRARY MANAGEMENT SYSTEM##
#-------------------------------------------------------#

print("\t\t_____________________________________________________________________")
print("\t\t|.....................@@@@@@WELCOME@@@@@@.....................|")
print("\t\t|.......................@@@@@@TO@@@@@@.......................|")
print("\t\t|...................@@@LIBRARY MANAGEMENT@@@...................|")
print("\t\t|......................@@@@@SYSTEM@@@@@......................|")
print("\t\t|..................@@MADE BY:VIPIN KUMAR@@.......|")
print("\t\t|...............SUBMITTED TO: MRS. MEENU SINGH...............|")
print("\t\t|...................@@@@YEAR: 2021-2022@@@@...................|")
print("\t\t–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
print("\n_______________________________________________________________________")

import mysql.connector as mc

mydb=mc.connect(host='local',user='<user_name>',passwd='1234')

cur=mydb.cursor() #---creating cursor object

#create table book
cur.execute("create table if not exist books(B_CODE varchar(20),B_NAME varchar(20),AU_NAME varchar(20),QTY int")

#create table issue
cur.execute("create table if not exist issue(Reg_no varchar(20),Name varchar(20),Phone_no int,B_code varchar(20),B_issue varchar(20),Issue_date date)")

#create table submit
cur.execute("create table if not exist submit(Reg_no varchar(20),Name varchar(20),B_code varchar(20),Submit_date date)")



#Add new books
def Add_Book():
	a=input("Enter bcode:")
	b=input("Enter bname:")
	c=input("Enter Authorname:")
	d=int(input("Enter quantity:"))
	rec=(a,b,c,d)
	s="insert into books values(%s,%s,%s,%s)"
	cur.execute(s,rec)
	mydb.commit()
	print("///..........................Data Entered Successful...............................///")
	main()


#To issue a book
def Issue_Book():
	a=input("Enter reg_no:")
	b=input("Enter name:")
	c=int(input("Enter phone_no:"))
	d=input("Enter book_code:")
	e=input("Enter book_issue:")
	f=input("Enter issue_date:")
	rec=(a,b,c,d,e,f)
	s="insert into issue values(%s,%s,%s,%s,%s,%s)"
	cur.execute(s,rec)
	mydb.commit()
	print("–––––––––––––––––––––––––––––––––––––––––––––––––––")
	print("Book issued to:",b)
	book_up(d,-1)
    
 
#To submit  book
def Submit_Book():
    r=input("Enter reg_no:")
    n=input("Enter name:")
    co=input("Enter book_code:")
    d=input("Enter submit_date:")
    a="insert into submit values(%s,%s,%s,%s)"
    data=(r,n,co,d)
    cur.execute(a,data)
    mydb.commit()
    print("–––––––––––––––––––––––––––––––––––––––––––––––––––")
    print("Book Submitted from:",n)
    book_up(d,1)
   

#To Book details
def Display_Book():
	print("–––––––––––––––––––––––––––––––––––––––––––––––––––")
	print("Press1: Search a book(B_CODE)\
	\nPress2:Dispaly all the books ")
	print("–––––––––––––––––––––––––––––––––––––––––––––––––––")
	n=int(input ("Enter your choice"))
	if n==1:
		r=input("Enter b_code:")
		j=(r,)
		s="select * from books where B_CODE=%s"
		cur.execute(s,j)
		res=cur.fetchall()
		print("[b_code,b_name,au_name,qty]")
		for i in res:
			print(i[0],i[1],i[2],i[3])
	elif n==2:
		a="select * from books"
		cur.execute(a)
		myresult=cur.fetchall()
		print("[b_code,b_name,au_name,qty]")
		for i in myresult:
			print(i[0],i[1],i[2],i[3])
	else:
		print("**************Wrong Choice**************")
		print("–––––––––––––––––––––––––––––––––––––––––––––––––––")
		main()


#To delete a book  from data
def Delete_Book():
    ac=input("Enter Book_Code")
    a="delete from books where B_CODE=%s"
    data=(ac,)
    cur.execute(a,data)
    mydb.commit()
    main()
   
 
#To update quantity of book
def book_up(d,u):
	s="select QTY from book where B_CODE =%s "
	n=(d,)
	cur.execute(s,n)
	myres=cur.fetchone()
	t=myres[0]+u
	mysql="update book set QTY=%s where B_CODE=%s"
	e=(t,n)
	cur.execute(mysql,e)
	mydb.commit()
	main()
	 
	 
def main():
	user_id=input("Enter user_id:")
	p_wd=input("Enter passed:")
	if p_wd=="1234":
		print("**************Hello sir/mam, You logged in successfully***************")
		print("_________________________________________________________")
		print("\nMAIN MENU:\
		\nPress1:Add Book\
		\nPress2:Issue Book\
		\nPress3:Submit Book\
		\nPress4:Display Books\
		\nPress5:Delete Book\
		\nPress6:Exit")
		print("–––––––––––––––––––––––––––––––––––––––––––––––––––")
		n=int(input("Enter your choice:"))
		if n==1:
			Add_Book()
		elif n==2:
			Issue_Book()
		elif n==3:
			Submit_Book()
		elif n==4:
			Display_Book()
		elif n==5:
			Delete_Book()
		elif n==6:
			print("–––––––––––––––––––––––––––––––––––––––––––––––––––")
			print("************** (:))Thanks For Using Our Program (:)) *****************")
			print("–––––––––––––––––––––––––––––––––––––––––––––––––––")
		else:
			print("*********Wrong Choice**************")
			main()
	else:
		print("*************WRONG PASSWORD**************")
		main()
main()
		