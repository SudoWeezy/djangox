from django.shortcuts import render
from django.http import HttpResponse
import requests
def hello_world(request):
   return HttpResponse("Hello, world. You're at the hello_word.")

def dog_picture(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        return HttpResponse(f'<img src="{image_url}" alt="Random Dog Image"/>')
    return HttpResponse("Failed to fetch dog image", status=500)


def random_user(request):
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]
        user_html = f'''
            <div>
                <img src="{user['picture']['large']}" alt="User Picture" "/>
                <p>Name: {user['name']['first']} {user['name']['last']}</p>
                <p>Email: {user['email']}</p>
                <p>Location: {user['location']['city']}, {user['location']['country']}</p>
            </div>
        '''
        return HttpResponse(user_html)
    return HttpResponse("Failed to fetch user data", status=500)

def pie_chart(request):
    # Data for the pie chart
    labels = ["Red", "Blue", "Yellow"]
    colors = ["#ff6384", "#36a2eb", "#ffce56"]

    # Create the pie chart segments
    pie_chart_html = '''
        <div class="pie-chart"></div>
        <div class="pie-chart-label">
    '''
    for label, color in zip(labels, colors):
        pie_chart_html += f'''
            <div><span style="background-color:{color};"></span>{label}</div>
        '''
    pie_chart_html += '</div>'

    return HttpResponse(pie_chart_html)

def index(request):
    if request.headers.get('Hx-Request'):  # Check if the request is made via HTMX
        return HttpResponse("Hello World")
    return render(request, 'main/index.html')
