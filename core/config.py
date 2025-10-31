from pathlib import Path

SAVE_DIRECTORY = Path("output")
TEMPLATE_PATH = Path("templates/welcome-model.docx")

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
    "{{ASSET}}": "EMC-118450",
}
