from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [

    	{"restaurants_name":"BackYard","food_type":"International"},
    	{"restaurants_name":"Mcdonalds","food_type":"Burger"},
    	{"restaurants_name":"PF Changs","food_type":"Asian"},
    	{"restaurants_name":"PF Changs","food_type":"Asian"}
    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": 
    	{
    		"restaurants_name":"PFChangs","food_type":"Asian"
    	}
    }
    return render(request, 'detail.html', context)
