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
pcu = (689,-683,"Petra Christian University")
bundaran_waru = Vertex(572,-775,"Bundaran Waru")
exit_tol_waru = Vertex(496,-807,"Exit Tol Waru")



graph = {
    pakuwon_mall : {},
    lenmarc_mall : {},
    persimpangan_HRMuhammad_Jonosewojo: {},
    papaya: {},
    pasar_modern: {},
    vasa_hotel: {},
    bundaran_satelit: {},
    gerbang_tol_satelit: {},
    persimpangan_mayjenSungkono_rayaDukuhKupang: {},
    shangrila_hotel: {},
    islamic_centre: {},
    ciputra_world: {},
    rumah_sakit_mayapada: {},
    persimpangan_adityawarman_indragiri: {},
    persimpangan_girilaya_diponegoro: {},
    persimpangan_indragiri_diponegoro: {},
    gor_pancasila: {},
    persimpangan_adityawarman_ciliwung: {},
    persimpangan_diponegoro_ciliwung: {},
    kebun_binatang_surabaya: {},
    taman_bungkul: {},
    persimpangan_DRSoetomo_rayaDarmo: {},
    persimpangan_pandegiling_rayaDarmo: {},
    persimpangan_uripSumoharjo_basukiRahmat: {},
    persimpangan_basukiRahmat_embongWungu: {},
    tunjungan_plaza: {},
    persimpangan_embongWungu_panglimaSudirman: {},
    monumen_bambu_runcing: {},
    persimpangan_ahmadYani_wonokromo: {},
    maspion_square: {},
    persimpangan_ahmadYani_siwalankerto: {},
    pcu: {},
    bundaran_waru: {},
    exit_tol_waru: {},
}

#29,34,32 jalan