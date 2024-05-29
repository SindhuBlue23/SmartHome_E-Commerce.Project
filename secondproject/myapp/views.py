from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from datetime import date, datetime
from django.contrib.auth import logout
from .models import product, supplier, categories, images12, cart, customer, billing, order, ordetails, cusinfo
from dateutil.parser import parse

# Create your views here.
def page1(req):
    u = req.user
    c = customer.objects.get(userid=req.user.id)
    return render(req, 'index.html', {"username": c.fname + ' ' + c.lname})

def page9(req):
    return render(req, 'frontpage.html')

def loadCart(req):
    u = req.user
    c = customer.objects.get(userid=req.user.id)
    cartItems = cart.objects.filter(cusid=c.cusid).select_related('pid').all()
    return render(req, 'cart.html', {"cartItems": list(cartItems)})

def page3(req):
    catname = req.GET.get('ProductType', 'Smart TV')
    c = categories.objects.get(catname=catname)
    products = product.objects.filter(cateid=c.cateid)
    categorynames = categories.objects.all()
    return render(req, 'left-sidebar.html',{"products":list(products),"categories":list(categorynames)})

def page4(req):
    return render(req, 'right-sidebar.html')

def page6(req):
    return render(req, 'lightbulb.html')

def page5(req):
    return render(req, 'switch.html')

def page7(req):
    return render(req, 'doorbell.html')

def page8(req):
    return render(req, 'smoke.html')

def profile(req):
    return render(req, 'profile.html')

def login(req):
    return render(req, 'login.html')

def admin(req):
    return render(req, 'admin.html')

def productsdisplay(req):
    productid = req.GET.get('pid', '')
    print(productid)
    prod = product.objects.get(pid=productid)
    #cat = categories.objects.get(cateid=prod.cateid)
    images = images12.objects.filter(pid=productid)
    return render(req, 'displayproducts.html',{"product":prod,"images":images})

def products(req):
    catname = req.GET.get('ProductType', 'Smart TV')
    c = categories.objects.get(catname=catname)
    products = product.objects.filter(cateid=c.cateid)
    categorynames = categories.objects.all()
    print('mmm')
    print(products)
    return render(req, 'products.html',{"products":list(products),"categories":list(categorynames)})

def update(req):
       print('Sindhu')
       print(req)
       pid = req.POST['pid']
       print(pid)
       x = product.objects.get(pid=pid)
       print(x)
       x.pname= req.POST.get('pname')
       x.unitsinstock = req.POST.get('uistock')
       x.price = req.POST.get('price')
       x.description = req.POST.get('description')
       x.save()
       print(x)
       return render(req, 'modify.html')

def remove(req):
    if req.method == 'POST':
       pid=req.POST['pid']
       x = product.objects.get(pid=pid)
       x.delete()
       deleteproduct = product.objects.all()
       return render(req, 'split.html',{"products":list(deleteproduct)})

def getProductById(req):
       productid = req.GET.get('pid','')
       print (productid)
       x = product.objects.get(pid=productid)
       return render(req, 'modify.html',{"product":x})

def getproducts(req):
       catname = req.GET.get('ProductType','Smart TV')
       c = categories.objects.get(catname=catname)
       products = product.objects.filter(cateid=c.cateid)
       categorynames = categories.objects.all()
       return render(req, 'split.html',{"products":list(products),"categories":list(categorynames)})

def pdetails(req):
    displaynames=supplier.objects.all()
    shownames = categories.objects.all()
    return render(req, 'prodetails.html',{"suppliers":list(displaynames),"categories":list(shownames)})

def loadproducts(req):
    catname = req.GET.get('ProductType', 'Smart TV')
    c = categories.objects.get(catname=catname)
    products = product.objects.filter(cateid=c.cateid)
    categorynames = categories.objects.all()
    return render(req, 'products.html', {"products": list(products), "categories": list(categorynames)})

def adminlogin(req):
    if req.method == "POST":
        username = req.POST['name']
        password = req.POST['pass']
        user = auth.authenticate(username=username, password=password)
        auth.login(req, user)
        if user is not None:
            if user.is_staff:
                catname = req.GET.get('ProductType', 'Smart TV')
                c = categories.objects.get(catname=catname)
                products = product.objects.filter(cateid=c.cateid)
                categorynames = categories.objects.all()
                return render(req, 'split.html', {"products": list(products), "categories": list(categorynames)})
            else:
                messages.info(req, 'Not an admin user')
                return render(req, 'admin.html')
        else:
                messages.info(req, 'Invalid username and password')
                return render(req, 'admin.html')
    else:
        return render(req, 'admin.html')

