create database ericsson_virtual; 
use ericsson_virtual;
create table employees(eid int,ename varchar(15),esal int);
describe employees;
alter table employees add column eadd varchar(15);
alter table employees drop esal;
alter table employees change eid empno int;
alter table employees rename to emps;
drop table emps;#delete entire table
truncate table employees;#delete only records/rows /data

insert into employees values(123,"mahesh",20000,"hyderabad");
insert into employees values(124,"naresh",40000,"banglore");
insert into employees values(125,"rajesh",50000,"hyderabad");
insert into employees values(126,"somesh",30000,"delhi");
insert into employees values(127,"suresh",35000,"banglore");
insert into employees values(128,"hitesh",45000,"delhi");
update employees set esal=esal+5000 where eadd="banglore";
update employees set esal=esal+500;
delete from employees where eid=128;
select ename,eadd from employees;
select * from employees;
select * from employees where eadd="banglore";
select * from employees where esal<40000;
select emp.*,max(esal) from employees emp;
select * from employees where esal=(select max(esal) from employees);
select min(esal) from employees;
select sum(esal) from employees;
select avg(esal) from employees;
select * from employees order by esal desc;
select e.eadd,sum(esal) from employees e group by e.eadd;




