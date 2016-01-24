app.factory('SearchSvc', function ($routeParams, $http, $q, AppConst, NavbarSvc, ProjectRes) {
    var service={};

    service.allList=false;

    service.countItemsOnRow=3;

    service.title=AppConst.search.strings.title;

    service.init=function(reload){
        NavbarSvc.init('search');

        service.searchText=$routeParams.searchText;

        if ($routeParams.searchText!=undefined){
            service.allList=[];
            $q.all([
                ProjectRes.getSearch($routeParams.searchText)
            ]).then(function(responseList) {
                for (var i=0;i<responseList.length;i++){
                    service.allList.push({
                        title: AppConst.project.strings.title,
                        url: AppConst.project.urls.url,
                        list: responseList[i].data.data.records
                    });
                }
            });
        }
    }
    return service;
  });