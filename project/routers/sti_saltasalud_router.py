class sti_SaltaSaludRouter:
    # Aplicaciones predeterminadas de django que deben estar si o si en la misma Base de Datos,
    # ya que no se permiten relaciones de Modelos que esten en diferentes Base de Datos
    router_app_labels_stiss= {'auth', 'contenttypes', 'sessions', 'admin'}

#Me dice si el modelo pertenece a la app que estoy intentando validar, me vaya a la base de datos
#donde tiene que estar si o si, esta es para leer
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels_stiss:
            return 'sti_saltasalud_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels_stiss:
            return 'sti_saltasalud_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.router_app_labels_stiss or
                obj2._meta.app_label in self.router_app_labels_stiss
        ):
            return True
        return None

    #Este metodo es para saber si se permiten migraciones y hacia donde tiene que ir
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels_stiss:
            return db == 'sti_saltasalud_db'
        return None

