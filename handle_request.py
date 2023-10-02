import argparse

# Configura el análisis de argumentos
parser = argparse.ArgumentParser(description="Procesar solicitud")
parser.add_argument("--issue", type=int, required=True, help="Número de issue")
parser.add_argument("--github-username", required=True, help="Nombre de usuario de GitHub")

args = parser.parse_args()
