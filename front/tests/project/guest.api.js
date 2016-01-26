describe('Project Guest API:', function() {
  var mytools = require('./../tools.js');

  var itemResponse = undefined, listbysearchResponse = undefined, listbytagResponse = undefined, listResponse = undefined, updateResponse = undefined;

  beforeEach(function(done){
    browser.driver.manage().window().setSize(1280, 1024);
    browser.get(browser.baseUrl).then(function(){
        mytools.getJson('/project/list', function(response){
            listResponse = response;
            var record = listResponse.data.records[0];

            mytools.getJson('/project/item/'+record.name, function(response){
                itemResponse = response;

                mytools.getJson('/project/listbytag/'+record.tags[0].text, function(response){
                    listbytagResponse = response;

                    mytools.getJson('/project/search/'+record.name, function(response){
                        listbysearchResponse = response;

                        done();
                    })
                })
            })
        })
    });
  });

  it('get /project/list and check structure', function() {
    expect(typeof listResponse).toEqual('object');
    expect(listResponse.code).toEqual('ok');
    var record = listResponse.data.records[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    expect(typeof listResponse.data.pageNumber).toEqual('number');
    expect(typeof listResponse.data.countRecordsOnPage).toEqual('number');
    expect(typeof listResponse.data.countAllRecords).toEqual('number');
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('get /project/item/:project_name and check structure', function() {
    expect(typeof itemResponse).toEqual('object');
    expect(itemResponse.code).toEqual('ok');
    var record = itemResponse.data;
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('get /project/listbytag/:tag_text and check structure', function() {
    expect(typeof listbytagResponse).toEqual('object');
    expect(listbytagResponse.code).toEqual('ok');
    var record = listbytagResponse.data.records[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    expect(typeof listbytagResponse.data.pageNumber).toEqual('number');
    expect(typeof listbytagResponse.data.countRecordsOnPage).toEqual('number');
    expect(typeof listbytagResponse.data.countAllRecords).toEqual('number');
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('get /project/search/:search_text and check structure', function() {
    expect(typeof listbysearchResponse).toEqual('object');
    expect(listbysearchResponse.code).toEqual('ok');
    var record = listbysearchResponse.data.records[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    expect(typeof listbysearchResponse.data.pageNumber).toEqual('number');
    expect(typeof listbysearchResponse.data.countRecordsOnPage).toEqual('number');
    expect(typeof listbysearchResponse.data.countAllRecords).toEqual('number');
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

});