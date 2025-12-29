from pathlib import Path

CORE_DIR = Path(__file__).resolve().parent
BASE_DIR = CORE_DIR.parent.parent

TEMPLATES_DIR = BASE_DIR / "templates" / "welcome-model.docx"
OUTPUT_DIR = BASE_DIR / "output"

data = {
    "{{USER_NAME}}": "{NAME}",
    "{{DOMAIN_ORG}}": "workongroup.com.br",
    "{{USER_PASSWD}}": "{PASSWD}",
    "{{EMAIL_PASSWD}}": "{PASSWD}",
    "{{GI_PASSWD}}": "1234",
    "{{TEAMS_PASSWD}}": "{PASSWD}",
    "{{VBD_PASSWD}}": "{PASSWD}",
    "{{FORTICLIENT_PASSWD}}": "workon2025",
    "{{PROCESS_NUMBER}}": "{PROCESS}",
    "{{ASSET}}": "XXX-000000",
}
