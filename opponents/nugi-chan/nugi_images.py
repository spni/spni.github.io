import sys

#colours:
#orange FF813E
#yellow FFDB39
#green 00D791
#test yellow FFE73C

#emotions:
#happy
#calm
#sad
#loss
#interested
#horny
#shocked
#awkward

#

#clothes = shoes, gloves, stockings, top, skirt, bra, panties
#9 total stages

#36**aa7.89.1.28.80.7.89.1.28.80_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10100000_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd0.1.49.49_ia_if2.55.55.55.1.0.0.0.0.0.0.0.0.0_ib0.60.55.0.0.0.0.1.29.55.0.29.55.0.1_id12.55.55.44.0.0.1.0.0.0.0.0.0.20_ic29.60.60.55.0_jc_ie_ja9.55.60.55_jb9.55.60.55_jd7.60.50.50_je7.60.50.50_jf_jg_ka4.61.61.61.0_kb4.61.61.61_kc2.41.0.20.0_kd2.41.0.20.0_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of3.8ACAD3.0.0.0_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og3.222222.56.0_oh3.222222.56.0_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0_ad0.0.0.0.0.0.0.0.0.0

version_str = "36**"

def get_emotion_data():
	em = dict()
	happy = dict()
	happy["pose"] = "aa28.43.1.42.47.28.43.1.42.47_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10100000_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd34.1.49.49"
	happy["blush_mod"] = 0
	em["happy"] = happy
	
	calm = dict()
	calm["pose"] = "aa7.91.1.28.51.7.91.1.28.51_ab_ac_ba50_bb5.1_bc188.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10100000_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd0.1.49.49"
	calm["blush_mod"] = 0
	em["calm"] = calm
	
	sad = dict()
	sad["pose"] = "aa6.100.1.16.47.6.100.1.16.47_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd12.1.49.49"
	sad["blush_mod"] = 0
	em["sad"] = sad
	
	loss = dict()
	loss["pose"] = "aa6.100.1.16.47.6.100.1.16.47_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd36.1.49.49"
	loss["blush_mod"] = 0
	em["loss"] = loss
	
	intr = dict()
	intr["pose"] = "aa31.69.0.16.47.31.69.0.16.47_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd17.1.49.49"
	intr["blush_mod"] = 1
	em["interested"] = intr
	
	horny = dict()
	horny["pose"] = "aa9.90.1.16.47.9.90.1.16.47_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.39.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb49.1.44.99_hc0.25.39.0.25.39_hd20.1.49.49"
	horny["blush_mod"] = 2
	em["horny"] = horny
	
	shk = dict()
	shk["pose"] = "aa17.94.1.0.47.17.94.1.0.47_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb49.1.44.99_hc0.97.39.0.97.39_hd40.1.49.49"
	shk["blush_mod"] = 0
	em["shocked"] = shk
	
	awk = dict()
	awk["pose"] = "aa20.76.1.16.27.20.76.1.16.27_ab_ac_ba50_bb5.1_bc188.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc0.5.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh9.E2D4F2_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc14.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb0.1.0.99_hc0.97.39.0.97.39_hd39.1.49.49"	#aa14.48.1.8.64.14.48.1.8.64_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb49.1.44.99_hc0.97.39.0.97.39_hd44.1.49.49
	awk["blush_mod"] = 1
	em["awkward"] = awk
	
	return em

