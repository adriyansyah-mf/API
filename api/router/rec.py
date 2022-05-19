from fastapi import APIRouter
from services.data import Recons

router = APIRouter(prefix="/api")


@router.get("/whois/{domain}")
def is_whois(domain: str):
    t = Recons()
    return t.is_whois(domain)


@router.get("/recon/{ip}")
def is_shodan(ip: str):
    t = Recons()
    return t.is_shodan(ip)


@router.get("/rec/{domain}")
def is_search(domain: str):
    t = Recons()
    return t.search(domain)


@router.post("/organization/{org}")
def is_or(org: str):
    t = Recons()
    return t.orga(org)
