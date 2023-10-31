from .. import Session

import time
from builtins import str
import sqlalchemy

class CRUDMixin:
    """
    Convenience functions for CRUD operations.

    Adapted from `flask-kit <https://github.com/semirook/flask-kit/blob/master/base/models.py>`_.
    """

    __table_args__ = {'extend_existing': True}

    @classmethod
    def find(cls, **kwargs):
        """
        Find an object in the database with certain properties.

        :param kwargs: the values of the object to find
        :type kwargs: dict
        :returns: the object that was found, or else None
        """
        return Session.query(cls).filter_by(**kwargs).first()

    @classmethod
    def query(cls, **kwargs):
        """
        Find an object in the database with certain properties.

        :param kwargs: the values of the object to find
        :type kwargs: dict
        :returns: the object that was found, or else None
        """
        return Session.query(cls).filter_by(**kwargs)

    @classmethod
    def find_or_create(cls, _commit=True, **kwargs):
        """
        Find an object or, if it does not exist, create it.

        :param kwargs: the values of the object to find or create
        :type kwargs: dict
        :returns: the object that was created
        """

        obj = cls.find(**kwargs)
        if not obj:
            obj = cls.create(_commit=_commit, **kwargs)
        return obj

    @classmethod
    def get_by_id(cls, id):
        """
        Retrieve an object of this class from the database.

        :param id: the id of the object to be retrieved
        :type id: integer
        :returns: the object that was retrieved
        """

        if any(
            (isinstance(id, str) and id.isdigit(),
             isinstance(id, (int, float))),
        ):
            return Session.query(cls).get(int(id))
        return None

    @classmethod
    def create(cls, _commit=True, **kwargs):
        """
        Create a new object.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :param kwargs: parameters corresponding to the new values
        :type kwargs: dict
        :returns: the object that was created
        """

        instance = cls(**kwargs)
        obj = instance.save(_commit)
        return obj

    def update(self, _commit=True, **kwargs):
        """
        Update this object with new values.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :param kwargs: parameters corresponding to the new values
        :type kwargs: dict
        :returns: the object that was updated
        """

        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return _commit and self.save() or self

    def save(self, _commit=True):
        """
        Save this object to the database.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :returns: the object that was saved
        """

        if _commit:
            count = 0
            while True:
                try:
                    Session.add(self)
                    Session.commit()
                    # if successful, break out of while loop
                    break
                except sqlalchemy.exc.OperationalError as e:
                    Session.rollback()
                    if count == 3:
                        print(e)
                        raise Exception(f"Failed to save to database: {e}")
                    count += 1
                    time.sleep(2)
        else:
            Session.add(self)

        return self

    def delete(self, _commit=True):
        """
        Delete this object.

        :param commit: whether to commit the change immediately to the database
        :type commit: boolean
        :returns: whether the delete was successful
        """

        Session.delete(self)
        return _commit and Session.commit()

    @classmethod
    def get_all(cls):
        return cls.query().all()

    def __repr__(self):
        return "<{}(id={})>".format(self.__class__.__name__, self.id)

    def __str__(self):
        return self.__repr__()
