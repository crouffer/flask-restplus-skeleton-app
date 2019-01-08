from application.database.i_application_dal import IApplicationDal


class ApplicationDal(IApplicationDal):

    @classmethod
    def __init__(cls, db=None, logger=None):
        if not db:
            from application.common.application_ioc import ApplicationIOC as ri
            cls.db = ri.get_db()
        else:
            cls.db = db

        if not logger:
            cls.logger = ri.get_logger()
        else:
            cls.logger = logger

    @classmethod
    def add_row(cls, value):
        from .models import ExampleDatabaseModel
        r = ExampleDatabaseModel()
        r.string_column = value
        cls.db.session.add(r)
        cls.db.session.commit()

        return r

    @classmethod
    def delete_row(cls, row_id):
        from .models import ExampleDatabaseModel
        r = cls.db.session.query(ExampleDatabaseModel) \
            .filter(ExampleDatabaseModel.id == row_id).one()
        cls.db.session.delete(r)
        cls.db.session.commit()

    @classmethod
    def get_row(cls, value):
        from .models import ExampleDatabaseModel
        query = cls.db.session.query(ExampleDatabaseModel) \
            .filter(ExampleDatabaseModel.string_column == value)

        return query.all()

    @classmethod
    def get_row_list(cls, offset=None, limit=None):
        from .models import ExampleDatabaseModel
        query = cls.db.session.query(ExampleDatabaseModel)

        if offset:
            query = query.offset(offset)

        if limit:
            query = query.limit(limit)

        return query.all()
