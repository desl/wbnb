"""empty message

Revision ID: b42331829911
Revises: 0d1155978d08
Create Date: 2017-05-30 11:24:37.123764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b42331829911'
down_revision = '0d1155978d08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parties', sa.Column('attendee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'parties', 'users', ['attendee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'parties', type_='foreignkey')
    op.drop_column('parties', 'attendee_id')
    # ### end Alembic commands ###
