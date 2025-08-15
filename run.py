from bootstrap.app import create_app
# Rodar localmente fora do Docker | python run.py
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)