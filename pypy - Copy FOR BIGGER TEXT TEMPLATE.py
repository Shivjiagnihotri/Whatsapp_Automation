import time
import pywhatkit
import pyautogui
import emojis

x=["+916361866784","+916362094440","+916362406069","+916362530547","+916369045145","+916370402070","+916370786109","+916372484438","+916379427918","+916380047620","+916381622326","+916383407616","+916383450564","+916383695240","+916383708571","+916385827487","+916388802514","+916395685992","+917000516460","+917004606071","+917005630769","+917008791985","+917013597221","+917014858684","+917016868492","+917020418262","+917020840567","+917021397814","+917022337091","+917028176958","+917030703390","+917032120088","+917032401482","+917032696483","+917032734397","+917038140040","+917038285109","+917038373791","+917040608072","+917042246678","+917042664376","+917057027554","+917057376569","+917057535906","+917057653977","+917075707691","+917083589566","+917093897711","+917095129253","+917207379303","+917208664454","+917217770772","+917218883991","+917219404770","+917237023579","+917241156150","+917250628610","+917259578979","+917263052175","+917263994554","+917276609280","+917287046695","+917288809874","+917304410105","+917347732162","+917349102411","+917350075276","+917350324490","+917364871935","+917366928995","+917385557187","+917386743343","+917386963472","+917396390531","+917397947828","+917401316520","+917416611718","+917416865234","+917451991627","+917459073175","+917488008584","+917488248448","+917488293697","+917492911588","+917500793997","+917517406524","+917518531456","+917542895753","+917569319153","+917569349327","+917620398078","+917660969938","+917675022136","+917678113246","+917703863968","+917709851593","+917710842844","+917731063250","+917732054858","+917735138281","+917738131243","+917743967475","+917744010199","+917747831988","+917750079414","+917756857366","+917760071431","+917765038833","+917766839651","+917768934231","+917769046182","+917780233698","+917794039837","+917795434552","+917798983831","+917842190388","+917846041535","+917873509182","+917875183829","+917875341302","+917887600760","+917887625279","+917887975009","+917889892982","+917893781103","+917902844354","+917905039062","+917905370069","+917906619557","+917908822046","+917973205969","+917974379478","+917978329931","+917981685988","+917985169119","+917989673390","+917995149104","+918007213346","+918007217993","+918007799296","+918056643517","+918074198947","+918074495719","+918080187713","+918083527757","+918087337353","+918088318068","+918088523912","+918088866245","+918095934073","+918096196174","+918097586618","+918108125208","+918108603709","+918110008827","+918122939804","+918123921093","+918125441676","+918125730438","+918143516512","+918144155978","+918144410649","+918148132582","+918150018296","+918173011575","+918179276499","+918179494098","+918179546430","+918180080546","+918197238468","+918197604578","+918197931758","+918208713800","+918217070674","+918237578007","+918247218864","+918247255993","+918248949791","+918249176374","+918249362604","+918275273140","+918275505757","+918277387773","+918285908039","+918296246141","+918299152447","+918308427406","+918308604344","+918308815043","+918317058732","+918328256540","+918329121087","+918329178636","+918329876253","+918329979753","+918331995794","+918332970058","+918340912267","+918355919374","+918358906293","+918374232934","+918379838325","+918390544139","+918390687214","+918390702751","+918408061444","+918410001906","+918421086006","+918421284372","+918431686819","+918456081461","+918464090226","+918465828150","+918480065146","+918489407322","+918496933827","+918497940878","+918500459663","+918508996317","+918530107998","+918543033225","+918543052078","+918549984316","+918553826514","+918561812104","+918578027933","+918580146169","+918590817660","+918593020457","+918600222253","+918600463621","+918600604820","+918600745410","+918605389091","+918610819832","+918617737268","+918618238976","+918618516453","+918623950926","+918639044772","+918639804234","+918652151771","+918668292787","+918688521369","+918688550366","+918688675066","+918688679104","+918688804341","+918688861259","+918697614807","+918698035891","+918698881757","+918709207030","+918722600185","+918722886923","+918726614741","+918754232390","+918754304399","+918754679130","+918755293505","+918762700337","+918766094052","+918778401010","+918778560406","+918788673200","+918792732462","+918805316411","+918830688378","+918830989720","+918838458481","+918856904770","+918861194533","+918882182670","+918884636772","+918888947628","+918896392319","+918897322746","+918897957436","+918897961744","+918908680606","+918910239972","+918919087942","+918919410751","+918921194443","+918921314630","+918939335801","+918939565912","+918943820114","+918951745496","+918962919492","+918975433904","+918975981537","+918983002989","+919000640937","+919000916080","+919008299141","+919008545615","+919011166961","+919011982267","+919014063941","+919014364359","+919021381850","+919021820804","+919029998067","+919033642825","+919036196360","+919048927661","+919049437161","+919052677465","+919067161999","+919067626217","+919075534108","+919075662429","+919075985066","+919082415691","+919087838010","+919096041473","+919108607542","+919108904132","+919110377509","+919110526187","+919110823599","+919110825773","+919111991895","+919112150101","+919112981494","+919113068924","+919113574747","+919115486889","+919121039153","+919122731213","+919131801767","+919146930784","+919148260963","+919151520938","+919168923631","+919175014696","+919175746856","+919175930689","+919177661300","+919182630076","+919264931313","+919284360910","+919327076993","+919334526710","+919340779692","+919340790484","+919344311450","+919344448247","+919346380484","+919347683621","+919347759282","+919350277090","+919353802240","+919359305755","+919359659741","+919359947376","+919370339933","+919370524042","+919380820916","+919381174448","+919381446070","+919381608318","+919390562754","+919390867545","+919391154460","+919391660110","+919392462361","+919398471981","+919398673137","+919398921058","+919403002845","+919404929143","+919405656963","+919421881151","+919431416148","+919437854745","+919438207985","+919443844825","+919447746927","+919490393042","+919494546168","+919503365104","+919503415436","+919503812850","+919503969208","+919505285227","+919511735770","+919513897429","+919519893364","+919527086322","+919550552502","+919556930700","+919559574481","+919561791225","+919561859323","+919562182035","+919562221357","+919566572131","+919573733739","+919579652873","+919580000983","+919586181629","+919588022481","+919588600318","+919588814882","+919591023487","+919591737155","+919591953129","+919595159536","+919603432913","+919604915242","+919606783930","+919607894222","+919620275679","+919620527657","+919633457381","+919637821720","+919640394573","+919640994312","+919651503682","+919655257302","+919655447552","+919657299839","+919661266730","+919665017093","+919666076865","+919674248564","+919676133045","+919677383070","+919686960687","+919696875145","+919699063497","+919701261729","+919704541263","+919713165566","+919738470724","+919740653738","+919742250371","+919763591901","+919763594395","+919765013259","+919777273376","+919787421517","+919788891363","+919789078897","+919809710344","+919821883772","+919838476102","+919844789388","+919848254406","+919848511700","+919853273147","+919860240637","+919860926686","+919881217061","+919885669526","+919886338605","+919890023747","+919896507111","+919908331255","+919921729400","+919922500001","+919947209939","+919947857944","+919948032508","+919948967405","+919951017502","+919951317980","+919951698636","+919952114299","+919952945204","+919960503788","+919962644137","+919966229286","+919970977857","+919972606750","+919975695848","+919980451816","+919981999152","+919989484195","+919989579480","+919991985565","+919994917854","+919996469455","+919996680417","+919999936792"]
i=0
j=len(x)-1
k=0


