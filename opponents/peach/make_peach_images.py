import sys

#emotions:
#happy
#calm
#sad
#interested
#horny
#shocked

#clothes = shoes, earrings, gloves, crown, dress, pants, bra, panties
#11 total stages

#36**aa7.92.1.28.52.7.92.1.28.52_ab_ac_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca64.0.30.64.35.34.34.0.0_cb0_da1.0.0.100_db_dd9.3.30.50.50_dh2.30.50.50.2_di7_qa_qb_dc1.1.1.1.1_ea8.FFE214.FFE214.56.0.0_ec16.100.FFE214.FFE214.56_ed22.55.0.1.FFE214.56_ef3.2.0.FFE214.FFE214.56_eg3.2.0.FFE214.FFE214.56_eh8.FFE214_r019.FFE214.FFE214.56.0.2.63.51.104.579.538.0_r23.FFE214.FFE214.FFE214.2.2.0.0.109.474.625.0_r317.FFE214.FFE214.56.0.2.47.10.88.488.615.0_r42.FFE214.FFE214.FFE214.2.2.100.100.192.527.613.0_r53.FFE214.FFE214.FFE214.0.2.4.0.62.495.561.0_r619.FFE214.FFE214.56.0.2.100.59.102.562.593.0_r742.FFE214.FFE214.56.0.2.34.37.86.541.595.0_r819.FFE214.56.56.0.2.100.100.100.582.550.0_r919.FFE214.56.56.0.2.50.50.86.588.580.0_fa12.50.50.50.50.65.56_fb00_fc1.9ED4FF.55.1.9ED4FF.55.50.61.61_fd0.0.16.FFE214.56_fe50.61_ff0000000000_fg1.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha88.88_hb49.1.44.90_hc0.59.39.0.59.39_hd0.1.49.49_ia_if_ib_id4.FFACCB.FFACCB.44.0.0.1.4.0.0.4.0.0.2_ic35.FFACCB.FFACCB.FE69A1.1_jc_ie4.56.56.0.13.FFACCB.FFACCB.0.13.FFACCB.FFACCB.0.1_ja_jb_jd8.D62929.50.50_je8.D62929.50.50_jf_jg_ka6.FE69A1.FFACCB.2.0_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la31.43.FE1414.59C1FF.1_lb_oa_os_ob_oc_od_oe_of_lc_m05.F9C971.3.0.1.2.63.15.0.13.2.61_m15.59C1FF.3.0.1.2.42.15.0.13.2.61_m25.59C1FF.3.0.0.1.16.15.52.41.2.61_n0_s312.FE69A1.FE69A1.56.0.65.0.500.839.1.6.0.45.2.61_s512.2.2.56.1.58.0.500.748.2.9.1.49.2.61_s71.FE69A1.FE69A1.30.0.100.0.444.874.1.6.0.100.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.3_oj0.55.55.0.3_ad0.0.0.0.0.0.0.0.0.0

version_str = "36**"

