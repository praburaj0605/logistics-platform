from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0006"
down_revision = "0005"
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "enquiries",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("client_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("clients.id"), nullable=False),
        sa.Column("origin", sa.String(50), nullable=False),
        sa.Column("destination", sa.String(50), nullable=False),
        sa.Column("service_type", sa.String(100), nullable=False),
        sa.Column("expected_ship_date", sa.DateTime(timezone=True)),
        sa.Column("notes", sa.Text()),
        sa.Column("status", sa.String(30), server_default="open"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )

def downgrade():
    op.drop_table("enquiries")
