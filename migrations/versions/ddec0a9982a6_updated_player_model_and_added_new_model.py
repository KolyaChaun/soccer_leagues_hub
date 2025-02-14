"""Updated Player model and added new model

Revision ID: ddec0a9982a6
Revises:
Create Date: 2025-02-13 15:28:48.065708

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ddec0a9982a6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_players_id", table_name="players")
    op.drop_table("players")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "players",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("surname", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("age", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("club", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="players_pkey"),
    )
    op.create_index("ix_players_id", "players", ["id"], unique=False)
    # ### end Alembic commands ###
