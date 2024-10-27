import urllib3
from locust import HttpUser,TaskSet, task, between
import random

#Desactivar advertencias SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class LoadTestUser(HttpUser):
    wait_time= between(1,2)
    host="https://pokeapi.co/api/v2"

    @task
    def Get_pokemons(self):
        name="Get_pokemons"
        response = self.client.get("/pokemon",verify=False)
        
        if response.status_code== 200:
            print(name)
            print("Get request successful")
            print(f"Tiempo de respuesta: {response.elapsed.total_seconds()*1000}ms")
            print("-------------------------------------------------------------------")
        else:
            print(f"Get request failed with status {response.status_code}")


    @task
    def Get_ability(self):
        name="Get_ability"
        response = self.client.get("/ability",verify=False)
        
        if response.status_code== 200:
            print(name)
            print("Get request successful")
            print(f"Tiempo de respuesta: {response.elapsed.total_seconds()*1000}ms")
            print("-------------------------------------------------------------------")
        else:
            print(f"Get request failed with status {response.status_code}")   


    @task
    def Get_berry(self):
        name="Get_berry"
        response = self.client.get("/berry",verify=False)
        
        if response.status_code== 200:
            print(name)
            print("Get request successful")
            print(f"Tiempo de respuesta: {response.elapsed.total_seconds()*1000}ms")
            print("-------------------------------------------------------------------")
        else:
            print(f"Get request failed with status {response.status_code}")   

        