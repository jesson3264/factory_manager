from django.shortcuts import render,redirect,get_object_or_404
from .models import Facility, Maintain,Repair
from .forms import BaoxiuForm,FacilityForm, FacilitySelectForm, MaintainAppendForm, MaintainSelectForm, RepairedSelectForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.core.mail import send_mail
from django.core.paginator import Paginator

def facility_document(request):
    items = Facility.objects.all()
    context= {}
    # 翻页信息
    paginator = Paginator(items, 10)  # 每页显示10个对象
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1

    page_number = int(page_number)
    total_pages = paginator.num_pages
    print("page_number:", page_number)
    page_info = {"number": page_number, "paginator": {}}
    page_info["paginator"]['num_pages'] = total_pages
    print("total_pages", total_pages)
    if total_pages > page_number:
        page_info['has_next'] = True
        page_info['next_page_number'] = page_number + 1
    if page_number > 1:
        page_info['has_previous'] = True
        page_info['previous_page_number'] = page_number - 1

    item = paginator.get_page(page_number)
    context['page_obj'] = page_info

    context['facilities'] = item
    return render(request, 'facility_document.html', context)


def maintain_document(request):
    items = Maintain.objects.all()
    context= {}

    # 翻页信息
    paginator = Paginator(items, 10)  # 每页显示10个对象
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
    item = paginator.get_page(page_number)
    context['page_obj'] = page_info

    context['facilities'] = item
    return render(request, 'maintain_document.html', context)


def baoxiu(request, user_pk):
    ur =get_object_or_404(User, pk=user_pk)
    context = {}
    if request.method == 'POST':
        baoxiu_form = BaoxiuForm(request.POST)
        if baoxiu_form.is_valid():
            question = baoxiu_form.cleaned_data['question']
            facility_name = baoxiu_form.cleaned_data['facility']
            try:
                faci_tems = Facility.objects.filter(facility_name=facility_name)
                faci_itm = None
                if len(faci_tems) == 0:
                    raise Exception("")
                faci_tem = faci_tems[0]
                user_tel = ur.get_staff_tel()
                add = Repair(facility_id=faci_tem, baoxiu_staff_name=ur, baoxiu_staff_tel=user_tel, baoxiu_complementary=question )
                add.save()
                send_mail('Subject here', '有一个故障需要您取处理.', 'jesson3264@163.com',
                          ['jesson3264@163.com'], fail_silently=True)
                return redirect(reverse('baoxiu_list'))
            except Exception as e:
                print('e')
                baoxiu_form.add_error('facility', '请输入正确的设备名称')
        # return render(request, 'baoxiu.html', context)
    else:
        baoxiu_form  = BaoxiuForm()

    context['baoxiu_form'] = baoxiu_form
    return render(request, 'baoxiu.html', context)


def baoxiu_list(request):
    items = Repair.objects.filter(repair_staff_name=None)
    context= {}

    # 翻页信息
    paginator = Paginator(items, 10)  # 每页显示10个对象
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
    item = paginator.get_page(page_number)
    context['page_obj'] = page_info


    context['repairs'] = item
    return render(request, 'baoxiu_list.html', context)

def waiting_repair(request):
    items = Repair.objects.filter(repair_staff_name=None)
    context = {}

    # 翻页信息
    paginator = Paginator(items, 10)  # 每页显示10个对象
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
    item = paginator.get_page(page_number)
    context['page_obj'] = page_info

    context['count'] = items.count()
    context['repairs'] = item
    return render(request, 'waiting_repair.html', context)

def repaired_list(request):
    items = Repair.objects.filter(~Q(repair_staff_name=None))
    context = {}

    # 翻页信息
    paginator = Paginator(items, 10)  # 每页显示10个对象
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
    item = paginator.get_page(page_number)
    context['page_obj'] = page_info

    context['count'] = items.count()
    context['repairs'] = item
    return render(request, 'repaired_list.html', context)

def mark_done(request,repair_pk,user_pk):
    user = request.user
    if user.is_authenticated:
        ur =get_object_or_404(User, pk=user_pk)
        repair_tem = Repair.objects.get(pk=repair_pk)
        repair_tem.repair_staff_name = ur
        repair_tem.save()
        return redirect(reverse('waiting_repair'))
    else:
        return redirect(reverse('login'))


