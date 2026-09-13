from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `author` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL,
    `age` VARCHAR(32) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `publish` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL,
    `email` VARCHAR(32) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `book` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(32) NOT NULL,
    `price` VARCHAR(32) NOT NULL,
    `img_url` VARCHAR(255),
    `bread` INT NOT NULL,
    `bcomment` INT NOT NULL,
    `publish_id` INT NOT NULL,
    CONSTRAINT `fk_book_publish_0c600934` FOREIGN KEY (`publish_id`) REFERENCES `publish` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `book_author` (
    `book_id` INT NOT NULL,
    `author_id` INT NOT NULL,
    FOREIGN KEY (`book_id`) REFERENCES `book` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_book_author_book_id_818352` (`book_id`, `author_id`)
) CHARACTER SET utf8mb4 COMMENT='作者';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmVtP2zAUgP8KytMmdVMJ7UB7S7uhMQZMwKZJgCIncdOoiR0cZ1Ch/PfZzsW5NSTl1q"
    "59Ke25xOd8sY99zIPiYQu6wUctpFNMlM87DwoCHmRfSprejgJ8X8q5gALDFaZA2hgBJcCk"
    "TDoBbgCZyIKBSRyfOhgxKQpdlwuxyQwdZEtRiJzbEOoU25BOIY/l6oaJHWTBexikP/2ZPn"
    "GgaxVCdSw+tpDrdO4L2RGih8KQj2boJnZDD0ljf85CRpm1gyiX2hBBAijkj6ck5OHz6JI8"
    "04ziSKVJHGLOx4ITELo0l25LBiZGnB+LJhAJ2nyUD+ruYH9wsPdpcMBMRCSZZD+K05O5x4"
    "6CwOmlEgk9oCC2EBglN/G3Qm48BaQeXWpfgsdCLsNLUTXRSwUSn5wyz8TPA/e6C5FNp+zn"
    "ntoA67d2Pv6mnb/bU9/zXDCbxPHcPk00qlBxnpIfsDvhS8w3mR5fwpNZbjJygQHM2R0gll"
    "7RYBUvsq2qPNWrneUGxrOg+p5OAJpfYv4p3tYRyx0gs+4NJZVwxJ6zzJtaskoo1+FgMjSv"
    "w4N+f6i0emNROuNSqRxM5KCXanuaEYEuzydTx/U8ZoaJwD2D85SlHlfQ7E0kqtgpUdIpwa"
    "E9zVzkDsG4srEhjdeKdjHWvnzlcr1ce8Vc8QBiq8ZKMo56xdBrtqs0pcWblZFabLeqNdqq"
    "qEPdTsU2c9jkcpvfrHzimJ0IZg5bgsna9Ww9JG4XhjmXpSgmq/TNIKrDYQuKzGohRqErcj"
    "QIBF3KYGb/eCVckYn4LMUwB8zEngfjbNsyy7lsKjY/NFwnmOqd9tyi0yahq5zNKySrGA8x"
    "gY6NjmHbQ/RP+aTVo9hwfibgLjvNleZI7Yk2eoXGJn9Mf1prIy95/p/mRuZUbm9kQ1hsbg"
    "odTLm9yXU+T2xuBMPm7iZdJTUNTm4BLe5xcut12+asWp3tbW/kXuyIDj3gdDqgZw6bTLDD"
    "rdyj12qjxO3w+JyXXZ7dwm1n2Ru1tzsJRE/cvBurvgZZx11b9BNNY80H0mZb8teo5P+FJE"
    "hWSduilXNZz7L1ItcKfGl0gJiYryfA3X6/BUBmtRCg0BUBshFp7S3D94uz03qIOZcSyF+I"
    "JXhlOSbt7bCzKL1ZTawNFHnWPGgvCG7dPLx3J9qfMtfxj7ORoIADahPxFPGA0av+06tme4"
    "n+AePXOJM="
)
