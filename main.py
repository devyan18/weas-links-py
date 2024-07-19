from app import create_app

app = create_app()

# if __name__ == '__main__':

#     from waitress import serve

#     print('Server running on http://localhost:5000')
#     serve(app, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(debug=True)
