from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

def get_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='chinook',
            user='root',
            password='1234'
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record}")

            # Perform a database operation
            cursor.execute("SELECT * FROM album;")
            result = cursor.fetchall()

            for row in result:
                print(row)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")