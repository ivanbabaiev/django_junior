from django.shortcuts import render, render_to_response


def index(request):
    """
    Call index.html
    """
    return render(request, 'index.html')


def custom_404_server_error(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def custom_500_server_error(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response
