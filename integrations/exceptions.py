class APIConversationError(Exception):
    """Raised when the OpenHands API returns an error during conversation operations."""

    def __init__(
        self,
        status_code: int,
        error_detail: str,
        error_id: str | None = None,
    ):
        self.status_code = status_code
        self.error_detail = error_detail
        self.error_id = error_id
        super().__init__(f'API error {status_code}: {error_detail}')

    def to_slack_message(self) -> str:
        lines = [
            '---',
            f'error_type: api_error',
            f'http_status: {self.status_code}',
        ]
        if self.error_id:
            lines.append(f'error_id: {self.error_id}')
        lines.append('---')
        lines.append('')
        lines.append(self.error_detail)
        if self.error_id:
            lines.append('')
            lines.append(f'Error ID: `{self.error_id}`')
        return '\n'.join(lines)
