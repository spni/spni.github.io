import sys

#emotions:
#happy
#calm
#sad
#loss
#interested - clasping hands together?
#horny
#shocked - maybe hands in front of face, with a gap in between her fingers to see through?
#excited
#stunned - eyes closed, I think.
#angry

#clothes = shoes, socks, jumper, tie, skirt, shirt, bra, panties
#11 total stages

#appearance:36**aa12.42.0.42.54.12.42.0.4.70_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.65.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha75.75_hb49.1.44.99_hc0.59.39.0.59.39_hd1.1.49.49_ia_if0.59.59.0.1.5.0.0.5.0.0.0.0.3_ib0.55.55.0.0.0.0.1.5.0.0.5.0.0.2_id_ic34.60.60.18191E.0_jc_ie_ja9.2C2E31.070809.55_jb9.2C2E31.070809.55_jd7.60.50.50_je7.60.50.50_jf_jg_ka6.55.55.E8E8E8.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of4.6.44.6.0_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0

version_str = "36**"

def get_emotion_data():
	emotions = dict()
	
	#happy
	em = dict()
	em["pose"] = "aa12.42.0.42.54.12.42.0.4.70_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.65.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha75.75_hb49.1.44.99_hc0.59.39.0.59.39_hd1.1.49.49"
	em["blush_mod"] = 0
	emotions["happy"] = em
	
	#calm
	em = dict()
	em["pose"] = "aa11.98.0.42.54.11.98.0.4.70_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.65.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha70.70_hb49.1.44.99_hc0.65.39.0.65.39_hd0.1.49.49"
	em["blush_mod"] = 0
	emotions["calm"] = em
	
	#sad
	em = dict()
	em["pose"] = "aa13.97.0.42.54.13.97.0.4.70_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa3.50.50.60.50.74.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha59.59_hb49.1.20.99_hc0.61.39.0.61.39_hd8.1.49.49"
	em["blush_mod"] = 0
	emotions["sad"] = em
	
	#loss
	em = dict()
	em["pose"] = "aa11.89.1.42.54.11.89.1.4.70_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.86.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha61.61_hb49.1.3.99_hc0.65.39.0.65.39_hd21.1.49.49"
	em["blush_mod"] = 0
	emotions["loss"] = em
	
	#interested
	em = dict()
	em["pose"] = "aa26.63.0.16.58.24.63.1.0.64_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa5.50.50.60.50.0.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha84.84_hb49.1.44.99_hc0.39.39.0.39.39_hd1.1.49.49"
	em["blush_mod"] = 1
	emotions["interested"] = em
	
	#horny
	em = dict()
	em["pose"] = "aa10.58.0.42.75.10.58.0.4.75_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.65.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha87.87_hb49.1.44.99_hc0.59.39.0.59.39_hd27.1.49.49"
	em["blush_mod"] = 2
	emotions["horny"] = em
	
	#shocked
	em = dict()
	em["pose"] = "aa65.38.1.27.41.75.36.1.4.60_ab_ac2.52.52.52_ba50_bb17.1_bc185.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.79.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha88.88_hb49.1.44.99_hc0.59.39.0.59.39_hd41.1.49.49"
	em["blush_mod"] = 1
	emotions["shocked"] = em
	
	#excited
	em = dict()
	em["pose"] = "aa7.44.0.43.54.7.44.0.6.43_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.99.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha96.96_hb49.1.44.99_hc0.41.39.0.41.39_hd34.1.49.49"
	em["blush_mod"] = 2
	emotions["excited"] = em
	
	#stunned
	em = dict()
	em["pose"] = "aa8.100.1.0.54.8.100.1.6.30_ab_ac2.52.52.52_ba50_bb17.1_bc185.500.8.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.59.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha73.73_hb49.1.44.45_hc0.0.39.0.0.39_hd40.1.49.49"
	em["blush_mod"] = 1
	emotions["stunned"] = em
	
	#angry
	em = dict()
	em["pose"] = "aa22.83.1.16.42.22.83.1.4.52_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa6.50.50.60.50.31.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha77.77_hb49.1.44.99_hc0.0.39.0.0.39_hd38.1.49.49"
	em["blush_mod"] = 0
	emotions["angry"] = em
	
	#smug
	em = dict()
	em["pose"] = "aa20.72.0.42.49.20.72.0.4.49_ab_ac2.52.52.52_ba50_bb18.1_bc150.500.0.0.1_bd18_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd9.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc0.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.38.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha63.63_hb49.1.44.99_hc0.35.39.0.35.39_hd2.1.49.49"
	em["blush_mod"] = 0
	emotions["smug"] = em
	
	return emotions

