import sys

#emotions:
#happy
#calm
#sad
#loss
#interested
#horny
#shocked
#excited
#annoyed

#clothes = knife, dress, bra, panties
#7 total stages
#is left-handed

#

version_str = "36**"

def get_emotion_data():
	emotions = dict()
	
	#happy
	em = dict()
	em["pose"] = "aa10.99.1.42.51.87.2.1.43.75_ab_ac_ba60_bb5.1_bc185.500.0.9.1_bd5_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.87_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.80.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd00100000_ha96.96_hb50.1.50.100_hc0.59.0.0.59.0_hd25.1.49.49"
	em["blush_mod"] = 0
	emotions["happy"] = em
	
	#calm
	em = dict()
	em["pose"] = "aa6.1.0.41.39.6.1.0.41.39_ab_ac_ba50_bb5.1_bc150.1000.8.10.1_bd5_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.85_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.80.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd00100000_ha73.73_hb50.1.50.100_hc0.61.0.0.61.0_hd0.1.49.49"
	em["blush_mod"] = 0
	emotions["calm"] = em
	
	#sad
	em = dict()
	em["pose"] = "aa5.1.1.41.20.5.1.1.41.20_ab_ac_ba50_bb5.1_bc150.1000.8.10.1_bd5_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.82_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.80.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd00100000_ha68.68_hb50.1.9.100_hc0.61.0.0.61.0_hd8.1.49.49"
	em["blush_mod"] = 0
	emotions["sad"] = em
	
	#loss
	em = dict()
	em["pose"] = "aa14.84.1.42.45.14.84.1.42.45_ab_ac_ba50_bb5.1_bc150.1000.8.10.1_bd5_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.77_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.80.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd00100000_ha87.87_hb50.1.9.100_hc0.68.0.0.68.0_hd38.1.49.49"
	em["blush_mod"] = 0
	emotions["loss"] = em
	
	#interested
	em = dict()
	em["pose"] = "aa28.70.0.42.45.28.70.0.42.45_ab_ac_ba50_bb6.1_bc150.1000.8.10.1_bd6_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.90_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.39.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd00100000_ha85.85_hb50.1.9.100_hc0.40.13.0.40.13_hd1.1.49.49"
	em["blush_mod"] = 1
	emotions["interested"] = em
	
	#horny
	em = dict()
	em["pose"] = "aa7.91.1.28.51.7.91.1.28.51_ab_ac_ba50_bb6.1_bc150.1000.8.10.1_bd6_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.90_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.21.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd00100000_ha85.85_hb50.1.9.100_hc0.11.13.0.11.13_hd27.1.49.49"
	em["blush_mod"] = 2
	emotions["horny"] = em
	
	#shocked
	em = dict()
	em["pose"] = "aa16.90.1.42.45.16.90.1.42.45_ab_ac_ba50_bb4.1_bc150.1000.8.10.1_bd4_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.80_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.80.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd00100000_ha89.89_hb50.1.9.100_hc0.11.0.0.11.0_hd41.1.49.49"
	em["blush_mod"] = 1
	emotions["shocked"] = em
	
	#excited
	em = dict()
	em["pose"] = "aa20.43.1.42.45.20.43.1.42.45_ab_ac_ba50_bb7.1_bc150.1000.8.10.1_bd7_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.95_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.17.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd00100000_ha95.95_hb50.1.9.100_hc0.13.13.0.13.13_hd27.1.49.49"
	em["blush_mod"] = 2
	emotions["excited"] = em
	
	#annoyed
	em = dict()
	em["pose"] = "aa10.93.1.42.45.10.93.1.42.45_ab_ac_ba50_bb5.1_bc150.1000.8.10.1_bd5_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.85_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.10.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.27.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd00100000_ha75.75_hb50.1.9.100_hc0.6.13.0.6.13_hd47.1.49.49"
	em["blush_mod"] = 0
	emotions["annoyed"] = em
	
	return emotions

