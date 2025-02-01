from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from transformers import AutoModelForCausalLM, AutoTokenizer  
import ollama


# Create your views here.

def focusApp(request):
    main_page = loader.get_template('main.html')
    return HttpResponse(main_page.render())

def loginPage(request):
    loginPage = loader.get_template('login.html')
    return HttpResponse(loginPage.render())



def dashboardPage(request):
    dashboardPage = loader.get_template('dashboard.html')
    return HttpResponse(dashboardPage.render())

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process_task(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            task = data.get("task", "")
            task_date = data.get("date", "")

            if not task or not task_date:
                return JsonResponse({"message": "Please provide both task and date."}, status=400)

            # Print received task and date in the terminal
            print(f"✅ Received Task: {task}, Date: {task_date}")

            # Return a response message to the frontend
            print("before ai response")
            prompt = f"""
            The user has a task: "{task}" scheduled on {task_date}.
            Generate a list of subtasks that need to be completed before the main task. 
            Each subtask should have:
            - A name
            - The estimated time it takes to complete (in hours or days)
            - The suggested date on which it should be completed

            Return the output as a valid JSON object in the following format:
            {{
                "subtasks": [
                    {{"name": "Subtask 1", "duration": "2 hours", "date": "YYYY-MM-DD"}},
                    {{"name": "Subtask 2", "duration": "1 day", "date": "YYYY-MM-DD"}}
                ]
            }}

            Ensure the output is only valid JSON without extra text.
            """

            response = ollama.generate(model="deepseek-r1:1.5b",prompt=prompt)
            print('after')
            ai_response = json.loads(response['response'])
            print(ai_response)

            return JsonResponse({"message": "Thank you! Your task has been submitted successfully.",
                                 "subtasks": ai_response['subtasks']})

        except Exception as e:
            print(f"❌ Error processing request: {e}")
            return JsonResponse({"message": "An error occurred while processing your task."}, status=500)

    return JsonResponse({"message": "Invalid request method."}, status=405)
