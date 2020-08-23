
from app.spider.yushu_book import YuShuBook
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, func
from sqlalchemy.orm import relationship
from app.models.base import Base, db


class Wish(Base):
    __tablename__ = 'wish'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = cls.query.filter_by(launched = False, uid = uid).all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        from app.models.gift import Gift
        count_list = db.session.query(Gift.isbn, func.count(Gift.id)).filter(Gift.status == 1,
                                          Gift.launched == False,
                                          Gift.isbn.in_(isbn_list)).group_by(Gift.isbn).all()
        # 以字典的方式返回，会更容易表达清楚数据含义，这里不建议直接返回，没有标识的数据，使用字典还有一点是比较方便
        count_list = [{'isbn':w[0], 'count':w[1]}for w in count_list]
        return count_list
