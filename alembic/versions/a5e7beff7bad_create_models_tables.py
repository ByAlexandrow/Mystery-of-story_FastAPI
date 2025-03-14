"""create models tables

Revision ID: a5e7beff7bad
Revises: 
Create Date: 2025-03-12 15:46:17.709700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5e7beff7bad'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admins_email'), 'admins', ['email'], unique=False)
    op.create_index(op.f('ix_admins_id'), 'admins', ['id'], unique=False)
    op.create_index(op.f('ix_admins_is_admin'), 'admins', ['is_admin'], unique=False)
    op.create_index(op.f('ix_admins_password'), 'admins', ['password'], unique=False)
    op.create_index(op.f('ix_admins_username'), 'admins', ['username'], unique=False)
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('cover_img', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=False)
    op.create_index(op.f('ix_categories_is_published'), 'categories', ['is_published'], unique=False)
    op.create_index(op.f('ix_categories_title'), 'categories', ['title'], unique=False)
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('cover_img', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('pdf', sa.String(), nullable=True),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['admins.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_articles_content'), 'articles', ['content'], unique=False)
    op.create_index(op.f('ix_articles_id'), 'articles', ['id'], unique=False)
    op.create_index(op.f('ix_articles_is_published'), 'articles', ['is_published'], unique=False)
    op.create_index(op.f('ix_articles_title'), 'articles', ['title'], unique=False)
    op.create_table('carousels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_carousels_id'), 'carousels', ['id'], unique=False)
    op.create_index(op.f('ix_carousels_is_published'), 'carousels', ['is_published'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_carousels_is_published'), table_name='carousels')
    op.drop_index(op.f('ix_carousels_id'), table_name='carousels')
    op.drop_table('carousels')
    op.drop_index(op.f('ix_articles_title'), table_name='articles')
    op.drop_index(op.f('ix_articles_is_published'), table_name='articles')
    op.drop_index(op.f('ix_articles_id'), table_name='articles')
    op.drop_index(op.f('ix_articles_content'), table_name='articles')
    op.drop_table('articles')
    op.drop_index(op.f('ix_categories_title'), table_name='categories')
    op.drop_index(op.f('ix_categories_is_published'), table_name='categories')
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_table('categories')
    op.drop_index(op.f('ix_admins_username'), table_name='admins')
    op.drop_index(op.f('ix_admins_password'), table_name='admins')
    op.drop_index(op.f('ix_admins_is_admin'), table_name='admins')
    op.drop_index(op.f('ix_admins_id'), table_name='admins')
    op.drop_index(op.f('ix_admins_email'), table_name='admins')
    op.drop_table('admins')
    # ### end Alembic commands ###
