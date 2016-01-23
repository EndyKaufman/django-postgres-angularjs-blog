app.factory('ProjectSvc', function ($routeParams, $http, AppConst, NavbarSvc) {
    var service={};

    service.item=false;
    service.list=false;

    service.tags=['tag1', 'tag21', 'tag23', 'tag44','tag133', 'tag215', 'tag235', 'tag445','tag155', 'tag2155', 'tag23555', 'tag44555'];
    service.types=[
        {id:1,title:'Text'},
        {id:2,title:'Html'},
        {id:3,title:'Url'},
        {id:4,title:'Markdown'}
    ];

    service.projectUrl=AppConst.project.urls.url;
    service.tagUrl=AppConst.tag.urls.url;

    service.countItemsOnRow=2;

    service.title=AppConst.project.strings.title;

    service.getItem=function(name){
        return $http({
                  method: 'GET',
                  url: AppConst.project.urls.getData+'/item/'+name
               });
    };
    service.getList=function(){
        return $http({
                  method: 'GET',
                  url: AppConst.project.urls.getData+'/list'
               });
    };
    service.getSearch=function(searchText){
        return $http({
                  method: 'GET',
                  url: AppConst.project.urls.getData+'/search/'+searchText
               });
    };
    service.getListByTag=function(tagText){
        return $http({
                  method: 'GET',
                  url: AppConst.project.urls.getData+'/listbytag/'+tagText
               });
    };

    service.init=function(reload){
        NavbarSvc.init('project');

        if ($routeParams.projectName!=undefined){
            if (service.item.name!==$routeParams.projectName)
                service.getItem($routeParams.projectName).then(
                    function (response) {
                        service.item=response.data.data;
                    },
                    function (response) {
                        service.item={};
                        console.log('error', response);
                    }
                );
        }else{
            service.getList().then(function (response) {
                service.list=response.data.data.records;
                service.pageNumber=response.data.data.pageNumber;
                service.countRecordsOnPage=response.data.data.countRecordsOnPage;
                service.countAllRecords=response.data.data.countAllRecords;
            }, function (response) {
                service.list=[];
                console.log('error', response);
            });
        }
    }
    return service;
  });