def get_emotion_data():
	emotions = dict()
	
	#happy
	em = dict()
	em["pose"] = "aa19.61.0.8.6.19.61.1.8.6_ab_ac_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca64.0.30.64.35.34.34.0.0_cb0_da1.0.0.100_db_dd9.3.30.50.50_dh2.30.50.50.2_di7_qa_qb_dc1.1.1.1.1_ea8.FFE214.FFE214.56.0.0_ec16.100.FFE214.FFE214.56_ed22.55.0.1.FFE214.56_ef3.2.0.FFE214.FFE214.56_eg3.2.0.FFE214.FFE214.56_eh8.FFE214_r019.FFE214.FFE214.56.0.2.63.51.104.579.538.0_r23.FFE214.FFE214.FFE214.2.2.0.0.109.474.625.0_r317.FFE214.FFE214.56.0.2.47.10.88.488.615.0_r42.FFE214.FFE214.FFE214.2.2.100.100.192.527.613.0_r53.FFE214.FFE214.FFE214.0.2.4.0.62.495.561.0_r619.FFE214.FFE214.56.0.2.100.59.102.562.593.0_r742.FFE214.FFE214.56.0.2.34.37.86.541.595.0_r819.FFE214.56.56.0.2.100.100.100.582.550.0_r919.FFE214.56.56.0.2.50.50.86.588.580.0_fa12.50.50.50.50.65.56_fb00_fc1.9ED4FF.55.1.9ED4FF.55.50.61.61_fd0.0.16.FFE214.56_fe50.61_ff0000000000_fg1.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha6.6_hb49.1.50.90_hc0.59.39.0.59.39_hd23.1.49.49"
	em["blush_mod"] = 0
	emotions["happy"] = em
	
	#calm
	em = dict()
	em["pose"] = "aa7.92.1.28.52.7.92.1.28.52_ab_ac_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca64.0.30.64.35.34.34.0.0_cb0_da1.0.0.100_db_dd9.3.30.50.50_dh2.30.50.50.2_di7_qa_qb_dc1.1.1.1.1_ea8.FFE214.FFE214.56.0.0_ec16.100.FFE214.FFE214.56_ed22.55.0.1.FFE214.56_ef3.2.0.FFE214.FFE214.56_eg3.2.0.FFE214.FFE214.56_eh8.FFE214_r019.FFE214.FFE214.56.0.2.63.51.104.579.538.0_r23.FFE214.FFE214.FFE214.2.2.0.0.109.474.625.0_r317.FFE214.FFE214.56.0.2.47.10.88.488.615.0_r42.FFE214.FFE214.FFE214.2.2.100.100.192.527.613.0_r53.FFE214.FFE214.FFE214.0.2.4.0.62.495.561.0_r619.FFE214.FFE214.56.0.2.100.59.102.562.593.0_r742.FFE214.FFE214.56.0.2.34.37.86.541.595.0_r819.FFE214.56.56.0.2.100.100.100.582.550.0_r919.FFE214.56.56.0.2.50.50.86.588.580.0_fa12.50.50.50.50.65.56_fb00_fc1.9ED4FF.55.1.9ED4FF.55.50.61.61_fd0.0.16.FFE214.56_fe50.61_ff0000000000_fg1.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha88.88_hb49.1.44.90_hc0.59.39.0.59.39_hd0.1.49.49"
	em["blush_mod"] = 0
	emotions["calm"] = em
	
	#sad
	em = dict()
	em["pose"] = "aa7.98.1.28.52.7.98.1.28.52_ab_ac_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca64.0.30.64.35.34.34.0.0_cb0_da1.0.0.100_db_dd9.3.30.50.50_dh2.30.50.50.2_di7_qa_qb_dc1.1.1.1.1_ea8.FFE214.FFE214.56.0.0_ec16.100.FFE214.FFE214.56_ed22.55.0.1.FFE214.56_ef3.2.0.FFE214.FFE214.56_eg3.2.0.FFE214.FFE214.56_eh8.FFE214_r019.FFE214.FFE214.56.0.2.63.51.104.579.538.0_r23.FFE214.FFE214.FFE214.2.2.0.0.109.474.625.0_r317.FFE214.FFE214.56.0.2.47.10.88.488.615.0_r42.FFE214.FFE214.FFE214.2.2.100.100.192.527.613.0_r53.FFE214.FFE214.FFE214.0.2.4.0.62.495.561.0_r619.FFE214.FFE214.56.0.2.100.59.102.562.593.0_r742.FFE214.FFE214.56.0.2.34.37.86.541.595.0_r819.FFE214.56.56.0.2.100.100.100.582.550.0_r919.FFE214.56.56.0.2.50.50.86.588.580.0_fa12.50.50.50.50.65.56_fb00_fc1.9ED4FF.55.1.9ED4FF.55.50.61.61_fd0.0.16.FFE214.56_fe50.61_ff0000000000_fg1.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha79.79_hb49.1.29.90_hc0.59.39.0.59.39_hd5.1.49.49"
	em["blush_mod"] = 0
	emotions["sad"] = em
	
	#interested
	em = dict()
	em["pose"] = "aa8.73.1.47.31.8.73.1.47.31_ab_ac_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca64.0.30.64.35.34.34.0.0_cb0_da1.0.0.100_db_dd9.3.30.50.50_dh2.30.50.50.2_di7_qa_qb_dc1.1.1.1.1_ea8.FFE214.FFE214.56.0.0_ec16.100.FFE214.FFE214.56_ed22.55.0.1.FFE214.56_ef3.2.0.FFE214.FFE214.56_eg3.2.0.FFE214.FFE214.56_eh8.FFE214_r019.FFE214.FFE214.56.0.2.63.51.104.579.538.0_r23.FFE214.FFE214.FFE214.2.2.0.0.109.474.625.0_r317.FFE214.FFE214.56.0.2.47.10.88.488.615.0_r42.FFE214.FFE214.FFE214.2.2.100.100.192.527.613.0_r53.FFE214.FFE214.FFE214.0.2.4.0.62.495.561.0_r619.FFE214.FFE214.56.0.2.100.59.102.562.593.0_r742.FFE214.FFE214.56.0.2.34.37.86.541.595.0_r819.FFE214.56.56.0.2.100.100.100.582.550.0_r919.FFE214.56.56.0.2.50.50.86.588.580.0_fa12.50.50.50.50.65.56_fb00_fc1.9ED4FF.55.1.9ED4FF.55.50.61.61_fd0.0.16.FFE214.56_fe50.61_ff0000000000_fg1.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha96.96_hb49.1.44.90_hc0.60.39.0.60.39_hd17.1.49.49"
	em["blush_mod"] = 1
	emotions["interested"] = em
	
	#horny
	em = dict()
	em["pose"] = "aa20.80.0.28.52.20.80.0.28.52_ab_ac_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca64.0.30.64.35.34.34.0.0_cb0_da1.0.0.100_db_dd9.3.30.50.50_dh2.30.50.50.2_di7_qa_qb_dc1.1.1.1.1_ea8.FFE214.FFE214.56.0.0_ec16.100.FFE214.FFE214.56_ed22.55.0.1.FFE214.56_ef3.2.0.FFE214.FFE214.56_eg3.2.0.FFE214.FFE214.56_eh8.FFE214_r019.FFE214.FFE214.56.0.2.63.51.104.579.538.0_r23.FFE214.FFE214.FFE214.2.2.0.0.109.474.625.0_r317.FFE214.FFE214.56.0.2.47.10.88.488.615.0_r42.FFE214.FFE214.FFE214.2.2.100.100.192.527.613.0_r53.FFE214.FFE214.FFE214.0.2.4.0.62.495.561.0_r619.FFE214.FFE214.56.0.2.100.59.102.562.593.0_r742.FFE214.FFE214.56.0.2.34.37.86.541.595.0_r819.FFE214.56.56.0.2.100.100.100.582.550.0_r919.FFE214.56.56.0.2.50.50.86.588.580.0_fa12.50.50.50.50.65.56_fb00_fc1.9ED4FF.55.1.9ED4FF.55.50.61.61_fd0.0.16.FFE214.56_fe50.61_ff0000000000_fg1.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha100.100_hb49.1.44.90_hc0.60.39.0.60.39_hd35.1.49.49"
	em["blush_mod"] = 2
	emotions["horny"] = em
	
	#shocked
	em = dict()
	em["pose"] = "aa16.72.1.47.29.16.72.1.47.29_ab_ac_ba50_bb17.1_bc150.500.8.0.1_bd17_be180_ca64.0.30.64.35.34.34.0.0_cb0_da1.0.0.100_db_dd9.3.30.50.50_dh2.30.50.50.2_di7_qa_qb_dc1.1.1.1.1_ea8.FFE214.FFE214.56.0.0_ec16.100.FFE214.FFE214.56_ed22.55.0.1.FFE214.56_ef3.2.0.FFE214.FFE214.56_eg3.2.0.FFE214.FFE214.56_eh8.FFE214_r019.FFE214.FFE214.56.0.2.63.51.104.579.538.0_r23.FFE214.FFE214.FFE214.2.2.0.0.109.474.625.0_r317.FFE214.FFE214.56.0.2.47.10.88.488.615.0_r42.FFE214.FFE214.FFE214.2.2.100.100.192.527.613.0_r53.FFE214.FFE214.FFE214.0.2.4.0.62.495.561.0_r619.FFE214.FFE214.56.0.2.100.59.102.562.593.0_r742.FFE214.FFE214.56.0.2.34.37.86.541.595.0_r819.FFE214.56.56.0.2.100.100.100.582.550.0_r919.FFE214.56.56.0.2.50.50.86.588.580.0_fa12.50.50.50.50.65.56_fb00_fc1.9ED4FF.55.1.9ED4FF.55.50.61.61_fd0.0.16.FFE214.56_fe50.61_ff0000000000_fg1.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb0_gc0.0_ge0000000000_gh_gf_gg_gd10000000_ha100.100_hb49.1.44.90_hc0.47.39.0.47.39_hd39.1.49.49"
	em["blush_mod"] = 0
	emotions["shocked"] = em
	
	#awkward
	#em = dict()
	#em["pose"] = "aa20.76.1.16.27.20.76.1.16.27_ab_ac_ba50_bb5.1_bc188.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc0.5.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh9.E2D4F2_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc14.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb0.1.0.99_hc0.97.39.0.97.39_hd39.1.49.49"	#aa14.48.1.8.64.14.48.1.8.64_ab_ac_ba50_bb5.1_bc150.500.0.0.1_bd5_be180_ca55.0.32.55.34.35.34.0.0_cb0_da1.0.0.100_db_dd9.0.20.50.50_dh1.30.50.50.4_di8_qa_qb_dc1.1.1.1.1_ea32.EAD9EE.EAD9EE.56.0.0_ec_ed2.44.1.1.EAD9EE.56_ef1.2.0.EAD9EE.EAD9EE.56_eg1.2.0.EAD9EE.EAD9EE.56_eh_r061.EAD9EE.EAD9EE.56.0.0.100.100.10.692.536.1_fa24.50.50.50.50.65.56_fb11_fc1.35A0AA.55.1.35A0AA.55.55.103134.103134_fd16.0.26.EAD9EE.56_fe50.61_ff0000000000_fg0.50_t0_pa0.0.0.0.40.50.85.85.0.0_pb_pc_pd_pe_ga0_gb1_gc1.0_ge0000000000_gh_gf_gg_gd10000000_ha89.89_hb49.1.44.99_hc0.97.39.0.97.39_hd44.1.49.49
	#em["blush_mod"] = 1
	#emotions["awkward"] = em
	
	return emotions

