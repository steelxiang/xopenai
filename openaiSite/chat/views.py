from django.shortcuts import render

from django.http import HttpResponse
import os
import openai


# openai.api_key = os.getenv("OPENAI_API_KEY")


# Create your views here.
def chat(request):
    if request.method == 'POST':
        prompt = request.POST.get("prompt")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["||"]
        )
        answer = response['choices'][0]['text']

    return HttpResponse(answer)


def image(request):
    if request.method == 'POST':
        prompt = request.POST.get("prompt")
        response = openai.Image.create(
            prompt=prompt,
            n=2,
            size="512x512"
        )
        answer = response['data']

    return HttpResponse(answer)


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
