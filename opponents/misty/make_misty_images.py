import sys
import string

#emotions:
#happy
#calm
#sad
#loss
#interested
#horny
#angry
#shocked
#awkward - nervous?
#embarrassed - angry embarrassed

#clothes = shoes, shorts, top, hair band, bra, panties
#9 total stages

#appearance:36**aa85.0.0.43.53.85.0.0.43.53_ab_ac_ba50_bb2.0_bc150.500.0.0.1_bd27_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.77.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha77.77_hb49.1.50.55_hc0.52.30.0.52.30_hd1.1.49.49_ia_if2.EEE685.EEE685.42.1.0.0.0.0.0.0.0.0.1_ib_id_ic_jc_ie0.56.56.0.17.41A9B8.BEE2E7.0.17.41A9B8.BEE2E7.0.0_ja14.55.2.0_jb14.55.2.0_jd13.30.6.30_je13.30.6.30_jf_jg_ka10.19.42.42.0_kb10.19.42.42_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s02.6.6.45.0.73.90.390.631.2.10.0.50.2.61_s12.6.6.45.0.73.90.609.631.2.10.0.50.2.61_s22.6.6.43.0.50.90.390.513.2.7.0.50.2.61_s32.6.6.43.0.50.90.610.512.2.7.0.50.2.61_s42.6.6.19.0.61.100.682.889.2.7.1.7.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0

version_str = "36**"

def get_emotion_data():
	emotions = dict()
	
	#happy
	em = dict()
	em["pose"] = "aa85.0.0.43.53.85.0.0.43.53_ab_ac_ba50_bb2.0_bc150.500.0.0.1_bd27_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.77.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha88.88_hb49.1.50.55_hc0.52.30.0.52.30_hd24.1.49.49"
	em["blush_mod"] = 0
	emotions["happy"] = em
	
	#calm
	em = dict()
	em["pose"] = "aa35.76.0.42.36.35.76.0.42.36_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.77.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha69.69_hb49.1.50.55_hc0.52.30.0.52.30_hd0.1.49.49"
	em["blush_mod"] = 0
	emotions["calm"] = em
	
	#sad
	em = dict()
	em["pose"] = "aa14.92.0.42.36.14.92.0.42.36_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.77.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha58.58_hb49.1.30.55_hc0.52.0.0.52.0_hd5.1.49.49"
	em["blush_mod"] = 0
	emotions["sad"] = em
	
	#loss
	em = dict()
	em["pose"] = "aa5.98.0.42.36.5.98.0.42.36_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.77.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha67.67_hb49.1.40.55_hc0.52.0.0.52.0_hd38.1.49.49"
	em["blush_mod"] = 0
	emotions["loss"] = em
	
	#interested
	em = dict()
	em["pose"] = "aa14.73.0.42.36.14.73.0.42.36_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.77.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha61.61_hb49.1.50.70_hc0.52.30.0.52.30_hd34.1.49.49"
	em["blush_mod"] = 1
	emotions["interested"] = em
	
	#horny
	em = dict()
	em["pose"] = "aa18.43.0.42.56.18.43.0.42.56_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.36.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha75.75_hb49.1.50.80_hc0.18.30.0.18.30_hd25.1.49.49"
	em["blush_mod"] = 2
	emotions["horny"] = em
	
	#angry
	em = dict()
	em["pose"] = "aa15.44.1.42.49.8.96.1.42.39_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.27.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha63.63_hb49.1.50.66_hc0.0.7.0.0.7_hd48.1.49.49"
	em["blush_mod"] = 1
	emotions["angry"] = em
	
	#shocked
	em = dict()
	em["pose"] = "aa10.0.1.47.52.10.0.1.47.52_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.77.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha85.85_hb49.1.50.37_hc0.52.30.0.52.30_hd41.1.49.49"
	em["blush_mod"] = 2
	emotions["shocked"] = em
	
	#awkward
	em = dict()
	em["pose"] = "aa10.91.1.42.36.10.91.1.42.36_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.87.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha60.60_hb0.1.20.36_hc0.66.13.0.66.13_hd39.1.49.49"
	em["blush_mod"] = 1
	emotions["awkward"] = em
	
	#embarrassed
	em = dict()
	em["pose"] = "aa67.40.1.26.36.67.40.1.26.36_ab_ac_ba50_bb17.0_bc150.500.0.0.1_bd17_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.40.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha90.90_hb49.1.50.90_hc0.0.30.0.0.30_hd40.1.49.49"
	em["blush_mod"] = 2
	emotions["embarrassed"] = em
	
	return emotions

