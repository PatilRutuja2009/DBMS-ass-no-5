ASSIGNMENT NO:-5
Problem Statement:- Write PL/SQL Block of code for different applications.

declare
days number;
date_of_issue1 date;
date_of_return1 date;
fine1 number;
roll_no1 Borrower5.Roll_No%Type;
roll_no2 Borrower5.Roll_No%Type;
book_name Borrower5.Name_of_Book%Type;
book_name1 Borrower5.Name_of_Book%Type;
begin
roll_no1:=&roll_no1;
book_name:='&book_name';
select Roll_No,Name_of_Book,Date_of_issue,Date_of_Return into roll_no2,book_name1,Date_of_return1,Date_of_issue1 from Borrower5 where Roll_No=roll_no1 and Name_of_Book=book_name;
days:=Date_of_return1-Date_of_issue1;
if(days<15)then
fine1:=0;
else
if(days>15 and days<30)then
fine1:=days*5;
else
if(days>30)then
fine1:=days*50;
end if;
end if;
end if;
insert into fine5 values(roll_no1,Date_of_return1,fine1);
update Borrower5 set status='r' where status='i' and Roll_no=roll_no1 and Name_of_Book=book_name;
end;
/
  1* insert into Borrower5 values(1,'Dinesh','01-jan-2018','DBMS','i','12-feb-2018')
SQL> /

1 row created.
SQL> ed
Wrote file afiedt.buf
84
q
  1* insert into Borrower5 values(2,'Rajesh','03-mar-2018','RDBMS','i','06-june-2018')
1 row created.
SQL> ed    
Wrote file afiedt.buf
q
  1* insert into Borrower5 values(3,'Rajesh','07-mar-2018','CNE','r','30-mar-2018')
SQL> /

1 row created.
SQL> ed
Wrote file afiedt.buf
81
q
 1* insert into Borrower5 values(4,'Rajesh','20-apr-2018','SE&PM','r','30-may-2018')
SQL> /
Enter value for pm: 1
old   1: insert into Borrower5 values(4,'Rajesh','20-apr-2018','SE&PM','r','30-may-2018')
new   1: insert into Borrower5 values(4,'Rajesh','20-apr-2018','SE1','r','30-may-2018')
1 row created.
SQL> select * from Borrower5;
   ROLL_NO NAME               DATE_OF_ISSUE
---------- ------------------------------ ------------------
NAME_OF_BOOK               S DATE_OF_RETURN
------------------------------ - ------------------
     1 Dinesh              01-JAN-18
DBMS                   i 12-FEB-18

     2 Rajesh              03-MAR-18
RDBMS                   i 06-JUN-18

     3 Mahesh              07-MAR-18
CNE                   r 30-MAR-18


   ROLL_NO NAME               DATE_OF_ISSUE
---------- ------------------------------ ------------------
NAME_OF_BOOK               S DATE_OF_RETURN
------------------------------ - ------------------
     4 Dipak              20-APR-18
SE1                   r 30-MAY-18

OUTPUT:
Enter value for roll_no1: 1
old  10: roll_no1:=&roll_no1;
new  10: roll_no1:=1;
Enter value for book_name: DBMS
old  11: book_name:='&book_name';
new  11: book_name:='DBMS';
PL/SQL procedure successfully completed.
SQL> select * from Borrower5;

   ROLL_NO NAME               DATE_OF_ISSUE
---------- ------------------------------ ------------------
NAME_OF_BOOK               S DATE_OF_RETURN
------------------------------ - ------------------
     1 Dinesh              01-JAN-18
DBMS                   r 12-FEB-18

     2 Rajesh              03-MAR-18
RDBMS                   i 06-JUN-18

     3 Mahesh              07-MAR-18
CNE                   r 30-MAR-18


   ROLL_NO NAME               DATE_OF_ISSUE
---------- ------------------------------ ------------------
NAME_OF_BOOK               S DATE_OF_RETURN
------------------------------ - ------------------
     4 Dipak              20-APR-18
SE1                   r 30-MAY-18

SQL> select * from fine5;

    ROLLIN DATE_R          AMOUNT
---------- ------------------ ----------
     1 01-JAN-18               0

