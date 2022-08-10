"""add-feature-flags

Revision ID: e73795f53a56
Revises: 296e2665785f
Create Date: 2022-08-10 14:33:38.599178

"""
import sqlalchemy as sa
from alembic import op

import prefect

# revision identifiers, used by Alembic.
revision = "e73795f53a56"
down_revision = "296e2665785f"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "feature_flag",
        sa.Column(
            "id",
            prefect.orion.utilities.database.UUID(),
            server_default=sa.text(
                "(\n    (\n        lower(hex(randomblob(4)))\n        || '-'\n        || lower(hex(randomblob(2)))\n        || '-4'\n        || substr(lower(hex(randomblob(2))),2)\n        || '-'\n        || substr('89ab',abs(random()) % 4 + 1, 1)\n        || substr(lower(hex(randomblob(2))),2)\n        || '-'\n        || lower(hex(randomblob(6)))\n    )\n    )"
            ),
            nullable=False,
        ),
        sa.Column(
            "created",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("(strftime('%Y-%m-%d %H:%M:%f000', 'now'))"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("(strftime('%Y-%m-%d %H:%M:%f000', 'now'))"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("data", sa.JSON(), server_default="{}", nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_feature_flag")),
    )
    with op.batch_alter_table("feature_flag", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_feature_flag__name"), ["name"], unique=True
        )
        batch_op.create_index(
            batch_op.f("ix_feature_flag__updated"), ["updated"], unique=False
        )


def downgrade():
    with op.batch_alter_table("feature_flag", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_feature_flag__updated"))
        batch_op.drop_index(batch_op.f("ix_feature_flag__name"))

    op.drop_table("feature_flag")
