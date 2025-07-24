'''
Esse módulo tem como objetivo simular um servidor web http

O servidor web HTTP basicamente possibilita que duas máquinas 
consigam se comunicar, você tem uma máquina cliente e a máquina 
servidor. O cliente vai requisitar algo para a máquina servidora 
e essa requisição geralmente ela é delineada usando métodos 
HTTP: os principais são o GET, POST, PUT e o DELETE. Cada um 
desses métodos tem um objetivo específico

GET -> é utilizado para consultar informações em um servidor
POST -> para incluir informações
PUT -> para atualizar informações
DELETE -> para excluir informações

Por sua vez, o servidor vai devolver uma resposta para o 
cliente, essa resposta vem em forma de status code. Você tem 
códigos que podem ir da família 100 até a família 500. Exemplo 
200 -> sucesso, 400 -> houve erro no lado do cliente.

================================================================
TESTE

Se as máquinas (física e virtual) estiverem na mesma rede, você 
pode simular uma comunicação entre o servidor web HTTP, em que 
um servidor vai ser sua máquina física e o cliente vai ser a 
máquina virtual

** Coloque a placa em modo bridge no Virtual Box **

O cliente não necessariamente precisa ser uma VM, pode ser um 
celular, outro PC.

1. Saiba o endereço IP da sua máquina física (não é o 
'localhost'). Para saber use o comando:
$ ifconfig # No Windows é 'ipconfig'. 'ip s' também funciona

2. No terminal (da máquina física) digite:
$ python -m http.server

O servidor web vai ser iniciado no diretório que você tá!

3. Abra o endereço gerado, exemplo: 'ip_da_sua_maquina:8000', na 
VM. Também dá pra abrir no navegador da máquina física.

4. Na VM é possível acessar os arquivos do diretório da máquina 
física, onde foi iniciado o servidor HTTP.

'''