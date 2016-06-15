import sys

#colours:
#orange FF813E
#yellow FFDB39
#green 00D791
#test yellow FFE73C

#emotions:
#happy
#calm
#dissapointed
#loss
#interested
#horny
#excited (in place of shocked?)
#appreciative (like a lesser version of horny)
#

#clothes = shoes, earrings, gloves, crown, dress, bra, panties
#9 total stages

version_str = "33**"

def get_emotion_data():
	em = dict()
	happy = dict()
	happy["face"] = "fa7.40.60.57.42.35.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd25.1.49.49_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0_ad0.0.0.0.0.0.0.0.0.0"
	happy["blush_mod"] = 0
	happy["arms"] = "aa32.76.1.8.100.32.76.1.8.100_ab_ac_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0_ad0.0.0.0.0.0.0.0.0.0"
	em["happy"] = happy
	
	calm = dict()
	calm["face"] = "fa12.40.60.57.42.65.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd0.1.49.49"
	calm["blush_mod"] = 0
	calm["arms"] = "aa15.86.0.8.100.15.86.0.8.100_ab_ac_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0_ad0.0.0.0.0.0.0.0.0.0"
	em["calm"] = calm
	
	diss = dict()
	diss["face"] = "fa0.40.60.57.42.35.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_ha89.89_hb49.1.44.99_hc0.79.39.0.79.39_hd4.1.49.49"
	diss["blush_mod"] = 0
	diss["arms"] = "aa9.97.0.8.55.9.97.0.8.55_ab_ac"
	em["disappointed"] = diss
	
	loss = dict()
	loss["face"] = "fa6.40.60.57.42.35.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd11.1.49.49"
	loss["blush_mod"] = 0
	loss["arms"] = "aa9.83.0.8.55.9.83.0.8.55_ab_ac"
	em["loss"] = loss
	
	intr = dict()
	intr["face"] = "fa12.40.60.57.42.17.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_ha87.87_hb49.1.44.99_hc0.25.39.0.25.39_hd20.1.49.49"
	intr["blush_mod"] = 0
	intr["arms"] = "aa13.84.0.42.65.13.84.0.42.65_ab_ac"
	em["interested"] = intr
	
	horny = dict()
	horny["face"] = "fa1.40.60.57.42.10.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd27.1.49.49"
	horny["blush_mod"] = 1
	horny["arms"] = "aa7.92.1.28.51.7.92.1.28.51_ab_ac"
	em["horny"] = horny
	
	exc = dict()
	exc["face"] = "fa1.40.60.57.42.35.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_ha89.89_hb49.1.44.99_hc0.18.39.0.18.39_hd34.1.49.49"
	exc["blush_mod"] = 2
	exc["arms"] = "aa36.76.1.42.32.36.76.1.42.32_ab_ac"
	em["excited"] = exc
	
	appr = dict()
	appr["face"] = "fa1.40.60.57.42.59.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd20.1.49.49"
	appr["blush_mod"] = 0
	appr["arms"] = "aa13.84.1.42.65.13.84.1.42.65_ab_ac"
	em["appreciative"] = appr
	
	return em

