app.factory('NavbarSvc', function ($routeParams, $rootScope, $route, $location, $window, AppConst) {
    var service={};

    $rootScope.$on('$routeChangeStart',function(event, current, previous){
        service.init();
        $rootScope.$broadcast('navbar.change', event, current, previous);
    });

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

        if (item.url===undefined)
            item.url='#/'+item.name;

        item.active=(item.name==$routeParams.navId);
        if (item.hiddenHandler!=undefined)
            item.hidden=item.hiddenHandler();
        else
            if (item.hidden===undefined)
                item.hidden=false;
    }

    service.goBack=function(){
        console.log($window.history.length);
        if ($window.history.length>2)
            $window.history.back();
        else
            service.goHome();
    }
    service.goHome=function(){
        $location.path(service.homeUrl);
    }

    service.init=function(navId){
        if (navId!=undefined)
            $routeParams.navId=navId;
        else
        if ($route.current !== undefined && $route.current.$$route!==undefined && $route.current.$$route.navId!=undefined)
            $routeParams.navId=$route.current.$$route.navId
        else
        if ($route.current !== undefined && $route.current.params!==undefined && $route.current.params.navId!=undefined)
            $routeParams.navId=$route.current.params.navId;

        service.homeUrl=AppConst.homeUrl;
        service.brand=AppConst.brand;
        service.items=AppConst.navbar;
        for (var i=0;i<service.items.left.length;i++){
            modifiItem(service.items.left[i]);
        }
        for (var i=0;i<service.items.right.length;i++){
            modifiItem(service.items.right[i]);
        }
        $rootScope.$broadcast('navbar.change', false, {current:{params:{navId:$routeParams.navId}}}, false);
    }

    return service;
  });