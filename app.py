from sharpy import create_app

app = create_app()

if __name__ == '__main__':
    print("App is running in local dev web-server mode!")
    app.run()
