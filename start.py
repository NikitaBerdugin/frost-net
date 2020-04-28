def start():
    return '''<!doctype html>
                    <html lang="en">
                        <head>
                            <!-- Required meta tags -->
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <!-- Bootstrap CSS -->
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

                            <title>frost</title>
                        </head>
                        <body>
                            <h1 class='text-center'> Добро пожаловать </h1>
                            <h2 class='text-center'> В социальную сеть frost-net </h2>
                            <h2 class='text-center'> Введите почту и пароль для входа </h2>
                        <div class="container">
                        <div class="row">
                            <div class="col-sm">
                                <form>
                                <div class="form-group">
                                    <label for="exampleInputEmail1">адрес электронной почты</label>
                                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                                    <small id="emailHelp" class="form-text text-muted">Мы никогда не передадим вашу электронную почту кому-либо еще.</small>
                                </div>
                                <div class="form-group">
                                    <label for="exampleInputPassword1">пароль</label>
                                    <input type="password" class="form-control" id="exampleInputPassword1">
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="exampleCheck1">
                                     <label class="form-check-label" for="exampleCheck1">запомнить меня</label>
                                </div>
                                <a href="http://127.0.0.1:8080/im" type="submit" class="btn btn-primary">войти</a>
                                <a href="http://127.0.0.1:8080/regist" type="submit" class="btn btn-primary">регистрация</a>
                                </form>
                            </div>
                        </div>
                        </div>

                        </body>
                    </html>'''