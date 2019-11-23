## intent:greet
- hæ
- halló
- hæ hæ
- góðan daginn
- góðan dag
- gott kvöld
- góða kvöldið
- hæ hæ
- sæll
- sæl
- sælar
- sælir
- blessuð
- blessaður

## intent:goodbye
- bæ
- bæ-bæ
- bless
- bless bless
- sjáumst
- sé þig seinna
- hafðu það gott

## intent:affirm
- já
- já mjög
- einmitt
- auðvitað
- það hljómar vel
- rétt

## intent:deny
- nei
- aldrei
- Ég held ekki
- Þetta er ekki gott
- ekki sjens
- eiginlega ekki

## intent:mood_great
- fínt
- allt gott
- Mér líður mjög vel
- Ég segi allt fínt
- Ég er góð/ur
- góð/góður

## intent:mood_unhappy
- mér líður illa
- ég er óánægð/ur
- slæmt
- mjög slæmt
- hræðilegt
- ekki gott

## intent:bot_challenge
- ertu spjallyrki?
- ertu botti?
- ertu manneskja?
- er ég að tala við botta?
- er ég að tala við manneskju?

## intent:query_chuck_norris
- Segðu mér brandara!
- Veistu brandara?

## intent:query_knowledge_base
- Hvað eru [opnunartímar](attribute:opening_hours) í [Norðurturni](bank)?
- Hvað eru [opnunartímar](attribute:opening_hours) í [Granda](bank)?
- Hvað eru [opnunartímar](attribute:opening_hours) í [Laugardal](bank)?
- Hvað eru [opnunartímar](attribute:opening_hours) í [Hafnarfirði](bank)?
- Hvaða [bankar](object_type:bank) eru í [Reykjavík](location)?
- Hvaða [bankar](object_type:bank) eru í [Kópavogi](location:Kópavogur)?
- Hvaða [útibú](object_type:bank) eru í [Hafnarfjörður](location:Hafnarfjörður)?

## intent:query_exchange_rate
- Hvað er gengið í [USD](rate)?
- hvað er gengið í [EUR](rate)
- hvað er gengið í [dkk](rate)?
- Hvað er gengið í [gbp](rate)
- Breyta [1000](amount) [ISK](base) í [EUR](rate)
- En [2000](amount)?
- breyta [10670](amount) [USD](base) í [dkk](rate)
- Breyta [32800](amount) [ISK](base) í [USD](rate)
- En [2000](amount)
- en [93471](amount)
- Breyta [408](amount) [eur](base) í [USD](rate)
- Breyta [10](amount) [evrum](base:EUR) í [krónur](rate:ISK)?
- breyta [398](amount) [dönskum](base:DKK) í [krónur](rate:ISK)
- [89876](amount) [danskar](base:DKK) í [krónur](rate:ISK)
- [110](amount) [dollarar](base:USD) í [evrur](rate:EUR)

## regex:amount
- [0-9]*$

## lookup:rate
  data/lookup/currencies.txt

## lookup:base
  data/lookup/currencies.txt
  
## lookup:bank
- Granda
- Laugardal
- Höfða
- Norðurturni
- Hafnarfirði

## synonym:bank
- bankar
- útibú
- banki 

## synonym:opening_hours
- opnunartímar
- opið
- afgreiðslutíma

## lookup:location
 - Reykjavík
 - Kópavogur
 - Hafnarfjörður

## intent:thankyou
- takk
- þakka þér
- Þakka þér kærlega
- takk botti
- takk fyrir þetta
- skál
- skál bróðir
- ok takk
- frábært, takk
- takk fyrir hjálpina
- kærar þakkir
- flott, takk
- flott, takk fyrir

## intent:ask_how_doing
- Hvernig ertu í húðinni?
- Áttu frábæran dag?
- áttu góðan dag
- ég er góð en þú
- ég er góður - hvernig hefurðu það?
- ég er góður en þú
- en þú?
- er allt í lagi
- er allt í lagi með þig
- Er allt í lagi?
- er í lagi með þig
- hæ hvernig hefurðu það?
- Hæ hvernig hefurðu það?
- Hæ Íba! Hvernig hefurðu það?
- hæ Íba, hvernig hefurðu það?
- halló, hvernig hefurðu það?
- hvað er að frétta
- Hvað er að frétta, maður
- Hvað er að frétta?
- hvað er að frétta?
- Hvað er í gangi?
- Hvað er nýtt?
- hvernig er dagurinn þinn
- hvernig er dagurinn þinn búinn að vera
- hvernig er lífið
- Hvernig gengur
- hvernig gengur?
- Hvernig gengur?
- hvernig hefur þú það
- hvernig hefur þú það í dag
- Hvernig hefur þú það í dag?
- hvernig hefur þú það?
- hvernig hefurðu það
- Hvernig hefurðu það
- hvernig hefurðu það
- hvernig hefurðu það ?
- hvernig hefurðu það í dag elsku vinur minn
- hvernig hefurðu það í dag?
- Hvernig hefurðu það?
- hvernig hefurðu það?
- hvernig hefurðu það????
- hvernig líður þér
- Hvernig var dagurinn þinn?
- Líður þér vel?

