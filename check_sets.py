# проверяет, входит ли множество b в множество a

a = [
'ВалютаРегламентированногоУчета',
'КурсДокумента',
'КратностьДокумента',
'УчетВПродажныхЦенах',
'РозничнаяТорговляОблагаетсяЕНВД',
'ПоказыватьВДокументахСчетаУчета',
'ЕстьРасчетыВУсловныхЕдиницах',
'ОплатаВВалюте',
'СвойстваПлатежа',
'ПрименениеУСНДоходы',
'ПрименениеУСН',
'ИтогоВсегоНДС',
'ИтогоСуммаПлатежа',
'ПрименяетсяТолькоУСНПатент',
'ПрименяетсяУСНПатент',
'ПрименяетсяОсобыйПорядокНалогообложения',
'ТекущаяДатаДокумента',
'НадписьПатент',
'НТТНаЕНВД',
'ПорядокОтраженияАвансаСоответствиеЗначений',
'ПрочееТекстДоходыУСН',
'ПлательщикЕНВД',
'ПлательщикНДС',
'СостояниеДокумента',
'НастройкиУсловногоОформления',
'Новости',
'РеквизитыОрганизацииСсылка',
'ИспользоватьНесколькоБанковскихСчетовОрганизации',
'ОсновнойБанковскийСчетОрганизацииЗаполнен',
'ПредлагатьНовыйДоговор',
'РаздельныйУчетУСНТорговыйСбор',
'ВестиУчетПоДоговорам',
'РасшифровкаПлатежаСделка',
'РасшифровкаПлатежаДоговорКонтрагента',
'РасшифровкаПлатежаКурсВзаиморасчетов',
'РасшифровкаПлатежаСпособПогашенияЗадолженности',
'РасшифровкаПлатежаСтавкаНДС',
'РасшифровкаПлатежаСтатьяДвиженияДенежныхСредств',
'РасшифровкаПлатежаСуммаВзаиморасчетов',
'РасшифровкаПлатежаСуммаНДС',
'РасшифровкаПлатежаСчетНаОплату',
'РасшифровкаПлатежаСчетУчетаРасчетовПоАвансам',
'РасшифровкаПлатежаСчетУчетаРасчетовСКонтрагентом',
'РасшифровкаПлатежаДоходыУСН',
'РасшифровкаПлатежаПолеОтражениеАванса',
'РасшифровкаПлатежаДоговорКонтрагентаВалютаВзаиморасчетов',
'РасшифровкаПлатежаКратностьВзаиморасчетов',
'РасшифровкаПлатежаПорядокОтраженияАванса',
'РасшифровкаПлатежаСуммаПлатежа',
'НадписьСуммаДокумента',
'ТекстНеобходимоЗаполнитьПатент',
'ПрименяетсяНесколькоПатентов',
'РасчетыПриОплате',
'РасчетыПриОплатеВидимость',
'РасшифровкаПлатежаПолеОтражениеДохода',
'ПолеОтражениеДоходаВидимость',
'ПорядокОтраженияДоходаСоответствиеЗначений']
b = ['РасшифровкаПлатежаДоговорКонтрагента',
'РасшифровкаПлатежаСпособПогашенияЗадолженности',
'РасшифровкаПлатежаСделка',
'РасшифровкаПлатежаСуммаПлатежа',
'РасшифровкаПлатежаКурсВзаиморасчетов',
'РасшифровкаПлатежаСуммаВзаиморасчетов',
'РасшифровкаПлатежаСтавкаНДС',
'РасшифровкаПлатежаСуммаНДС',
'РасшифровкаПлатежаСчетНаОплату',
'РасшифровкаПлатежаСтатьяДвиженияДенежныхСредств',
'РасшифровкаПлатежаСчетУчетаРасчетовСКонтрагентом',
'РасшифровкаПлатежаСчетУчетаРасчетовПоАвансам',
'РасшифровкаПлатежаКратностьВзаиморасчетов',
'РасшифровкаПлатежаПорядокОтраженияАванса',
'РасшифровкаПлатежаДоходыУСН']

check = 0
for i in b:
    if i in a:
        check+=1
if check == len(b):
    print ("include")
else:
    print ("not include")