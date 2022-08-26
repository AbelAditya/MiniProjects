import csv
fv=open('Airport M.csv' , 'w')
w=csv.writer(fv)
w.writerow(['AIRCRAFT','DESTINATION','TIME OF DEPARTURE','ETA','STATUS'])
w.writerow(['IG0073','CHENNAI','17:00','19:30','BOARDING'])
w.writerow(['AI1345','DELHI','18:00','21:00','SECURITY'])
w.writerow(['SJ6589','CALCUTTA','12:00','14:00','CHECK IN'])
fv.close
print('done')
fv.close()

print('\t\tWelcome to Madurai Airport(IXM). \n\t\t Please log in to access the data')
print("\tWhat would you like to access?")
print("\tINFORMATIVE DISPLAY(1)")
print("\tEMPLOYEE SHIFT LIST(2)")
print("\tSEE THE SHIFT(3)\n \tCLOCK IN/OUT")
d=int(input('enter your choice(numeric value):'))


    
if d==1:
    x=int(input('enter your id number:'))
    if x in[12,23,34,5457,56,67,34,57] :
        f=open('Airport M.csv', 'r')
        for i in f:
            print('\t\t',i)
        f.close
        a=input('\t Would you like to update the display?\n Press "y" to update\n\t Would you like to add a flight? \nif yes , type "add":')
        if a.lower()=='add':
            flightno=input("Enter flight number(mind the caps lock):")
            dest=input("Enter destination:")
            etd=input("Enter ETD:")
            eta=input("Enter ETA:")
            stat=input('Update status:')
            fd=open('Airport M.csv' ,'a',newline='')
            w=csv.writer(fd)
            w.writerow([flightno,dest,etd,eta,stat])
            fd.close()

           
            
        elif a.lower()=='y':
            r=csv.reader(open('Airport M.csv','r'))
            lines=list(r)
            print(lines)
            n=input('Enter the aircraft number(ensure capslock):')
            for i in lines:
                if i==[]:
                    lines.remove(i)
            
            for i in lines:
                if i[0]==n:
                    print(i)
                    z=input("What would you like to update?:\n \t1. Destination\n\t 2.ETD \n\t 3. ETA \n\t 4. STATUS")
                    
                    if z=='1':
                        print("Current destination", i[1])
                        y=input("Enter new destination:")
                        i[1]=y
                        print("New destination",i[1])
                        
                        print(i)
                    elif z=='2':

                        print('Current ETD',i[2])
                        y=input('Enter new ETD:')
                        i[2]=y
                        print('New ETD:',i[2])
                        print(i)
                    elif z=='3':
                        print('Current ETA',i[3])
                        y=input('Enter new ETA:')
                        i[3]=y
                        print('New ETA:',i[3])
                    elif z=='4':
                        print('Current status',i[4])
                        y=input('Enter new status:')
                        i[4]=y
                        print('New status:',i[4])
                     
                print(i)
                up=open('Airport M.csv' ,'w',newline='')
                for i in lines:
                    w=csv.writer(up)
                    w.writerow(i)
                   
                up.close()
                

                    
                
              
elif d==2:
    k=input('Which shift would you like to access? \n Morning or Evening?')
    if k.lower()=='m':
        g=int(input('Would you like to display the list(1) or \nadd an employee(2) or \n remove an employee(3)'))
        if g==1:
            with open('Employee list (M).csv','r') as em:
                for i in em:
                    print(i)  
          
        elif g==2:
            em=open('Employee list (M).csv','a')
            q=csv.writer(em)
            q.writerow(['ID','NAME','SECTION','STATUS'])
            g=int(input('enter the number of employees are to be added'))
                
            for i in range(g):
                p=input('enter id number')
                o=input('enter name')
                l=input('enter section')
                s=input('enter status')
                q.writerow([p,o,l,s])
            em.close()
        elif g==3:
            r=csv.reader(open('Employee list (M).csv','r'))
            lines=list(r)
            for i in lines:
                if i==[]:
                    lines.remove(i)
            em=open('Employee list (M).csv','w')
            q=csv.writer(em)
            l=input('Enter the id of the employee you want to remove from this shift:')
            for i in lines:
                print(i)
                if i[0]==l:
                    continue
                else:
                    q.writerow(i)
                    print(i)
            em.close()
            
    elif k.lower()=='e':
        g=int(input('Would you like to display list or \nadd an employee?(2)or \nremove an employee(3)'))
        if g==1:
            with open('Employee list (E).csv','r') as ev:
                for i in ev:
                    print(i)
        elif g==2:
            ev=open('Employee list (E).csv','a')
            q=csv.writer(ev)
            g=int(input('enter the number of employees are to be added'))
            q.writerow(['ID','NAME','SECTION','STATUS'])
            for i in range(g):
                p=input('enter id number')
                o=input('enter name')
                l=input('enter section')
                s=input('enter status')
                q.writerow([p,o,l,s])
            ev.close()
        elif g==3:
            r=csv.reader(open('Employee list (E).csv','r'))
            lines=list(r)
            for i in lines:
                if i==[]:
                    lines.remove(i)
            em=open('Employee list (E).csv','w')
            q=csv.writer(em)
            l=input('Enter the id of the employee you want to remove from this shift:')
            for i in lines:
                print(i)
                if i[0]==l:
                    continue
                else:
                    q.writerow(i)
                    print(i)
            em.close()
            
elif d==3:
    h=int(input('\tAre you admin?(1) OR\t\n Are you clocking in?(2)'))
    if h==1:
        y=int(input('Please enter your password'))
        if y in[12,23,34,5457,56,67,34,57]:
            o=input('Enter M for morning shift or E for evening shift')
            if o.lower()=='m':
                 ev=csv.reader(open('Employee list (M).csv','r'))
                 emps=list(ev)
                 for i in emps:
                     print(i)
            elif o.lower()=='e':
                ev=csv.reader(open('Employee list (E).csv','r'))
                emps=list(ev)
                for i in emps:
                    print(i)
            
    elif h==2:
        o=input("Please select your shift")
        
        if o.lower()=='m':
            print('Welcome to the morning shift:')
            f=input('Please enter your id to clock in')
            em=csv.reader(open('Employee list (M).csv'))
            eM=list(em)
            print(eM)
            for i in eM:
                if i==[]:
                    eM.remove(i)
            for i in eM:
                    
                if i[0]==f:
                    print('Current status',i[3])
                    y=input('enter 01 to clock in and 02 to clock out')
                    if y=='01':
                        i[3]='IN'
                    elif y=='02':
                        i[3]='OUT'
                    else:
                        print('wrong choice, try again.')
                        continue
                
                up=open('Employee list (M).csv' ,'w',newline='')
                for i in eM:
                    w=csv.writer(up)
                    w.writerow(i)
                    
                up.close()
                 
        elif o.lower()=='e':
            
            print('Welcome to the evening shift:')
            f=input('Please enter your id to clock in')
            em=csv.reader(open('Employee list (E).csv'))
            eM=list(em)
            print(eM)
            for i in eM:
                if i==[]:
                    eM.remove(i)
            for i in eM:
                    
                if i[0]==f:
                    print('Current status',i[3])
                    y=input('enter 01 to clock in and 02 to clock out')
                    if y=='01':
                        i[3]='IN'
                    elif y=='02':
                        i[3]='OUT'
                    else:
                        print('wrong choice, try again.')
                        continue
                    
                up=open('Employee list (E).csv' ,'w',newline='')
                for i in eM:
                    w=csv.writer(up)
                    w.writerow(i)
                    
                up.close()
