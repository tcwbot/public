Web scrapper project pulling all certifications that are offered by CCSF. A study involving multi processing threads.
There are two version of gets_certs.py. One is single threaded and the other is multi-threaded, which is faster.

# Output
```
231cs-python $ grep "Active" certs.txt | grep "Certificate" | sort -f | head -3
Accounting Assistant & Core Skills Certificate of Completion - Active
Acting Certificate of Achievement - Active
Addiction and Recovery Counseling Certificate of Achievement - Active

231cs-python $ grep "Active" certs.txt | grep "Certificate" | sort -f | tail -3
Welding Technology Level I Certificate of Accomplishment - Active
Wireless Networking Certificate of Accomplishment - Active
Yoga Certificate of Achievement - Active
```
