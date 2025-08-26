import pickle
import pandas as pd
import os
from django.shortcuts import render, redirect
from .models import Dress,UserMeasurements
from django.conf import settings
import requests

def indexAI(request):
    d = Dress.objects.all()
    return render(request,'indexAI.html')

def category(request):
    return render(request,'category.html')

def fabric(request):
    return render(request,'fabric.html')

def select_fabric(request):
    if request.method == 'POST':
        request.session['selected_fabric'] = request.POST.get('fabric')
        return redirect('category')

def select_dress(request):
    if request.method == 'POST':
        request.session['selected_dress'] = request.POST.get('dress_type')
        return redirect('measure')

MODEL_PATH = os.path.join('AiTailor', 'stitching_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def measurement_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        chest = float(request.POST.get('chest'))
        waist = float(request.POST.get('waist'))
        hips = float(request.POST.get('hips'))
        shoulders = float(request.POST.get('shoulders'))
        arm_length = float(request.POST.get('armLength'))
        desc = request.POST.get('description')
        fabric = request.POST.get('fabric')
        dress_type = request.POST.get('dress_type')

        UserMeasurements.objects.create(
            name=name,
            height=height,
            weight=weight,
            chest=chest,
            waist=waist,
            hips=hips,
            shoulders=shoulders,
            arm_length=arm_length,
            fabric=fabric,
            dress_type=dress_type,
        )

        input_dict = {
            'height': height,
            'chest': chest,
            'waist': waist,
            'hips': hips,
            'fabric': fabric,
            'dress_type': dress_type
        }

        input_df = pd.DataFrame([input_dict])
        input_df = pd.get_dummies(input_df)

        model_features = model.feature_names_in_
        for col in model_features:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[model_features]

        predicted_cost = model.predict(input_df)[0]

        # prompt = f"A beautiful elegant chubby {desc} {fabric} {dress_type} designed for women with chest {chest} centimeters, waist {waist} centimeters, hips {hips} centimeters, height {height} centimeters and wingspan {arm_length} centimeters that should be a professional lighting, front view "
        # image_url = generate_fal_image(prompt)

        image_url = settings.MEDIA_URL + f'template/{dress_type.lower().replace(" ", "_")}/{fabric.lower()}.png'


        return render(request, 'stitching_result.html', {
            'cost': round(predicted_cost, 2),
            'image_url': image_url
        })

    return render(request, 'measure.html')

def measure(request):
    return render(request, 'measure.html')

def result(request):
    return render(request, 'stitching_result.html')

def generate_fal_image(prompt):
    url = "https://fal.run/fal-ai/sana/sprint"
    headers = {
        "Authorization": "Key 19007d2d-1764-4884-8430-07f6f1dc83cf:135a9001927ba18d39813e23195b3466",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        data = response.json()
        print("Fal API Response:", data)

        image_url = data['images'][0]['url']
        return image_url

    except Exception as e:
        print("Error parsing response or extracting image:", e)
        return None

