Web scrapper project which pulls all certification titles that are offered by CCSF. A study involving multi processing threads.
There are two versions of [gets_certs.py](https://github.com/tcwbot/public/blob/main/scripts/python231/gets_cert.py). One is single threaded and the other [gets_certs_threaded.py](https://github.com/tcwbot/public/blob/main/scripts/python231/gets_certs_threaded.py) is multi-threaded, which is faster.

# Usages & Output
```
231cs-python $ python3 gets_certs_threaded.py

231cs-python $ grep "Active" certs.txt | grep "Certificate" | sort -f | head -3
Accounting Assistant & Core Skills Certificate of Completion - Active
Acting Certificate of Achievement - Active
Addiction and Recovery Counseling Certificate of Achievement - Active

231cs-python $ grep "Active" certs.txt | grep "Certificate" | sort -f | tail -3
Welding Technology Level I Certificate of Accomplishment - Active
Wireless Networking Certificate of Accomplishment - Active
Yoga Certificate of Achievement - Active
```
