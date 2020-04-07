# Honeypot
Which Honeypot(s) you deployed
Any issues you encountered
A summary of the data collected: number of attacks, number of malware samples, etc.
Any unresolved questions raised by the data collected

### Deployed Honeypots
The honeypots I deployed were:
  * Dionaea
  * Amun
  * Cowrie
  * Conpot
  * ElasticHoney
  * p0f
  
### Issues Encountered
At first I had a lot of issues with my deployment. My hpfeeds-broker had a FATAL error and my supervisorctl would not run, causing my honeypots to not transmit any data to mhn-admin. I attempted to resolve this issue by following many of the threads in the MHN GitHub issues page and MHN Google Forum containing relevant topics. Eventually I decided to do a clean reinstall of the entire system which got everything working.  
With my new deployment I tried to deploy a Glastopf honeypot, but for some reason it does not display on the Sensors page so any attacks on it do not get displayed. I have chosen to simply omit this honeypot from my submission.
  
### Summary of Collected Data
I got a lot of attacks very quickly after my honeypots were deployed. The Dionaea honeypot is overwhelmingly the most attacked honeypot with the next honeypot, Amun, having <10% the amount of attacks the Dionaea honeypot does. The list drops of significantly form here with the last honey pot, ElasticHoney, having only 1 attack. The list is as follows:
  1. Dionaea
  2. Amun
  3. p0f
  4. Conpot
  5. Cowrie
  6. ElasticHoney  
    
At first, many of the attacks displayed came from my nmap on the Dionaea honeypot but over time others surpassed my attacks.  
The Top 5 Attackers are (approx. at time of data export):
  1.  89.25.118.100 (6,823 attacks) - Botevgrad, Bulgaria
  2.  76.230.236.10 (4,438 attacks) - Miami, Florida
  3.  200.35.77.146 (1,815 attacks) - Bachaquero (Cabemas?), Venezuela
  4.  205.205.150.19 (161 attacks) - New York City, USA
  5.  14.135.120.19 (141 attacks) - Yinchuan?, China
  
The first place attacker from Botevgrad, Bulgeria contributed heavily to the ranking of Dionaea. While only 4 contries are represented in the top attacker rankings, attacks came from numerous countries around the world.

The Top Attacked Ports were:
  1. 1433 (9,227 times)
  2. 445 (470 times)
  3. 23 (195 times)
  4. 80 (190 times)
  5. 443 (133 times)
  
  1433 - TCP/Udp Wideopen Firewall rule
  80 - HTTP firewall rule
  Explanation!!
  
#### Bonus Malware Samples
I recieved 2 dionaea.capture payloads, which I believe is the malware samples that were wandted.
They are:
  url | daddr | saddr | dport | sport | sha512 | md5
  --- | ----- | ----- | ----- | ----- | ------ | ---
  | | 35.222.174.155 |	223.205.248.120 |	445 |	54706	| a823196596f18305c898c25590761dee23218f72bb7db629d63bb95cd3cf570184633017ee536bbcf831ae23c9f0678bfce4580b0cc49babfa9c731fd2c1e2e5 | 549ae01010e6b826a301851393ea8433
  | | 35.222.174.155 |	189.195.144.222 |	445 |	54951 | a823196596f18305c898c25590761dee23218f72bb7db629d63bb95cd3cf570184633017ee536bbcf831ae23c9f0678bfce4580b0cc49babfa9c731fd2c1e2e5 | 549ae01010e6b826a301851393ea8433
  
### Unresolved Questions Reaised by Collected Data

I don't understand why the Dionaea honeypot is the most attacked honeypot between all the ones I deployed. Considering the pattern, and it being the honeypot we were required to deploy it is probably the most attacked honeypot of all the MHN supported sensors. I tries to read up on what about Dionaea makes this the case, but found no results. Articles regarding honeypots corroborated my findings with Dionaea being their most attacked honeypot as well.  
I also want to know what the attackers aer attempting to gain from attacking vulnerable systems. I'm sure there are plenty of nefarious individuals out there, but I can't help but wonder exactly what kind of data they expect to find and if any of the attackers are state sponsored entities.  