def facility_append(request):
    usr = request.user
    if usr.is_authenticated:
        if request.method == 'POST':
            FacilityForms = FacilityForm(request.POST)
            if FacilityForms.is_valid():
                facility_name = FacilityForms.cleaned_data['facility_name']
                version = FacilityForms.cleaned_data['version']
                price = FacilityForms.cleaned_data['price']
                add = Facility(facility_name=facility_name, version=version,
                                   price=price, buyer=usr)
                add.save()
                return redirect(reverse('facility_document'))
        else:
            FacilityForms = FacilityForm()
            context = {}
            context['FacilityForms'] = FacilityForms
            return render(request, 'facility_append.html', context)
    else:
        return redirect(reverse('login'))


def facility_select(request):

    usr = request.user
    if usr.is_authenticated:
        if request.method == 'POST':
            FacilitySelectForms = FacilitySelectForm(request.POST)
            if FacilitySelectForms.is_valid():
                keyword = FacilitySelectForms.cleaned_data['keyword']
                valueword = FacilitySelectForms.cleaned_data['valueword']
                ans_tem = []
                print(keyword, valueword)
                if keyword == '1':#设备名称
                    ans_tem = Facility.objects.filter(Q(facility_name__contains=valueword))

                if keyword == '2':#购买时间
                    ans_tem = Facility.objects.filter(buy_time__contains=valueword)
                if keyword == '3':#购买人
                    ans_tem1 = User.objects.filter(Q(username__contains=valueword))
                    ans_tem = Facility.objects.filter(buyer__in=ans_tem1)

                if keyword == '4':#购买价格
                    ans_tem = Facility.objects.filter(price=valueword)

                context = {}
                context['facilities'] = ans_tem
                return render(request, 'facility_document.html', context)
        else:
            FacilitySelectForms = FacilitySelectForm()
            context = {}
            context['FacilitySelectForms'] = FacilitySelectForms
            return render(request, 'facility_select.html', context)
    else:
        return redirect(reverse('login'))


def facility_modify(request, facility_pk):
    usr = request.user
    if usr.is_authenticated:
        facility_tem = Facility.objects.get(pk=facility_pk)
        if request.method == 'POST':
            FacilityForms = FacilityForm(request.POST)
            if FacilityForms.is_valid():
                facility_tem.facility_name = FacilityForms.cleaned_data['facility_name']
                facility_tem.version = FacilityForms.cleaned_data['version']
                facility_tem.price = FacilityForms.cleaned_data['price']
                facility_tem.save()
                return redirect(reverse('facility_document'))
        else:
            FacilityForms = FacilityForm(initial={'facility_name':facility_tem.facility_name, 'version':facility_tem.version,'price':facility_tem.price})
            context = {}
            context['FacilityForms'] = FacilityForms
            return render(request, 'facility_modify.html', context)
    else:
        return redirect(reverse('login'))


def facility_delete(request, facility_pk):
    usr = request.user
    if usr.is_authenticated:
        pos = Facility.objects.get(pk=facility_pk)
        pos.delete()
        return redirect(reverse('facility_document'))
    else:
        return redirect(reverse('login'))


def maintain_append(request):
    usr = request.user
    if usr.is_authenticated:
        MaintainAppendForms = MaintainAppendForm()
        if request.method == 'POST':
            MaintainAppendForms = MaintainAppendForm(request.POST)
            if MaintainAppendForms.is_valid() is False:
                context = {'MaintainAppendForms': MaintainAppendForms}
                return render(request, 'maintain_append.html', context)

            if MaintainAppendForms.is_valid():
                try:
                    facility_tem= Facility.objects.get(facility_name=MaintainAppendForms.cleaned_data['facility_id'])
                    if facility_tem is None:
                        raise Exception('e')

                    complmentary = MaintainAppendForms.cleaned_data['complmentary']

                    add = Maintain(facility_id=facility_tem, complmentary=complmentary,
                                   staff_name=usr)
                    add.save()
                    return redirect(reverse('maintain_document'))
                except Exception as e:
                    context = {}
                    MaintainAppendForms.add_error('facility_id', '请确认设备名称是否存在')
                    context['MaintainAppendForms'] = MaintainAppendForms
                    return render(request, 'maintain_append.html', context)
        else:
            # MaintainAppendForms = MaintainAppendForm()
            context = {}
            context['MaintainAppendForms'] = MaintainAppendForms
            return render(request, 'maintain_append.html', context)

    else:
        return redirect(reverse('login'))


