"""empty message

Revision ID: 374100d4d9be
Revises: 
Create Date: 2021-04-25 20:43:05.422784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '374100d4d9be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tag', sa.String(length=30), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(
                        length=30), nullable=True),
                    sa.Column('last_name', sa.String(
                        length=30), nullable=True),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('username', sa.String(
                        length=40), nullable=False),
                    sa.Column('address', sa.String(length=500), nullable=True),
                    sa.Column('photo_url', sa.String(
                        length=500), nullable=True),
                    sa.Column('hashed_password', sa.String(
                        length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('carts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.Date(), nullable=True),
                    sa.Column('updated_at', sa.Date(), nullable=True),
                    sa.Column('order_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('stores',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=True),
                    sa.Column('address', sa.String(length=500), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=2000), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('orders',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('cart_id', sa.Integer(), nullable=False),
                    sa.Column('purchase_date', sa.Date(), nullable=True),
                    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('products',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=90), nullable=False),
                    sa.Column('store_id', sa.Integer(), nullable=True),
                    sa.Column('price', sa.String(length=10), nullable=False),
                    sa.Column('quantity', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=2000), nullable=False),
                    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('cart_product',
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('cart_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], ),
                    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
                    sa.PrimaryKeyConstraint('product_id', 'cart_id')
                    )
    op.create_table('favorites',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('user_id', 'product_id')
                    )
    op.create_table('photos',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=True),
                    sa.Column('photo_url', sa.String(
                        length=2000), nullable=True),
                    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('product_tag',
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('tag_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
                    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
                    sa.PrimaryKeyConstraint('product_id', 'tag_id')
                    )
    op.create_table('reviews',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('content', sa.String(
                        length=2000), nullable=False),
                    sa.Column('created_at', sa.Date(), nullable=True),
                    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # op.create_table('product_photo',
    # sa.Column('product_id', sa.Integer(), nullable=False),
    # sa.Column('photo_id', sa.Integer(), nullable=False),
    # sa.ForeignKeyConstraint(['photo_id'], ['photos.id'], ),
    # sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    # sa.PrimaryKeyConstraint('product_id', 'photo_id')
    # )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('product_tag')
    op.drop_table('photos')
    op.drop_table('favorites')
    op.drop_table('cart_product')
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_table('stores')
    op.drop_table('carts')
    op.drop_table('users')
    op.drop_table('tags')
    # ### end Alembic commands ###
