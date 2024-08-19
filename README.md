# ShieldedSurf
A security-focused project that aims to protect everyday internet surfers from malicious websites using Remote Browser Isolation (RBI).

Imagine you are surfing the web, and you click on a link. You are familiar with how to spot malicious websites so you are confident in your decision to click that one page. What you are not familiar with is that cyber-threats are evolving, and so to techniques to avoid suspicion.

You click on that link and it downloads something onto your desktop. By the time you notice, it is too late. You have been successfully exploited.

Source: https://www.forbes.com/advisor/education/it-and-tech/cybersecurity-statistics/#Sources

The following source states that at any given time, 4.1 million sites are infected with malware.

It's important to have a service that protects you from online threats, while ensuring your productivity and streamlined day-to-day tasks.

That is where **ShielededSurf** comes in. **ShieldedSurf** comprises of a RBI solution that sandboxes malicious websites (or suspected ones) into a containerized, remote environment. It shields your endpoint devices and personal devices from malicious downloads and allows you to go about your day. 💻


Docker image utilized: jlesage/docker-firefox

# Basic Flow
![image](https://github.com/user-attachments/assets/7ed02b78-fb4a-4a8a-9f6c-f32706de199c)

1) User, with ShieldedSurf Chrome Extension, clicks on malicious website masquerading as a safe website
2) ShieldedSurf containerizes the website to shield the user from any malicious downloads
3) The user safely browses the website in the remote environment with confidence because he/she is secured from any threats

# Current Progress
I have a bash file that will locally create a remote browser based on the URL from user input.
![PoC-OnPrem](poc_onprem.png)
