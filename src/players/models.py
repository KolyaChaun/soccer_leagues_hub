from sqlalchemy import Column, Integer, String, Date,ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    photo_url = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    team = relationship("Team", back_populates="players")
