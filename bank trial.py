print('''                  <<***STATE BANK OF INDIA***>>             ''')
print("                  [WITH You - all  the ways]           ")
print("welcome we can help you by:-")
print(" 1>> create a account \n 2>> open created account \n 3>> update a account ")
n=int(input('enter your response--'))
list1=[]
if n==1:
    print('For creating your account please give all deatls sir ....please enter correct details')
    print("                    <<<REGISTRATION FORM>>>              ")
    a=input('Enter Your Complete Name-')
    b=int(input('enter your coplete phone number-'))
    c=input('please enter father or mother name{any one name is compulsory}-')
    d=input('please enter a nominee name-')
    e=input('please enter the account type {buisness/joint/personal}-')
    f=input('please enter the amount you want to deposit=')
    g=float((input('enter the online transaction limit per month')))
    print('Thank you sir for giving your details and precious time your account is created and we welcome you in our BOB Family')
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1.append(d)
    list1.append(e)
    list1.append(f)
    list1.append(g)
    import random
    z=random.randint(696969,84848484)
    g=z
    print('Account Number provided:-',z)
    print("2>> open created account \n 3>> update a account \n 4>> exit ")
    l=int(input('enter your response'))
    def create():
        print('NAME=',a)
        print('Phone Number=',b)
        print('Gaurdian Name=',c)
        print('Nominee Name =',d)
        print('Account Type=',e)
        print('Account Balance=',f)
        print('Online transaction limit=',g)
    if l==2:
        k=int(input('enter your account number:-'))
        if k==g or k==g:
            create()
            print(list1)
    elif l==3:
        k=int(input('enter your account number:-'))
        if k==g or k==g:
            print('your account details are :-')
            create()
            print(list1)
            print("1>> Change phone number \n2>> change nominee name \n3>> Change account type")
            h=int(input('enter your response:-'))
            print('account details before',list1)
            if h==1:
                w=int(input('enter new phone number:-'))
                list1.remove(b)
                list1.insert(1,w)
            elif h==2:
                r=input('enter new nominee name')
                list1.remove(d)
                list1.insert(3,r)
            elif h==3:
                t=input('enter new account type:--')
                list1.remove(e)
                list1.insert(4,t)
            else:
                print('invalid input')
            print('Updated accpunt details',list1)
    else:
        print('invalid input !!!')
elif n==2 or n==3:
    print('your account is still not opened in our bank. so create a account')
print('THANK YOU FOR VISITING OUR SITE . MAY YOUR PROBLEM HAS BEEN SOLVED-- STATE BANK OF INDIA  ')