def signup(req):
    if req.method == "POST":
        userName = req.POST['userName']
        firstName = req.POST['firstName']
        lastName = req.POST['lastName']
        email = req.POST['email']
        password = req.POST['password']
        if User.objects.filter(username=userName).exists():
            messages.info(req, 'THis Username Already Exist')
            return render(req, 'login.html')
        if(password==password):
            user = User.objects.create_user(username=userName,password=password,email=email)
            user.save()
            cust = customer(userid=user.id, fname=firstName, lname=lastName)
            cust.save()
            u = req.user
            c = customer.objects.get(userid=req.user.id)
            return render(req, 'index.html', {"username": c.fname + ' ' + c.lname})
        else:
            messages.info(req, 'Password is not Matching')
            return render(req, 'login.html')

def createlog(req):
    if req.method == "POST":
        username = req.POST['nm']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        auth.login(req,user)
        if user is not None:
            u = req.user
            c = customer.objects.get(userid=req.user.id)
            print('sindhu')
            print(c)
            print(c.fname)
            return render(req, 'index.html', {"username": c.fname + ' ' + c.lname})
        else:
            messages.info(req,'Invalid username and password')
            return render(req,'login.html')
    else:
        return render(req, 'login.html')

def userlogout(req):
    if req.method == "GET":
        logout(req)
        return render(req, 'login.html')

def adminlogout(req):
    if req.method == "GET":
        logout(req)
        return render(req, 'admin.html')

def addproduct(req):
    #add code to copy image to image folder
    if req.method == "POST":
        print(req.FILES)
        # accessing value from front end pages
        supid = req.POST['selectedid']
        catid = req.POST['selectid']
        proname = req.POST['pname']
        unitstock = req.POST['uistock']
        price = req.POST['price']
        description = req.POST['description']
        img=req.FILES['pic1']
        imge=req.FILES['img2']
        image=req.FILES['img3']
        s = supplier.objects.get(sid=supid)
        c = categories.objects.get(cateid=catid)
        # storing in product database table
        p = product(sid=s,cateid=c,pname=proname,unitsinstock=unitstock, price=price, description=description, defaultimage=img)
        p.save()
        #add images to image table
        i1=images12(pid=p,image=img)
        i2=images12(pid=p,image=imge)
        i3=images12(pid=p,image=image)
        i1.save()
        i2.save()
        i3.save()
        return render(req, 'prodetails.html')
    else:
        return render(req, 'split.html')

def storecart(req):
    if req.method == 'POST':
        pid = req.POST['pid']
        qty = req.POST['quantity']
        price = req.POST['price']
        user = req.user
        total_amt = int(qty) * int(price)
        prod = product.objects.get(pid=pid)
        cust = customer.objects.get(userid=user.id)

        if req.user.is_authenticated:
            try:
                c = cart.objects.get(pid=prod, cusid=cust)
            except cart.DoesNotExist:
                c = None
            if c is None:
                c = cart(pid=prod, noproducts=qty, tprice=total_amt, cusid=cust)
                c.save()
            else:
                c.noproducts = c.noproducts + int(qty)
                c.tprice = c.noproducts * int(price)
                c.save()

            prod = product.objects.get(pid=pid)
            prod.unitsinstock = prod.unitsinstock-int(qty)
            prod.save()
            images = images12.objects.filter(pid=pid)
            messages.info(req, 'added to cart successfully!')
            return render(req, 'displayproducts.html', {"product": prod, "images": images})

def AddSupplier(req):
    if req.method == "POST":
        # accessing value from front end pages
        sname = req.POST['sname']
        semail = req.POST['semail']
        sphone = req.POST['sphone']
        s = supplier(sname=sname, semail=semail, sphno=sphone)
        s.save()
        messages.info(req, 'supplier added successfully!')
        return render(req,'addsupplier.html')
    else:
        return render(req,'addsupplier.html')

def ManageSuppliers(req):
    if req.method == "GET":
        suppliersList = supplier.objects.all()
        return render(req, 'managesuppliers.html', {"suppliers": list(suppliersList)})


def ModifySupplier(req):
    if req.method == "GET":
        sid = req.GET.get('sid')
        supplierObj = supplier.objects.get(sid=sid)
        return render(req, 'modifysupplier.html', {"supplier": supplierObj})
    elif req.method == "POST":
        sid = req.POST['sid']
        sname = req.POST['sname']
        semail = req.POST['semail']
        sphno = req.POST['sphno']
        supplierObj = supplier.objects.get(sid=sid)
        supplierObj.sname = sname
        supplierObj.semail = semail
        supplierObj.sphno = sphno
        supplierObj.save()
        messages.info(req, 'supplier updated successfully!')
        return render(req, 'modifysupplier.html', {"supplier": supplierObj})


