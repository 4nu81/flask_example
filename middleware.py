class middleware():
    """
    Simple Middleware example
    """

    def __init__(self, app):
        self.app = app
        
    def __call__(self, environ, start_response):
        print(f"middleware has been called.")
        return self.app(environ, start_response)
