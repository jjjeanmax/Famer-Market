from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from .tables import *


def menu_view(request):
    template = loader.get_template('statement/menu.html')
    return HttpResponse(template.render({'': ''}, request))


class AllMarketView(APIView):

    @staticmethod
    def get(request):
        qs = FamersInfos.objects.values(
            "fmid",
            "market_name",
            "country",
            "city",
            "state",
            "zip",
            "comment__reviews",
            "comment__ratings",
        )

        data = list(qs)
        paginator = Paginator(data, 13)
        page = request.GET.get('page')
        d = paginator.get_page(page)
        return render(request, 'statement/table.html', {"d": d})


class GetByEntry(APIView):
    @staticmethod
    def get(request):
        entry = request.GET.get('query')
        if len(entry) == 0:
            return redirect('all_market')

        qs_by_country = FamersInfos.objects.values(
            "fmid",
            "market_name",
            "country",
            "city",
            "state",
            "zip",
            "comment__reviews",
            "comment__ratings",
        ).filter(country=entry)

        qs_by_index = FamersInfos.objects.values(
            "fmid",
            "market_name",
            "country",
            "city",
            "state",
            "zip",
            "comment__reviews",
            "comment__ratings",

        ).filter(zip=entry)

        qs_by_state = FamersInfos.objects.values(
            "fmid",
            "market_name",
            "country",
            "city",
            "state",
            "zip",
            "comment__reviews",
            "comment__ratings",
        ).filter(state=entry)

        qs_by_city = FamersInfos.objects.values(
            "fmid",
            "market_name",
            "country",
            "city",
            "state",
            "zip",
            "comment__reviews",
            "comment__ratings",
        ).filter(city=entry)

        data_qs_by_country = list(qs_by_country)
        data_qs_by_index = list(qs_by_index)
        data_qs_by_state = list(qs_by_state)
        data_qs_by_city = list(qs_by_city)
        data = data_qs_by_city + data_qs_by_index + data_qs_by_state + data_qs_by_country
        paginator = Paginator(data, 13)
        page = request.GET.get('page')
        d = paginator.get_page(page)
        return render(request, 'statement/detail.html', {"d": d, "entry": entry})


class DetailMarket(APIView):
    @staticmethod
    def get(request, marketname):
        qs_by_market_name = FamersInfos.objects.values(
            "fmid",
            "market_name",
            "country",
            "city",
            "state",
            "zip",
            "web_site",
        ).filter(market_name=marketname)
        qs_by_market_name_product = FamersProducts.objects.values(
            "cheese",
            "flowers",
            "eggs",
            "vegetables",
            "meat",
            "trees",
            "wine",
            "coffee",
            "fruits",
            "Grains"
        ).filter(fmid=qs_by_market_name[0]["fmid"])

        qs_by_market_name_p_comments_user = CommentsUser.objects.values(
            "username",
            "reviews",
            "ratings",
        ).filter(fmid=qs_by_market_name[0]["fmid"])

        list_aviable_products = []
        for k, v in qs_by_market_name_product[0].items():
            if v == "Y":
                list_aviable_products.append(k)
        data = list(qs_by_market_name)

        return render(request, 'statement/infos.html',
                      {
                          "data": data,
                          "products": list_aviable_products,
                          "comments": qs_by_market_name_p_comments_user
                      })


def CommentView(request, marketname):
    qs_by_market_name = FamersInfos.objects.values("fmid").filter(market_name=marketname)
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            reviews = request.POST.get('reviews')
            ratings = request.POST.get('ratings')

            if len(username) != 0 and 1 <= int(ratings) <= 5:
                Comments, created = CommentsUser.objects.update_or_create(
                    fmid=qs_by_market_name[0]["fmid"],
                    username=username,
                    reviews=reviews,
                    ratings=ratings)
                Comments.save()

                faners_infos = FamersInfos.objects.get(market_name=marketname)
                faners_infos.comment = Comments
                faners_infos.save(update_fields=["comment"])
                return redirect('infos_market', marketname)

            context = {"market": marketname, "message": ""}
            return render(request, 'statement/comments.html', context)
        except Exception as e:
            print(e)
            context = {'message': "username already exist", "market": marketname}
            return render(request, 'statement/comments.html', context)

    context = {"market": marketname, "message": ""}
    return render(request, 'statement/comments.html', context)


def DeleteCommentView(request, marketname):
    qs_by_market_name = FamersInfos.objects.values("fmid").filter(market_name=marketname)
    CommentsUser.objects.filter(fmid=qs_by_market_name[0]["fmid"]).delete()
    return redirect('infos_market', marketname)


class SortByEntry(APIView):
    @staticmethod
    def get(request):
        entry = request.GET.get('q')
        try:
            if len(entry) == 0:
                return redirect('all_market')
        except TypeError:
            pass

        data = []

        if (str(entry).lower()) == "страна":
            print(True)
            qs_by_country = FamersInfos.objects.values(
                "fmid",
                "market_name",
                "country",
                "city",
                "state",
                "zip",
                "comment__reviews",
                "comment__ratings",
            ).order_by('-country')
            data_qs_by_country = list(qs_by_country)
            data += data_qs_by_country

        elif str(entry).lower() == "индекс":
            qs_by_index = FamersInfos.objects.values(
                "fmid",
                "market_name",
                "country",
                "city",
                "state",
                "zip",
                "comment__reviews",
                "comment__ratings",
            ).order_by('-zip')
            data += list(qs_by_index)

        elif str(entry).lower() == "штат":
            qs_by_state = FamersInfos.objects.values(
                "fmid",
                "market_name",
                "country",
                "city",
                "state",
                "zip",
                "comment__reviews",
                "comment__ratings",
            ).order_by('-state')
            data += list(qs_by_state)

        elif str(entry).lower() == "город":
            qs_by_city = FamersInfos.objects.values(
                "fmid",
                "market_name",
                "country",
                "city",
                "state",
                "zip",
                "comment__reviews",
                "comment__ratings",
            ).order_by('-city')
            data += list(qs_by_city)

        paginator = Paginator(data, 13)
        page = request.GET.get('page')
        d = paginator.get_page(page)
        return render(request, 'statement/statement_template.html', {"d": d, "entry": entry})
