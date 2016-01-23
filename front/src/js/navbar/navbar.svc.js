app.factory('NavbarSvc', function ($routeParams, $route, $rootScope, $location, AppConst) {
    var service={};

    function modifiItem(item){
        var navItem={};

        if (item.parent!=undefined && AppConst[item.parent]!=undefined && AppConst[item.parent][item.name]!=undefined)
            navItem=AppConst[item.parent][item.name];
        if (AppConst[item.name]!=undefined)
            navItem=AppConst[item.name];

        if (navItem.title!=undefined)
            item.title=navItem.title;
        if (navItem.url!=undefined)
            item.url=navItem.url;
        if (navItem.strings!=undefined && navItem.strings.title!=undefined)
            item.title=navItem.strings.title;
        if (navItem.urls!=undefined && navItem.urls.url!=undefined)
            item.url=navItem.urls.url;

        item.active=(item.name==$routeParams.navId);
        if (item.hiddenHandler!=undefined)
            item.hidden=item.hiddenHandler();
        else
            if (item.hidden===undefined)
                item.hidden=false;
    }

    service.goHome=function(){
        $location.path(service.brand.url.replace('#',''));
    }

    service.doSearch=function(searchText){
        $location.path(AppConst.search.urls.url.replace('#','')+'/'+searchText);
    }

    service.init=function(navId){
        if (navId!=undefined)
            $routeParams.navId=navId;
        else
        if ($route.current.$$route.navId!=undefined)
            $routeParams.navId=$route.current.$$route.navId;

        service.brand=AppConst.brand;
        service.items=AppConst.navbar;
        for (var i=0;i<service.items.left.length;i++){
            modifiItem(service.items.left[i]);
        }
        for (var i=0;i<service.items.right.length;i++){
            modifiItem(service.items.right[i]);
        }
    }

    return service;
  });