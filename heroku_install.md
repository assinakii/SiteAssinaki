# Criar a conta no heroku

Antes de começar execute o comando abaixo
```sh
pip install -r requeriments.txt
```

Agora você precisa ter acesso ao e-mail e seguir os passoa abaixo.

* login: assinaki@hotmail.com
* senha: [ver no rascunho do e-mail](https://outlook.live.com/mail/compose/AQMkADAwATY0MDABLWZiNTQtODdkNS0wMAItMDAKAEYAAANggYPBfJK2SIkCcBRhb8fiBwAfPRAIKmGyT44q9cSc8%2BIfAAACAQ8AAAAfPRAIKmGyT44q9cSc8%2BIfAAABWHIhAAAA)

* requisitos:

    * git

    * python3
    * [windows 64: instalar o cli](https://cli-assets.heroku.com/heroku-x64.exe)
    * [windows 32: instalar o cli](https://cli-assets.heroku.com/heroku-x86.exe)
    
Depois de instalar, digite no terminal da app, na ide, o comando do heroku:

```sh
    heroku login
    heroku: Press any key to open up the browser to login or q to exit:
```

ou

```sh
    heroku login --interactive
    Enter your Heroku credentials.
    Email: assinaki@hotmail.com
    Password: 
```

Para obter mais informações acesse o [devcenter](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

***
Execute com o comando abaixo para prepara o servdidor para receber a app

```sh
heroku create
```
Para fazer o ```deploy``` digite no terminal:
```sh
git push heroku master
```

