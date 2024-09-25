import boto3

def lambda_handler(event: any, context: any):
    # Obtém parâmetros do request
    user: str = event["user"]
    operacao: str = event["operacao"]

    # Instancia o client do DynamoDB
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("contador_acesso")
    message: str = ""

    if operacao == "ver_contagem":
        contador: int = 0

        # Obtém o contador de acesso para o usuário informado
        response = table.get_item(Key={"user": user})
        if "Item" in response:
            contador = response["Item"]["contador"]

        # Incrementa o contador e atualiza a tabela do DynamoDB.
        contador += 1
        table.put_item(Item={"user": user, "contador": contador})

        message += f"Olá {user}! Você acessou o sistema {contador} vezes."
    elif operacao == "remover_usuario":
        table.delete_item(Key={"user": user})
        message += f"O usuário {user} foi removido do sistema!"
    elif operacao == "listar_usuarios":
        response = table.scan()
        for user in response["Items"]:
            message += f"(Nome: {user["user"]}, Acessos: {user["contador"]}){' ' if response['Count'] > 1 else ''}"
        
    else:
        message += "Operação inválida!"
    return {"message": message}

#teste1 = {"user": "Tarcisio", "operacao": "ver_contagem"}
#teste2 = {"user": "Rabbit", "operacao": "ver_contagem"}
#teste3 = {"user": "", "operacao": "listar_usuarios"}
#teste4 = {"user": "Rabbit", "operacao": "remover_usuario"}