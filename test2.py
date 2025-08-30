# just to check if the pr is working and if cr is able to capture it in the report

# new lines of code added as per the comments fm reviewer

def get_pr_comments(self, owner, repo, pull_number):
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments"
        response = requests.get(url, headers=self.headers, verify=False)
        response.raise_for_status()
        return response.json()

def get_pr_comments(self, owner, repo, pull_number):
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments"
        response = requests.get(url, headers=self.headers, verify=False)
        response.raise_for_status()
        return response.json()