def get_image_data():
	d = dict()
	
	d["appearance"] = "36**aa12.42.0.42.54.12.42.0.4.70_ab_ac2.52.52.52_ba50_bb17.1_bc150.500.0.0.1_bd17_be180_ca61.0.40.61.14.8.34.0.9_cb0_da1.0.0.100_db_dd0.0.34.50.45_dh1.30.50.50.0_di4_qa_qb_dc40.1.1.1.1_ea26.A27241.A27241.56.0.0_ec10.0.A27241.A27241.56_ed28.50.1.1.A27241.56_ef_eg_eh4.A27241_r0_fa2.50.50.60.50.65.56_fb10_fc0.9.55.0.9.55.50.61.61_fd1.0.19.A27241.56_fe58.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha75.75_hb49.1.44.99_hc0.59.39.0.59.39_hd1.1.49.49_ia_if0.59.59.0.1.5.0.0.5.0.0.0.0.3_ib0.55.55.0.0.0.0.1.5.0.0.5.0.0.2_id_ic34.60.60.18191E.0_jc_ie_ja9.2C2E31.070809.55_jb9.2C2E31.070809.55_jd7.60.50.50_je7.60.50.50_jf_jg_ka6.55.55.E8E8E8.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of4.6.44.6.0_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	
	#these are separated out because parts of the descriptions change according to blush and love juice levels
	d["vagina"] = "dc40.1.1.1.1" #dc component
	d["face"] = "dd0.0.34.50.45" #dd component
	
	stages = list()
	
	#lj = love juices
	
	#fully clothed
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if0.59.59.0.1.5.0.0.5.0.0.0.0.3_ib0.55.55.0.0.0.0.1.5.0.0.5.0.0.2_id_ic34.60.60.18191E.0_jc_ie_ja9.2C2E31.070809.55_jb9.2C2E31.070809.55_jd7.60.50.50_je7.60.50.50_jf_jg_ka6.55.55.B71740.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of4.6.44.6.0_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost shoes
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if0.59.59.0.1.5.0.0.5.0.0.0.0.3_ib0.55.55.0.0.0.0.1.5.0.0.5.0.0.2_id_ic34.60.60.18191E.0_jc_ie_ja9.2C2E31.070809.55_jb9.2C2E31.070809.55_jd_je_jf_jg_ka6.55.55.B71740.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of4.6.44.6.0_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost socks
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if0.59.59.0.1.5.0.0.5.0.0.0.0.3_ib0.55.55.0.0.0.0.1.5.0.0.5.0.0.2_id_ic34.60.60.18191E.0_jc_ie_ja_jb_jd_je_jf_jg_ka6.55.55.B71740.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of4.6.44.6.0_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost jumper
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib0.55.55.0.0.0.0.1.5.0.0.5.0.0.2_id_ic34.60.60.18191E.0_jc_ie_ja_jb_jd_je_jf_jg_ka6.55.55.B71740.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of4.6.44.6.0_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost tie
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib0.55.55.0.0.0.0.1.5.0.0.5.0.0.2_id_ic34.60.60.18191E.0_jc_ie_ja_jb_jd_je_jf_jg_ka6.55.55.B71740.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost skirt
	s = {}
	s["blush"] = 1
	s["lj"] = 0
	s["clothes"] = "ia_if_ib0.55.55.0.0.0.0.1.5.0.0.5.0.0.2_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka6.55.55.B71740.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost blouse
	s = {}
	s["blush"] = 1
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka6.55.55.B71740.0_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost bra
	s = {}
	s["blush"] = 2
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb6.55.55.B71740_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost panties/nude
	s = {}
	s["blush"] = 2
	s["lj"] = 5
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s["other"] = ""
	stages.append(s)
	
	#masturbating
	s = {}
	s["blush"] = 4
	s["lj"] = 80
	s["clothes"] = stages[-1]["clothes"]
	s["other"] = ""
	stages.append(s)
	
	#finished
	s = {}
	s["blush"] = 3
	s["lj"] = 140
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
				
				
				image_name = "%d-%s" % (ind, em_name)
				f.write("%s=%s\n\n" % (image_name, em_desc))


def write_descriptions(out_name):
	character_data = get_image_data()
	emotion_data = get_emotion_data()
	make_descriptions(character_data, emotion_data, out_name)
	
if __name__ == "__main__":
	write_descriptions(sys.argv[1])
			