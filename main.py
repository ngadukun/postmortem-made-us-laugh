"""A blameless postmortem, played for laughs."""

POSTMORTEM = """INCIDENT POSTMORTEM #42: The Deploy Named final_v2_REAL

SUMMARY
On Tuesday at 09:14 we shipped final_v2_REAL to production.
By 09:15 it had renamed itself final_v2_REAL (copy) in the logs,
emailed every customer a receipt for $0.00, and promoted our
staging banana emoji to the live homepage hero image.

TIMELINE
09:14 - Deploy starts. Nobody questions the filename. This is
        formally recorded as Root Cause Zero.
09:16 - Support gets its first ticket: "Why did I just buy
        nothing, beautifully?" The receipt had confetti.
09:19 - Rollback begins. The rollback script, last edited in
        2021, asks if we are sure. We were not. We clicked yes.
09:31 - Site restored. The banana remains for nine extra
        minutes because, quote, "engagement is up 40%."

ROOT CAUSE
A config flag called USE_TEST_DATA was set to "false", which
our parser read as a non-empty string, which it read as true.
The flag was not lying. It was just raised in JavaScript.

WHAT WENT WELL
The incident channel stayed blameless, the banana got fan mail,
and the $0.00 receipts included a working unsubscribe link,
which is more than our real receipts manage.

ACTION ITEMS
1. Ban the word "final" from filenames by law and by linter.
2. Teach the parser that "false" is not a personality trait.
3. Keep the banana. It has a team now. It outranks two of us."""


def main() -> None:
    print(POSTMORTEM)


if __name__ == "__main__":
    main()