def get_image_data():
	d = dict()
	
	d["appearance"] = "ca71.0.15.72.32.36.34.6.17_cb0_da2.0.0.100_db_dh2.30.50.50.0_di4_qa_qb_eh1.38_ea2.38.37.35.0.0_ec14.100.38.37.35_ed_ef_eg_r015.37.35.56.0.2.100.77.81.599.522.0_r115.37.35.56.0.2.92.20.71.614.547.0_r215.37.35.56.0.1.100.100.154.616.486.0_r415.38.35.56.0.2.18.86.150.507.572.0_r515.38.35.56.0.2.44.100.93.561.524.0_r642.38.38.35.0.2.79.72.314.573.565.0_fa1.40.60.57.42.35.56_fb00_fc6.20.55.6.20.55.33.21.21_fd1.0.23.38.56_fe83.69_ff0000000000_fg1.55_pa0.0.0.0.62.52.84.84.0.0_pb_pc_pd_pe"
	
	d["vagina"] = "dc0.4.2.2.2"
	d["face"] = "dd9.3.45.43.25"
	
	stages = list()
	
	s0 = {}
	s0["blush"] = 0
	s0["lj"] = 0
	s0["clothes"] = "ia_ib_id3.FFDB39.FFDB39.FF813E.0.0.24.27.55.6.27.55.6_if_ic_jc_ie_ja_jb_jd5.FF813E.55.57_je5.FF813E.55.57_jf_jg_ka32.FF813E.FF813E.3_kb21.FF813E.FF813E.FF813E_kc_kd_ke_kf_la31.43.32.3.1_lb_oa_os_ob4.55.00D791.0_oc4.55.00D791.0_od_oe_of_lc_m054.55.55.55.0.2.43.47.0.12.0.61_m15.00D791.2.61.2.2.22.15.0.12.2.61_n0_s01.FF813E.FF813E.30.0.66.0.458.850.1.6.0.70.2.61_og7.55.44.0_oh7.55.44.0_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0"
	s0["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s0)
	
	#lost shoes
	s1 = {}
	s1["blush"] = 0
	s1["lj"] = 0
	s1["clothes"] = "ia_ib_id3.FFDB39.FFDB39.FF813E.0.0.24.27.55.6.27.55.6_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka32.FF813E.FF813E.3_kb21.FF813E.FF813E.FF813E_kc_kd_ke_kf_la31.43.32.3.1_lb_oa_os_ob4.55.00D791.0_oc4.55.00D791.0_od_oe_of_lc_m054.55.55.55.0.2.43.47.0.12.0.61_m15.00D791.2.61.2.2.22.15.0.12.2.61_n0_s01.FF813E.FF813E.30.0.66.0.458.850.1.6.0.70.2.61_og7.55.44.0_oh7.55.44.0_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0"
	s1["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s1)
	
	#lost earrings
	s2 = {}
	s2["blush"] = 0
	s2["lj"] = 0
	s2["clothes"] = "ia_ib_id3.FFDB39.FFDB39.FF813E.0.0.24.27.55.6.27.55.6_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka32.FF813E.FF813E.3_kb21.FF813E.FF813E.FF813E_kc_kd_ke_kf_la31.43.32.3.1_lb_oa_os_ob_oc_od_oe_of_lc_m054.55.55.55.0.2.43.47.0.12.0.61_m15.00D791.2.61.2.2.22.15.0.12.2.61_n0_s01.FF813E.FF813E.30.0.66.0.458.850.1.6.0.70.2.61_og7.55.44.0_oh7.55.44.0_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0"
	s2["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s2)
	
	#lost gloves
	s3 = {}
	s3["blush"] = 0
	s3["lj"] = 0
	s3["clothes"] = "ia_ib_id3.FFDB39.FFDB39.FF813E.0.0.24.27.55.6.27.55.6_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka32.FF813E.FF813E.3_kb21.FF813E.FF813E.FF813E_kc_kd_ke_kf_la31.43.32.3.1_lb_oa_os_ob_oc_od_oe_of_lc_m054.55.55.55.0.2.43.47.0.12.0.61_m15.00D791.2.61.2.2.22.15.0.12.2.61_n0_s01.FF813E.FF813E.30.0.66.0.458.850.1.6.0.70.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s3["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s3)
	
	#lost crown
	s4 = {}
	s4["blush"] = 0
	s4["lj"] = 0
	s4["clothes"] = "ia_ib_id3.FFDB39.FFDB39.FF813E.0.0.24.27.55.6.27.55.6_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka32.FF813E.FF813E.3_kb21.FF813E.FF813E.FF813E_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m054.55.55.55.0.2.43.47.0.12.0.61_m15.00D791.2.61.2.2.22.15.0.12.2.61_n0_s01.FF813E.FF813E.30.0.66.0.458.850.1.6.0.70.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s4["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s4)
	
	#lost dress
	s5 = {}
	s5["blush"] = 1
	s5["lj"] = 0
	s5["clothes"] = "ia_ib_id_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka32.FF813E.FF813E.3_kb21.FF813E.FF813E.FF813E_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s5["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s5)
	
	#lost bra
	s6 = {}
	s6["blush"] = 2
	s6["lj"] = 0
	s6["clothes"] = "ia_ib_id_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb21.FF813E.FF813E.FF813E_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s6["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s6)
	
	#lost panties
	s6 = {}
	s6["blush"] = 3
	s6["lj"] = 0
	s6["clothes"] = "ia_ib_id_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s6["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s6)
	
	#masturbating
	s7 = {}
	s7["blush"] = 6
	s7["lj"] = 50
	s7["clothes"] = "ia_ib_id_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s7["legs"] = "ba50_bb64.1_bc185.200.0.0.1_bd64_be180"
	stages.append(s7)
	
	#masturbating
	s8 = {}
	s8["blush"] = 4
	s8["lj"] = 150
	s8["clothes"] = "ia_ib_id_if_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s8["legs"] = "ba50_bb17.1_bc493.500.8.0.1_bd17_be180"
	stages.append(s8)
	
	d["stages"] = stages
	
	blush = list()
	blush.append(( 0,  9)) # no blush
	blush.append((14,  9)) # lost dress
	blush.append((27,  0)) # lost bra
	blush.append((50,  1)) # lost panties
	blush.append((60, 10)) # finished
	blush.append((70, 12)) # no blush
	blush.append((80, 14)) # masturbating
	#want to leave something for heavy masturbating & orgasm
	d["blush"] = blush
	
	return d
	