def DeleteSupplier(req):
    if req.method == "POST":
        sid = req.POST['sid']
        x = supplier.objects.get(sid=sid)
        x.delete()
        supplierList = supplier.objects.all()
        return render(req, 'managesuppliers.html', {"suppliers": list(supplierList)})

def AddCategory(req):
    if req.method == "POST":
        # accessing value from front end pages
        catname = req.POST['catname']
        description = req.POST['description']
        s = categories(catname=catname, description=description)
        s.save()
        messages.info(req, 'category added successfully!')
        return render(req,'addcategory.html')
    else:
        return render(req,'addcategory.html')

def ManageCategories(req):
        if req.method == "GET":
            categoriesList = categories.objects.all()
            return render(req, 'managecategories.html', {"categories": list(categoriesList)})

def ModifyCategory(req):
    print(req)
    if req.method =="GET":
        catId = req.GET.get('catId')
        category = categories.objects.get(cateid=catId)
        return render(req, 'modifycategory.html', {"category":category})
    elif req.method == "POST":
        catId = req.POST['catId']
        catName = req.POST['catname']
        description = req.POST['description']
        category = categories.objects.get(cateid=catId)
        category.catname=catName
        category.description = description
        category.save()
        messages.info(req, 'category updated successfully!')
        return render(req, 'modifycategory.html', {"category": category})

def DeleteCategory(req):
    if req.method == "POST":
        catId = req.POST['catId']
        x = categories.objects.get(cateid=catId)
        x.delete()
        categoriesList = categories.objects.all()
        return render(req, 'managecategories.html', {"categories": list(categoriesList)})

def placeOrder(req):
    if req.method == "POST":
        addressid = req.POST['addressid']
        grandtotal = req.POST['grandtotal']
        print('details are')
        cardid = req.POST['selectedcard']
        print(addressid)
        print(cardid)
        address = cusinfo.objects.get(cusinfoid=addressid)
        card = billing.objects.get(bid=cardid)
        print(address)
        print(card)
        u = req.user
        c = customer.objects.get(userid=req.user.id)
        cartitems = cart.objects.filter(cusid=c).all()
        saveditems = list(cartitems)
        o = order(cusid=c, odate=date.today(), shipdate=date.today(), ostatus='ordered', totalprice=grandtotal, addressid=address,cardid=card)
        o.save()
        for item in saveditems:
           od = ordetails(oid=o, pid=item.pid, quantity=item.noproducts, price=item.tprice)
           od.save()
        cartItems = cart.objects.filter(cusid=c)
        cartItems.delete()
        u = req.user
        c = customer.objects.get(userid=req.user.id)
        return render(req, 'index.html', {"username": c.fname + ' ' + c.lname})

def ManageAddress(req):
    if req.method == "GET":
        print(req.user.id)
        c = customer.objects.get(userid=req.user.id)
        cusinfoList = cusinfo.objects.filter(cusid=c)
        return render(req, 'manageAddress.html', {"cusinfos": list(cusinfoList)})

def AddAddress(req):
    if req.method == "POST":
        # accessing value from front end pages
        aemail = req.POST['email']
        phnum = req.POST['number']
        address = req.POST['add']
        acountry = req.POST['country']
        acity = req.POST['city']
        print(req.user.id)
        c = customer.objects.get(userid=req.user.id)
        print(c)
        # storing in product database table
        a = cusinfo(cusid=c, country=acountry, address=address, phno=phnum, email=aemail, city=acity)
        a.save()
        messages.info(req, 'Address added successfully!')
        return render(req,'addAddress.html')
    else:
        return render(req,'addAddress.html')

def ModifyAddress(req):
    print(req)
    if req.method == "GET":
        cusinfoId = req.GET.get('cusinfoId')
        address = cusinfo.objects.get(cusinfoid=cusinfoId)
        return render(req, 'modifyAddress.html', {"address": address})
    elif req.method == "POST":
         cusinfoId = req.POST['cusinfoId']
         aemail = req.POST['email']
         phnum = req.POST['number']
         aaddress = req.POST['add']
         acountry = req.POST['country']
         acity = req.POST['city']
         address = cusinfo.objects.get(cusinfoid=cusinfoId)
         address.email = aemail
         address.phno = phnum
         address.address = aaddress
         address.country = acountry
         address.city = acity
         address.save()
         messages.info(req, 'Address updated successfully!')
         return render(req, 'modifyAddress.html', {"address": address})

def DeleteAddress(req):
    if req.method == "POST":
        cusinfoId = req.POST['cusinfoId']
        x = cusinfo.objects.get(cusinfoid=cusinfoId)
        x.delete()
        cusinfoList = cusinfo.objects.all()
        return render(req, 'manageAddress.html', {"cusinfo": list(cusinfoList)})