while i<=j:
    pywhatkit.sendwhatmsg_instantly(
        phone_no=x[i],
        message="Are you tired of searching for the perfect internship opportunity? Look no further! Zuno by Foundit (formerly Monster India) is here to offer you the dream internship opportunities in the fields of AI/ML, Frontend and Backend Developments, Digital Designer, and Content Creator. \n\nRegister for FREE and apply now using the link provided below! Don't wait any longer, as the last date to apply is today! With a monthly stipend of 30K, you can kickstart your career and gain valuable experience in your preferred domain. \n\nThe location of the internship is in Bengaluru and Jalandhar, so take advantage of this opportunity to explore new cities and cultures. Only a few vacancies are available, so hurry and apply now! \n\n Don't miss out on this golden opportunity! Join our WhatsApp group to stay updated on the latest information about the internship. Click the link below to apply and secure your dream internship today.\n\n 👉 Register now: https://bit.ly/InternshipByFoundit \n\n👉 Join our WhatsApp group: https://chat.whatsapp.com/LRpDWIRsuuk8kEofjuU37U"

    )
    
    time.sleep(20)
    pyautogui.press("enter")
    #pyautogui.typewrite(emojis.encode(":wave: Please register and join our group."))
    #pyautogui.press("enter")
    time.sleep(2)
    i=i+1
