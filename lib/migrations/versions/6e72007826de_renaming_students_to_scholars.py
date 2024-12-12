"""Renaming students to scholars

Revision ID: 6e72007826de
Revises: 791279dd0760
Create Date: 2024-12-12 12:09:36.372954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e72007826de'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')
