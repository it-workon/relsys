from infra.plan_infra import save_machine_plan


def register_machine_plan(
    computer_name: str,
    username: str,
    employee_name: str,
    department: str,
    asset_tag: str,
    leasing_company: str,
    model: str,
    office_version: str,
) -> str:
    values = [
        computer_name.upper(),
        username,
        employee_name,
        department,
        asset_tag,
        leasing_company,
        model,
        office_version,
    ]

    return save_machine_plan(values)