def get_image_data():
	d = dict()
	
	d["appearance"] = ""
	
	#these are separated out because parts of the descriptions change according to blush and love juice levels
	d["vagina"] = "dc1.1.1.1.1_eh8.FFE214"
	d["face"] = "dd9.3.30.50.50"
	
	stages = list()
	
	#lj = love juices
	#fully clothed
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id4.FFACCB.FFACCB.44.0.0.1.4.0.0.4.0.0.2_ic35.FFACCB.FFACCB.FE69A1.1_jc_ie4.56.56.0.13.FFACCB.FFACCB.0.13.FFACCB.FFACCB.0.1_ja_jb_jd8.D62929.50.50_je8.D62929.50.50_jf_jg_ka6.FE69A1.FFACCB.2.0_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la31.43.FE1414.59C1FF.1_lb_oa_os_ob_oc_od_oe_of_lc_m05.F9C971.3.0.1.2.63.15.0.13.2.61_m15.59C1FF.3.0.1.2.42.15.0.13.2.61_m25.59C1FF.3.0.0.1.16.15.52.41.2.61_n0_s312.FE69A1.FE69A1.56.0.65.0.500.839.1.6.0.45.2.61_s512.2.2.56.1.58.0.500.748.2.9.1.49.2.61_s71.FE69A1.FE69A1.30.0.100.0.444.874.1.6.0.100.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.3_oj0.55.55.0.3"
	s["other"] = ""
	stages.append(s)
	
	#lost shoes
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id4.FFACCB.FFACCB.44.0.0.1.4.0.0.4.0.0.2_ic35.FFACCB.FFACCB.FE69A1.1_jc_ie4.56.56.0.13.FFACCB.FFACCB.0.13.FFACCB.FFACCB.0.1_ja_jb_jd_je_jf_jg_ka6.FE69A1.FFACCB.2.0_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la31.43.FE1414.59C1FF.1_lb_oa_os_ob_oc_od_oe_of_lc_m05.F9C971.3.0.1.2.63.15.0.13.2.61_m15.59C1FF.3.0.1.2.42.15.0.13.2.61_m25.59C1FF.3.0.0.1.16.15.52.41.2.61_n0_s312.FE69A1.FE69A1.56.0.65.0.500.839.1.6.0.45.2.61_s512.2.2.56.1.58.0.500.748.2.9.1.49.2.61_s71.FE69A1.FE69A1.30.0.100.0.444.874.1.6.0.100.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.3_oj0.55.55.0.3"
	s["other"] = ""
	stages.append(s)
	
	#lost earrings
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id4.FFACCB.FFACCB.44.0.0.1.4.0.0.4.0.0.2_ic35.FFACCB.FFACCB.FE69A1.1_jc_ie4.56.56.0.13.FFACCB.FFACCB.0.13.FFACCB.FFACCB.0.1_ja_jb_jd_je_jf_jg_ka6.FE69A1.FFACCB.2.0_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la31.43.FE1414.59C1FF.1_lb_oa_os_ob_oc_od_oe_of_lc_m05.F9C971.3.0.1.2.63.15.0.13.2.61_m15.59C1FF.3.0.1.2.42.15.0.13.2.61_n0_s312.FE69A1.FE69A1.56.0.65.0.500.839.1.6.0.45.2.61_s512.2.2.56.1.58.0.500.748.2.9.1.49.2.61_s71.FE69A1.FE69A1.30.0.100.0.444.874.1.6.0.100.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi0.55.55.0.3_oj0.55.55.0.3"
	s["other"] = ""
	stages.append(s)
	
	#lost gloves
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id4.FFACCB.FFACCB.44.0.0.1.4.0.0.4.0.0.2_ic35.FFACCB.FFACCB.FE69A1.1_jc_ie4.56.56.0.13.FFACCB.FFACCB.0.13.FFACCB.FFACCB.0.1_ja_jb_jd_je_jf_jg_ka6.FE69A1.FFACCB.2.0_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la31.43.FE1414.59C1FF.1_lb_oa_os_ob_oc_od_oe_of_lc_m05.F9C971.3.0.1.2.63.15.0.13.2.61_m15.59C1FF.3.0.1.2.42.15.0.13.2.61_n0_s312.FE69A1.FE69A1.56.0.65.0.500.839.1.6.0.45.2.61_s512.2.2.56.1.58.0.500.748.2.9.1.49.2.61_s71.FE69A1.FE69A1.30.0.100.0.444.874.1.6.0.100.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost crown
	s = {}
	s["blush"] = 0
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id4.FFACCB.FFACCB.44.0.0.1.4.0.0.4.0.0.2_ic35.FFACCB.FFACCB.FE69A1.1_jc_ie4.56.56.0.13.FFACCB.FFACCB.0.13.FFACCB.FFACCB.0.1_ja_jb_jd_je_jf_jg_ka6.FE69A1.FFACCB.2.0_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m05.F9C971.3.0.1.2.63.15.0.13.2.61_m15.59C1FF.3.0.1.2.42.15.0.13.2.61_n0_s312.FE69A1.FE69A1.56.0.65.0.500.839.1.6.0.45.2.61_s512.2.2.56.1.58.0.500.748.2.9.1.49.2.61_s71.FE69A1.FE69A1.30.0.100.0.444.874.1.6.0.100.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost dress
	s = {}
	s["blush"] = 1
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id_ic_jc_ie4.56.56.0.13.FFACCB.FFACCB.0.13.FFACCB.FFACCB.0.1_ja_jb_jd_je_jf_jg_ka6.FE69A1.FFACCB.2.0_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s312.FE69A1.FE69A1.56.0.65.0.500.839.1.6.0.45.2.61_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj_s312.FE69A1.FE69A1.56.0.65.0.500.839.1.6.0.45.2.61"
	s["other"] = ""
	stages.append(s)
	
	#lost pants
	s = {}
	s["blush"] = 1
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka6.FE69A1.FFACCB.2.0_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#lost bra
	s = {}
	s["blush"] = 2
	s["lj"] = 0
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb6.FE69A1.FFACCB.2_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	
	#lost panties/nude
	s = {}
	s["blush"] = 3
	s["lj"] = 50
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#masturbating
	s = {}
	s["blush"] = 4
	s["lj"] = 90
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
	s["other"] = ""
	stages.append(s)
	
	#finished
	s = {}
	s["blush"] = 3
	s["lj"] = 150
	s["clothes"] = "ia_if_ib_id_ic_jc_ie_ja_jb_jd_je_jf_jg_ka_kb_kc_kd_ke_kf_la_lb_oa_os_ob_oc_od_oe_of_lc_m0_n0_s0_og_oh_oo_op_oq_or_om_on_ok_ol_oi_oj"
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
		
		for ind, stage in enumerate(pd["stages"]):
			if ind == len(pd["stages"]) - 2:
				#skip the masturbation stage, all of those are custom images
				continue
				#pass
		
			stage_desc = version_str + stage["clothes"] # + pd["appearance"] + "_"
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
			