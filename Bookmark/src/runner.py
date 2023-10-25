import sys
sys.path.append("/home/dhruvish.p@ah.zymrinc.com/Documents/GitHub/Flask_project")  # Replace with the actual path to your project directory

from src import create_app

application = create_app()

if __name__ == '__main__':
    application.run()
