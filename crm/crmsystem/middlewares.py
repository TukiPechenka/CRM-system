from django.contrib.auth.decorators import login_required


class LoginRequiredMiddleware:
    """
    Миддлвэйр запроса логина на всех страницах приложения
    (Кроме Административного интерфейса и страницы логирования)
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Функция запроса на всех представлениях логина
        """

        if (
            request.path.startswith("/admin")
            or request.user.is_authenticated
            or view_func.view_class.__name__ == "LoginView"
        ):
            return view_func(request, *view_args, **view_kwargs)

        return login_required(view_func)(request, *view_args, **view_kwargs)
