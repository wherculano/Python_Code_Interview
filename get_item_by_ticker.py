"""
Problem Description
You are given a REST API endpoint that returns a JSON array of company objects. 
Each object contains information such as rank, company name, market capitalization, ticker symbol, and sector.
Your task is to implement a function that:
Sends a GET request to the provided endpoint
Parses the JSON response
Searches for a company with a given ticker value
Returns the corresponding object if found
If no company with the specified ticker exists, the function should return None.
"""
import requests
from typing import Any, Dict, Optional


URL = "https://ddhost.in/sample-data/zeroda.json"


def get_company_by_ticker(ticker: str) -> Optional[Dict[str, Any]]:  # Tipagem clara
    response = requests.get(URL, timeout=5)  # Evita travamento de rede
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):  # Não quebra com JSON inválido
        raise ValueError("Unexpected response format: expected a list")

    return next(  # Para na primeira ocorrência
        (
            item
            for item in data
            if isinstance(item, dict) and item.get("ticker") == ticker  # Não assume chave existente
        ),
        None,
    )


if __name__ == "__main__":
    valid_ticker = "INFY"
    result = get_company_by_ticker(valid_ticker)
    print(result)