def make_descriptions(pd, ems, out_filename):
	#pd = player data
	#ems = emotion data
	
	#get complete vagina description string
	def get_v_str(desc, lj):
		#desc = vagina description string, lj = love juice level
		a, b = desc.split(".", 1)
		return "dc" + ("%d." % lj) + b
	
	#get blush/blue face desciption string
	def get_b_str(blush, blue):
		return "gc%d.%d" % (blush, blue)
	
	#get complete face description string
	def get_face_str(desc, sticker_type):
		a, b = desc.split(".", 1)
		return "dd" + ("%d." % sticker_type) + b
	
	with open(out_filename, "w") as f:
		
		for ind, stage in enumerate(pd["stages"]):
			stage_desc = version_str + pd["appearance"] + "_" + stage["clothes"] + "_" + stage["legs"] + "_" + get_v_str(pd["vagina"], stage["lj"])
			
			if ind == 8:
				#setup scene for masturbation
				f.write("masturbation-setup=33***bc185.200.0.0.1_ga0*0*0*0*0*0*0*0*0#/]ua1.0.0.0_ub_uc7.0.30_ud7.0\n\n")
				
			if ind == 9:
				#reset scene for finished stage
				f.write("finished-setup=33***bc185.500.0.0.1_ga0*0*0*0*0*0*0*0*0#/]ua1.0.0.0_ub_uc7.0.30_ud7.0\n\n")
			
			for em_name, em in ems.iteritems():
				blush_ind = stage["blush"] + em["blush_mod"]
				if blush_ind < 0:
					blush_ind = 0
				if blush_ind >= len(pd["blush"]):
					blush_ind = len(pd["blush"]) - 1
				blush = pd["blush"][blush_ind]
				em_desc = stage_desc + "_" + em["face"] + "_" + em["arms"]
				em_desc += "_" + get_b_str(blush[0], 0)
				em_desc += "_" + get_face_str(pd["face"], blush[1])
				
				image_name = "%d-%s" % (ind, em_name)
				f.write("%s=%s\n\n" % (image_name, em_desc))


def write_descriptions(out_name):
	character_data = get_image_data()
	emotion_data = get_emotion_data()
	make_descriptions(character_data, emotion_data, out_name)
	
if __name__ == "__main__":
	write_descriptions(sys.argv[1])
			