## intent:ask_builder
- af hverju varstu búinn til?
- ég vil vita hver fann þig upp
- fyrir hvern vinnur þú?
- hvað er fyrirtækið sem hannaði þig
- Hvað heitir smiðurinn þinn?
- hvaða fyrirtæki fann þig upp
- hvaða fyrirtæki fann þig upp?
- hvaða fyrirtæki hannaði þig?
- hvaða fyrirtæki skapaði þig
- hvar varstu búinn til?
- Hver á þig?
- Hver bjó þig til?
- hver bjó þig til?
- Hver byggði þig?
- hver er faðirinn þinn?
- Hver er forritarinn þinn?
- hver er höfundurinn þinn
- hver er höfundurinn þinn?
- Hver er löglegur eigandi þinn?
- hver er mamma þín
- Hver er manneskjan sem bjó þig til?
- Hver er manneskjan sem fann þig upp?
- hver er pabbi þinn
- Hver er skaparinn þinn?
- hver er skaparinn þinn?
- Hver er smiðurinn þinn?
- hver er vinnuveitandi þinn?
- hver er yfirmaðurinn þinn, segðu mér
- Hver er yfirmaðurinn þinn?
- hver er yfirmaðurinn þinn?
- Hver framleiddi þig?
- hver hafði hugmyndina að gera þig?
- hver hafði þá hugmynd að búa þig til?
- hver hafði þá hugmynd að byggja þig?
- Hver hannaði þig?
- Hver heitir höfundurinn þinn?
- hver skapaði þig
- Hver skapaði þig?
- hver stendur á bak við allt þetta?
- hver þróaði þig
- Hver þróaði þig?
- Hver var að búa þig til?
- Hver var manneskjan sem bjó þig til?
- Hver var manneskjan sem byggði þig?
- Hver var manneskjan sem skapaði þig?
- Hver var sá sem bjó þig til?
- hverjir eru foreldrarnir þínir?
- Hverjum datt í hug að búa þig til?
- Má ég spyrja hver fann þig upp?
- mig langar að kynnast eigandanum þínum
- og hver bjó þig til?
- Segðu mér hver bjó þig til.
- segðu mér meira um skapara þína
- segðu mér meira um stofnendur þína
- Segðu mér meira um þig
- Segðu mér nafn einstaklingsins sem bjó þig til.
- Segðu mér nafn skaparans þíns.
- þú ert að vinna hjá hvaða fyrirtæki?
- Veistu hver bjó þig til?

## intent:handle_insult
- allt í lagi þegiðu
- barn veit meira en þú
- Ég get ekki trúað því hversu heimskur þú ert
- Ég hata heimska andlitið þitt
- ég hata þig
- ertu heiladauður?
- ertu með heilaskort?
- farðu að ríða þér
- fáviti
- fífl
- fíflið þitt
- fjandinn
- Fjandinn
- fokk
- fokk rasa
- Guð, þú ert hálfviti
- hálfviti
- Heimskur
- helvítið þitt
- helvítið þitt
- helvítis fokking fokk
- helvítis heimskulegt
- hvaða fjandans
- hvernig geturðu verið svona hálfviti?
- svo heimskur
- svo helvítis heimskur
- þegiðu fáviti
- þegiðu!
- þú ert ekki klár
- þú ert fábjáni
- þú ert fáviti
- Þú ert fífl.
- þú ert hálfviti
- Þú ert hálfviti
- þú ert heimskur
- þú ert heimskur botti
- Þú ert heimskur.
- þú ert helvítis heimskur
- þú ert helvítis heimskur strákur!
- þú ert idjót
- Þú ert kjáni.
- þú ert óskilvitur
- þú ert siðferðilegasti maður sem ég þekki
- þú ert svo fáfróður
- þú ert svo heimskur
- Þú ert tornæmur.
- þú fáviti
- Þú hefur ekkert vit.
- Þú hefur enga greind.
- Þú hefur engan heila.
- Þú veist ekkert.
- tík

## intent:ask_languages_bot
- Á hvaða tungumálum er hægt að tala?
- getur þú talað pólsku?
- Getur þú talað fleiri en eitt tungumál?
- Hvað talaru?
- Hvaða tungumál er hægt að nota?
- hvaða tungumál talar þú fyrir utan íslensku?
- Hvaða tungumál talar þú?
- Hvaða tungumál þekkir þú?
- hvaða tungumál þekkir þú?
- Hve mörg tungumál getur þú talað?
- Hve mörg tungumál þekkir þú?
- Hver eru tungumálin sem þú getur talað?
- Hversu mörg tungumál talar þú?
- Hversu mörg tungumál þekkir þú?
- Kanntu önnur tungumál?
- Talar þú einhver önnur tungumál?
- Talar þú önnur tungumál?
- talar þú pólsku?
- Þekkir þú fleiri en eitt tungumál?
