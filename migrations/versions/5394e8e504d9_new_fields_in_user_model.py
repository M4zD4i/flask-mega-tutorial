"""new fields in user model

Revision ID: 5394e8e504d9
Revises: 875ea3d8ad6c
Create Date: 2018-06-20 20:12:34.487756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5394e8e504d9'
down_revision = '875ea3d8ad6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
