app.factory('SearchSvc', function ($rootScope, $routeParams, $http, $q, $location, AppConst, NavbarSvc, TagSvc, ProjectRes) {
    var service={};

    service.allList=false;

    service.countItemsOnRow=3;

    service.title=AppConst.search.strings.title;
    service.searchText='';

    $rootScope.$on('navbar.change',function(event, eventRoute, current, previous){
        if (current.params!=undefined && current.params.navId!='search'){
            service.searchText='';
        }
    });

    service.doSearch=function(searchText){
        $location.path('/search/'+searchText);
    }

    service.init=function(reload){
        NavbarSvc.init('search');

        service.searchText=$routeParams.searchText;

        if ($routeParams.searchText!=undefined){
            service.allList=[];
            $q.all([
                TagSvc.load(),
                ProjectRes.getSearch($routeParams.searchText)
            ]).then(function(responseList) {
                for (var i=1;i<responseList.length;i++){
                    if (i==1)
                        service.allList.push({
                            name: 'project',
                            list: responseList[i].data.data
                        });
                }
            });
        }
    }
    return service;
  });