from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Notice
from django.db.models import Q
from .forms import notice_publishForm
from .forms import NoticeSelectForm
from django.core.mail import send_mail
from django.core.paginator import Paginator

def notice(request, notice_pk):
    notice = Notice.objects.filter(pk=notice_pk)
    context = {}
    context['notice'] = notice
    return render(request, 'notice.html', context)


def notice_select(request):
    usr = request.user
    if usr.is_authenticated:
        if request.method == 'POST':
            MaintainSelectForms = NoticeSelectForm(request.POST)
            if MaintainSelectForms.is_valid():
                keyword = MaintainSelectForms.cleaned_data['keyword']
                valueword = MaintainSelectForms.cleaned_data['valueword']
                ans_tem = []
                print(keyword, valueword)
                if keyword == '1':  # 标题
                    ans_tem = Notice.objects.filter(Q(title__contains=valueword))
                    # ans_tem = Notice.objects.filter(notice_id__in=ans_tem1)

                if keyword == '2':  # 内容
                    ans_tem = Notice.objects.filter(Q(content__contains=valueword))
                    # ans_tem = Notice.objects.filter(otice_id__in=ans_tem1)

                if keyword == '3': # 发表人
                    ans_tem = Notice.objects.filter(Q(author__contains=valueword))
                context = {}
                context['notice'] = ans_tem
                return render(request, 'notice_lists.html', context)
        else:
            nsf = NoticeSelectForm()
            context = {}
            context['NoticeSelectForm'] = nsf
            return render(request, 'notice_select.html', context)
    else:
        return redirect(reverse('login'))


def notice_publish(request):
    if request.method == 'POST':
        notice_form = notice_publishForm(request.POST)
        if notice_form.is_valid():
            title = notice_form.cleaned_data['title']
            content = notice_form.cleaned_data['content']
            author = request.user
            add = Notice(title=title, content=content, author=author)
            add.save()
            send_mail('Subject here', '有新通知.', 'jesson3264@163.com',
                      ['jesson3264@163.com'], fail_silently=True)
            return redirect(reverse('notice_lists'))
    else:
        notice_form = notice_publishForm()
    context = {}
    context['notice_form'] = notice_form
    return render(request, 'notice_publish.html', context)


def notice_lists(request):
    items = Notice.objects.all()
    context = {}
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

    context['page_obj'] = page_info
    item = paginator.get_page(page_number)

    context['notice'] = item
    return render(request, 'notice_lists.html', context)


def NoticeModify(request, notice_pk):
    usr = request.user
    notc = get_object_or_404(Notice, pk=notice_pk)
    if usr.is_authenticated:
        if request.method == 'POST':
            notice_form = notice_publishForm(request.POST)
            if notice_form.is_valid():
                notc.title = notice_form.cleaned_data['title']
                notc.content = notice_form.cleaned_data['content']
                notc.author = usr
                notc.save()
                return redirect(reverse('notice_lists'))

        notice_form = notice_publishForm(initial={'title': notc.title, 'author': notc.author, 'content': notc.content})
        context = {}
        context['notice_form'] = notice_form
        return render(request, 'notice_modify.html', context)
    else:
        return redirect(reverse('login'))


def delete_notice(request, notice_pk):
    usr = request.user
    notc = get_object_or_404(Notice, pk=notice_pk)
    if usr.is_authenticated:
        notc.delete()
        return redirect(reverse('notice_lists'))
    else:
        return redirect(reverse('login'))
