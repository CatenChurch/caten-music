"""empty message

Revision ID: fb8363a06628
Revises: 926ce5f75aef
Create Date: 2019-05-29 23:56:59.098302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb8363a06628'
down_revision = '926ce5f75aef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songlists', sa.Column('songs_description_list', sa.ARRAY(sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('songlists', 'songs_description_list')
    # ### end Alembic commands ###