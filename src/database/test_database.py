import os
import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import database as db

def generate_database():
    # si la base de données exite on supprimer
    if db.database != None:
        db.database.close()
    os.remove('database.db') if os.path.exists('database.db') else None

    # on crée la base de données
    db.GenerateDatabase()

    # si la base de données exite
    assert os.path.exists('database.db') == True
    return


def test_user_insert():
    generate_database()

    user = db.UserType(
        None,
        "test", 
        db.Chiffrement("test")
    )

    # Insertion d'un utilisateur
    user = db.UserTable.Insert(user)

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectBy_ID(user)) > 0
    return

def test_user_update():
    generate_database()

    user = db.UserType(
        None,
        "test", 
        db.Chiffrement("test")
    )

    # Insertion d'un utilisateur
    user = db.UserTable.Insert(user)

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectBy_ID(user)) > 0

    # on met à jour le mot de passe
    user.password = db.Chiffrement("test2")
    db.UserTable.Update(user)

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectBy_ID(user)) > 0

    # on vérifie que le mot de passe a bien été mis à jour
    assert db.Compare("test2", user.password)
    return

def test_user_delete():
    generate_database()

    user = db.UserType(
        None,
        "test", 
        db.Chiffrement("test")
    )

    # Insertion d'un utilisateur
    user = db.UserTable.Insert(user)

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectBy_ID(user)) > 0

    # on supprime l'utilisateur
    db.UserTable.Delete(user)

    # on vérifie que l'utilisateur n'existe plus
    assert len(db.UserTable.SelectBy_ID(user)) == 0
    return

def test_user_select():
    generate_database()

    user = db.UserType(
        None,
        "test", 
        db.Chiffrement("test")
    )

    # Insertion d'un utilisateur
    user = db.UserTable.Insert(user)

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectBy_ID(user)) > 0

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectBy_Username(user)) > 0

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectAll()) > 0
    return



def test_token():
    generate_database()

    # Insertion d'un utilisateur
    user = db.UserType(
        None,
        "test", 
        db.Chiffrement("test")
    )
    user = db.UserTable.Insert(user)

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectBy_ID(user)) > 0

    # on génère un token
    newToken: db.TokenType = db.TokenType(
        None,
        user.id,
        db.GenerateToken(user.id),
        db.GenerateToken(user.id),
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    newToken = db.TokenTable.Insert(newToken)

    # on vérifie que le token existe
    assert len(db.TokenTable.SelectBy_ID(newToken)) > 0

    # on vérifie que le token existe
    assert len(db.TokenTable.SelectBy_UserID(newToken)) > 0

    # on vérifie que le token existe
    assert len(db.TokenTable.SelectAll()) > 0

    # on supprime le token
    db.TokenTable.Delete(newToken)

    # on vérifie que le token n'existe plus
    assert len(db.TokenTable.SelectBy_AccessToken(newToken)) == 0
    return



def test_measure():
    generate_database()

    # Insertion d'un utilisateur
    user = db.UserType(
        None,
        "test", 
        db.Chiffrement("test")
    )
    user = db.UserTable.Insert(user)

    # on vérifie que l'utilisateur existe
    assert len(db.UserTable.SelectBy_ID(user)) > 0

    # on créé un composant
    component = db.ComponentType(
        None,
        user.id,
        "testComponent"
    )
    component = db.ComponentTable.Insert(component)

    # on vérifie que le composant existe
    assert len(db.ComponentTable.SelectBy_ID(component)) > 0

    # On créé une unité
    unit = db.UniteType(
        None,
        component.id,
        "testUnit"
    )
    unit = db.UniteTable.Insert(unit)

    # on vérifie que l'unité existe
    assert len(db.UniteTable.SelectBy_ID(unit)) > 0

    # on créé une mesure
    measure = db.MeasureType(
        None,
        unit.id,
        1,
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    measure = db.MeasureTable.Insert(measure)

    # on vérifie que la mesure existe
    assert len(db.MeasureTable.SelectBy_ID(measure)) > 0

    # on créé une seconde mesure 1 jours plus tard
    measure2 = db.MeasureType(
        None,
        unit.id,
        5,
        (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    )
    measure2 = db.MeasureTable.Insert(measure2)

    # on vérifie que la mesure existe
    assert len(db.MeasureTable.SelectBy_ID(measure2)) > 0

    # On recupere les mesures sur une plage de temps
    assert len(db.MeasureTable.SelectBy_DateRange(
        (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
        (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    )) == 2

    # On recupere les mesures sur une plage de temps
    assert len(db.MeasureTable.SelectBy_DateRange(
        (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
        (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
    )) == 1

    # suppression des mesures
    db.MeasureTable.Delete(measure)
    assert len(db.MeasureTable.SelectBy_ID(measure)) == 0
    
    # suppression des mesures
    db.MeasureTable.Delete(measure2)
    assert len(db.MeasureTable.SelectBy_ID(measure2)) == 0

    # suppression des unités
    db.UniteTable.Delete(unit)

    # suppression des composants
    db.ComponentTable.Delete(component)

    # suppression des utilisateurs
    db.UserTable.Delete(user)

    return








test_user_insert()
test_user_update()
test_user_delete()
test_user_select()
test_token()
test_measure()