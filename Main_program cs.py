from prettytable import PrettyTable
import csv
import random
import mysql.connector
tbl23=PrettyTable()
mycon=mysql.connector.connect(host='localhost',user='chiru',passwd='chiru')
mycur=mycon.cursor()
def connection(user):
    global mycon,mycur
    mycon=mysql.connector.connect(host='localhost',user='chiru',passwd='chiru',db=user)
    mycur=mycon.cursor()
mycur.execute("CREATE DATABASE IF NOT EXISTS timetable")
from datetime import datetime
passparameter=input('enter R for arrangements/T for timetable: ')
print('_____________________________________________________________________________________________________________________________')
print()
print('--------------------------------WAIT-----------------------------------------------------------------------------------------')
if passparameter=='R' or passparameter=='r':
     connection('timetable')
     tablesofte='show tables'
     mycur.execute(tablesofte)
     bata=mycur.fetchall()
     print('''    1:monday
    2:tuesday
    3:wednesday
    4:thusday
    5:friday
    6:saturaday
    7:sunday''')
     print('______________________________________________________________________________________',end='')
     print('____________________________________')
     dayofarr=int(input('enter for the day which arragement on: '))
     klkj=[]
     for q in bata:
          tulp=list(q)
          if tulp[0][0:1] in ["1","2","3","4","5","6","7","8","9","0","s"]:
               continue
          elif tulp[0][0:7] in 'arrangement':
               continue
          else:
               if tulp[0][0:1] in '1234567890':
                    continue
               else:
                    if tulp[0][0:7] in 'arrangement':
                        continue
                    else:
                        klkj+=tulp
     arrlist=[]
     for teac in klkj:
          count=0
          teachedr='select * from {}'.format(teac)
          mycur.execute(teachedr)
          opio=mycur.fetchall()
          for i in opio:
               if i==[]:
                    break
               else:
                    if str(dayofarr) in i[0][1]:
                         count+=1
          if count<6:
               arrlist+=[[teac]+[count]]
     arrteach=int(input('arrangement for how many teachers: '))
     print('___________________________________________________________')
     listo=[]
     print('enter details of teachers for arrangement')
     print()
     for arre in range(arrteach):
          print('----------------------------------------------------')
          tedetail=input('enter teacher name: ')
          print()
          listo+=[tedetail]
     arrangement=[]
     for i in listo:
           show_tables_query = "SHOW TABLES LIKE %s"
           mycur.execute(show_tables_query, ('%' + i + '%',))
           data = mycur.fetchall()
           data_list=list(data)
           for sub in data_list:
                tea='select * from {}'.format(sub[0])
                mycur.execute(tea)
                data2=mycur.fetchall()
                arrangl=[]
                for ped in data2:
                     li=list(ped)
                     if str(dayofarr) == str([ped][0][0][1]):
                         arrangl+=[li]
                for n in arrangl:
                    rand=random.choice(arrlist)
                    if rand[1]<6 and rand not in listo:
                         arrangement+=[[n]+[rand[0]]]
     print(arrangement)
     dateti= datetime.now()
     datetimen = dateti.strftime("%Y%m%d%H%M%S")
     creatab='create table {}(period varchar(100),class varchar(10),teacher varchar(100))'.format(str('arrangement'+str(datetimen)))
     mycur.execute(creatab)
     for mn in arrangement:
          insertda='''insert into {}(period,class,teacher) values
          ("{}","{}","{}")'''.format(str('arrangement'+str(datetimen)),mn[0][0],mn[0][1],mn[1])
          mycur.execute(insertda)
     mycon.commit()
     fina='arrangement'+str(datetimen)+'.csv'
     mp=open(fina, 'w')
     mycsv = csv.writer(mp)
     tabl='select * from {}'.format(str('arrangement'+str(datetimen)))
     mycur.execute(tabl)
     meta=mycur.fetchall()
     for each in meta:
          if each==[]:
               continue
          else:
               mycsv.writerow(each)
     mp.close()
     print('succesfully inserted arrangement data')
