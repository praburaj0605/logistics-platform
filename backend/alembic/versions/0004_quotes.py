from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "quotes",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("client_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("clients.id"), nullable=False),
        sa.Column("vendor_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("vendors.id"), nullable=False),
        sa.Column("service_type", sa.String(100), nullable=False),
        sa.Column("origin", sa.String(50), nullable=False),
        sa.Column("destination", sa.String(50), nullable=False),
        sa.Column("base_rate", sa.Float(), nullable=False),
        sa.Column("final_rate", sa.Float(), nullable=False),
        sa.Column("currency", sa.String(10), server_default="INR"),
        sa.Column("status", sa.String(30), server_default="generated"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )

def downgrade():
    op.drop_table("quotes")
