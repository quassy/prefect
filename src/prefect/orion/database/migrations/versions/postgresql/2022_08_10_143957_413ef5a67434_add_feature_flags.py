"""add-feature-flags

Revision ID: 413ef5a67434
Revises: 60e428f92a75
Create Date: 2022-08-10 14:39:57.882716

"""
import sqlalchemy as sa
from alembic import op

import prefect

# revision identifiers, used by Alembic.
revision = "413ef5a67434"
down_revision = "60e428f92a75"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "feature_flag",
        sa.Column(
            "id",
            prefect.orion.utilities.database.UUID(),
            server_default=sa.text("(GEN_RANDOM_UUID())"),
            nullable=False,
        ),
        sa.Column(
            "created",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("data", sa.JSON(), server_default="{}", nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_feature_flag")),
    )
    op.create_index(
        op.f("ix_feature_flag__name"), "feature_flag", ["name"], unique=True
    )
    op.create_index(
        op.f("ix_feature_flag__updated"), "feature_flag", ["updated"], unique=False
    )


def downgrade():
    op.drop_index(op.f("ix_feature_flag__updated"), table_name="feature_flag")
    op.drop_index(op.f("ix_feature_flag__name"), table_name="feature_flag")
    op.drop_table("feature_flag")
