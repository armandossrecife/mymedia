import os

# Todo: checar os diretorios img, uploads e thumbnails
class Constant:
    PATH_MYADMIN = os.path.abspath(os.getcwd())
    PATH_MYAPP = PATH_MYADMIN + '/app'
    PATH_STATIC = PATH_MYADMIN + '/app/static'
    PATH_IMG = PATH_MYADMIN + '/app/static/img'
    PATH_UPLOADS = PATH_MYADMIN + '/app/static/uploads'
    PATH_UPLOADS_THUMBNAILS = PATH_MYADMIN + '/app/static/uploads/thumbnails'