def get_image_data():
	d = dict()
	
	d["appearance"] = "aa7.0.1.0.35.7.0.1.0.35_ab_ac_ba50_bb5.1_bc185.500.4.15.1_bd5_be180_ca50.0.27.50.40.20.34.40.10_cb0_daECF5FA.0.0.70_db_dd9.0.34.50.50_dhD3DBDF.30.50.50.0_di5_qa_qb_dc0.1.ECF5FA.ECF5FA.ECF5FA_ea32.6E798A.6E798A.8BB4C0.0.0_ec6.30.6E798A.6E798A.8BB4C0_ed5.66.1.1.6E798A.8BB4C0_ef_eg_eh1.6E798A_r0_fa19.50.50.60.50.60.56_fb00_fc0.61.61.0.61.61.50.61.61_fd1.0.50.43.56_fe58.61_ff0000000000_fg2.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc23.0_ge0000000000_gh_gf_gg_gd00100000_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd1.1.49.100_ia_if_ib_id0.A6DEE7.A6DEE7.A6DEE7.0.0.1.1.0.0.1.0.0.19_ic16.55.55.57.0_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	
	#these are separated out because parts of the descriptions change according to blush and love juice levels
	d["vagina"] = "dc0.1.ECF5FA.ECF5FA.ECF5FA" #dc component
	d["face"] = "dd9.0.34.50.50" #dd component
	
	stages = list()
	
	#lj = love juices
	
	#fully clothed
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id0.A6DEE7.A6DEE7.A6DEE7.0.0.1.1.0.0.1.0.0.19_ic16.55.55.57.0_jc_ie_ja_jb_jd_je_jf_jg_ka18.55.9199A6.9FAFC4.0_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s["other"] = ""
	stages.append(s)
	
	#lost knife
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id0.A6DEE7.A6DEE7.A6DEE7.0.0.1.1.0.0.1.0.0.19_ic16.55.55.57.0_jc_ie_ja_jb_jd_je_jf_jg_ka18.55.9199A6.9FAFC4.0_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s["other"] = ""
	stages.append(s)
	
	#lost dress
	s = {}
	s["blush"] = 1
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id_ic16.55.55.57.0_jc_ie_ja_jb_jd_je_jf_jg_ka18.55.9199A6.9FAFC4.0_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s["other"] = ""
	stages.append(s)
	
	#lost bra
	s = {}
	s["blush"] = 2
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id_ic16.55.55.57.0_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s["other"] = ""
	stages.append(s)
	
	#nude
	s = {}
	s["blush"] = 2
	s["lj"] = 20
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s["other"] = ""
	stages.append(s)
	
	#masturbating
	s = {}
	s["blush"] = 4
	s["lj"] = 90
	s["clothes"] = stages[-1]["clothes"]
	s["other"] = ""
	stages.append(s)
	
	#finished
	s = {}
	s["blush"] = 3
	s["lj"] = 150
	s["clothes"] = stages[-1]["clothes"]
	s["other"] = ""
	stages.append(s)
	
	d["stages"] = stages
	
	blush = list()
	blush.append(( 0,  9)) #0 no blush
	blush.append((14,  9)) #1 lost dress
	blush.append((27,  0)) #2 lost bra
	blush.append((50,  1)) #3 nude & finished
	blush.append((60, 10)) #4 masturbating
	blush.append((70, 12)) #5 stage + emotion mod
	blush.append((80, 14)) #6 
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
		
		#need a special scene setup to make Spooky float
		f.write("floating-setup=33***bc185.500.0.10.1_ga0*0*0*0*0*0*0*0*0#/]ua1.0.0.0_ub_uc7.0.30_ud7.0\n\n")
		
		for ind, stage in enumerate(pd["stages"]):
			if ind == len(pd["stages"]) - 2:
				#skip the masturbation stage, all of those are custom images
				#continue
				pass
		
			stage_desc = version_str + stage["clothes"] # + pd["appearance"] + "_"
			if "other" in stage and len(stage["other"]) > 0:
				stage_desc += "_" + stage["other"]
			
			for em_name, em in ems.iteritems():
				blush_ind = stage["blush"] + em["blush_mod"]
				if blush_ind < 0:
					blush_ind = 0
				if blush_ind >= len(pd["blush"]):
					blush_ind = len(pd["blush"]) - 1
				blush = pd["blush"][blush_ind]
				em_desc = stage_desc + "_" + em["pose"]
				em_desc += "_" + get_b_str(blush[0], 0)
				
				#put in the strings that need to be replaced last, so that they don't get overwritten
				em_desc += "_" + get_face_str(pd["face"], blush[1])
				em_desc += "_" + get_v_str(pd["vagina"], stage["lj"])
				
				
				image_name = "%d-%s" % (ind, em_name)
				f.write("%s=%s\n\n" % (image_name, em_desc))


def write_descriptions(out_name):
	character_data = get_image_data()
	emotion_data = get_emotion_data()
	make_descriptions(character_data, emotion_data, out_name)
	
if __name__ == "__main__":
	write_descriptions(sys.argv[1])
			