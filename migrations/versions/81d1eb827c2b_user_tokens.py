"""user tokens

Revision ID: 81d1eb827c2b
Revises: 63d4c1ac1b92
Create Date: 2018-08-20 20:09:03.186163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81d1eb827c2b'
down_revision = '63d4c1ac1b92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###
