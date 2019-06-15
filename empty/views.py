from django.shortcuts import render

# Create your views here.


def main(request):
    template_name = 'empty/page.html'

    return  render(request, template_name)