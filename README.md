# Hunting-Lists
A repository of IoC lists to use for threat hunting queries

<div id="badges">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/cyb3rmik3/Hunting-Lists?style=flat-square&color=blue">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/forks/cyb3rmik3/Hunting-Lists?style=flat-square&color=blue">
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/cyb3rmik3/Hunting-Lists?style=flat-square&color=yellow">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/cyb3rmik3/Hunting-Lists?style=flat-square&color=yellow">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/cyb3rmik3/Hunting-Lists?style=flat-square&color=green">
  <img alt="GitHub License" src="https://img.shields.io/github/license/cyb3rmik3/Hunting-Lists?style=flat-square&color=green">
</div>

## Sources documentation
| File  | Source | Last updated | Comment |
| ------------- | ------------- | ------------- | ------------- |
| [netcraft-tlds](https://github.com/cyb3rmik3/Hunting-Lists/blob/main/netcraft-tlds.csv)  | [Cybercrime on Top Level Domains](https://trends.netcraft.com/cybercrime/tlds)  | 14/04/2024  | Top 20 TLDs selected based on incidents to sites ratio  |
| [phishing-keywords](https://github.com/cyb3rmik3/Hunting-Lists/blob/main/phishing-keywords.csv)  | [PwC-IR Business Email Compromise Guide](https://github.com/PwC-IR/Business-Email-Compromise-Guide), [The top phishing keywords in the last 10k+ malicious emails we investigated](https://expel.com/blog/top-phishing-keywords/) | 04/10/2023 | Phishing subject keywords |
| [rmm-software](https://github.com/cyb3rmik3/Hunting-Lists/blob/main/rmm-software.csv)  | [Detecting RMM tools using Microsoft Defender for Endpoint](https://www.michalos.net/2023/11/27/detecting-rmm-tools-using-microsoft-defender-for-endpoint/) | 25/11/2023 | DeviceProcessEvents artifacts for RMM tools hunting |
| [spamhaus-abused-tlds](https://github.com/cyb3rmik3/Hunting-Lists/blob/main/spamhaus-abused-tlds.csv)  | [The 10 Most Abused Top Level Domains](https://www.spamhaus.org/statistics/tlds/) | 14/04/2024 | TLDs with the worst reputations for spam operations |
| [crowdstrike-phishing-domains](https://github.com/cyb3rmik3/Hunting-Lists/blob/main/crowdstrike-phishing-domains.csv) | [Don't Fall for It: Hackers Pounce on CrowdStrike Outage With Phishing Emails](https://www.pcmag.com/news/dont-fall-for-it-hackers-pounce-on-crowdstrike-outage-with-phishing-emails), [Phishers Feast on CrowdStrike Chaos: Exploiting Global Outage for Cyber Scams](https://www.securityblue.team/blog/posts/crowdstrike-global-outage-exploited-by-cyber-scammers?s=09), [Suspicious Domains Exploiting the Recent CrowdStrike Outage!](https://socradar.io/suspicious-domains-exploiting-the-recent-crowdstrike-outage/) | 20/07/2024 | Domains possibly associated with Crowdtrike phishing |
