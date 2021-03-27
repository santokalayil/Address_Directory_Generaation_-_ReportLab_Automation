def run_updates():
    import os
    from database.post import post_query
    update = lambda q: post_query(q, os.path.join("database", "sqlite.db"))  # update function

    # famid 85 member_Name 'Leela Raju' - dob year is wrong
    dob, dom = '07/05/1963', '07/05/1984'
    update(f'''UPDATE members SET dob = "{dob}" WHERE famid=85 AND member_name="Leela Raju";''')
    update(f'''UPDATE members SET dom = "{dom}" WHERE famid=85 AND member_name="Leela Raju";''')

    # changing dr. john's native home address
    native_house_name = "Kshemalayam, NIRA-153"
    update(f'''UPDATE nat_addr SET house_name = "{native_house_name}"
    WHERE famid=(select famid from families where email = "joseabrahamtvm@gmail.com");''')

    print('All edits completed!')
    return 0