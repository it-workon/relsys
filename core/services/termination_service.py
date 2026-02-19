from infra.termination_infra import save_termination_record


def register_termination(
    employee_name: str,
    ad_disabled: bool,
    email_disabled: bool,
    gi_disabled: bool,
    vbd_disabled: bool,
    teams_disabled: bool,
    forticlient_disabled: bool,
    papercut_disabled: bool,
    backup: str,
    authorization: str,
    termination_date: str,
    zeev: str,
    termination_term: str,
) -> str:
    values = [
        employee_name.upper(),
        "ok" if ad_disabled else "",
        "ok" if email_disabled else "",
        "ok" if gi_disabled else "",
        "ok" if vbd_disabled else "",
        "ok" if teams_disabled else "",
        "ok" if forticlient_disabled else "",
        "ok" if papercut_disabled else "",
        backup,
        authorization,
        termination_date,
        zeev,
        termination_term,
    ]

    return save_termination_record(values)
