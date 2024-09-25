# Laboratório CN - DynamoDB
## Apresentação
Neste lab, nós iremos criar uma tabela simples para computar a quantidade de acessos de um dado usuário dentro de um sistema fictício.

## Passo a passo
1. A partir da **página inicial do console**, digite na barra de pesquisa **DynamoDB** e acesse o serviço:
    ![](/Imagens/1.png)
2. Clique em **Criar tabela**:
    ![](/Imagens/2.png)
3. Coloque exatamente as informações mostradas no print e crie a tabela:
    > **Nome da tabela:** contador_acesso

    > **Chave de partição:** user

    > **Configurações da tabela:** configurações padrão

    ![](/Imagens/3.png)
4. Após criar a tabela no DynamoDB, será necessário alterar as configurações no IAM. Sendo assim, digite **IAM** na barra de pesquise e acesse o serviço:
    ![](/Imagens/4.png)
5. No menu lateral, clique em **Políticas** e depois clique no botão **Criar política**:
    ![](/Imagens/5.png)
6. Pesquise pelo **DynamoDB** e o selecione:
    ![](/Imagens/6.png)
7. Marque as opções apresentadas no print e depois clique em **Próximo**:
    > **Ações manuais:** Todas as ações do DynamoDB (dynamodb:*)

    > **Effect:** Permitir

    > **Recursos:** Tudo

    ![](/Imagens/7.png)
8. Informe algum nome para a política e aperte em **Criar política**:
    ![](/Imagens/8.png)
9. Agora é hora de preparar o ambiente de execução no Lambda. Portanto, pesquise por ele na barra de pesquise e acesse o serviço:
    ![](/Imagens/9.png)
10. Clique em **Criar função**:
    ![](/Imagens/10.png)
11. Preencha os campos referente à criação da função de acordo com o print abaixo:
    > **Nome da função:** LabDynamoDB

    > **Tempo de execução:** Python 3.12

    > **Arquitetura:** x86_64
    
    > **Papel de execução:** Usar uma função existente
    
    > **Função existente:** LabRole

    ![](/Imagens/11.png)
12. Cole o código do arquivo **lambda_function.py** deste repositório, clique em **Deploy** para salvar o código e depois clique em **Test**:
    ![](/Imagens/12.png)
13. Informe o nome da função e cole o JSON referente ao teste 1 no campo do **Json do evento** e clique em **Salvar**:

    ```
    {"user": "Tarcisio", "operacao": "ver_contagem"} 
    ```
    ![](/Imagens/13.png)

14. Clique em **Test** e observe o resultado gerado:
    ![](/Imagens/14.png)
15. Acesse a tabela criada no painel do DynamoDB e clique em **Explorar itens da tabela** para visualizar o resultado da operação direto no database:
    ![](/Imagens/16.png)
16. Realize outras operações utilizandos os JSONs abaixo para criar outro usuário, visualizar os usuários e remover um usuário:
    ```
    {"user": "Tarcisio", "operacao": "ver_contagem"}
    {"user": "Rabbit", "operacao": "ver_contagem"}
    {"user": "", "operacao": "listar_usuarios"}
    {"user": "Rabbit", "operacao": "remover_usuario"}
    ```