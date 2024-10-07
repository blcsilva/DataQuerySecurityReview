import json
from google.cloud import bigquery
from google.cloud import compute_v1
from google.oauth2 import service_account

def load_credentials_from_file(credentials_file):
    # Carrega as credenciais a partir do arquivo JSON
    credentials = service_account.Credentials.from_service_account_file(credentials_file)
    return credentials

def main():
    # Caminho para o arquivo de credenciais JSON
    credentials_file = "google_service_account.json"    
    # Carregar credenciais
    credentials = load_credentials_from_file(credentials_file)

    # Usar as credenciais para criar um cliente BigQuery
    project_id = 'seu_project_id'
    client = bigquery.Client(credentials=credentials, project=project_id)
    
    # Exemplo: Listar datasets no BigQuery
    datasets = client.list_datasets()
    print("Datasets:")
    for dataset in datasets:
        print(dataset.dataset_id)

    # Usar as credenciais para criar um cliente Compute
    compute_client = compute_v1.InstancesClient(credentials=credentials)
    
    # Exemplo: Listar instâncias de Compute Engine
    zone = 'us-central1-a'  # Substitua pela sua zona
    project = 'seu_project_id'  # Substitua pelo seu ID de projeto
    instances = compute_client.list(project=project, zone=zone)
    print("Instances:")
    for instance in instances:
        print(instance.name)

if __name__ == "__main__":
    main()