def ManageCard(req):
    if req.method == "GET":
        print(req.user.id)
        c = customer.objects.get(userid=req.user.id)
        billingList = billing.objects.filter(cusid=c)
        return render(req, 'manageCard.html', {"billing": list(billingList)})

def AddCard(req):
    if req.method == "POST":
        # accessing value from front end pages
        cname = req.POST['cardname']
        cnum = req.POST['cardnumber']
        emonth = req.POST['month']
        eyear = req.POST['year']
        cvv = req.POST['cardcvv']
        print(req.user.id)
        c = customer.objects.get(userid=req.user.id)
        print(c)
        # storing in product database table
        b = billing(cusid=c, cardname=cname, cardnum=cnum, expmonth=emonth, expyear=eyear, cvv=cvv)
        b.save()
        messages.info(req, 'Card added successfully!')
        return render(req,'addCard.html')
    else:
        return render(req,'addCard.html')

def ModifyCard(req):
    print(req)
    if req.method == "GET":
        bId = req.GET.get('bId')
        card = billing.objects.get(bid=bId)
        return render(req, 'modifyCard.html', {"billing": card})
    elif req.method == "POST":
         bId = req.POST['bId']
         cname = req.POST['cardname']
         cnum = req.POST['cardnumber']
         emonth = req.POST['month']
         eyear = req.POST['year']
         cvv = req.POST['cardcvv']
         card = billing.objects.get(bid=bId)
         card.cardname = cname
         card.cardnum = cnum
         card.expmonth = emonth
         card.expyear = eyear
         card.cvv = cvv
         card.save()
         messages.info(req, 'Card updated successfully!')
         return render(req, 'modifyCard.html', {"billing": card})

def DeleteCard(req):
    if req.method == "POST":
        bId = req.POST['bId']
        x = billing.objects.get(bid=bId)
        x.delete()
        billingList = billing.objects.all()
        return render(req, 'manageCard.html', {"billing": list(billingList)})

def GetAddresses(req):
        c = customer.objects.get(userid=req.user.id)
        cartItems = cart.objects.filter(cusid=c).all()
        totalProducts = cartItems.count()
        grandtotal = req.POST["grandtotal"]
        for i in range(0, totalProducts):
            pid = req.POST.get("products[" + str(i) + "]['pid']")
            if pid:
                productprice = req.POST["products[" + str(i) + "]['productprice']"]
                totalprice = req.POST["products[" + str(i) + "]['totalprice']"]
                prodid = int(req.POST["products[" + str(i) + "]['pid']"])
                quantity = req.POST["products[" + str(i) + "]['quantity']"]
                cid = req.POST["products[" + str(i) + "]['cid']"]
                usercart = cart.objects.get(cid=cid)
                usercart.noproducts = quantity
                usercart.tprice = totalprice
                usercart.save()
                addressList = cusinfo.objects.filter(cusid=c)
        return render(req, 'selectAddress.html', {"addresses": list(addressList),"grandtotal":grandtotal})

def GetCards(req):
    addressid = req.GET.get('selectedaddress')
    grandtotal = req.GET.get('grandtotal')
    c = customer.objects.get(userid=req.user.id)
    cardList = billing.objects.filter(cusid=c)
    return render(req, 'selectCard.html', {"cards": list(cardList),"addressid":addressid,"grandtotal":grandtotal})

def OrderStatus(req):
    c = customer.objects.get(userid=req.user.id)
    orders = order.objects.filter(cusid=c).all()
    return render(req, 'OrderStatus.html',{"orders": list(orders)})

def AdminOrderStatus(req):
    orders = order.objects.all()
    return render(req, 'AdminOrderStatus.html', {"orders": list(orders)})

def ModifyOrder(req):
    if req.method == "GET":
        oId = req.GET.get('oId')
        orders = order.objects.get(oid=oId)
        return render(req, 'modifyOrder.html', {"order": orders})
    elif req.method == "POST":
        oId = req.POST['oId']
        ostatus = req.POST['ostatus']
        odate = req.POST['odate']
        #t=datetime.strptime('Sept. 6, 2021','%mmm. %d, %Y')
        orderdetails = order.objects.get(oid=oId)
        orderdetails.ostatus = ostatus
        orderdetails.shipdate = parse(odate)
        orderdetails.save()
        messages.info(req, 'Order updated successfully!')
        return render(req, 'modifyOrder.html', {"order": orderdetails})

def removeFromCart(req):
    c = customer.objects.get(userid=req.user.id)
    cid = req.GET.get('cid')
    x = cart.objects.get(cid=cid)
    x.delete()
    cartItems = cart.objects.filter(cusid=c).select_related('pid').all()
    return render(req, 'cart.html', {"cartItems": list(cartItems)})