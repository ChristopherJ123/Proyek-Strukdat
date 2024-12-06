from Graph import Graph
from Path import Path
from Vertex import Vertex
from Walking import Walking
from Car import Car
from Motorcycle import Motorcycle

gr = Graph()
car = Car(50, 10)
motor = Motorcycle(40, 10)

pakuwon_mall = Vertex(0,0,"Pakuwon Mall")
lenmarc_mall = Vertex(65,41,"Lenmarc Mall")
persimpangan_HRMuhammad_Jonosewojo = Vertex(88,85, "Persimpangan HR Muhammad - Jonosewojo")
papaya = Vertex(76,103,"Papaya")
pasar_modern = Vertex(156,144,"Pasar Modern")
vasa_hotel = Vertex(251,32,"Vasa Hotel")
bundaran_satelit = Vertex(301,8,"Bundaran Satelit")
gerbang_tol_satelit = Vertex(263,-17,"Gerbang Tol Satelit")
persimpangan_mayjenSungkono_rayaDukuhKupang = Vertex(402,-14,"Persimpangan Mayjen Sungkono-Raya Dukuh Kupang")
shangrila_hotel = Vertex(422,-23,"Shangrila Hotel")
islamic_centre = Vertex(419,29,"Islamic Centre")
ciputra_world = Vertex(479,-32,"Ciputra World")
rumah_sakit_mayapada = Vertex(561,-44, "Rumah Sakit Mayapada")
persimpangan_adityawarman_indragiri = Vertex(585,-44,"Persimpangan Adityawarman-Indragiri")
persimpangan_girilaya_diponegoro = Vertex(541,91,"Persimpangan Girilaya-Diponegoro")
persimpangan_indragiri_diponegoro = Vertex(632,56,"Persimpangan Indragiri-Diponegoro")
gor_pancasila = Vertex(606,20,"GOR Pancasila")
persimpangan_adityawarman_ciliwung = Vertex(621,-70,"Persimpangan Adityawarman-Ciliwung")
persimpangan_diponegoro_ciliwung = Vertex(668,-32,"Persimpangan Diponegoro-Ciliwung")
kebun_binatang_surabaya = Vertex(689,-76,"Kebung Binatang Surabaya")
taman_bungkul = Vertex(689,-20,"Taman Bungkul")
persimpangan_DRSoetomo_rayaDarmo = Vertex(703,88,"Persimpangan Dr Soetomo-Raya Darmo")
persimpangan_pandegiling_rayaDarmo = Vertex(715,133,"Persimpangan Pandegiling-Raya Darmo")
persimpangan_uripSumoharjo_basukiRahmat = Vertex(724,177,"Persimpangan Urip Sumoharjo-Basuki Rahmat")
persimpangan_basukiRahmat_embongWungu = Vertex(709,266,"Persimpangan Basuki Rahmat-Embong Wungu")
tunjungan_plaza = Vertex(706,286,"Tunjungan Plaza")
persimpangan_embongWungu_panglimaSudirman = Vertex(754,251,"Persimpangan Embong Wungu-Panglima Sudirman")
monumen_bambu_runcing = Vertex(748,239,"Monumen Bambu Runcing")
persimpangan_ahmadYani_wonokromo = Vertex(665,-207,"Persimpangan Ahmad Yani-Wonokromo")
maspion_square = Vertex(641,-334,"Maspion Square")
persimpangan_ahmadYani_siwalankerto = Vertex(585,-677,"Persimpangan Ahmad Yani-Siwalankerto")
pcu = Vertex(689,-683,"Petra Christian University")
bundaran_waru = Vertex(572,-775,"Bundaran Waru")
exit_tol_waru = Vertex(496,-807,"Exit Tol Waru")

Path("",1,True,0.0)

mayjen_jonosewojo = Path("Mayjen Jonosewojo",1,True,0.0)
raya_darmo_permai_selatan = Path("Raya Darmo Permai Selatan",1,True,0.0)
raya_darmo_permai = Path("Raya Darmo Permai",1,True,0.0)
HRMuhammad = Path("HR Muhammad",1,True,0.0)
mayjen_sungkono = Path("Mayjen Sungkono",1,True,0.0)
jalan_tol_satelit = Path("Jalan Tol Satelit",1,True,0.0)
tol_perak_waru = Path("Tol Perak Waru",1,True,0.0)
raya_dukuh_kupang = Path("Raya Dukuh Kupang",1,True,0.0)
girilaya = Path("Girilaya",1,True,0.0)
adityawarman = Path("Adityawarman",1,True,0.0)
diponegoro = Path("Diponegoro",1,True,0.0)
drSoetomo = Path("Dr Soetomo",1,True,0.0)
indragiri = Path("Indragiri",1,True,0.0)
ciliwung = Path("Ciliwung",1,True,0.0)
raya_darmo = Path("Raya Darmo",1,True,0.0)
wonokromo = Path("Wonokromo",1,True,0.0)
urip_sumoharjo = Path("Urip Sumoharjo",1,True,0.0)
basuki_rahmat = Path("Basuki Rahmat",1,True,0.0)
embong_wungu = Path("Embong Wungu",1,True,0.0)
panglima_sudirman = Path("Panglima Sudirman",1,True,0.0)
ahmad_yani = Path("Ahmad Yani",1,True,0.0)
siwalankerto = Path("Siwalankerto",1,True,0.0)
raya_geluran = Path("Raya Geluran",1,True,0.0)



