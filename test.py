from auto_smart_commit import extract_jira_issue_key


class TestExtractJiraIssueKey:
    message = "PRJ-123-my-life-for-aiur"
    expected_result = "PRJ-123"

    def test_extract_jira_issue_key(self):
        result = extract_jira_issue_key(self.message)
        assert result == self.expected_result

    def test_extract_jira_issue_key_capitals(self):
        result = extract_jira_issue_key(self.message.upper())
        print(result)
        expected_result = "PRJ-123"
        assert result == expected_result

    def test_extract_jira_issue_key_lower(self):
        result = extract_jira_issue_key(self.message.lower())
        assert result is None

    def test_extract_jira_issue_key_underscore(self):
        result = extract_jira_issue_key(self.message.replace("-", "_"))
        assert result is None
