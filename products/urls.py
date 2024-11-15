from django.urls import path, include
from . import checkviews
from . import views

urlpatterns = [
    # login to admin path
    path('admindash', views.admindash, name='admindash'),
    path('getproductsbycategory', views.getproductsbycategory, name='getproductsbycategory'),
    path('addproductspage', views.adminaddproductpage, name='addproductspage'),
    path('categoriespage', views.categoriespage, name='categoriespage'),
    path('updatecategory', views.updatecategory, name='updatecategory'),
    path('createcategory', views.createcategory, name='createcategory'),
    path('marquespage', views.marquespage, name='marquespage'),
    path('updatemarque', views.updatemarque, name='updatemarque'),
    path('createmarque', views.createmarque, name='createmarque'),
    path('checkref', views.checkref, name='checkref'),
    path('supplierspage', views.supplierspage, name='supplierspage'),
    path('addsupplier', views.addsupplier, name='addsupplier'),
    path('getsupplierdata', views.getsupplierdata, name='getsupplierdata'),
    path('updatesupplier', views.updatesupplier, name='updatesupplier'),
    path('addoneproduct', views.addoneproduct, name='addoneproduct'),
    path('viewoneproduct/<int:id>', views.viewoneproduct, name='viewoneproduct'),
    path('updateproduct', views.updateproduct, name='updateproduct'),
    path('alertstock', views.alertstock, name='alertstock'),
    path('getlowbycategory', views.getlowbycategory, name='getlowbycategory'),
    path('commandsupplier', views.commandsupplier, name='commandsupplier'),
    path('recevoir', views.recevoir, name='recevoir'),
    path('suppliercommanproducts', views.suppliercommanproducts, name='suppliercommanproducts'),
    path('searchref', views.searchref, name='searchref'),
    path('addsupply', views.addsupply, name='addsupply'),
    path('supplier/<int:id>', views.supplierinfo, name='supplierinfo'),
    path('client/<int:id>', views.clientinfo, name='clientinfo'),
    path('clientspage', views.clientspage, name='clientspage'),
    path('addclient', views.addclient, name='addclient'),
    path('getclientdata', views.getclientdata, name='getclientdata'),
    path('updateclient', views.updateclient, name='updateclient'),
    path('commercialspage', views.commercialspage, name='commercialspage'),
    path('addcommercial', views.addcommercial, name='addcommercial'),
    path('checkusername', views.checkusername, name='checkusername'),
    path('checkcodeclient', views.checkcodeclient, name='checkcodeclient'),
    path('bonlivraison', views.bonlivraison, name='bonlivraison'),
    path('updatecommercial', views.updatecommercial, name='updatecommercial'),
    path('getscommercialdata', views.getscommercialdata, name='getscommercialdata'),
    path('onereppage/<int:id>', views.onereppage, name='onereppage'),
    path('addbonlivraison', views.addbonlivraison, name='addbonlivraison'),
    path('bonlivraisondetails/<int:id>', views.bonlivraisondetails, name='bonlivraisondetails'),
    path('bonsortiedetails/<int:id>', checkviews.bonsortiedetails, name='bonsortiedetails'),
    path('getrepswithprice', views.getrepswithprice, name='getrepswithprice'),
    path('getclientprice', views.getclientprice, name='getclientprice'),
    path('listbonlivraison', views.listbonlivraison, name='listbonlivraison'),
    path('activerproduct', views.activerproduct, name='activerproduct'),
    path('desactiverproduct', views.desactiverproduct, name='desactiverproduct'),
    path('generatefacture/<int:id>', views.generatefacture, name='generatefacture'),
    path('createfacture', views.createfacture, name='createfacture'),
    path('modifierlivraison/<int:id>', views.modifierlivraison, name='modifierlivraison'),
    path('modifierfacture/<int:id>', views.modifierfacture, name='modifierfacture'),
    path('updatebonlivraison', views.updatebonlivraison, name='updatebonlivraison'),
    path('updatebonfacture', views.updatebonfacture, name='updatebonfacture'),
    path('listfactures', views.listfactures, name='listfactures'),
    path('degenerer', views.degenerer, name='degenerer'),
    path('facturedetails/<int:id>', views.facturedetails, name='facturedetails'),
    path('listreglementbl', views.listreglementbl, name='listreglementbl'),
    path('listreglementfc', views.listreglementfc, name='listreglementfc'),
    path('getclientbons', views.getclientbons, name='getclientbons'),
    path('getclientfactures', views.getclientfactures, name='getclientfactures'),
    path('reglebons', views.reglebons, name='reglebons'),
    path('checknpiece', views.checknpiece, name='checknpiece'),
    path('viewreglement/<int:id>', views.viewreglement, name='viewreglement'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('reglefactures', views.reglefactures, name='reglefactures'),
    path('situationcl', views.situationcl, name='situationcl'),
    path('avoirclient', views.avoirclient, name='avoirclient'),
    path('recevoirexcel', views.recevoirexcel, name='recevoirexcel'),
    path('addavoirclient', views.addavoirclient, name='addavoirclient'),
    path('checkbl/<int:id>', views.checkbl, name='checkbl'),
    path('checkfacture/<int:id>', views.checkfacture, name='checkfacture'),
    path('relevclient', views.relevclient, name='relevclient'),
    path('relevclientfc', views.relevclientfc, name='relevclientfc'),
    path('situationclfc', views.situationclfc, name='situationclfc'),
    path('getclientrep/<int:id>', views.getclientrep, name='getclientrep'),
    path('listbonachat', views.listbonachat, name='listbonachat'),
    path('bonachatdetails/<int:id>', views.bonachatdetails, name='bonachatdetails'),
    path('modifierbonachat/<int:id>', views.modifierbonachat, name='modifierbonachat'),
    path('updatebonachat', views.updatebonachat, name='updatebonachat'),
    path('updatebonachat', views.updatebonachat, name='updatebonachat'),
    path('listreglementsupp', views.listreglementsupp, name='listreglementsupp'),
    path('getsuppbons', views.getsuppbons, name='getsuppbons'),
    path('reglebonsachat', views.reglebonsachat, name='reglebonsachat'),
    path('journalachat', views.journalachat, name='journalachat'),
    path('searchproduct', views.searchproduct, name='searchproduct'),
    path('filterbldate', views.filterbldate, name='filterbldate'),
    path('searchclient', views.searchclient, name='searchclient'),
    path('searchsupplier', views.searchsupplier, name='searchsupplier'),
    path('journalvente', views.journalvente, name='journalvente'),
    path('situationsupplier', views.situationsupplier, name='situationsupplier'),
    path('facture', views.facture, name='facture'),
    path('getclientfactureprice', views.getclientfactureprice, name='getclientfactureprice'),
    path('addfacture', views.addfacture, name='addfacture'),
    path('getreglementbl/<int:id>', views.getreglementbl, name='getreglementbl'),
    path('updatereglebons', views.updatereglebons, name='updatereglebons'),
    path('getreglementfc/<int:id>', views.getreglementfc, name='getreglementfc'),
    path('updatereglefactures', views.updatereglefactures, name='updatereglefactures'),
    path('avoirsupplier', views.avoirsupplier, name='avoirsupplier'),
    path('addavoirsupp', views.addavoirsupp, name='addavoirsupp'),
    path('getlastsuppprice', views.getlastsuppprice, name='getlastsuppprice'),
    path('boncommandedetails/<int:id>', views.boncommandedetails, name='boncommandedetails'),
    path('genererbonlivraison/<int:id>', views.genererbonlivraison, name='genererbonlivraison'),
    path('createclientaccount', views.createclientaccount, name='createclientaccount'),
    path('listboncommnd', views.listboncommnd, name='listboncommnd'),
    path('carlogospage', views.carlogospage, name='carlogospage'),
    path('createlogo', views.createlogo, name='createlogo'),
    path('updatelogo', views.updatelogo, name='updatelogo'),
    path('getnotpaid', views.getnotpaid, name='getnotpaid'),
    path('filterfcdate', views.filterfcdate, name='filterfcdate'),
    path('filterachatdate', views.filterachatdate, name='filterachatdate'),
    path('updateclientpassword', views.updateclientpassword, name='updateclientpassword'),
    path('listavoirclient', views.listavoirclient, name='listavoirclient'),
    path('listavoirsupplier', views.listavoirsupplier, name='listavoirsupplier'),
    path('relevsupplier', views.relevsupplier, name='relevsupplier'),
    path('filterreglbldate', views.filterreglbldate, name='filterreglbldate'),
    path('filterreglfcdate', views.filterreglfcdate, name='filterreglfcdate'),
    path('sortupbl', views.sortupbl, name='sortupbl'),
    path('sortdownbl', views.sortdownbl, name='sortdownbl'),
    path('sortdownfc', views.sortdownfc, name='sortdownfc'),
    path('sortupfc', views.sortupfc, name='sortupfc'),
    path('journalventefc', views.journalventefc, name='journalventefc'),
    path('excelclients', views.excelclients, name='excelclients'),
    path('excelpdcts', views.excelpdcts, name='excelpdcts'),
    path('deactivateaccount', views.deactivateaccount, name='deactivateaccount'),
    path('activateaccount', views.activateaccount, name='activateaccount'),
    path('stocksection', views.stocksection, name='stocksection'),
    path('stock', views.stock, name='stock'),
    path('getreglementsupp/<int:id>', views.getreglementsupp, name='getreglementsupp'),
    path('updatereglesupp', views.updatereglesupp, name='updatereglesupp'),
    path('avoirdetails/<int:id>', views.avoirdetails, name='avoirdetails'),
    path('avoirsuppdetails/<int:id>', views.avoirsuppdetails, name='avoirsuppdetails'),
    path('modifieravoir/<int:id>', views.modifieravoir, name='modifieravoir'),
    path('updatebonavoir', views.updatebonavoir, name='updatebonavoir'),
    path('filternonreglr', views.filternonreglr, name='filternonreglr'),
    path('tabs', views.tabs, name='tabs'),
    path('notifyadmin', views.notifyadmin, name='notifyadmin'),
    path('listecheance', views.listecheance, name='listecheance'),
    path('echeancetoday', views.echeancetoday, name='echeancetoday'),
    path('disablenotif', views.disablenotif, name='disablenotif'),
    path('getconnectedusers', views.getconnectedusers, name='getconnectedusers'),
    path('payreglbl', views.payreglbl, name='payreglbl'),
    path('payreglfc', views.payreglfc, name='payreglfc'),
    path('boncommandes', views.boncommandes, name='boncommandes'),
    path('listeconnected', views.listeconnected, name='listeconnected'),
    path('promotionspage', views.promotionspage, name='promotionspage'),
    path('createpromotion', views.createpromotion, name='createpromotion'),
    path('updatepromotion', views.updatepromotion, name='updatepromotion'),
    path('filternonreglrfc', views.filternonreglrfc, name='filternonreglrfc'),
    path('updatereppassword', views.updatereppassword, name='updatereppassword'),
    path('createrepaccount', views.createrepaccount, name='createrepaccount'),
    path('searchproductsforstock', views.searchproductsforstock, name='searchproductsforstock'),
    path('loadstock/', views.loadstock, name='loadstock'),
    path('loadlistbl/', views.loadlistbl, name='loadlistbl'),
    path('loadlistachat/', views.loadlistachat, name='loadlistachat'),
    path('searchforlistbl', views.searchforlistbl, name='searchforlistbl'),
    path('searchforlistachat', views.searchforlistachat, name='searchforlistachat'),
    path('createnewrepaccount', views.createnewrepaccount, name='createnewrepaccount'),
    path('createnewclientaccount', views.createnewclientaccount, name='createnewclientaccount'),
    path('yeardatabl', views.yeardatabl, name='yeardatabl'),
    path('loadreglbl/', views.loadreglbl, name='loadreglbl'),
    path('loadclients/', views.loadclients, name='loadclients'),
    path('exportproducts', views.exportproducts, name='exportproducts'),
    path('loadjournalachat/', views.loadjournalachat, name='loadjournalachat'),
    path('loadjournalachatfc/', views.loadjournalachatfc, name='loadjournalachatfc'),
    path('loadjournalvente/', views.loadjournalvente, name='loadjournalvente'),
    path('loadjournalventefc/', views.loadjournalventefc, name='loadjournalventefc'),
    path('journalventefc', views.journalventefc, name='journalventefc'),
    path('exportbl', views.exportbl, name='exportbl'),
    path('datepdct', views.datepdct, name='datepdct'),
    path('exportfc', views.exportfc, name='exportfc'),
    path('searchforlistclient', views.searchforlistclient, name='searchforlistclient'),
    path('showdeactivated', views.showdeactivated, name='showdeactivated'),
    path('laodblregl/', views.laodblregl, name='laodblregl'),
    path('searchclientbls/', views.searchclientbls, name='searchclientbls'),
    path('searchregl', views.searchregl, name='searchregl'),
    path('laodblinupdateregl/', views.laodblinupdateregl, name='laodblinupdateregl'),
    path('loadlistfc/', views.loadlistfc, name='loadlistfc'),
    path('yeardatafc', views.yeardatafc, name='yeardatafc'),
    path('laodfcregl/', views.laodfcregl, name='laodfcregl'),
    path('searchclientfcs', views.searchclientfcs, name='searchclientfcs'),
    path('laodfcinupdateregl/', views.laodfcinupdateregl, name='laodfcinupdateregl'),
    path('searchclientfcsupdatereg', views.searchclientfcsupdatereg, name='searchclientfcsupdatereg'),
    path('yeardatajournalv', views.yeardatajournalv, name='yeardatajournalv'),
    path('searchclientblsupdatereg', views.searchclientblsupdatereg, name='searchclientblsupdatereg'),
    path('loadlistbc/', views.loadlistbc, name='loadlistbc'),
    path('yeardatabc', views.yeardatabc, name='yeardatabc'),
    path('journalachatfc', views.journalachatfc, name='journalachatfc'),
    path('getnotpaidfc', views.getnotpaidfc, name='getnotpaidfc'),
    path('searchforlistfc', views.searchforlistfc, name='searchforlistfc'),
    path('viewreglementfc/<int:id>', views.viewreglementfc, name='viewreglementfc'),
    path('searchreglfc', views.searchreglfc, name='searchreglfc'),
    path('yeardatareglfc', views.yeardatareglfc, name='yeardatareglfc'),
    path('filterbcdate', views.filterbcdate, name='filterbcdate'),
    path('deletebonachat', views.deletebonachat, name='deletebonachat'),
    path('searchforjv', views.searchforjv, name='searchforjv'),
    path('filterjvdate', views.filterjvdate, name='filterjvdate'),
    path('yeardatajournalvfc', views.yeardatajournalvfc, name='yeardatajournalvfc'),
    path('searchforjvfc', views.searchforjvfc, name='searchforjvfc'),
    path('filterjvfcdate', views.filterjvfcdate, name='filterjvfcdate'),
    path('filterjachdate', views.filterjachdate, name='filterjachdate'),
    path('searchforjach', views.searchforjach, name='searchforjach'),
    path('yeardatajach', views.yeardatajach, name='yeardatajach'),
    path('filterjachfcdate', views.filterjachfcdate, name='filterjachfcdate'),
    path('searchforjachfc', views.searchforjachfc, name='searchforjachfc'),
    path('yeardatajachfc', views.yeardatajachfc, name='yeardatajachfc'),
    path('updaterepdata', views.updaterepdata, name='updaterepdata'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('makebondelivered', views.makebondelivered, name='makebondelivered'),
    path('getitemsforlistbl', views.getitemsforlistbl, name='getitemsforlistbl'),
    path('refspage', views.refspage, name='refspage'),
    path('updateadmindata', views.updateadmindata, name='updateadmindata'),
    path('notavailable', views.notavailable, name='notavailable'),
    path('cartpage', views.cartpage, name='cartpage'),
    path('excelnotav', views.excelnotav, name='excelnotav'),
    path('addclientdivers', views.addclientdivers, name='addclientdivers'),
    path('deletereglbl', views.deletereglbl, name='deletereglbl'),
    path('deletereglfc', views.deletereglfc, name='deletereglfc'),
    path('changeclientbl', views.changeclientbl, name='changeclientbl'),
    path('comptable', views.comptable, name='comptable'),
    path('reliquatpage', views.reliquatpage, name='reliquatpage'),
    path('deletsearchedref', views.deletsearchedref, name='deletsearchedref'),
    path('getcompatbilse', views.getcompatbilse, name='getcompatbilse'),
    path('listnotifications', views.listnotifications, name='listnotifications'),
    path('addnotification', views.addnotification, name='addnotification'),
    path('updatenotification', views.updatenotification, name='updatenotification'),
    path('updatefacturenote', views.updatefacturenote, name='updatefacturenote'),
    path('updatefacturerep', views.updatefacturerep, name='updatefacturerep'),
    path('updateproductstock', views.updateproductstock, name='updateproductstock'),
    path('updatetransportbl', views.updatetransportbl, name='updatetransportbl'),
    path('updatenotebl', views.updatenotebl, name='updatenotebl'),
    path('updaterepbl', views.updaterepbl, name='updaterepbl'),
    path('stockupdated', views.stockupdated, name='stockupdated'),
    path('updateproductstockfc', views.updateproductstockfc, name='updateproductstockfc'),
    path('getclientcode', views.getclientcode, name='getclientcode'),
    path('allowcatalog', views.allowcatalog, name='allowcatalog'),
    path('filterepbons', views.filterepbons, name='filterepbons'),
    path('searchclientrep', views.searchclientrep, name='searchclientrep'),
    path('updateavoirnote', views.updateavoirnote, name='updateavoirnote'),
    path('getreliquatcommande', views.getreliquatcommande, name='getreliquatcommande'),
    path('printed', views.printed, name='printed'),
    path('getnongenerer', views.getnongenerer, name='getnongenerer'),
    path('addrepnote', views.addrepnote, name='addrepnote'),
    path('alertreliquatcommande', views.alertreliquatcommande, name='alertreliquatcommande'),
    path('makeitemsent', views.makeitemsent, name='makeitemsent'),
    path('updatedateavsupp', views.updatedateavsupp, name='updatedateavsupp'),
    path('sendrelevclient', views.sendrelevclient, name='sendrelevclient'),
    path('sendrelevclientfc', views.sendrelevclientfc, name='sendrelevclientfc'),
    path('sd52/8554/tsgs', views.tsgs, name='tsgs'),
    path('bons/bprint/12455t/bonlivraisonprint/<int:id>', views.bonlivraisonprint, name='bonlivraisonprint'),
    path('bons/bprint/12455t/boncmndprint/<int:id>', views.boncmndprint, name='boncmndprint'),
    path('bons/bprint/12455t/factureprint/<int:id>', views.factureprint, name='factureprint'),
    path('bons/bprint/12455t/bonachatprint/<int:id>', views.achatprint, name='achatprint'),
    path('refusedreglfc', views.refusedreglfc, name='refusedreglfc'),
    path('refusedreglbl', views.refusedreglbl, name='refusedreglbl'),
    path('bons/bprint/12455t/relevblprint', views.relevblprint, name='relevblprint'),
    path('bons/bprint/12455t/relevsuppprint', views.relevsuppprint, name='relevsuppprint'),
    path('bons/bprint/12455t/relevfcprint', views.relevfcprint, name='relevfcprint'),
    path('deletereglsupp', views.deletereglsupp, name='deletereglsupp'),
    path('cancelpdctnew', views.cancelpdctnew, name='cancelpdctnew'),
    path('makepdctnew', views.makepdctnew, name='makepdctnew'),
    path('etatblclients', views.etatblclients, name='etatblclients'),
    path('filterclients', views.filterclients, name='filterclients'),
    path('etatfcclients', views.etatfcclients, name='etatfcclients'),
    path('pdctrepport', views.pdctrepport, name='pdctrepport'),
    path('getpdctins', views.getpdctins, name='getpdctins'),
    path('getpdctouts', views.getpdctouts, name='getpdctouts'),
    path('pdctscategoryrepport', views.pdctscategoryrepport, name='pdctscategoryrepport'),
    path('commandpdct', views.commandpdct, name='commandpdct'),
    path('minstockpdct', views.minstockpdct, name='minstockpdct'),
    path('etude', views.etude, name='etude'),
    path('boncomparer', views.boncomparer, name='boncomparer'),
    path('getachatfacture', views.getachatfacture, name='getachatfacture'),
    path('yeardatabachat', views.yeardatabachat, name='yeardatabachat'),
    path('newfob', views.newfob, name='newfob'),
    path('etatblfc', views.etatblfc, name='etatblfc'),
    path('situationclblfc', views.situationclblfc, name='situationclblfc'),
    path('excelecheaces', views.excelecheaces, name='excelecheaces'),
    path('getnpiecedata', views.getnpiecedata, name='getnpiecedata'),
    path('saverowech', views.saverowech, name='saverowech'),
    path('getmonthecheances', views.getmonthecheances, name='getmonthecheances'),
    path('grouper', views.grouper, name='grouper'),
    path('searchforlistbc', views.searchforlistbc, name='searchforlistbc'),
    path('searchproductbonsortie', views.searchproductbonsortie, name='searchproductbonsortie'),
    # path('makebondelivered', views.makebondelivered, name='makebondelivered'),
    # path('makebondelivered', views.makebondelivered, name='makebondelivered'),
    # path('makebondelivered', views.makebondelivered, name='makebondelivered'),
    # path('makebondelivered', views.makebondelivered, name='makebondelivered'),
    # path('makebondelivered', views.makebondelivered, name='makebondelivered'),
    # path('makebondelivered', views.makebondelivered, name='makebondelivered'),
    path('checklivraisonno', checkviews.checklivraisonno, name='checklivraisonno'),
    path('checkfactureno', checkviews.checkfactureno, name='checkfactureno'),
    path('duplicate', checkviews.duplicate, name='duplicate'),
    path('ste1', checkviews.ste1, name='ste1'),
    path('ste2', checkviews.ste2, name='ste2'),
    path('pointdevente', checkviews.pointdevente, name='pointdevente'),
    path('bonsortie', checkviews.bonsortie, name='bonsortie'),
    path('addbonsortie', checkviews.addbonsortie, name='addbonsortie'),
    path('farahhome', checkviews.farahhome, name='farahhome'),
    path('clientsection', checkviews.clientsection, name='clientsection'),
    path('ventesection', checkviews.ventesection, name='ventesection'),
    path('achatsection', checkviews.achatsection, name='achatsection'),
    path('orghhome', checkviews.orghhome, name='orghhome'),
    path('listbonsortie', checkviews.listbonsortie, name='listbonsortie'),
    path('suppliersection', checkviews.suppliersection, name='suppliersection'),
    # path('checkfactureno', checkviews.checkfactureno, name='checkfactureno'),
    # path('checkfactureno', checkviews.checkfactureno, name='checkfactureno'),
]