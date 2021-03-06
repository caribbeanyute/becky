"""empty message

Revision ID: 2ec5e16a97da
Revises: 
Create Date: 2020-05-14 14:58:34.090593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ec5e16a97da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appliedpromotions',
    sa.Column('apID', sa.Integer(), nullable=False),
    sa.Column('pID', sa.Integer(), nullable=True),
    sa.Column('cID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('apID')
    )
    op.create_table('book',
    sa.Column('bookID', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(asdecimal=True), nullable=False),
    sa.Column('reorderthres', sa.Integer(), nullable=False),
    sa.Column('stoporder', sa.Boolean(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('bookID')
    )
    op.create_table('cart',
    sa.Column('cID', sa.Integer(), nullable=False),
    sa.Column('custID', sa.Integer(), nullable=True),
    sa.Column('bookID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('cID')
    )
    op.create_table('order',
    sa.Column('ordID', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('cust', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('ordID')
    )
    op.create_table('promotions',
    sa.Column('pID', sa.Integer(), nullable=False),
    sa.Column('promoCode', sa.String(length=25), nullable=True),
    sa.Column('percoff', sa.Float(asdecimal=True), nullable=False),
    sa.Column('expDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('pID')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('pwd_hash', sa.String(length=200), nullable=True),
    sa.Column('urole', sa.String(length=80), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('member', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('items',
    sa.Column('itID', sa.Integer(), nullable=False),
    sa.Column('ordID', sa.Integer(), nullable=False),
    sa.Column('bookID', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(asdecimal=True), nullable=False),
    sa.ForeignKeyConstraint(['ordID'], ['order.ordID'], ),
    sa.PrimaryKeyConstraint('itID')
    )
    op.create_index(op.f('ix_items_ordID'), 'items', ['ordID'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_items_ordID'), table_name='items')
    op.drop_table('items')
    op.drop_table('user')
    op.drop_table('promotions')
    op.drop_table('order')
    op.drop_table('cart')
    op.drop_table('book')
    op.drop_table('appliedpromotions')
    # ### end Alembic commands ###
