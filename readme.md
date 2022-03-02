# GENERETOR
um gerador de horários para as escolas

## 1 - Como rodar o projeto ? entre no terminal e siga o passo a passo abaixo:

#### 1.1 - Faça o clone do repositório:
``` git clone https://github.com/DgSantos017/generettor-scholl ``` <br />
ou <br />
``` git clone https://github.com/DgSantos017/generettor-scholl ``` 

#### 1.2 - entre no diretório do repositório clonado:
``` cd generettor-scholl ``` 

#### 1.3 - crie um ambiente virtual:
``` python -m venv venv``` 

#### 1.4 - ative ambiente virtual (você sempre vai trabalhar nesse ambiente):
``` source venv/bin/activate``` 

#### 1.5 - uma vez dentro do ambiente virtual, instale as dependências:
``` pip install -r requirements.txt```

#### 1.6 - com os 2 próximos comandos, rode as migrations (para criar as tabelas no banco de dados interno):
``` python manage.py makemigrations ``` <br /><br />
```  python manage.py migrate ```

#### 1.7 - por fim, inicie o servidor para rodar o projeto:
``` python manage.py runserver ```
##### 1.7.1 - se todos os passos foram bem executados, seu projeto vai rodar localmente no seguinte endereço:
http://localhost:8000/


# deseja consumir a API ? segue abaixo todos os endpoints:

## 2 - USUÁRIO

### 2.1 - Cadastrar

#### POST - ```https://dgeneretord.herokuapp.com/register/```
```json
// BODY REQUEST
{
   "username": "Drica",
   "password": "1234",
   "email": "d@gmail.com"
}  
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
   "id": 1,
   "username": "Drica",
   "email": "d@gmail.com",
   "is_superuser": true
}
```

### 2.2 - Login

#### POST - ```https://dgeneretord.herokuapp.com/login/```
```json
// BODY REQUEST
{
   "username": "Drica",
   "password": "1234"
}
    
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
   "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

## 3 - MATERIAS

### 3.1 - Cadastrar materias

#### POST - ```https://dgeneretord.herokuapp.com/materias/```
```json
// BODY REQUEST
{
   "name_materia": "Programacao"
}
    
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
   "id": 1,
   "name_materia": "Programacao",
   "qtd_aulas": 0,
   "professor": ""
}
```

### 3.2 - Complementar as informações da Materia

#### PUT - ```https://dgeneretord.herokuapp.com/materia/1/complement/```

```json
// BODY REQUEST
{
   "qtd_aulas": 8,
   "professor": "Drica"
}
    
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
   "id": 1,
   "name_materia": "Programacao",
   "qtd_aulas": 8,
   "professor": "Drica"
}
```

### 3.3 - Listar materias

#### GET - ```https://dgeneretord.herokuapp.com/materias/```

```json
// RESPONSE STATUS -> HTTP 200 OK
[
  {
    "id": 1,
    "name_materia": "Programacao",
    "qtd_aulas": 8,
    "professor": "Drica"
  },
  {
    "id": 2,
    "name_materia": "Fisica",
    "qtd_aulas": 0,
    "professor": ""
  },
  {
    "id": 3,
    "name_materia": "Astronomia",
    "qtd_aulas": 0,
    "professor": ""
  }
]
```

### 3.4 - Listar materia especifica por ID

#### GET - ```https://dgeneretord.herokuapp.com/materia/1```

```json
// RESPONSE STATUS -> HTTP 200 OK

{
  "id": 1,
  "name_materia": "Programacao",
  "qtd_aulas": 8,
  "professor": "Drica"
}
```

### 3.6 - Editar nome da materia

#### PUT - ```https://dgeneretord.herokuapp.com/materia/1```
```json
// BODY REQUEST
{
  "name_materia": "Desenvolvimento backEnd"
}
    
```

```json
// RESPONSE STATUS -> HTTP 200 OK

{
    "id": 1,
    "name_materia": "Desenvolvimento backEnd",
    "qtd_aulas": 8,
    "professor": "Drica"
  }
```

### 3.7 - Deletar materia

#### DELETE - ```https://dgeneretord.herokuapp.com/materia/2```

```json
// RESPONSE STATUS -> HTTP 204 NO CONTENT

```

## 4 - TURMAS

### 4.1 - Cadastrar turma

#### POST - ```https://dgeneretord.herokuapp.com/turmas/```
```json
// BODY REQUEST
{
   "name_turma": "Labenu",
   "turno": "Vespertino"
}
    
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
   "id": 1,
   "name_turma": "Labenu",
   "turno": "Vespertino",
   "materias": []
}
```


### 4.2 - adicionar materias na turma

#### PUT - ```https://dgeneretord.herokuapp.com/turma/1/materias/```