def get_image_data():
	d = dict()
	
	d["appearance"] = "aa13.97.1.28.40.13.97.1.28.40_ab_ac_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.5.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh9.11_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc2.0_ge0000000000_gh_gf_gg_gd10100000_ha89.89_hb49.1.44.99_hc0.59.39.0.59.39_hd0.1.49.49"
	
	d["vagina"] = "dc1.5.1.1.1_eh9.E2D4F2"
	d["face"] = "dd9.0.20.50.50"
	
	stages = list()
	
	#lj = love juices
	#fully clothed
	s0 = {}
	s0["blush"] = 0
	s0["lj"] = 0
	s0["clothes"] = "ia_if2.55.55.55.1.0.0.0.0.0.0.0.0.0_ib0.60.55.0.0.0.0.1.29.55.0.29.55.0.1_id12.55.55.44.0.0.1.0.0.0.0.0.0.20_ic29.60.60.55.0_jc_ie_ja9.55.60.55_jb9.55.60.55_jd7.60.50.50_je7.60.50.50_jf_jg_ka4.61.61.61.0_kb4.61.61.61_kc2.41.0.20.0_kd2.41.0.20.0_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of3.8ACAD3.0.0.0_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og3.222222.56.0_oh3.222222.56.0_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0_ad0.0.0.0.0.0.0.0.0.0"
	s0["other"] = ""
	stages.append(s0)
	
	#lost shoes
	s1 = {}
	s1["blush"] = 0
	s1["lj"] = 0
	s1["clothes"] = "ia_if2.55.55.55.1.0.0.0.0.0.0.0.0.0_ib0.60.55.0.0.0.0.1.29.55.0.29.55.0.1_id12.55.55.44.0.0.1.0.0.0.0.0.0.20_ic29.60.60.55.0_jc_ie_ja9.55.60.55_jb9.55.60.55_jd_je_jf_jg_ka4.61.61.61.0_kb4.61.61.61_kc2.41.0.20.0_kd2.41.0.20.0_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of3.8ACAD3.0.0.0_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og3.222222.56.0_oh3.222222.56.0_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.0_oj0.55.55.0.0_ad0.0.0.0.0.0.0.0.0.0"
	s1["other"] = ""
	stages.append(s1)
	
	#lost gloves
	s2 = {}
	s2["blush"] = 0
	s2["lj"] = 0
	s2["clothes"] = "ia_if2.55.55.55.1.0.0.0.0.0.0.0.0.0_ib0.60.55.0.0.0.0.1.29.55.0.29.55.0.1_id12.55.55.44.0.0.1.0.0.0.0.0.0.20_ic29.60.60.55.0_jc_ie_ja9.55.60.55_jb9.55.60.55_jd_je_jf_jg_ka4.61.61.61.0_kb4.61.61.61_kc2.41.0.20.0_kd2.41.0.20.0_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of3.8ACAD3.0.0.0_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s2["other"] = ""
	stages.append(s2)
	
	#lost stockings
	s3 = {}
	s3["blush"] = 0
	s3["lj"] = 0
	s3["clothes"] = "ia_if2.55.55.55.1.0.0.0.0.0.0.0.0.0_ib0.60.55.0.0.0.0.1.29.55.0.29.55.0.1_id12.55.55.44.0.0.1.0.0.0.0.0.0.20_ic29.60.60.55.0_jc_ie_ja_jb_jd_je_jf_jg_ka4.61.61.61.0_kb4.61.61.61_kc2.41.0.20.0_kd2.41.0.20.0_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of3.8ACAD3.0.0.0_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s3["other"] = ""
	stages.append(s3)
	
	#lost top
	s4 = {}
	s4["blush"] = 1
	s4["lj"] = 0
	s4["clothes"] = "ia_if_ib_id_ic29.60.60.55.0_jc_ie_ja_jb_jd_je_jf_jg_ka4.61.61.61.0_kb4.61.61.61_kc2.41.0.20.0_kd2.41.0.20.0_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s4["other"] = ""
	stages.append(s4)
	
	#lost skirt
	s5 = {}
	s5["blush"] = 1
	s5["lj"] = 0
	s5["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka4.61.61.61.0_kb4.61.61.61_kc2.41.0.20.0_kd2.41.0.20.0_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s5["other"] = ""
	stages.append(s5)
	
	#lost bra
	s6 = {}
	s6["blush"] = 2
	s6["lj"] = 0
	s6["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb4.61.61.61_kc_kd_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s6["other"] = ""
	stages.append(s6)
	
	#lost panties/nude
	s6 = {}
	s6["blush"] = 3
	s6["lj"] = 0
	s6["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s6["other"] = ""
	stages.append(s6)
	
	#masturbating
	s7 = {}
	s7["blush"] = 6
	s7["lj"] = 50
	s7["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s7["other"] = ""
	stages.append(s7)
	
	#finished
	s8 = {}
	s8["blush"] = 4
	s8["lj"] = 150
	s8["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la4.55.55.0.1_lb_oa_os_ob_oc_od_oe_of_lc_m04.60.3.0.0.1.40.15.66.70.2.61_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_ad0.0.0.0.0.0.0.0.0.0"
	s8["other"] = ""
	stages.append(s8)
	
	d["stages"] = stages
	
	blush = list()
	blush.append(( 0,  9)) # no blush
	blush.append((14,  9)) # lost top
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
		
		#write unique setup string - you need to zoom out a bit so that all of her hair fits in
		f.write("nugi-setup=33***bc188.500.0.0.1_ga0*0*0*0*0*0*0*0*0#/]ua1.0.0.0_ub_uc6.0.12_ud7.0\n\n")
		
		for ind, stage in enumerate(pd["stages"]):
			if ind == len(pd["stages"]) - 2:
				#skip the masturbation stage, all of those are custom images
				continue
		
			stage_desc = version_str + pd["appearance"] + "_" + stage["clothes"]
			if "other" in stage and len(stage["other"]) > 0:
				stage_desc += "_" + stage["other"]
			
			#if ind == 8:
				#setup scene for masturbation
				#f.write("masturbation-setup=33***bc185.200.0.0.1_ga0*0*0*0*0*0*0*0*0#/]ua1.0.0.0_ub_uc7.0.30_ud7.0\n\n")
				
			#if ind == 9:
				#reset scene for finished stage
				#f.write("finished-setup=33***bc185.500.0.0.1_ga0*0*0*0*0*0*0*0*0#/]ua1.0.0.0_ub_uc7.0.30_ud7.0\n\n")
			
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
			