describe('Project Guest API:', function() {
  var helpers = require('./../helpers.js');

  var itemResponse = undefined, listbysearchResponse = undefined, listbytagResponse = undefined, listResponse = undefined, updateResponse = undefined;
/*
  beforeEach(function(done){
    browser.driver.manage().window().setSize(1280, 1024);
    browser.get(browser.baseUrl).then(function(){
        helpers.getJson('/project/list', function(response){
            listResponse = response;
            var record = listResponse.data[0];

            helpers.getJson('/project/item/'+record.name, function(response){
                itemResponse = response;

                helpers.getJson('/project/listbytag/'+record.tags[0].text, function(response){
                    listbytagResponse = response;

                    helpers.getJson('/project/search/'+record.name, function(response){
                        listbysearchResponse = response;

                        done();
                    })
                })
            })
        })
    });
  });

  it('GET /project/list & check structure', function() {
    expect(typeof listResponse).toEqual('object');
    expect(listResponse.code).toEqual('ok');
    var record = listResponse.data[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('GET /project/item/:project_name & check structure', function() {
    expect(typeof itemResponse).toEqual('object');
    expect(itemResponse.code).toEqual('ok');
    var record = itemResponse.data[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('GET /project/listbytag/:tag_text & check structure', function() {
    expect(typeof listbytagResponse).toEqual('object');
    expect(listbytagResponse.code).toEqual('ok');
    var record = listbytagResponse.data[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('GET /project/search/:search_text & check structure', function() {
    expect(typeof listbysearchResponse).toEqual('object');
    expect(listbysearchResponse.code).toEqual('ok');
    var record = listbysearchResponse.data[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });
*/
});