```json
// BODY REQUEST
{
   "id_materias": [1, 2, 3]
}
    
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
   "id": 1,
   "name_turma": "Labenu",
   "turno": "Vespertino",
   "materias": [
	   {
	      "id": 1,
	      "name_materia": "Programacao",
        "qtd_aulas": 8,
        "professor": "Drica"
	   },
	   {
	     "id": 2,
	     "name_materia": "Fisica",
		   "qtd_aulas": 0,
		 "  professor": ""
	   },
	   {
	     "id": 3,
	     "name_materia": "Astronomia",
		   "qtd_aulas": 0,
		   "professor": ""
	   }
   ]
}
```

### 4.3 - Listar turmas

#### GET - ```https://dgeneretord.herokuapp.com/turmas/```


```json
// RESPONSE STATUS -> HTTP 200 OK
[
  {
   "id": 1,
   "name_turma": "Labenu",
   "turno": "Vespertino",
   "materias": [
	   {
	     "id": 1,
	     "name_materia": "Programacao",
		   "qtd_aulas": 8,
		   "professor": "Drica"
	   },
	   {
	     "id": 2,
	     "name_materia": "Fisica",
		   "qtd_aulas": 0,
		   "professor": ""
	   },
	   {
	     "id": 3,
	     "name_materia": "Astronomia",
		   "qtd_aulas": 0,
		   "professor": ""
	   }
   ]
  },
  {
   "id": 2,
   "name_turma": "Kenzie",
   "turno": "Matutino",
   "materias": []
  },
  {
   "id": 3,
   "name_turma": "Trybe",
   "turno": "Noturno",
   "materias": []
  }
]
```

### 4.4 - Listar turma especifica por ID

#### GET - ```https://dgeneretord.herokuapp.com/turma/1```


```json
// RESPONSE STATUS -> HTTP 200 OK
{
   "id": 1,
   "name_turma": "Labenu",
   "turno": "Vespertino",
   "materias": [
	   {
	     "id": 1,
	     "name_materia": "Programacao",
		   "qtd_aulas": 8,
		   "professor": "Drica"
	   },
	   {
	     "id": 2,
	     "name_materia": "Fisica",
		   "qtd_aulas": 0,
		   "professor": ""
	   },
	   {
	     "id": 3,
	     "name_materia": "Astronomia",
		   "qtd_aulas": 0,
		   "professor": ""
	   }
```

### 4.5 - Editar nome da turma

#### PUT - ```https://dgeneretord.herokuapp.com/turma/2```
```json
// BODY REQUEST
{
  "name_turma": "Kenzie Academy"
}
    
```

```json
// RESPONSE STATUS -> HTTP 200 OK

{
   "id": 2,
   "name_turma": "Kenzie Academy",
   "turno": "Matutino",
   "materias": []
  }
```

### 4.6 - Deletar turma


#### DELETE - ```https://dgeneretord.herokuapp.com/turma/2```

```json
// RESPONSE STATUS -> HTTP 204 NO CONTENT

```

## 5 - EXCEÇÕES

### 5.1 - Recursos especificos que pedem ID (Ex: foi solicitado um curso que não existe)
```json
// RESPONSE STATUS -> HTTP 404 Not Found
{
   "error": "course does not exist"
}
```
### 5.2 - Cadastrar um recurso que já existe (Ex: tentativa de cadastrar usuário já cadastrado)
```json
// RESPONSE STATUS -> HTTP 409 - Conflict
{
    "error": "user already exists"
}
```

### 5.3 - Autorização, baseado no tipo de usuário 

#### 5.3.1 - Realizar login em uma conta ainda não criada
```json
// RESPONSE STATUS -> HTTP 401 - Unauthorized
{
    "error": "Incorrect login or password"
}
```
#### 5.3.2  - Token inexistente
```json
// RESPONSE STATUS -> HTTP 401 - Unauthorized
{
  "detail": "Authentication credentials were not provided."
}
```

#### 5.3.3  - Token inválido
```json
// RESPONSE STATUS -> HTTP 401 - Unauthorized
{
    "detail": "Invalid token."
}
```
#### 5.3.4 - Token válido, porém não atende os requisitos mínimos de permissão(ex: aluno tentando criar curso)
```json
// RESPONSE STATUS -> HTTP 403
{
    "detail": "You do not have permission to perform this action."
}
```

### 5.4 - Formato de requisição incorreta (ex: ao tentar realizar o login, o usuário não informou o username)
```json
// RESPONSE STATUS -> HTTP 400 - Bad Request
{
    "error": "is missing 'username'"
}
```

### 5.5 - a atividade que algum aluno tenha feito uma submissão não pode sofrer alteração no nome ou na pontuação
```json
// RESPONSE STATUS -> HTTP 400 Bad Request
{
   "error": "You can not change an Activity with submissions"
}
```