def get_image_data():
	d = dict()
	
	d["appearance"] = "36**aa85.0.0.43.53.85.0.0.43.53_ab_ac_ba50_bb2.0_bc150.500.0.0.1_bd27_be180_ca64.0.38.64.30.15.23.35.7_cb0_da1.0.0.100_db0.2_dd9.3.20.50.45_dh1.32.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0_fa2.50.60.60.50.77.56_fb10_fc3.34.55.3.34.55.50.61.61_fd2.0.27.32.56_fe50.64_ff0000000000_fg2.55_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10100000_ha77.77_hb49.1.50.55_hc0.52.30.0.52.30_hd1.1.49.49_ia_if2.EEE685.EEE685.42.1.0.0.0.0.0.0.0.0.1_ib_id_ic_jc_ie0.56.56.0.17.41A9B8.BEE2E7.0.17.41A9B8.BEE2E7.0.0_ja14.55.2.0_jb14.55.2.0_jd13.30.6.30_je13.30.6.30_jf_jg_ka10.19.42.42.0_kb10.19.42.42_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s02.6.6.45.0.73.90.390.631.2.10.0.50.2.61_s12.6.6.45.0.73.90.609.631.2.10.0.50.2.61_s22.6.6.43.0.50.90.390.513.2.7.0.50.2.61_s32.6.6.43.0.50.90.610.512.2.7.0.50.2.61_s42.6.6.19.0.61.100.682.889.2.7.1.7.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	
	#these are separated out because parts of the descriptions change according to blush and love juice levels
	d["vagina"] = "dc0.1.1.1.1" #dc component
	d["face"] = "dd9.3.20.50.45" #dd component
	
	stages = list()
	
	#lj = love juices
	
	#fully clothed - 0
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if2.EEE685.EEE685.42.1.0.0.0.0.0.0.0.0.1_ib_id_ic_jc_ie0.56.56.0.17.41A9B8.BEE2E7.0.17.41A9B8.BEE2E7.0.0_ja14.55.2.0_jb14.55.2.0_jd13.30.6.30_je13.30.6.30_jf_jg_ka10.19.42.42.0_kb10.19.42.42_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s02.6.6.45.0.73.90.390.631.2.10.0.50.2.61_s12.6.6.45.0.73.90.609.631.2.10.0.50.2.61_s22.6.6.43.0.50.90.390.513.2.7.0.50.2.61_s32.6.6.43.0.50.90.610.512.2.7.0.50.2.61_s42.6.6.19.0.61.100.682.889.2.7.1.7.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost shoes - 1
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if2.EEE685.EEE685.42.1.0.0.0.0.0.0.0.0.1_ib_id_ic_jc_ie0.56.56.0.17.41A9B8.BEE2E7.0.17.41A9B8.BEE2E7.0.0_ja_jb_jd_je_jf_jg_ka10.19.55.B71740.0_kb10.19.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s02.6.6.45.0.73.90.390.631.2.10.0.50.2.61_s12.6.6.45.0.73.90.609.631.2.10.0.50.2.61_s22.6.6.43.0.50.90.390.513.2.7.0.50.2.61_s32.6.6.43.0.50.90.610.512.2.7.0.50.2.61_s42.6.6.19.0.61.100.682.889.2.7.1.7.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost shorts - 2
	s = {}
	s["blush"] = 0
	s["lj"] = 1
	s["clothes"] = "ia_if2.EEE685.EEE685.42.1.0.0.0.0.0.0.0.0.1_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka10.19.55.B71740.0_kb10.19.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s42.6.6.19.0.61.100.682.889.2.7.1.7.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost top - 3
	s = {}
	s["blush"] = 0
	s["lj"] = 1
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka10.19.55.B71740.0_kb10.19.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s42.6.6.19.0.61.100.682.889.2.7.1.7.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost hair band - 4
	s = {}
	s["blush"] = 0
	s["lj"] = 1
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka10.19.55.B71740.0_kb10.19.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost bra - 5
	s = {}
	s["blush"] = 1
	s["lj"] = 2
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb10.19.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost panties/nude - 6
	s = {}
	s["blush"] = 1
	s["lj"] = 2
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#masturbating - 7
	s = {}
	s["blush"] = 4
	s["lj"] = 80
	s["clothes"] = stages[-1]["clothes"]
	s["other"] = ""
	stages.append(s)
	
	#finished - 8
	s = {}
	s["blush"] = 3
	s["lj"] = 180
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
		
		#put special setup code here
		
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
				
				#misty's hair without her hair band
				if ind >= 4:
					#em_desc += "_" + "ea6.32.32.56.0.0_ec19.28.32.32.56_ed0.23.0.1.32.56_ef_eg_eh1.32_r0"
					em_desc = string.replace(em_desc, "ea6.32.32.56.0.0_ec_ed0.23.0.1.32.56_ef_eg_eh1.32_r045.32.32.56.1.0.51.51.45.617.548.0", "ea6.32.32.56.0.0_ec19.28.32.32.56_ed0.23.0.1.32.56_ef_eg_eh1.32_r0")
				
				image_name = "%d-%s" % (ind, em_name)
				f.write("%s=%s\n\n" % (image_name, em_desc))


def write_descriptions(out_name):
	character_data = get_image_data()
	emotion_data = get_emotion_data()
	make_descriptions(character_data, emotion_data, out_name)
	
if __name__ == "__main__":
	write_descriptions(sys.argv[1])
			