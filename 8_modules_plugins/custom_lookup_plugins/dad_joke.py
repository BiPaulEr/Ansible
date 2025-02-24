import requests
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        headers = {"Accept": "application/json"}
        response = requests.get("https://icanhazdadjoke.com/", headers=headers)

        if response.status_code != 200:
            return ["❌ Impossible de récupérer une blague"]

        joke = response.json().get("joke", "Aucune blague trouvée")
        return [joke]

