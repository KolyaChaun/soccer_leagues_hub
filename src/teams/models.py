from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, nullable=True)
    emblem_url = Column(String, nullable=False)
    form_color = Column(String, nullable=True)
    avg_age = Column(Integer, nullable=False)

    players = relationship("Player", back_populates="team")