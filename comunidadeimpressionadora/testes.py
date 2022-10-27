# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username='Andriel', email='and.alex@gmail.com', senha='123456')
#     usuario2 = Usuario(username='Alexandre', email='alex.and@gmail.com', senha='1234567')
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     database.session.commit()
# with app.app_context():
#     # meus_usuarios = Usuario.query.all()
#     # print(meus_usuarios[0].username)
#     usuario_teste = Usuario.query.filter_by(id=1).all()
#     print(usuario_teste)
#     print(usuario_teste[0].username)

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Meu primeiro post', corpo='Criando meu primeiro post no meu blog.')
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.all()
#     print(post[0].corpo)
#     print(post[0].autor.username)

# with app.app_context():
#     database.drop_all()
#     database.create_all()