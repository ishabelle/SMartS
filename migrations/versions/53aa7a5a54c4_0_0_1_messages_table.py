"""messages table

Revision ID: 53aa7a5a54c4
Revises: 
Create Date: 2021-05-20 09:52:05.413941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53aa7a5a54c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('receiver', sa.String(length=50), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('text', sa.String(length=160), nullable=True),
    sa.Column('sender', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
