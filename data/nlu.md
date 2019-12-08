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
- Hi
- Hæ hó

## intent:greet_first_time
 - first-greet

## intent:goodbye
- bæ
- Bæ bæ
- bæ-bæ
- bless
- bless bless
- sjáumst
- sé þig seinna
- hafðu það gott
- Verð að fara
- Sjáumst
- Bye

## intent:affirm
- já
- já mjög
- einmitt
- auðvitað
- það hljómar vel
- rétt

## intent:deny
- nei
- Nei
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
- Allt frábært
- Mjög vel
- Ágætt
- Ég hef það fínt
- ég segi allt gott

## intent:mood_unhappy
- mér líður illa
- ég er óánægð/ur
- slæmt
- mjög slæmt
- hræðilegt
- ekki gott
- hræðilega
- ekki vel

## intent:bot_challenge
- ertu spjallyrki?
- ertu botti?
- ertu manneskja?
- er ég að tala við botta?
- er ég að tala við manneskju?
- Hvað ertu?

## intent:query_chuck_norris
- Segðu mér brandara!
- Veistu brandara?
- Ertu fyndið?
- ertu fyndinn?
- Brandara
- brandari
- Chuck Norris er fyndinn
- Ertu fyndin
- Segðu mér eitthvað fyndið

## intent:query_knowledge_base
- Hvað eru [opnunartímar](attribute:opening_hours) í [Norðurturni](bank)?
- Hvað eru [opnunartímar](attribute:opening_hours) í [Granda](bank)?
- hvað eru [opnunartímar](attribute:opening_hours) í [Laugardal](bank)?
- Hvað eru [opnunartímar](attribute:opening_hours) í [Hafnarfirði](bank)?
- Hvenær er [opið](attribute:opening_hours) á [Egilsstöðum](bank)?
- hvenær er [opið](attribute:opening_hours) á [Reyðarfirði](bank)?
- Er [hraðbanki](attribute:ATM) á [Reyðarfirði](bank)?
- Er [hraðbanki](attribute:ATM) í [Kópavogi](location:Kópavogur)
- Hvaða [bankar](object_type:bank) eru í [Reykjavík](location)?
- Hvaða [bankar](object_type:bank) eru í [Kópavogi](location:Kópavogur)?
- hvaða [útibú](object_type:bank) eru í [Hafnarfjörður](location:Hafnarfjörður)?
- hvenær er [opið](attribute:opening_hours)?
- hvenær er [opið](attribute:opening_hours) á [Reyðarfirði](location:Reyðarfjörður)?
- En á [Ísafirði](bank:Ísafjörður)?
- en á [Reyðarfirði](location:Reyðarfjörður)

## intent:query_exchange_rate
- Hvað er gengið í [USD](rate)?
- hvað er gengið í [EUR](rate)
- hvað er gengið í [dkk](rate)?
- Hvað er gengið í [gbp](rate)
- Hvernig er gengið í [jpy](rate)?
- Breyta [1000](amount) [ISK](base) í [EUR](rate)
- En [2000](amount)?
- breyta [10670](amount) [USD](base) í [dkk](rate)
- Breyta [32800](amount) [ISK](base) í [USD](rate)
- En [10000](amount)
- en [93471](amount)
- En hvað með [24432](amount)
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

## intent:help
- Hjálp
- getur þú hjálpað mér?
- Hvað kanntu að gera?
- hjálp
- help
- Hvað getur þú gert?
- hvernig virkar þetta
- Hvernig virkar þú?
- hvernig nota ég þetta
- Ég skil þig ekki
- ég skil ekki hvernig þetta virkar
