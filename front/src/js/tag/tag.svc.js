app.factory('TagSvc', function ($routeParams, $http, $q, $rootScope, AppConst, TagRes, ProjectRes, NavbarSvc) {
    var service={};

    service.list=false;
    service.allList=false;

    service.tagUrl=AppConst.tag.urls.url;

    service.countItemsOnRow=3;

    service.title=AppConst.tag.strings.title;

    service.init=function(reload){
        NavbarSvc.init('tag');

        service.tagText=$routeParams.tagText;

        if ($routeParams.tagText!=undefined){
            service.allList=[];
            $q.all([
                service.load(),
                ProjectRes.getListByTag($routeParams.tagText)
            ]).then(function(responseList) {
                for (var i=1;i<responseList.length;i++){
                    service.allList.push({
                        title: AppConst.project.strings.title,
                        url: AppConst.project.urls.url,
                        list: responseList[i].data.data.records
                    });
                }
            });
        }
    }

    service.load=function(){
        var deferred = $q.defer();
        if (service.list===false)
            TagRes.getList().then(function (response) {
                service.list=response.data.data.records;
                service.pageNumber=response.data.data.pageNumber;
                service.countRecordsOnPage=response.data.data.countRecordsOnPage;
                service.countAllRecords=response.data.data.countAllRecords;
                deferred.resolve(service.list);
                $rootScope.$broadcast('tag.load', service.list);
            },
            function (response) {
                service.list=[];
                console.log('error', response);
                deferred.resolve(service.list);
            })
        else
            deferred.resolve(service.list);
        return deferred.promise;
    }
    return service;
  });