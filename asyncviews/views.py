import asyncio # importando asyncio para usar funções assíncronas
import httpx # importando httpx para fazer chamadas HTTP assíncronas
from django.http import HttpResponse # importando HttpResponse para retornar respostas HTTP

async def http_call_async(): # definindo uma função assíncrona para fazer chamadas HTTP
    for num in range(1, 8): # loop para imprimir números 
        await asyncio.sleep(1) # aguardando 1 segundo de forma assíncrona
        print(num) # imprimindo o número atual do loop
    async with httpx.AsyncClient() as client: # criando um cliente HTTP assíncrono usando httpx
        r = await client.get("https://httpbin.org") # fazendo uma chamada GET assíncrona para o site httpbin.org
        print(r) # imprimindo a resposta da chamada HTTP

async def async_view(request): # definindo uma view assíncrona para lidar com requisições HTTP
    loop = asyncio.get_event_loop() # obtendo o loop de eventos atual
    loop.create_task(http_call_async()) # criando uma tarefa assíncrona para executar a função http_call_async
    return HttpResponse("Non-blocking HTTP request") # retornando uma resposta HTTP imediatamente, sem bloquear a execução da função http_call_async