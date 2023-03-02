import uuid

from django.shortcuts import render

from django.http import HttpResponse
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
uu = str(uuid.uuid4())


# Create your views here.
def chat(request):
    if request.method == 'POST':
        prompt = request.POST.get("prompt")
        message = [{
            "role": "user",
            "content": prompt,
        }]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message,
            # id=session_key
            # user=session_key
            # temperature=0.5,
            # max_tokens=1024,
            # top_p=1,
            # frequency_penalty=0.0,
            # presence_penalty=0.0,
            # stop=["||"]
        )
        answer = response['choices'][0]['message']["content"]
    context = {'title': 'Hello world hahahha',
               "message": answer
               }
    # return HttpResponse(answer)
    return render(request, 'index.html', context)


def image(request):
    if request.method == 'POST':
        prompt = request.POST.get("prompt")
        response = openai.Image.create(
            prompt=prompt,
            n=2,
            size="512x512"
        )
        answer = response['data']
    context = {'title': 'Hello world ',
               "message": answer
               }
    # return HttpResponse(answer)
    return render(request, 'index.html', context)


def edit(request):
    if request.method == 'POST':
        prompt = request.POST.get("prompt")
        image = request.FILES.get("image")
        mask = request.FILES.get("mask")
        # prompt = request.POST.get("prompt")
        response = openai.Image.create_edit(
            image=image,
            mask=mask,
            # mask=open("mask.png", "rb"),
            prompt=prompt,
            n=2,
            size="1024x1024"
        )
        answer = response['data']

    return HttpResponse(answer)


def test(request):
    context = {'hello': 'Hello world hahahha'}
    return render(request, 'test.html', context)


def test(request):
    context = {'title': 'Hello world hahahha'}
    return render(request, 'index.html', context)
