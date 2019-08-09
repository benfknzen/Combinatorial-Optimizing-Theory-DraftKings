import scrapy
from tutorial.items import UfcStats
from scrapy.loader import ItemLoader
linker = []
i = 0
item_universal = []
item = UfcStats()

class UfcScrape(scrapy.Spider):
    name = "mmaspider"
    # allowed_domains = ['ufcstats.com']  Giving me a lot of issues 3.30.2019
    # response.css('a::attr(href)').getall()
    # links to dive into:  links = response.xpath('//a[contains(@href, "fighter-details")]/@href').extract()
    # start_urls = [
    #  'http://ufcstats.com/event-details/2f8f3c69522db931',
    #  'http://ufcstats.com/event-details/6c9383ffab2725a5',
    #  'http://ufcstats.com/event-details/c0c1bc0766df4c00',
    #  'http://ufcstats.com/event-details/b16a7e6a627e9789',
    #  'http://ufcstats.com/event-details/e31502e3f79d00c5',
    #  'http://ufcstats.com/event-details/cbc071cb20ea59c7',
    #  'http://ufcstats.com/event-details/6b8f28da9a483049',
    #  'http://ufcstats.com/event-details/9de7c97e1c0d7927',
    #  'http://ufcstats.com/event-details/351264d11286d09a',
    #  'http://ufcstats.com/event-details/c912f676692c353a',
    #  'http://ufcstats.com/event-details/7dcf06c1967801c1',
    #  'http://ufcstats.com/event-details/b0550072e5f0afa7',
    #  'http://ufcstats.com/event-details/9649d75defe0dedb',
    #  'http://ufcstats.com/event-details/487c170da059857d',
    #  'http://ufcstats.com/event-details/80eacd4da0617c57',
    #  'http://ufcstats.com/event-details/e96d8538d3f9d0ed',
    #  'http://ufcstats.com/event-details/2d5fbe2103f97053',
    #  'http://ufcstats.com/event-details/6546af7ab545b90c',
    #  'http://ufcstats.com/event-details/a7a79b8efbceaaac',
    #  'http://ufcstats.com/event-details/b5882371e2a3900d',
    #  'http://ufcstats.com/event-details/84283233ec42be5f',
    #  'http://ufcstats.com/event-details/d4da8995fc91e7ef',
    #  'http://ufcstats.com/event-details/c046100aea0dba9a',
    #  'http://ufcstats.com/event-details/7a703c565ccaa18f',
    #  'http://ufcstats.com/event-details/2a74bbba57058f12',
    #  'http://ufcstats.com/event-details/d1d20e651e6cbc02',
    #  'http://ufcstats.com/event-details/c7ac79839e86ce33',
    #  'http://ufcstats.com/event-details/de25520d54eab12d',
    #  'http://ufcstats.com/event-details/aa3153a9941b4d44',
    #  'http://ufcstats.com/event-details/42c96a9c4802e2e1',
    #  'http://ufcstats.com/event-details/20821819c401ced8',
    #  'http://ufcstats.com/event-details/33a331684283900f',
    #  'http://ufcstats.com/event-details/1ef0eae31904e534',
    #  'http://ufcstats.com/event-details/852454c572675334',
    #  'http://ufcstats.com/event-details/8d49545dadf9b919',
    #  'http://ufcstats.com/event-details/d5ae8074631762fc',
    #  'http://ufcstats.com/event-details/c0342805a1948cbb',
    #  'http://ufcstats.com/event-details/03b1e846b09f721d',
    #  'http://ufcstats.com/event-details/322a56923b396b4d',
    #  'http://ufcstats.com/event-details/4f732e58ed907eff',
    #  'http://ufcstats.com/event-details/b45d6b73f4ca4467',
    #  'http://ufcstats.com/event-details/35585d970300d45a',
    #  'http://ufcstats.com/event-details/8215e4fe24e8e81b',
    #  'http://ufcstats.com/event-details/ac5f67109accb482',
    #  'http://ufcstats.com/event-details/2eae41f61776c60f',
    #  'http://ufcstats.com/event-details/d29b5c4f22c6357d',
    #  'http://ufcstats.com/event-details/f5990c11974d8e9c',
    #  'http://ufcstats.com/event-details/3144121470023e9a',
    #  'http://ufcstats.com/event-details/67ec58d7cf599835',
    #  'http://ufcstats.com/event-details/ad99fa5325519169',
    #  'http://ufcstats.com/event-details/620be7e0712d431b',
    #  'http://ufcstats.com/event-details/49e7e05f902479ca',
    #  'http://ufcstats.com/event-details/eed2b71d77d95416',
    #  'http://ufcstats.com/event-details/7929be8290289a47',
    #  'http://ufcstats.com/event-details/daa89f01e1c0f42a',
    #  'http://ufcstats.com/event-details/d181689653115b6a',
    #  'http://ufcstats.com/event-details/15515e797aedc137',
    #  'http://ufcstats.com/event-details/7cf20446453f852b',
    #  'http://ufcstats.com/event-details/602bb270f2bdbf02',
    #  'http://ufcstats.com/event-details/02177caefe7c07d4',
    #  'http://ufcstats.com/event-details/fc1868f56d3036eb',
    #  'http://ufcstats.com/event-details/04076783ca83d6ae',
    #  'http://ufcstats.com/event-details/eaa0a728cc91ef60',
    #  'http://ufcstats.com/event-details/bcd124bcd3d5be46',
    #  'http://ufcstats.com/event-details/9e30f69cc0869301',
    #  'http://ufcstats.com/event-details/30e8b4505f5ccf92',
    #  'http://ufcstats.com/event-details/e7bc606d269896aa',
    #  'http://ufcstats.com/event-details/caced97768818230',
    #  'http://ufcstats.com/event-details/d856a0080ac09ed7',
    #  'http://ufcstats.com/event-details/a25b71fe5e31fa97',
    #  'http://ufcstats.com/event-details/a7724f51e32e763e',
    #  'http://ufcstats.com/event-details/d6b68eaf4b68b160',
    #  'http://ufcstats.com/event-details/cc5834a495d1ea08',
    #  'http://ufcstats.com/event-details/9211aae062b799d6',
    #  'http://ufcstats.com/event-details/1979c80150f630c4',
    #  'http://ufcstats.com/event-details/d86e913c548c07c2',
    #  'http://ufcstats.com/event-details/a3244e3238541482',
    #  'http://ufcstats.com/event-details/f4a031ac205ac580',
    #  'http://ufcstats.com/event-details/ff9578cdbfabd323',
    #  'http://ufcstats.com/event-details/9f3d6ddef3d3cccc',
    #  'http://ufcstats.com/event-details/d7907a9a968e4d29',
    #  'http://ufcstats.com/event-details/686cccbf1a4de453',
    #  'http://ufcstats.com/event-details/23bd78c3f89bdb54',
    #  'http://ufcstats.com/event-details/99bf06f20491cb54',
    #  'http://ufcstats.com/event-details/353de740bb6c7e75',
    #  'http://ufcstats.com/event-details/90e7447d8b7f3f35',
    #  'http://ufcstats.com/event-details/1507214bbc7a79e2',
    #  'http://ufcstats.com/event-details/1c7cce2f5c17160d',
    #  'http://ufcstats.com/event-details/5df10509264586e5',
    #  'http://ufcstats.com/event-details/bc7f7f0ba3db74d2',
    #  'http://ufcstats.com/event-details/ed069a95aaaf4f56',
    #  'http://ufcstats.com/event-details/e7bfdb5e0112891e',
    #  'http://ufcstats.com/event-details/c0231720fe516994',
    #  'http://ufcstats.com/event-details/47b7e4e60813b7b2',
    #  'http://ufcstats.com/event-details/20e403a1acfef130',
    #  'http://ufcstats.com/event-details/b4ad3a06ee4d660c',
    #  'http://ufcstats.com/event-details/865aa315ea62c511',
    #  'http://ufcstats.com/event-details/6a8a06b542e1516d',
    #  'http://ufcstats.com/event-details/4512e46543b960ad',
    #  'http://ufcstats.com/event-details/46effbd1135423c5',
    #  'http://ufcstats.com/event-details/4b2390cfaceb91d8',
    #  'http://ufcstats.com/event-details/32541eb5d12668b4',
    #  'http://ufcstats.com/event-details/6e3282d57d2467a0',
    #  'http://ufcstats.com/event-details/7139cd2ae4bf6a29',
    #  'http://ufcstats.com/event-details/bd4389b71fdc0ce2',
    #  'http://ufcstats.com/event-details/73e09f837f3b5ecc',
    #  'http://ufcstats.com/event-details/5cde96e0a1a1fffe',
    #  'http://ufcstats.com/event-details/6810d8d2dd557cf9',
    #  'http://ufcstats.com/event-details/4956f60b7fa57c1a',
    #  'http://ufcstats.com/event-details/6083f497c22cc075',
    #  'http://ufcstats.com/event-details/154a6b3ffae264cd',
    #  'http://ufcstats.com/event-details/a196332ee4aa8a82',
    #  'http://ufcstats.com/event-details/e18012194473e8b0',
    #  'http://ufcstats.com/event-details/d6455cb4bee503ce',
    #  'http://ufcstats.com/event-details/2dc7f1762dc0a7ef',
    #  'http://ufcstats.com/event-details/2b4faacc16d66898',
    #  'http://ufcstats.com/event-details/cfbccfed4e4796fe',
    #  'http://ufcstats.com/event-details/5da4e8dc02e50ac0',
    #  'http://ufcstats.com/event-details/232c582f29f8f65e',
    #  'http://ufcstats.com/event-details/72cbe507644a587c',
    #  'http://ufcstats.com/event-details/8a028648f3f0761d',
    #  'http://ufcstats.com/event-details/5e7a28f20927d64a',
    #  'http://ufcstats.com/event-details/aa5b4eff51bdc7d1',
    #  'http://ufcstats.com/event-details/cd42bbe8887bba90',
    #  'http://ufcstats.com/event-details/45a2ba3ef82b9700',
    #  'http://ufcstats.com/event-details/563d051c9e769b24',
    #  'http://ufcstats.com/event-details/ff4c3ab594c7fac3',
    #  'http://ufcstats.com/event-details/990060b2a68a7b82',
    #  'http://ufcstats.com/event-details/a4bf17bd3ba3423b',
    #  'http://ufcstats.com/event-details/a314687f372b2cec',
    #  'http://ufcstats.com/event-details/3d481aa374c954a1',
    #  'http://ufcstats.com/event-details/e7e970d508529bf3',
    #  'http://ufcstats.com/event-details/4887e5bc4dbb73ff',
    #  'http://ufcstats.com/event-details/e60201cfab7d656d',
    #  'http://ufcstats.com/event-details/db1f2ed63b54b9a7',
    #  'http://ufcstats.com/event-details/39c568f8c579913e',
    #  'http://ufcstats.com/event-details/d56bb6dff2ae77eb',
    #  'http://ufcstats.com/event-details/de99da2c0d18d34a',
    #  'http://ufcstats.com/event-details/b3fb8d2293e17a59',
    #  'http://ufcstats.com/event-details/c6becb722706c7d8',
    #  'http://ufcstats.com/event-details/380e8b023290d091',
    #  'http://ufcstats.com/event-details/80d918336163b80c',
    #  'http://ufcstats.com/event-details/354808cf38d9d73c',
    #  'http://ufcstats.com/event-details/20fbff570c678e1c',
    #  'http://ufcstats.com/event-details/dd39f1ca787a3d9d',
    #  'http://ufcstats.com/event-details/4d636c3aa1105950',
    #  'http://ufcstats.com/event-details/243b07fc65ccbb16',
    #  'http://ufcstats.com/event-details/8d04923f2db59b7f',
    #  'http://ufcstats.com/event-details/5345f86680378fc1',
    #  'http://ufcstats.com/event-details/f3155a94ca420126',
    #  'http://ufcstats.com/event-details/119ebea97e914dcf',
    #  'http://ufcstats.com/event-details/a4dd5c9a75763295',
    #  'http://ufcstats.com/event-details/82f5c81f4e3c3eb5',
    #  'http://ufcstats.com/event-details/2ce6541127b0e232',
    #  'http://ufcstats.com/event-details/b71667c778b6d9e5',
    #  'http://ufcstats.com/event-details/a9c45a8b21eabadc',
    #  'http://ufcstats.com/event-details/0c3838c8f7c620c2',
    #  'http://ufcstats.com/event-details/ef7fa30364cbe7f2',
    #  'http://ufcstats.com/event-details/36877f0e62b25b96',
    #  'http://ufcstats.com/event-details/a890f9a791ed615d',
    #  'http://ufcstats.com/event-details/3be081c29bf734d9',
    #  'http://ufcstats.com/event-details/86e388ed20761ad9',
    #  'http://ufcstats.com/event-details/194fc025f9355db6',
    #  'http://ufcstats.com/event-details/a58114c6dd0add64',
    #  'http://ufcstats.com/event-details/06dc1a58663579d2',
    #  'http://ufcstats.com/event-details/aae0897825336b1a',
    #  'http://ufcstats.com/event-details/4f7e290e71d60f87',
    #  'http://ufcstats.com/event-details/b1605ea39fba6af6',
    #  'http://ufcstats.com/event-details/8a1b4330c7957961',
    #  'http://ufcstats.com/event-details/997b4f52f76a0b53',
    #  'http://ufcstats.com/event-details/bc7cf284c1c2f16e',
    #  'http://ufcstats.com/event-details/5de61b03868035ff',
    #  'http://ufcstats.com/event-details/16d09e800ad7ec79',
    #  'http://ufcstats.com/event-details/fa534853eb195270',
    #  'http://ufcstats.com/event-details/f54200f1dfb9b5d4',
    #  'http://ufcstats.com/event-details/ad4e9055bf8cd04d',
    #  'http://ufcstats.com/event-details/0577808d22dfe79c',
    #  'http://ufcstats.com/event-details/f9c7fe2682af3802',
    #  'http://ufcstats.com/event-details/43563a32c3f10e95',
    #  'http://ufcstats.com/event-details/706404da0775dcbc',
    #  'http://ufcstats.com/event-details/f9aa6376ae16bfb4',
    #  'http://ufcstats.com/event-details/a72d260b436924c4',
    #  'http://ufcstats.com/event-details/4e5bbc4566049cbf',
    #  'http://ufcstats.com/event-details/d4a12dfa4067742f',
    #  'http://ufcstats.com/event-details/222d6b547de2e035',
    #  'http://ufcstats.com/event-details/dfdd0c5dd0d4bc23',
    #  'http://ufcstats.com/event-details/155a02a8b4311057',
    #  'http://ufcstats.com/event-details/59851163aaf1aed8',
    #  'http://ufcstats.com/event-details/6ca68b636fbc1f18',
    #  'http://ufcstats.com/event-details/371a1c91b24dec2b',
    #  'http://ufcstats.com/event-details/53f02bbc41d99432',
    #  'http://ufcstats.com/event-details/0313bf497de9c470',
    #  'http://ufcstats.com/event-details/8dc4f34c1f50d00d',
    #  'http://ufcstats.com/event-details/3bb030257966b022',
    #  'http://ufcstats.com/event-details/2dea80c069847321',
    #  'http://ufcstats.com/event-details/a71feb7ea7592a71',
    #  'http://ufcstats.com/event-details/9bcfb40dbcd50568',
    #  'http://ufcstats.com/event-details/269d103c96a4c3a5',
    #  'http://ufcstats.com/event-details/063649e21bc9d6d5',
    #  'http://ufcstats.com/event-details/770b9d4813c25902',
    #  'http://ufcstats.com/event-details/fd7acf42bd6e7e95',
    #  'http://ufcstats.com/event-details/05fbfe628658c538',
    #  'http://ufcstats.com/event-details/073eee4e62f0d988',
    #  'http://ufcstats.com/event-details/79ded75550efc139',
    #  'http://ufcstats.com/event-details/1c5879330d42255f',
    #  'http://ufcstats.com/event-details/53adf5b845d91e4a',
    #  'http://ufcstats.com/event-details/c0ed7b208197e8de',
    #  'http://ufcstats.com/event-details/ac9521250dc1a14c',
    #  'http://ufcstats.com/event-details/5b5307450405abf0',
    #  'http://ufcstats.com/event-details/1fcfc3709fe58151',
    #  'http://ufcstats.com/event-details/59aaf2730b84698a',
    #  'http://ufcstats.com/event-details/b757c73f443d4fca',
    #  'http://ufcstats.com/event-details/9ca265dfe8323db3',
    #  'http://ufcstats.com/event-details/579fcdfcabd23a7b',
    #  'http://ufcstats.com/event-details/4f2fcbefb668689d',
    #  'http://ufcstats.com/event-details/a421465acbe59c77',
    #  'http://ufcstats.com/event-details/f9f07bb5a43535ed',
    #  'http://ufcstats.com/event-details/d632d156c0549e07',
    #  'http://ufcstats.com/event-details/d5f820c11a121050',
    #  'http://ufcstats.com/event-details/179f1948dc234f1f',
    #  'http://ufcstats.com/event-details/ebc1f40e00e0c481',
    #  'http://ufcstats.com/event-details/a26198ba5093147e',
    #  'http://ufcstats.com/event-details/3138fab619faf4d1',
    #  'http://ufcstats.com/event-details/51b0bb73a1da34bc',
    #  'http://ufcstats.com/event-details/fc31f896cde2bc2e',
    #  'http://ufcstats.com/event-details/a8d521d913df4e31',
    #  'http://ufcstats.com/event-details/30a09e43f15f1d75',
    #  'http://ufcstats.com/event-details/e5c9de15bb58b1c6',
    #  'http://ufcstats.com/event-details/83d0de122f2f9664',
    #  'http://ufcstats.com/event-details/480b702debcb5433',
    #  'http://ufcstats.com/event-details/ee457ef1e1c326c1',
    #  'http://ufcstats.com/event-details/9a967e8e43dcef63',
    #  'http://ufcstats.com/event-details/28f3c2258a1d8874',
    #  'http://ufcstats.com/event-details/5d7c18191b8aa432',
    #  'http://ufcstats.com/event-details/35dc6220b113b7ec',
    #  'http://ufcstats.com/event-details/60884f31ead1609c',
    #  'http://ufcstats.com/event-details/eae4aec1a5a8ff01',
    #  'http://ufcstats.com/event-details/43612456979e5d5e',
    #  'http://ufcstats.com/event-details/df5a77121ba84a5d',
    #  'http://ufcstats.com/event-details/b23fca14c7b79935',
    #  'http://ufcstats.com/event-details/980b4e712489098e',
    #  'http://ufcstats.com/event-details/e5c38954c006f15c',
    #  'http://ufcstats.com/event-details/cf1a88371c8cb690',
    #  'http://ufcstats.com/event-details/ebc5af72ad5a28cb',
    #  'http://ufcstats.com/event-details/5330fe7e4c3af81c',
    #  'http://ufcstats.com/event-details/e0b74df14f52cd15',
    #  'http://ufcstats.com/event-details/8fd1f27e86661ede',
    #  'http://ufcstats.com/event-details/7865707fd684d77b',
    #  'http://ufcstats.com/event-details/3c241737a6069b9f',
    #  'http://ufcstats.com/event-details/030f08370fd1c2bb',
    #  'http://ufcstats.com/event-details/ea0ad155451ed1f5',
    #  'http://ufcstats.com/event-details/aa79d5399571068e',
    #  'http://ufcstats.com/event-details/ce47f49e5c386a9c',
    #  'http://ufcstats.com/event-details/6291ac0a3726732f',
    #  'http://ufcstats.com/event-details/f1b2a4365799c48b',
    #  'http://ufcstats.com/event-details/83c6c3e0f8bde8ee',
    #  'http://ufcstats.com/event-details/09c44b317c98bf96',
    #  'http://ufcstats.com/event-details/4679a38cced7c64a',
    #  'http://ufcstats.com/event-details/601cf40c09090853',
    #  'http://ufcstats.com/event-details/738acab0c6934dd8',
    #  'http://ufcstats.com/event-details/56f4b81ec4db61af',
    #  'http://ufcstats.com/event-details/c6e6926a81adcd00',
    #  'http://ufcstats.com/event-details/c6da1c24fe473418',
    #  'http://ufcstats.com/event-details/e8c170a64dc920ac',
    #  'http://ufcstats.com/event-details/d1e6a6536ee62517',
    #  'http://ufcstats.com/event-details/d41937647eae9a34',
    #  'http://ufcstats.com/event-details/319fa1bd3176bded',
    #  'http://ufcstats.com/event-details/96d173b7f92aa520',
    #  'http://ufcstats.com/event-details/6a0b80a24f22e152',
    #  'http://ufcstats.com/event-details/6cbb7661c3258617',
    #  'http://ufcstats.com/event-details/53e533db1b8e9712',
    #  'http://ufcstats.com/event-details/3c48019bc387b80c',
    #  'http://ufcstats.com/event-details/f62850b3c7480db9',
    #  'http://ufcstats.com/event-details/abbc4fc02e0d84b3',
    #  'http://ufcstats.com/event-details/d3b5ad3b15a64a18',
    #  'http://ufcstats.com/event-details/e8efeb9cf33b1941',
    #  'http://ufcstats.com/event-details/3da19339ee7051d5',
    #  'http://ufcstats.com/event-details/505934897b8b4824',
    #  'http://ufcstats.com/event-details/49590e0508b2c19f',
    #  'http://ufcstats.com/event-details/96087e90d900f0ef',
    #  'http://ufcstats.com/event-details/4985113c0928aa62',
    #  'http://ufcstats.com/event-details/8caca5857ce0e30b',
    #  'http://ufcstats.com/event-details/5898357a45a73674',
    #  'http://ufcstats.com/event-details/155bfc7ed36622df',
    #  'http://ufcstats.com/event-details/21f2974fd08085e3',
    #  'http://ufcstats.com/event-details/b5ea750025697880',
    #  'http://ufcstats.com/event-details/8377c5572cb356f3',
    #  'http://ufcstats.com/event-details/0a97691039c4bbfb',
    #  'http://ufcstats.com/event-details/df2cf66d8c0123db',
    #  'http://ufcstats.com/event-details/c3c23c99477c041b',
    #  'http://ufcstats.com/event-details/4d74641fac830182',
    #  'http://ufcstats.com/event-details/18524b46c570730b',
    #  'http://ufcstats.com/event-details/91720876db0ee468',
    #  'http://ufcstats.com/event-details/6d7886b094b471ac',
    #  'http://ufcstats.com/event-details/1f5f75658551f2d3',
    #  'http://ufcstats.com/event-details/0ec821423baa26bd',
    #  'http://ufcstats.com/event-details/1c061eb6e29eaa0a',
    #  'http://ufcstats.com/event-details/e780ccc79a209985',
    #  'http://ufcstats.com/event-details/8788beb528894f33',
    #  'http://ufcstats.com/event-details/7d5b12de1625984e',
    #  'http://ufcstats.com/event-details/44f9c777fed7ca03',
    #  'http://ufcstats.com/event-details/73ef22f25d0f70e2',
    #  'http://ufcstats.com/event-details/1ffc38f67785797b',
    #  'http://ufcstats.com/event-details/18968f97ad34f15c',
    #  'http://ufcstats.com/event-details/4c8d6fde2dde07c4',
    #  'http://ufcstats.com/event-details/f1f9e48a0d150757',
    #  'http://ufcstats.com/event-details/83fd97284f4bb4a4',
    #  'http://ufcstats.com/event-details/d023ae89a2a4a41e',
    #  'http://ufcstats.com/event-details/aac5ac38148f0528',
    #  'http://ufcstats.com/event-details/3ba3b5cc94498437',
    #  'http://ufcstats.com/event-details/b732b326c362fb62',
    #  'http://ufcstats.com/event-details/2db7fa8db6bc9632',
    #  'http://ufcstats.com/event-details/8a59d346dc976a10',
    #  'http://ufcstats.com/event-details/1411c630ba711b64',
    #  'http://ufcstats.com/event-details/a54fc2d6fc224dc3',
    #  'http://ufcstats.com/event-details/88a9bc81271ccd89',
    #  'http://ufcstats.com/event-details/65ddc8a9ac4e8531',
    #  'http://ufcstats.com/event-details/282fa667ff9c51ed',
    #  'http://ufcstats.com/event-details/d1152823307d7e7c',
    #  'http://ufcstats.com/event-details/132f860d02953f4c',
    #  'http://ufcstats.com/event-details/5d7bdab5e03e3216',
    #  'http://ufcstats.com/event-details/dd992d569aaebee6',
    #  'http://ufcstats.com/event-details/0ff11cc094e887bc',
    #  'http://ufcstats.com/event-details/afdb76fbd86f6d11',
    #  'http://ufcstats.com/event-details/d512d9f204059f57',
    #  'http://ufcstats.com/event-details/ad32471f01e7b1a5',
    #  'http://ufcstats.com/event-details/acff437707625fc7',
    #  'http://ufcstats.com/event-details/054defd5420a551f',
    #  'http://ufcstats.com/event-details/2f3f12002564bb55',
    #  'http://ufcstats.com/event-details/f12f979b657ab876',
    #  'http://ufcstats.com/event-details/140745cbbcb023ac',
    #  'http://ufcstats.com/event-details/9bcf8603ceb25680',
    #  'http://ufcstats.com/event-details/cfb65863d5099327',
    #  'http://ufcstats.com/event-details/bfc2fc38a0e20211',
    #  'http://ufcstats.com/event-details/d0c29452d3272603',
    #  'http://ufcstats.com/event-details/24b033b3daf1c9df',
    #  'http://ufcstats.com/event-details/3ed134d85dfbd7b4',
    #  'http://ufcstats.com/event-details/c80095f6092271a7',
    #  'http://ufcstats.com/event-details/3795fca327cbcf23',
    #  'http://ufcstats.com/event-details/49efbdc6c9f650c4',
    #  'http://ufcstats.com/event-details/15edcf67ccf5be84',
    #  'http://ufcstats.com/event-details/58bc81376286b3d3',
    #  'http://ufcstats.com/event-details/a6d8bfe9e0c8153b',
    #  'http://ufcstats.com/event-details/821cd80aab70d5f9',
    #  'http://ufcstats.com/event-details/91d73ee59347ac16',
    #  'http://ufcstats.com/event-details/84a067c46306a737',
    #  'http://ufcstats.com/event-details/fa8b9e6b0c2269f8',
    #  'http://ufcstats.com/event-details/7c0847d3854a95f2',
    #  'http://ufcstats.com/event-details/896c322f56b8be5a',
    #  'http://ufcstats.com/event-details/a8ea84cbe1655f0a',
    #  'http://ufcstats.com/event-details/c6a33ff198aaaeeb',
    #  'http://ufcstats.com/event-details/48d1f690b763934c',
    #  'http://ufcstats.com/event-details/0ee783aa00e468f0',
    #  'http://ufcstats.com/event-details/4908c5ee68a50ee5',
    #  'http://ufcstats.com/event-details/cb6783c39c01d896',
    #  'http://ufcstats.com/event-details/c4b6099f0d25f75e',
    #  'http://ufcstats.com/event-details/1652f3213655b935',
    #  'http://ufcstats.com/event-details/04d5718ed2661e8c',
    #  'http://ufcstats.com/event-details/29b5791e51e7e832',
    #  'http://ufcstats.com/event-details/7d21de9c6d7c98b2',
    #  'http://ufcstats.com/event-details/d1759b2b7be9be56',
    #  'http://ufcstats.com/event-details/2a542ee8a8b83559',
    #  'http://ufcstats.com/event-details/68c6cd5287b473a7',
    #  'http://ufcstats.com/event-details/23ab42947c1990e3',
    #  'http://ufcstats.com/event-details/ea398c802d9998ee',
    #  'http://ufcstats.com/event-details/30cd319d39ee689b',
    #  'http://ufcstats.com/event-details/a2b06ca02bca14c0',
    #  'http://ufcstats.com/event-details/c670aa48827d6be6',
    #  'http://ufcstats.com/event-details/312f47c3d2f83ffa',
    #  'http://ufcstats.com/event-details/279093302a6f44b3',
    #  'http://ufcstats.com/event-details/0db70ca89e1c7374',
    #  'http://ufcstats.com/event-details/19ffeb5e3fffd6d5',
    #  'http://ufcstats.com/event-details/46f11d15c0134fe3',
    #  'http://ufcstats.com/event-details/bf12aca029bfcc47',
    #  'http://ufcstats.com/event-details/2299605af59fd309',
    #  'http://ufcstats.com/event-details/2efbc83a6b9b7f86',
    #  'http://ufcstats.com/event-details/2549d63da9c456cb',
    #  'http://ufcstats.com/event-details/ad047e3073a775f3',
    #  'http://ufcstats.com/event-details/b9e871af730f826c',
    #  'http://ufcstats.com/event-details/598a58db87b890ee',
    #  'http://ufcstats.com/event-details/597db668b01c442c',
    #  'http://ufcstats.com/event-details/33e33d51f289d2a1',
    #  'http://ufcstats.com/event-details/a24e080000fa7a35',
    #  'http://ufcstats.com/event-details/7269329bd87eb479',
    #  'http://ufcstats.com/event-details/df85d6ec3493d120',
    #  'http://ufcstats.com/event-details/1d147d4163a6989b',
    #  'http://ufcstats.com/event-details/91181b29be041f1c',
    #  'http://ufcstats.com/event-details/bad28b7b34f334de',
    #  'http://ufcstats.com/event-details/f341f9551ba744e2',
    #  'http://ufcstats.com/event-details/0aa92558424ced9e',
    #  'http://ufcstats.com/event-details/a5c53b3ddb31cc7d',
    #  'http://ufcstats.com/event-details/2a6f8136da1e52c0',
    #  'http://ufcstats.com/event-details/e7ec11096eac0282',
    #  'http://ufcstats.com/event-details/5ca158b1cc9cb242',
    #  'http://ufcstats.com/event-details/304fcd812f12c589',
    #  'http://ufcstats.com/event-details/2e04a3b4a2011b97',
    #  'http://ufcstats.com/event-details/4604ab1de9058474',
    #  'http://ufcstats.com/event-details/c1684f00c626f4c0',
    #  'http://ufcstats.com/event-details/a6c2f5381d575920',
    #  'http://ufcstats.com/event-details/de3ed2e152520c8d',
    #  'http://ufcstats.com/event-details/63b65af1c5cb02cb',
    #  'http://ufcstats.com/event-details/13c4313ed0f744f3',
    #  'http://ufcstats.com/event-details/ee5df903f80c6816',
    #  'http://ufcstats.com/event-details/21b8a0f5c231096f',
    #  'http://ufcstats.com/event-details/3fed746acfd026dd',
    #  'http://ufcstats.com/event-details/baf942f4bcb09894',
    #  'http://ufcstats.com/event-details/13b2f59210dda9cc',
    #  'http://ufcstats.com/event-details/577ec7e108b94be3',
    #  'http://ufcstats.com/event-details/13e62d766b709aa6',
    #  'http://ufcstats.com/event-details/f717b6002486f73f',
    #  'http://ufcstats.com/event-details/46c8ec317aff28ac',
    #  'http://ufcstats.com/event-details/f70144caea5c4c80',
    #  'http://ufcstats.com/event-details/445a98acb8985970',
    #  'http://ufcstats.com/event-details/1dab0d1d81dd06db',
    #  'http://ufcstats.com/event-details/a54a35a670d8e852',
    #  'http://ufcstats.com/event-details/03688dc3c3af3ac1',
    #  'http://ufcstats.com/event-details/b361180739bed4b0',
    #  'http://ufcstats.com/event-details/0e9869d712e81f8f',
    #  'http://ufcstats.com/event-details/977081bc01197656',
    #  'http://ufcstats.com/event-details/2ee09ec2a0695eb9',
    #  'http://ufcstats.com/event-details/c7e9d15cfce52f1d',
    #  'http://ufcstats.com/event-details/31ceaf0e670c1578',
    #  'http://ufcstats.com/event-details/271fe91f4ba9d2c5',
    #  'http://ufcstats.com/event-details/efaf544314bb5c2e',
    #  'http://ufcstats.com/event-details/669a3cb6e394f515',
    #  'http://ufcstats.com/event-details/3f24c96753dbd9f9',
    #  'http://ufcstats.com/event-details/d3711d3784b76255',
    #  'http://ufcstats.com/event-details/c933d423ebdbbbdb',
    #  'http://ufcstats.com/event-details/fbbde91f7bc2d3c5',
    #  'http://ufcstats.com/event-details/85d905f7c4f5a1af',
    #  'http://ufcstats.com/event-details/ce783bf73b5131f9',
    #  'http://ufcstats.com/event-details/b4bc2e3353a770b5',
    #  'http://ufcstats.com/event-details/429e7d3725852ce9',
    #  'http://ufcstats.com/event-details/e8fb8e53bc2e29d6',
    #  'http://ufcstats.com/event-details/94609dd91731d428',
    #  'http://ufcstats.com/event-details/e670f8cc2969a789',
    #  'http://ufcstats.com/event-details/c61f66d8c3fd5f07',
    #  'http://ufcstats.com/event-details/108afe61a26bcbf4',
    #  'http://ufcstats.com/event-details/ae58685caf8e4a0d',
    #  'http://ufcstats.com/event-details/bba678d312590087',
    #  'http://ufcstats.com/event-details/e06fd1260ac865a7',
    #  'http://ufcstats.com/event-details/0cf935519d439ba6',
    #  'http://ufcstats.com/event-details/1dc56b59cb28425d',
    #  'http://ufcstats.com/event-details/9ccdd2ce45903f34',
    #  'http://ufcstats.com/event-details/9fd1f08dd4aec14a',
    #  'http://ufcstats.com/event-details/02fc8f50f56eb307',
    #  'http://ufcstats.com/event-details/946f341df6472ee0',
    #  'http://ufcstats.com/event-details/4dc496aa0cfc0d95',
    #  'http://ufcstats.com/event-details/c75b99887c8c3f5a',
    #  'http://ufcstats.com/event-details/7b9aa973e5c04624',
    #  'http://ufcstats.com/event-details/20bd6c3e03c46ee6',
    #  'http://ufcstats.com/event-details/2b1587a3376ab743',
    #  'http://ufcstats.com/event-details/08ae5cd9aef7ddd3',
    #  'http://ufcstats.com/event-details/da6dfd09cca1d705',
    #  'http://ufcstats.com/event-details/31652c9267606d54',
    #  'http://ufcstats.com/event-details/cedfdf8d423d500c',
    #  'http://ufcstats.com/event-details/d2b1c1317a39f6c6',
    #  'http://ufcstats.com/event-details/20ec0061400178ca',
    #  'http://ufcstats.com/event-details/a8fa0c4e95512806',
    #  'http://ufcstats.com/event-details/afaad7d6a581e307',
    #  'http://ufcstats.com/event-details/1a1a4d7a29041d77',
    #  'http://ufcstats.com/event-details/a7b48e18ca27795d',
    #  'http://ufcstats.com/event-details/a220be6d41d6f97d',
    #  'http://ufcstats.com/event-details/c9bbf1a0285a8076',
    #  'http://ufcstats.com/event-details/32a3025d5db456ae',
    #  'http://ufcstats.com/event-details/4a01dc8376736ef5',
    #  'http://ufcstats.com/event-details/749685d24e2cac50',
    #  'http://ufcstats.com/event-details/29f935654825331b',
    #  'http://ufcstats.com/event-details/07a18ae55dfc3cd9',
    #  'http://ufcstats.com/event-details/dc950d59dc590aca',
    #  'http://ufcstats.com/event-details/5bd533d50c8e7b8a',
    #  'http://ufcstats.com/event-details/96eff1a628adcc7f',
    #  'http://ufcstats.com/event-details/9b5b5a75523728f3',
    #  'http://ufcstats.com/event-details/6ceff86fae4f6b3b',
    #  'http://ufcstats.com/event-details/aee8eecfc4bfb1e7',
    #  'http://ufcstats.com/event-details/a390eb8a9b2df298',
    #  'http://ufcstats.com/event-details/b63e800c18e011b5',
    #  'http://ufcstats.com/event-details/31bbd46d57dfbcb7',
    #  'http://ufcstats.com/event-details/5af480a3b2e1726b',
    #  'http://ufcstats.com/event-details/1c3f5e85b59ec710',
    #  'http://ufcstats.com/event-details/dedc3bb440d09554',
    #  'http://ufcstats.com/event-details/b60391da771deefe',
    #  'http://ufcstats.com/event-details/1a49e0670dfaca31',
    #  'http://ufcstats.com/event-details/a6a9ab5a824e8f66',
    #  'http://ufcstats.com/event-details/6420efac0578988b'
    #
    # ]

    start_urls = ['http://ufcstats.com/event-details/e5d03e4d966126bd']

    def parse(self, response):
        links = response.xpath('//a[contains(@href, "fighter-details")]/@href').extract()
        linker = links
        fighters = response.xpath('//a[@class="b-link b-link_style_black"]').extract()
        numfights = int(len(links)/2)
        i = 0
        for j in range(1, numfights+1):

            scrap_fighter_name1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[2]/p[1]/a/text())'
            scrap_strikes1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[3]/p[1]/text())'
            scrap_takedowns1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[4]/p[1]/text())'
            scrap_submission_attempts1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[5]/p[1]/text())'
            scrap_passes1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[6]/p[1]/text())'
            scrap_weight_class1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[7]/p/text())'
            scrap_method1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[8]/p[1]/text())'
            scrap_round1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[9]/p/text())'
            scrap_time1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[10]/p/text())'
            scrap_result1 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[2]/p[1]/a/text())'

            scrap_fighter_name2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[2]/p[2]/a/text())'
            scrap_strikes2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[3]/p[2]/text())'
            scrap_takedowns2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[4]/p[2]/text())'
            scrap_submission_attempts2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[5]/p[2]/text())'
            scrap_passes2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[6]/p[2]/text())'
            scrap_weight_class2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[7]/p/text())'
            scrap_method2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[8]/p[2]/text())'
            scrap_round2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[9]/p/text())'
            scrap_time2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[10]/p/text())'
            scrap_result2 = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[2]/p[1]/a/text())'

            if links[i+1] is not None:
                item2 = {
                    # static items
                    'Date': response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()')[1].getall(),
                    'Location': response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()')[1].getall(),
                    'Event_Name': response.xpath('normalize-space(/html/body/section/div/h2/span/text())').getall(),

                    # dynamic items
                    'Fighter_Name1': response.xpath(scrap_fighter_name1).getall(),
                    'Strikes1': response.xpath(scrap_strikes1).getall(),
                    'Takedowns1': response.xpath(scrap_takedowns1).getall(),
                    'Submission_Attempts1': response.xpath(scrap_submission_attempts1).getall(),
                    'Passes1': response.xpath(scrap_passes1).getall(),
                    'Weight_Class1': response.xpath(scrap_weight_class1).getall(),
                    'Method1': response.xpath(scrap_method1).getall(),
                    'Round1': response.xpath(scrap_round1).getall(),
                    'Time1': response.xpath(scrap_time1).getall(),
                    'Result1': response.xpath(scrap_result1).getall(),

                    'Fighter_Name2': response.xpath(scrap_fighter_name2).getall(),
                    'Strikes2': response.xpath(scrap_strikes2).getall(),
                    'Takedowns2': response.xpath(scrap_takedowns2).getall(),
                    'Submission_Attempts2': response.xpath(scrap_submission_attempts2).getall(),
                    'Passes2': response.xpath(scrap_passes2).getall(),
                    'Weight_Class2': response.xpath(scrap_weight_class2).getall(),
                    'Method2': response.xpath(scrap_method2).getall(),
                    'Round2': response.xpath(scrap_round2).getall(),
                    'Time2': response.xpath(scrap_time2).getall(),
                    'Result2': response.xpath(scrap_result2).getall(),

                    'Height1': "999",
                    'Weight1': "999",
                    'Reach1': "999",
                    'Stance1': "999",
                    'DOB1': "999",
                    'Strikes_Per_Min1': "999",
                    'TD_Avg1': "999",

                    # 'Height2': "777",
                    # 'Weight2': "777",
                    # 'Reach2': "777",
                    # 'Stance2': "777",
                    # 'DOB2': "777",
                    # 'Strikes_Per_Min2': "777",
                    # 'TD_Avg2': "777",
                }

                item3 = scrapy.Request(url=links[i], callback=self.parse_indetail, meta=item2)
                # I need to pass actual data into the meta data prior to the next scrapy request

                # item3.meta['Height1'] = item3.__dict__.keys()

                item4 = scrapy.Request(url=links[i+1], callback=self.parse_indetail_2, meta=item3.meta)
                # yield item3

                yield item4


                # item4 = scrapy.Request(url=links[i+1], callback=self.parse_indetail_2, meta=item2)
                # yield item4


                i += 2


                # 7.18.2019 I want to append two sets of call back data into the meta data before yielding
                # item3 = scrapy.Request(url=links[i], callback=self.parse_indetail, meta=item2)

                # item2.update(item1)

    def parse_indetail(self, response):

        # load meta data first
        item['Submission_Attempts1'] = response.meta['Submission_Attempts1']
        item['Passes1'] = response.meta['Passes1']
        item['Fighter_Name1'] = response.meta['Fighter_Name1']
        item['Strikes1'] = response.meta['Strikes1']
        item['Takedowns1'] = response.meta['Takedowns1']
        item['Weight_Class1'] = response.meta['Weight_Class1']
        item['Method1'] = response.meta['Method1']
        item['Round1'] = response.meta['Round1']
        item['Time1'] = response.meta['Time1']
        item['Result1'] = response.meta['Result1']

        item['Submission_Attempts2'] = response.meta['Submission_Attempts2']
        item['Passes2'] = response.meta['Passes2']
        item['Fighter_Name2'] = response.meta['Fighter_Name2']
        item['Strikes2'] = response.meta['Strikes2']
        item['Takedowns2'] = response.meta['Takedowns2']
        item['Weight_Class2'] = response.meta['Weight_Class2']
        item['Method2'] = response.meta['Method2']
        item['Round2'] = response.meta['Round2']
        item['Time2'] = response.meta['Time2']
        item['Result2'] = response.meta['Result2']

        item['Date'] = str(response.meta['Date']).strip().replace('\n', '')
        item['Location'] = str(response.meta['Location']).strip().replace('\n', '')
        item['Event_Name'] = response.meta['Event_Name']

        # Passing data relevant to the new response page

        item['Height1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')
        response.meta['Height1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')

        item['Weight1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()').getall()[1]).strip().replace('\n', '')
        item['Reach1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[3]/text()').getall()[1]).strip().replace('\n', '')
        item['Stance1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[4]/text()').getall()[1]).strip().replace('\n', '')
        item['DOB1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[5]/text()').getall()[1]).strip().replace('\n', '')
        item['Strikes_Per_Min1'] = str(response.xpath('/html/body/section/div/div/div[2]/div[1]/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')
        item['TD_Avg1'] = str(response.xpath('/html/body/section/div/div/div[2]/div[1]/div[2]/ul/li[2]/text()').getall()[1]).strip().replace('\n', '')

        return item
        # return scrapy.Request(url='http://ufcstats.com/fighter-details/d4691518d012b9e7', callback=self.parse_indetail_2, meta=item)

    def parse_indetail_2(self, response):
        item = UfcStats()

        # load meta data first
        item['Submission_Attempts1'] = response.meta['Submission_Attempts1']
        item['Passes1'] = response.meta['Passes1']
        item['Fighter_Name1'] = response.meta['Fighter_Name1']
        item['Strikes1'] = response.meta['Strikes1']
        item['Takedowns1'] = response.meta['Takedowns1']
        item['Weight_Class1'] = response.meta['Weight_Class1']
        item['Method1'] = response.meta['Method1']
        item['Round1'] = response.meta['Round1']
        item['Time1'] = response.meta['Time1']
        item['Result1'] = response.meta['Result1']

        item['Submission_Attempts2'] = response.meta['Submission_Attempts2']
        item['Passes2'] = response.meta['Passes2']
        item['Fighter_Name2'] = response.meta['Fighter_Name2']
        item['Strikes2'] = response.meta['Strikes2']
        item['Takedowns2'] = response.meta['Takedowns2']
        item['Weight_Class2'] = response.meta['Weight_Class2']
        item['Method2'] = response.meta['Method2']
        item['Round2'] = response.meta['Round2']
        item['Time2'] = response.meta['Time2']
        item['Result2'] = response.meta['Result2']

        item['Date'] = str(response.meta['Date']).strip().replace('\n', '')
        item['Location'] = str(response.meta['Location']).strip().replace('\n', '')
        item['Event_Name'] = response.meta['Event_Name']

        # Passing data relevant to the new response page

        item['Height1'] = response.meta['Height1']
        item['Weight1'] = response.meta['Weight1']
        item['Reach1'] = response.meta['Reach1']
        item['Stance1'] = response.meta['Stance1']
        item['DOB1'] = response.meta['DOB1']
        item['Strikes_Per_Min1'] = response.meta['Strikes_Per_Min1']
        item['TD_Avg1'] = response.meta['TD_Avg1']

        item['Height2'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')
        item['Weight2'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()').getall()[1]).strip().replace('\n', '')
        item['Reach2'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[3]/text()').getall()[1]).strip().replace('\n', '')
        item['Stance2'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[4]/text()').getall()[1]).strip().replace('\n', '')
        item['DOB2'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[5]/text()').getall()[1]).strip().replace('\n', '')
        item['Strikes_Per_Min2'] = str(response.xpath('/html/body/section/div/div/div[2]/div[1]/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')
        item['TD_Avg2'] = str(response.xpath('/html/body/section/div/div/div[2]/div[1]/div[2]/ul/li[2]/text()').getall()[1]).strip().replace('\n', '')

        return item


