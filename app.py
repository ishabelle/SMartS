from smarts import create_app
from flask import Flask

app = create_app()

if __name__ == "__main__":
    app.debug = True
    PORT = process.env.PORT | '8080'
    app.run()
    app.run(
        host='localhost',
        port=PORT,
        debug=True,
    )


# if __name__ == "__main__":
#     app.debug = True
#     # PORT = process.env.PORT | '8080'
#     app.run()
#     app.run(
#         host='localhost',
#         # port=PORT,
#         port=5000,
#         debug=True
#     )