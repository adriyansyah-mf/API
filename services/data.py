
import whois
import shodan
from schemas.shodanschema import ShodansSchema
# import nmap


class Recons:
    api_key = shodan.Shodan("jetAKCLb0j0ptRLWxo6g58EPkknlxSwR")
    def is_whois(self,domain: str):
        """
        Whois lookup
        """
        return whois.whois(domain)

    def is_shodan(self,ip: str):
        return self.api_key.host(ip)

    def search(self, keyword: str) -> ShodansSchema:
        a = []
        try:
            results = self.api_key.search(keyword)
            count = results['total']
            for result in results['matches']:
                a.append(result)

            return ShodansSchema(
                total=count,
                data=a,
            )
        except shodan.APIError as e:
            return "Error"

    def orga(self, organ:str):
        try:
            results = self.api_key.org(organ)
            return results
        except shodan.APIError as e:
            return "Error"

    # def port(self, ip:str):
    #     try:
    #         results = self.api_key.host(ip)

