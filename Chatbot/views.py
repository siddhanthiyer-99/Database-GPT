import openai
import os
import supabase
import pandas as pd
import psycopg2

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from .models import chatlog
from FourthSquare.settings import DATABASE_URI, DATABASE_NAME, DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_PORT
database_uri = DATABASE_URI

db = SQLDatabase.from_uri(database_uri)

llm = ChatOpenAI(temperature=0,model="gpt-3.5-turbo-1106")

conn = psycopg2.connect(database=DATABASE_NAME,
                            user=DATABASE_USER,
                            password=DATABASE_PASS,
                            host=DATABASE_HOST,
                            port=DATABASE_PORT)

# print("connection successful")
def get_query(prompt):
    query_chain = create_sql_query_chain(llm,db,k=10)
    assistant_response = {'SQL Query':query_chain.invoke({'question':prompt})}
    chatbot_response = assistant_response['SQL Query']
    return chatbot_response

def get_query_result(prompt):
    query = get_query(prompt)

    exec_sql = conn.cursor()

    exec_sql.execute(query)
    records = exec_sql.fetchall()
    exec_sql.close()
    return(records)

def interpret(prompt):
    full_chain = SQLDatabaseChain.from_llm(llm, db, verbose=False, use_query_checker=True, return_intermediate_steps=True)
    assistant_response = full_chain(prompt)
    return assistant_response['result']


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('signed')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            csrf_token = request.COOKIES.get('csrftoken')
            # return redirect(f'http://localhost:8501/?csrf_token={csrf_token}')
            return redirect('signed')
        else:
            messages.success(request, ('There was an error, try again!'))
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})
    
def home_page(request):
    return render(request, 'home.html', {})

def signup_user(request):
    return render(request, 'signup.html', {})

def signed(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    else:
        if request.user.is_authenticated:
            is_superuser = request.user.is_superuser
            group_name = request.user.groups.filter(name='admins').exists()
            return render(request, 'signedin.html', {'is_superuser': is_superuser, 'group_name': group_name})
        else:
            return redirect('login')
        
def databasegpt(request):
    # request.session.create()
    # username = 'admin'
    # session_id = request.session.session_key
    # print("Session ID:", session_id)
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method=="POST":
            request.session.create()
            session_id = request.session.session_key
            username = request.user.username

            user_prompt= request.POST.get('prompt')
            selected_mode = request.POST.get('mode')
            
            print(selected_mode)
            
            chatbot_response = interpret(user_prompt)
            
            if selected_mode == 'get-query':
                chatbot_response = get_query(user_prompt)

            elif selected_mode == 'get-query-execute':
                chatbot_response = get_query_result(user_prompt)
            
            elif selected_mode == 'interpret':
                chatbot_response = interpret(user_prompt)
            # responses.append('BOT: ' + chatbot_response)

            response_data = {
                'user': user_prompt,
                'bot': chatbot_response
            }
            
            # store_data(session_id, username, user_prompt, selected_mode, chatbot_response)
            new_chatlog = chatlog(session_id=session_id, username=username, prompt=user_prompt, mode=selected_mode, response=chatbot_response)
            new_chatlog.save()

            print(chatbot_response)
            # print(repr(chatbot_response))
            
            return JsonResponse(response_data)
    return render(request, 'databasegpt.html')