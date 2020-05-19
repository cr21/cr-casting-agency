"""empty message

Revision ID: c3c738ccba8a
Revises: 
Create Date: 2020-05-19 00:23:43.802105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3c738ccba8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=False),
    sa.Column('actor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_table('actors')
    # ### end Alembic commands ###
