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

## intent:greet_first_time
 - first-greet

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
- hvað eru [opnunartímar](attribute:opening_hours) í [Laugardal](bank)?
- Hvað eru [opnunartímar](attribute:opening_hours) í [Hafnarfirði](location)?
- Hvenær er [opið](attribute:opening_hours) á [Egilsstöðum](bank)?
- hvenær er [opið](attribute:opening_hours) á [Reyðarfirði](bank)?
- Er [hraðbanki](attribute:ATM) á [Reyðarfirði](bank)?
- Er [hraðbanki](attribute:ATM) í [Kópavogi](location:Kópavogur)
- Hvaða [bankar](object_type:bank) eru í [Reykjavík](location)?
- Hvaða [bankar](object_type:bank) eru í [Kópavogi](location:Kópavogur)?
- hvaða [útibú](object_type:bank) eru í [Hafnarfjörður](location:Hafnarfjörður)?

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

## intent:query_geolocation
- [64.1539630](latitude) [-21.950570](longitude)
- [64.120677](latitude) [-21.8099861](longitude)
- [63.786486](latitude) [-18.058027](longitude)
- [64.000000](latitude) [-22.0000009](longitude)
- [30.00200](latitude) [-20.09000](longitude)

## intent:query_search_banks
- Hvar er næsti banki við mig?
- Næsti banki?
- Banka
- Hvar er næsti Íslandsbanki?
- Hvar er ég?
- hvar er ég
- Ég veit ekki hvar ég er
- ég er týnd
- Ég er týndur

## regex:amount
- [0-9]*$

## regex:longitude
- ^-\d{2}(\.\d{5,6,7,8})?$

## regex:latitude
-  ^[+]?\d{2}(\.\d{5,6,7,8})?$ 

## lookup:rate
  data/lookup/currencies.txt

## lookup:base
  data/lookup/currencies.txt
  
## lookup:bank
  data/lookup/banks.txt

## synonym:bank
- bankar
- útibú
- banki 

## synonym:opening_hours
- opnunartímar
- opið
- afgreiðslutíma

## lookup:location
  data/lookup/locations.txt

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