def maintain_modify(request, maintain_pk):
    usr = request.user
    if usr.is_authenticated:
        maintain_tem = Maintain.objects.get(pk=maintain_pk)
        if request.method == 'POST':
            MaintainAppendForms = MaintainAppendForm(request.POST)
            if MaintainAppendForms.is_valid():
                maintain_tem.facility_id = Facility.objects.get(facility_name=MaintainAppendForms.cleaned_data['facility_id'])
                maintain_tem.complmentary = MaintainAppendForms.cleaned_data['complmentary']

                maintain_tem.save()
                return redirect(reverse('maintain_document'))
        else:
            MaintainAppendForms = MaintainAppendForm(initial={'facility_id':maintain_tem.facility_id, 'complmentary':maintain_tem.complmentary})
            context = {}
            context['MaintainAppendForms'] = MaintainAppendForms
            return render(request, 'maintain_modify.html', context)
    else:
        return redirect(reverse('login'))


def maintain_select(request):
    usr = request.user
    if usr.is_authenticated:
        if request.method == 'POST':
            MaintainSelectForms = MaintainSelectForm(request.POST)
            if MaintainSelectForms.is_valid():
                keyword = MaintainSelectForms.cleaned_data['keyword']
                valueword = MaintainSelectForms.cleaned_data['valueword']
                ans_tem = []
                print(keyword, valueword)
                if keyword == '1':#设备名称
                    ans_tem1 = Facility.objects.filter(Q(facility_name__contains=valueword))
                    ans_tem = Maintain.objects.filter(facility_id__in=ans_tem1)

                if keyword == '2':#购买人
                    ans_tem1 = User.objects.filter(Q(username__contains=valueword))
                    ans_tem = Maintain.objects.filter(staff_name__in=ans_tem1)


                context = {}
                context['facilities'] = ans_tem
                return render(request, 'maintain_document.html', context)
        else:
            MaintainSelectForms = MaintainSelectForm()
            context = {}
            context['MaintainSelectForms'] = MaintainSelectForms
            return render(request, 'maintain_select.html', context)
    else:
        return redirect(reverse('login'))


def repaired_select(request):

    usr = request.user
    if usr.is_authenticated:
        if request.method == 'POST':
            RepairedSelectForms = RepairedSelectForm(request.POST)
            if RepairedSelectForms.is_valid():
                keyword = RepairedSelectForms.cleaned_data['keyword']
                valueword = RepairedSelectForms.cleaned_data['valueword']
                ans_tem = []
                if keyword == '1':#设备名称
                    ans_tem1 = Facility.objects.filter(Q(facility_name__contains=valueword))
                    ans_tem = Repair.objects.filter(facility_id__in=ans_tem1)

                if keyword == '2':#报修人
                    ans_tem1 = User.objects.filter(Q(username__contains=valueword))
                    ans_tem = Repair.objects.filter(Q(baoxiu_staff_name__in=ans_tem1),~Q(repair_staff_name=None))
                if keyword == '3':#维修人
                    ans_tem1 = User.objects.filter(Q(username__contains=valueword))
                    ans_tem = Repair.objects.filter(repair_staff_name__in=ans_tem1)


                context = {}
                print(ans_tem.count())
                context['count'] = ans_tem.count()
                context['repairs'] = ans_tem
                return render(request, 'repaired_list.html', context)
        else:
            RepairedSelectForms = RepairedSelectForm()
            context = {}
            context['MaintainSelectForms'] = RepairedSelectForms
            return render(request, 'maintain_select.html', context)
    else:
        return redirect(reverse('login'))


def maintain_delete(request, maintain_pk):
    usr = request.user
    if usr.is_authenticated:
        pos = Maintain.objects.get(pk=maintain_pk)
        pos.delete()
        return redirect(reverse('maintain_document'))
    else:
        return redirect(reverse('login'))