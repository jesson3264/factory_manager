from django.shortcuts import render
from .models import Orders
from .forms import OrderForm, OrderSelectForm
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from warehouse.models import Product
from django.core.mail import send_mail
from django.core.paginator import Paginator

def order_list(request):
    ## order_lists 1
    order_lists = Orders.objects.all()
    context = {}
    # 翻页信息
    paginator = Paginator(order_lists, 10)  # 每页显示10个对象

    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1

    page_number = int(page_number)
    total_pages = paginator.num_pages
    print("page_number:", page_number)
    page_info = {}
    page_info["number"] = page_number
    page_info["paginator"] = {}
    page_info["paginator"]['num_pages'] = total_pages
    print("total_pages", total_pages)
    if total_pages > page_number:
        page_info['has_next'] = True
        page_info['next_page_number'] = page_number + 1
    if page_number > 1:
        page_info['has_previous'] = True
        page_info['previous_page_number'] = page_number - 1

    context['page_obj'] = page_info

    order_list = paginator.get_page(page_number)
    context['order_lists'] = order_list

    return render(request, 'order_list.html', context)


def order_modify(request, order_pk):
    usr = request.user
    if usr.is_authenticated:
        order_tem = Orders.objects.get(pk=order_pk)
        if request.method == 'POST':
            ordermodifyform = OrderForm(request.POST)
            if ordermodifyform.is_valid():
                print(ordermodifyform.cleaned_data['order_name'])
                order_tem.order_name = Product.objects.get(product_name=ordermodifyform.cleaned_data['order_name'])
                order_tem.order_client = ordermodifyform.cleaned_data['order_client']
                order_tem.order_number = ordermodifyform.cleaned_data['order_number']
                order_tem.order_price = ordermodifyform.cleaned_data['order_price']
                order_tem.order_total_price = ordermodifyform.cleaned_data['order_total_price']
                order_tem.order_end = ordermodifyform.cleaned_data['order_end']
                order_tem.order_supplement = ordermodifyform.cleaned_data['order_supplement']
                order_tem.save()
                return redirect(reverse('order_list'))
        else:
            ordermodifyform = OrderForm(initial={'order_name':order_tem.order_name, 'order_client':order_tem.order_client,
                                                 'order_number':order_tem.order_number, 'order_price':order_tem.order_price,
                                                 'order_total_price':order_tem.order_total_price,'order_end':order_tem.order_end,
                                                 'order_supplement':order_tem.order_supplement})
            context = {}
            context['ordermodifyform'] = ordermodifyform
            return render(request, 'order_modify.html', context)
    else:
        return redirect(reverse('login'))


def order_delete(request, order_pk):
    usr = request.user
    if usr.is_authenticated:
        order_tem = Orders.objects.get(pk=order_pk)
        order_tem.delete()
        return redirect(reverse('order_list'))
    else:
        return redirect(reverse('login'))

def order_append(request):
    usr = request.user
    if usr.is_authenticated:
        if request.method == 'POST':
            orderappendform = OrderForm(request.POST)
            if orderappendform.is_valid():
                order_name = orderappendform.cleaned_data['order_name']
                order_tem = Product.objects.get(product_name=order_name)
                order_client = orderappendform.cleaned_data['order_client']
                order_number = orderappendform.cleaned_data['order_number']
                order_price = orderappendform.cleaned_data['order_price']
                order_total_price = orderappendform.cleaned_data['order_total_price']
                order_end = orderappendform.cleaned_data['order_end']
                order_supplement = orderappendform.cleaned_data['order_supplement']
                add = Orders(order_name=order_tem, order_client=order_client, order_number=order_number,order_price=order_price,
                             order_total_price=order_total_price, order_end=order_end, order_supplement=order_supplement)
                add.save()
                send_mail('Subject here', '有一个新的订单.', 'jesson3264@163.com',
                          ['jesson3264@163.com'], fail_silently=False)
                return redirect(reverse('order_list'))
        else:
            orderappendform = OrderForm()
            context = {}
            context['orderappendform'] = orderappendform
            return render(request, 'order_append.html', context)
    else:
        return redirect(reverse('login'))


def order_select(request):
    usr = request.user
    if usr.is_authenticated:
        if request.method == 'POST':
            OrderSelectForms = OrderSelectForm(request.POST)
            if OrderSelectForms.is_valid():
                keyword = OrderSelectForms.cleaned_data['keyword']
                valueword = OrderSelectForms.cleaned_data['valueword']
                ans_tem = []
                print(keyword, valueword)
                if keyword == '1':  # 产品
                    ans_tem1 = Product.objects.filter(product_name__contains=valueword)
                    ans_tem = Orders.objects.filter(order_name__in=ans_tem1)

                if keyword == '2':  # 客户
                    ans_tem = Orders.objects.filter(order_client__contains=valueword)

                context = {}
                context['order_lists'] = ans_tem
                return render(request, 'order_list.html', context)
        else:
            OrderSelectForms = OrderSelectForm()
            context = {}
            context['OrderSelectForms'] = OrderSelectForms
            return render(request, 'order_select.html', context)
    else:
        return redirect(reverse('login'))
