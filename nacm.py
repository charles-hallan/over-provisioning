# CoS_i: CoS(MRth_i, Brv_i, Bu_i)

import subprocess
import socket
from time import sleep

def require(link, cos, brq):
	if cos.bu + brq < cos.mrth: # Bov > 0
		if ( cos.bav - brq > 0 ):
			cos.bu_add(brq)
			cos.bav_sub()
			return True;
		else:
			require_aux(link,cos,brq)
			return True;

	else:
		brl = release_sum(link, cos, brq)
		cos.mrth_add(brl)
		if brl > 0:
			require_aux(link,cos,brq)
			return True;

		else:
			return False;

def require_aux(link,cos,brq):
	cos.overprov(brq)
	cos.bu_add(brq)
	cos.bav_sub()

def release(link,cos,brl,id):
    if cos == "A":
        link.cos_a.bu_sub(brl)
        link.cos_a.bav_sub();
        del link.stats_a[id];

    elif cos == "B":
        link.cos_b.bu_sub(brl)
        link.cos_b.bav_sub();
        del link.stats_b[id];

    elif cos == "C":
        link.cos_c.bu_sub(brl)
        link.cos_c.bav_sub();
        del link.stats_c[id];

def release_sum(link,cos,brq):
	brl=0
	for j in link.cos_list:
		if j != cos:
			brl_mrth = j.bw_release()
			brl = brl + brl_mrth;

	if cos.mrth - cos.bu + brl > brq:
		for k in link.cos_list:
			if k != cos:
				k.mrth = k.mrth - k.bw_release()
		return brl;
	else:
		return 0;
