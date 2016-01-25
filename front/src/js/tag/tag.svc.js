app.factory('TagSvc', function ($routeParams, $http, $q, $rootScope, AppConst, TagRes, ProjectRes, NavbarSvc) {
    var service={};

    service.list=false;
    service.allList=false;

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

    service.searchTag=function(query){
        var list=[];
        for (var i=0;i<service.list.length;i++){
            if (service.list[i].text.indexOf(query)!=-1)
                list.push(service.list[i]);
        }
        return list;
    }

    service.load=function(){
        var deferred = $q.defer();
        if (service.list===false)
            TagRes.getList().then(function (response) {
                var data=angular.copy(response.data.data);
                service.list=data.records;
                service.pageNumber=data.pageNumber;
                service.countRecordsOnPage=data.countRecordsOnPage;
                service.countAllRecords=data.countAllRecords;
                deferred.resolve(service.list);
                $rootScope.$broadcast('tag.load', service.list);
            },
            function (response) {
                service.list=[];
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, {
                        object: service
                    });
                deferred.resolve(service.list);
            })
        else
            deferred.resolve(service.list);
        return deferred.promise;
    }
    return service;
  });