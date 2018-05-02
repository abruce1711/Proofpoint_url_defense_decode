# Proofpoint URL Defense Decode

<a href="https://www.proofpoint.com/uk/products/email-protection">Proofpoint</a> is a mail filtering service we currently use for our clients at work.

They provide a service to protect URL's but in doing so they re-write the URL into a readable but coded version of itself.
This can make it difficult when dealing with spam emails for our clients, to see where the spam links are taking them.

For example it would take the link for this readme file and re-write it into the following - 

"https://urldefense.proofpoint.com/v2/url?u=https-3A__github.com_abruce1711_Proofpoint-5Furl-5Fdefense-5Fdecode_new_master-3Freadme-3D1&d=DwMCaQ&c=euGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM&r=3UDI-QCTDd2cB7S6vMRxarf6npHG9GelAe_MzGuBs6g&m=pN3JxYQAtyhMLRziWnmRheGaP6BINoRANQxbdkZf2rw&s=Md3pEMF_ICMWghMUXTF5SJCq-Gj6XMz_yA6CE6THzrE&e="

I have created this Python script to decode this, and set it into a Flask application for use at my work.
