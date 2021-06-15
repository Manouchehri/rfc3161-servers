#!/usr/bin/env python3

import rfc3161ng

# hashes_types = ['md2', 'md4', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'ripemd160', 'mdc2']
hashes_types = ['sha1', 'sha256', 'sha384', 'sha512']

with open('server_list.txt', 'r') as server_list_file:
    for server in server_list_file:
        server = server.strip()
        # print(server)
        for hash_type in hashes_types:
            rt = rfc3161ng.RemoteTimestamper(server, hashname=hash_type, include_tsa_certificate=True)
            try:
                tst = rt.timestamp(data=b'David Manouchehri')
                # check_passed = rt.check(tst, data=b'David Manouchehri')
                print("Success using " + server + " with " + hash_type + " at " + str(rfc3161ng.get_timestamp(tst)))
            except:
                print("Failed to use " + server + " with " + hash_type)
