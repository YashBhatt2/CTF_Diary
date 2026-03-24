# General Methodology
For forensic CTFs I like to start with this sequence:
```bash
file filename
exiftool filename
```
Exiftool obviously gives the Metadata of the file, to make sure it IS a stegenography problem,
here are the clues:
1. It has to be an image, stegenography is literally hiding data in images.
2. If there is a password in the metadata and the image is a Jpg, the tool you should use is Steghide
3. If the image is a png, then the flag can be encoded in the least signifcant bit of every pixel, this is can be taken care of the tool called zsteg. [Aperisolve](https://www.aperisolve.com/) is a website that does all of stegenography in one go.
