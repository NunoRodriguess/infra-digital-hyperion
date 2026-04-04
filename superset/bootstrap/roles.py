from superset.app import create_app

app = create_app()

with app.app_context():
    from superset.extensions import security_manager

    print("Applying Superset role permissions...")

    def grant(role_name):
        role = security_manager.find_role(role_name)

        if not role:
            print(f"{role_name} not found")
            return

        perms = [
            ("all_datasource_access", "all_datasource_access"),
            ("all_database_access", "all_database_access"),
        ]

        for perm, view in perms:
            pv = security_manager.find_permission_view_menu(perm, view)
            if pv:
                security_manager.add_permission_role(role, pv)
                print(f"Granted {perm} → {role_name}")
            else:
                print(f"{perm} missing")

    grant("Gamma")
    grant("Public")

    security_manager.get_session.commit()

    print("Permissions applied successfully")