graph = {
    pakuwon_mall : {lenmarc_mall : mayjen_jonosewojo},
    lenmarc_mall : {pakuwon_mall : mayjen_jonosewojo, persimpangan_HRMuhammad_Jonosewojo : mayjen_jonosewojo},
    persimpangan_HRMuhammad_Jonosewojo: {lenmarc_mall : mayjen_jonosewojo, papaya : raya_darmo_permai_selatan, pasar_modern : raya_darmo_permai, vasa_hotel : HRMuhammad},
    papaya: {persimpangan_HRMuhammad_Jonosewojo : raya_darmo_permai_selatan},
    pasar_modern: {persimpangan_HRMuhammad_Jonosewojo : raya_darmo_permai},
    vasa_hotel: {persimpangan_HRMuhammad_Jonosewojo : HRMuhammad, bundaran_satelit : HRMuhammad},
    bundaran_satelit: {vasa_hotel : HRMuhammad, persimpangan_mayjenSungkono_rayaDukuhKupang : mayjen_sungkono, gerbang_tol_satelit : jalan_tol_satelit},
    gerbang_tol_satelit: {bundaran_satelit : jalan_tol_satelit, exit_tol_waru : tol_perak_waru},
    persimpangan_mayjenSungkono_rayaDukuhKupang: {bundaran_satelit : mayjen_sungkono, shangrila_hotel : mayjen_sungkono, islamic_centre : raya_dukuh_kupang},
    shangrila_hotel: {ciputra_world : mayjen_sungkono, persimpangan_mayjenSungkono_rayaDukuhKupang : mayjen_sungkono},
    islamic_centre: {persimpangan_mayjenSungkono_rayaDukuhKupang : raya_dukuh_kupang, persimpangan_girilaya_diponegoro : girilaya},
    ciputra_world: {shangrila_hotel : mayjen_sungkono, rumah_sakit_mayapada : mayjen_sungkono},
    rumah_sakit_mayapada: {ciputra_world : mayjen_sungkono, persimpangan_adityawarman_indragiri : adityawarman},
    persimpangan_adityawarman_indragiri: {rumah_sakit_mayapada : adityawarman, persimpangan_adityawarman_ciliwung : adityawarman, gor_pancasila : indragiri},
    persimpangan_girilaya_diponegoro: {islamic_centre : girilaya, persimpangan_indragiri_diponegoro : diponegoro},
    persimpangan_indragiri_diponegoro: {persimpangan_girilaya_diponegoro : diponegoro, persimpangan_DRSoetomo_rayaDarmo : drSoetomo, gor_pancasila : indragiri},
    gor_pancasila: {persimpangan_adityawarman_indragiri : indragiri, persimpangan_indragiri_diponegoro : indragiri},
    persimpangan_adityawarman_ciliwung: {persimpangan_adityawarman_indragiri : adityawarman, persimpangan_diponegoro_ciliwung : ciliwung},
    persimpangan_diponegoro_ciliwung: {kebun_binatang_surabaya : diponegoro, persimpangan_adityawarman_ciliwung : ciliwung},
    kebun_binatang_surabaya: {persimpangan_diponegoro_ciliwung : diponegoro, taman_bungkul : raya_darmo, persimpangan_ahmadYani_wonokromo : wonokromo},
    taman_bungkul: {persimpangan_DRSoetomo_rayaDarmo : raya_darmo, taman_bungkul : raya_darmo},
    persimpangan_DRSoetomo_rayaDarmo: {persimpangan_indragiri_diponegoro : drSoetomo, taman_bungkul : raya_darmo, persimpangan_pandegiling_rayaDarmo : raya_darmo},
    persimpangan_pandegiling_rayaDarmo: {persimpangan_DRSoetomo_rayaDarmo : raya_darmo, persimpangan_uripSumoharjo_basukiRahmat : urip_sumoharjo},
    persimpangan_uripSumoharjo_basukiRahmat: {persimpangan_pandegiling_rayaDarmo : urip_sumoharjo, persimpangan_basukiRahmat_embongWungu: basuki_rahmat},
    persimpangan_basukiRahmat_embongWungu: {persimpangan_embongWungu_panglimaSudirman : embong_wungu, tunjungan_plaza : basuki_rahmat},
    tunjungan_plaza: {},
    persimpangan_embongWungu_panglimaSudirman: {monumen_bambu_runcing : panglima_sudirman},
    monumen_bambu_runcing: {persimpangan_uripSumoharjo_basukiRahmat : panglima_sudirman},
    persimpangan_ahmadYani_wonokromo: {kebun_binatang_surabaya : wonokromo, maspion_square : ahmad_yani},
    maspion_square: {persimpangan_ahmadYani_wonokromo : ahmad_yani, persimpangan_ahmadYani_siwalankerto : ahmad_yani},
    persimpangan_ahmadYani_siwalankerto: {maspion_square : ahmad_yani, pcu : siwalankerto, bundaran_waru : ahmad_yani},
    pcu: {persimpangan_ahmadYani_siwalankerto : siwalankerto},
    bundaran_waru: {persimpangan_ahmadYani_siwalankerto : ahmad_yani, exit_tol_waru : raya_geluran},
    exit_tol_waru: {bundaran_waru : raya_geluran, gerbang_tol_satelit : tol_perak_waru},
}

gr.make_graph(graph)
distances, predecessor = gr.shortest_distances(pakuwon_mall, car)
print("===DISTANCES===")
for key, value in distances.items():
    print(f"{key.name}: {value*10} M")

print()
print("===PREDECESSOR===")

for key, value in predecessor.items():
    print(f"{key.name}: {value[0].name if value[0] else None} {value[1].road_name if value[1] else None}")

print()
print("Pergi dari A ke F:")
gr.go_from_a_to_b(pakuwon_mall, pcu, car)



#29,34,32 jalan