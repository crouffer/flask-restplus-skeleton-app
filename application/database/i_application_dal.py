class IApplicationDal:
    @classmethod
    def add_row(cls, value):
        raise NotImplementedError()

    @classmethod
    def delete_row(cls, row_id):
        raise NotImplementedError()

    @classmethod
    def get_row(cls, value):
        raise NotImplementedError()

    @classmethod
    def get_row_list(cls, offset, limit):
        raise NotImplementedError()
