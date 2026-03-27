# Memory Forensics
Some of the most valuable pieces of information of someone's traces on the system is the memory dump.
A memory dump is a snapshot of the computer's volatile ram.

Thsi is the workflow described in the ctf handbook:
1. Run strings for clues
2. Identify the image profile (which OS, version, etc.)
3. Dump processes and look for suspicious processes
4. Dump data related interesting processes
5. View data in a format relating to the process (Word: .docx, Notepad: .txt, Photoshop: .psd, etc.)

jere is a syntactical manual: [Volatality](https://ctf101.org/forensics/what-is-memory-forensics/)