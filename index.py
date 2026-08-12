import bottle
from bottle import route, run, template
import image


def call_service():
    directoryName = 'photos'
    image.process(directoryName)

# Process images once when application starts
print("Starting image processing...")
call_service()
print("Image processing completed.")

@route('/')
def index():
    """Home page"""
    title = "Image Processor App"
    return template(
        'index.tpl',
        data="Request completed!",
        title=title
    )

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000, debug=False, reloader=True)

app = bottle.default_app()
