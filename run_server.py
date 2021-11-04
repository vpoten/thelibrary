import src

"""
Run server, useful for debug
"""
if __name__ == '__main__':
    app = src.create_app()
    app.run(port='5000', debug=True)