elif passparameter=='t' or passparameter=='T':
          table=[]
          classsection=''
          opio=''
          csvp=''
          cla_ss=""
          def timetable(day):
               global table,classsection,cla_ss,ipio,csvp
               tablename=classsection
               table=table+[tablename]
               kp=open(opio,'a')
               wy=csv.writer(kp)
               y='''create table {}(c1 varchar(1500),c2 varchar(1150),c3 varchar(1150),c4 varchar(1150),c5 varchar(1150)
               ,c6 varchar(1150),c7 varchar(1150),c8 varchar(1150))'''.format(tablename)
               mycur.execute(y)
               for i in day:
                   tabs = len(i)
                   values = [str(item) for item in i[:tabs]]
                   columns = ', '.join(['c{}'.format(j+1) for j in range(tabs)])
                   placeholders = ', '.join(['"{}"'.format(value) for value in values])
                   query = 'INSERT INTO {} ({}) VALUES ({})'.format(tablename, columns, placeholders)
                   mycur.execute(query)
               mycon.commit()
               pel=[]
               for i in range(len(day[0])):
                    pel+=[str(i+1)]
               whole=[]
               whole+=[['Day']+[*pel]]
               tbl_head=whole
               for per in day:
                    tana=[]
                    for days in per:
                         tana+=[days[1]]
                    if day.index(per)==0:
                         whole+=[['MON']+[*tana]]
                    elif day.index(per)==1:
                         whole+=[['TUE']+[*tana]]
                    elif day.index(per)==2:
                         whole+=[['WED']+[*tana]]
                    elif day.index(per)==3:
                         whole+=[['THU']+[*tana]]
                    elif day.index(per)==4:
                         whole+=[['FRI']+[*tana]]
                    elif day.index(per)==5:
                         whole+=[['SAT']+[*tana]]
                    else:
                         whole+=[['sunday']+[*tana]]
               wy.writerow(['CLASS:'+tablename])
               wy.writerows(whole)
               lisang=[]
               for mmkd in whole:
                       if whole.index(mmkd)==0:
                           continue
                       else:
                            lisang+=[mmkd]
               tbl23=PrettyTable(tbl_head[0])
               for i in lisang:
                   tbl23.add_row(i)
               print(tbl23)
               return table
          noofclasslis=[]
          def noofclass():
               global cla_ss,classsection,opio,csvp
               import csv
               import random
               noofclass=int(input('enter no of class: '))
               print('______________________________________________________________')
               print()
               startclass=int(input('enter first starting class: '))
               print('_______________________________________________________________')
               print()
               endingclass=int(input('enter last ending class:  '))
               print('______________________________________________________________')
               print()
               noofsections=int(input('enter no of sections per each class: '))
               print('______________________________________________________________')
               print()
               nos=[]
               for i in range(noofsections):
                    print('enter ' ,i+1, 'section name')
                    print('--------------------------------')
                    print()
                    section=input('enter section name: ')
                    print('---------------------------------')
                    print()
                    nos=nos+[section]
               pe=int(input('enter no. periods in a day: '))
               print('---------------------------------------------------------')
               days=int(input('enter no. days per week: '))
               print('---------------------------------------------------------')
               cla_ss = (endingclass-startclass)+1
               csvp=input('enter a file name to save: ')
               opio=csvp+'.csv'
               kp=open(opio,'w')
               wy=csv.writer(kp)
               for nooftime in range(noofsections*noofclass):
                    if cla_ss*noofsections != noofclass:
                              print('you entered incorrect details of no of class')
                              break
                    while startclass < endingclass+1:
                         for k in nos:
                              classsection=''
                              classsection+=str(startclass)+k
                              print('**********************************************************************************',end='')
                              print('**********************************************')
                              print()
                              print('enter details for class: ',classsection)
                              y="select name,sub from s where cla_ss like '%{}%'".format(classsection)
                              mycur.execute(y)
                              data=mycur.fetchall()
                              periodnumber=[]
                              print('ENTER NUMBER OF PERIODS EQUAL TO :',pe*days,'FOR CLASS ',classsection)
                              i=0
                              while True:
                                   sum=0
                                   i=0
                                   lisofp=[]
                                   for i in range(len(data)):
                                        everyweek=[]
                                        classperiods=list(data[i])
                                        everyweek=everyweek+classperiods
                                        print('--------------------------------------------------------------')
                                        print(classperiods)
                                        print()
                                        print('enter number of',str(classperiods[1]),' periods per week')
                                        print()
                                        noofperiodsperweek=int(input('enter no. of periods per week: '))
                                        everyweek=everyweek+[noofperiodsperweek]+[int(0)]
                                        periodnumber.append(everyweek)
                                        sum=sum+noofperiodsperweek
                                   if sum==pe*days:
                                        break
                                   else:
                                       if i==3:
                                           break
                                       if sum>pe*days:
                                            i+=1
                                            print('you entered more no. of periods then required','please enter again')
                                            
                                       else:
                                            i+=1
                                            print('you entered less no. of periods then required','please enter again')
                                       
                              mycode=periodnumber
                              day=[]
                              while len(day)<days:
                                   per=[]
                                   while len(per)<pe:
                                        period=list(random.choice(periodnumber))
                                        if table==[]:
                                             for i in range(len(periodnumber)):
                                                  if periodnumber[i][0] == period[0] and periodnumber[i][2] != 0 :
                                                       per.append(period)
                                                       periodnumber[i][2] -= 1
                                                       break
                                             
                                        else:
                                             connection('timetable')
                                             poi = len(day)
                                             iop = len(per)
                                             for classe in table:
                                                  cuiig='select * from {}'.format(classe)
                                                  mycur.execute(cuiig)
                                                  check=mycur.fetchall()
                                                  if period[0] in check[poi][iop]:
                                                       break
                                                  else:
                                                       for i in range(len(periodnumber)):
                                                            if periodnumber[i][0] == period[0] and periodnumber[i][2] != 0:
                                                                 per.append(period)
                                                                 periodnumber[i][2] -= 1
                                                                 break
                                                  break
                                   liste=[]
                                   for job in per:
                                        liste+=[job[1]]
                                   ft=False
                                   for my in liste:
                                        for perd in periodnumber:
                                             if perd[1]==my:
                                                  perd[3]+=1
                                                  break
                                   mycode=periodnumber
                                   for jobe in mycode:
                                        if jobe[2]==1:
                                             if jobe[2]==jobe[3]:
                                                  ffffjj=False
                                                  continue
                                        elif jobe[2]!=1:
                                             if jobe[3]<(jobe[2]/4)+1:
                                                  ft=False
                                                  continue
                                        else:
                                             ffffjj=True
                                             break
                                   if ft :
                                        for mkd in periodnumber:
                                             mkd[2]+=1
                                             mkd[3]=0
                                   else:
                                        if len(day)==days:
                                             break
                                        else:
                                             day.append(per)
                                             for yd in periodnumber:
                                                  yd[3]=0
                              fun=timetable(day)
                         startclass+=1
          print('ENTER "L" FOR LESS NUMBER OF TEACHERS DATA AND "M" FOR MORE NUMBER OF TEACHER DATA')
          print()
          nopi=input('enter your choice: ')
          print('_______________________________________WAIT____________________________________',end='')
          print('__________________________________________________')
          if nopi=='m' or nopi=='M':
               print()
               connection('timetable')
               z='drop database timetable'
               mycur.execute(z)
               oip='create database timetable'
               mycur.execute(oip)
               connection('timetable')
               x='create table s(sno int,name char(30),sub char(20),cla_ss varchar(150))'
               mycur.execute(x)
               print('CREATE A CSV FILE WITH TEACHERS DATA AS (SERIAL NO.,NAME,SUBJECT,TEACHING CLASS')
               print()
               taj=input('ENTER CSV FILE NAME: ')
               print('______________________________________________________________________________________')
               print()
               print('--------------------------------WAIT--------------------------------------------------')
               majj=taj+'.csv'
               fp=open(majj,'r')
               w=csv.reader(fp)
               for i in w:
                    if i==[]:
                        continue
                    else:
                         a=i[0]
                         b=i[1]
                         c=i[2]
                         d=i[3]
                         pa='insert into s(sno,name,SUB,cla_ss) values({},"{}","{}","{}")'.format(a,b,c,d)
                         mycur.execute(pa)
               mycon.commit()
               maketi=noofclass()
          if nopi=='l' or nopi=='L':
               print()
               print('................................WAIT...................................................')
               connection('timetable')
               z='drop database timetable'
               mycur.execute(z)
               oip='create database timetable'
               mycur.execute(oip)
               connection('timetable')
               x='create table s(sno int,name char(30),sub char(20),cla_ss varchar(150))'
               mycur.execute(x)
               numteachers=int(input('enter number of teachers'))
               print('_________________________________________________________________________________________')
               for i in range(numteachers):
                              a=int(input('enter s.no'))
                              print('-------------------------------------------------------------------')
                              b=input('enter name')
                              print('-------------------------------------------------------------------')
                              c=input('enter subject')
                              print('-------------------------------------------------------------------')
                              d=input('enter teaching class')
                              print('-------------------------------------------------------------------')
                              pa='insert into s(sno,name,SUB,cla_ss) values({},"{}","{}","{}")'.format(a,b,c,d)
                              mycur.execute(pa)
               mycon.commit()
               maketi=noofclass()
          listobya=[]
          teach=input('enter Y if you want add periods of each teachers/ enter anything else to exit: ')
          if teach=='Y' or teach=='y':
               teacher=input('enter file name to add teachers data: ')
               print('------------------------------------------------------------------------------------')
               print('__________________________________________WAIT_______________________________________')
               marcht=teacher+'.csv'
               tb=open(marcht,'w')
               ty=csv.writer(tb)
               x='select name,sub,cla_ss from s'
               mycur.execute(x)
               data=mycur.fetchall()
               for yu in data:
                         sdf=yu[0]
                         sa_pu=''
                         for char in str([yu]):
                              if char in ['1','2','3','4','5','6','7','8','9']:
                                   break
                              if char.isalnum():
                                   sa_pu += char
                         listobya+=sa_pu
                         y = 'create table {}(period varchar(200),class varchar(50))'.format(sa_pu)
                         mycur.execute(y)
                         for man in table:
                              io='select * from {}'.format(man)
                              mycur.execute(io)
                              meta=mycur.fetchall()
                              for uiop in meta:
                                   for lkjfas in uiop:
                                        if lkjfas==None:
                                            continue
                                        else:
                                             if sdf in lkjfas:
                                                  hgjfkd=[meta.index(uiop)]
                                                  mzm=[uiop.index(lkjfas)]
                                                  insert_query = '''insert into {} values
                                                  ("{}","{}")'''.format(sa_pu,[(hgjfkd[0]+1)]+[(mzm[0]+1)],man)
                                                  mycur.execute(insert_query)
                                                  mycon.commit()
                         listopk='select * from {}'.format(sa_pu)
                         mycur.execute(listopk)
                         pata=mycur.fetchall()
                         ty.writerow([sdf])
                         ty.writerows(pata)
               print('data inserted successfully into',csvp,'and',teacher)
               tb.close()
else:
     print('enter correct choice')
mycon.close()
