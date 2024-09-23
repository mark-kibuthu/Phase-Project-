"""Create initial tables

Revision ID: 44bf94831294
Revises: 
Create Date: 2024-09-23 19:00:37.976328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44bf94831294'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('students',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('major', sa.String(length=50), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
    )
    
    op.create_table('courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('credits', sa.Integer(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=False),
    )

    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('department', sa.String(length=50), nullable=False),
    )

    op.create_table('enrollments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False),
        sa.Column('semester', sa.String(length=10), nullable=False),
    )
