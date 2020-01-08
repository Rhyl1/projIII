from django.shortcuts import render

# Create your views here.
def get_ferment_list(request):
    results = Item.objects.all()
    return render(request, "ferment_list.html", {
        'items': results
    })

    