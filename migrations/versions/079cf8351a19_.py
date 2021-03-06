"""empty message

Revision ID: 079cf8351a19
Revises: 66c7787c546e
Create Date: 2016-08-01 23:13:46.838010

"""

# revision identifiers, used by Alembic.
revision = '079cf8351a19'
down_revision = '66c7787c546e'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('export_jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('user_email', sa.String(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('export_jobs')
    ### end Alembic commands ###
