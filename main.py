#file that runs the Application

#import
from website import create_app

#clases
app = create_app()

#only if main.py it's running. The application will run.
if __name__ == '__main__':
    app.run(debug=True)


