#!/usr/bin/env python3
"""Generate README.md (category tables) + index.html (GitHub Pages gallery) for logos-apps."""
import os, json, html

import os as _os
SRC = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
REPO = "ln-dev7/logos-apps"
PAGES_URL = "https://logos.lndev.me/"
ZIP_URL = f"https://github.com/{REPO}/archive/refs/heads/master.zip"

CATS = [
    ("ai",     "🤖 AI & Machine Learning"),
    ("lang",   "💻 Languages & Runtimes"),
    ("fw",     "⚛️ Frameworks & UI Libraries"),
    ("dev",    "🛠️ Dev Tools, CI/CD & Testing"),
    ("cloud",  "☁️ Cloud, Hosting & Infrastructure"),
    ("db",     "🗄️ Databases & Data"),
    ("design", "🎨 Design & Creative"),
    ("social", "💬 Social & Communication"),
    ("pay",    "💳 Payments, Fintech & Crypto"),
    ("prod",   "📋 Productivity & Collaboration"),
    ("shop",   "🛒 E-commerce & CMS"),
    ("media",  "🎵 Media & Entertainment"),
    ("os",     "🖥️ OS, Platforms & Browsers"),
    ("mkt",    "📊 Analytics, Marketing & CRM"),
    ("sec",    "🔐 Security & Identity"),
    ("web",    "🌐 Web Standards & Protocols"),
    ("corp",   "🏢 Companies & Services"),
    ("other",  "📦 Others"),
]
CAT_TITLES = dict(CATS)

M = {}
def add(cat, names):
    for n in names.split():
        M[n] = cat

add("ai", """ai anthropic claude openai github-copilot google-bard google-gemini google-palm deepseek
mistral-ai moonshot-ai qwen grok x-ai perplexity midjourney hugging-face stability-ai tensorflow
pytorch caffe2 matplotlib numpy pandas seaborn jupyter dialogflow api-ai mindsdb nanonets gradio
streamlit danfo brainjs opencv floydhub model-context-protocol""")

add("lang", """python micro-python pyscript javascript typescript java go gopher rust ruby jruby php
swift kotlin scala haskell erlang clojure cljs dart lua perl r-lang c c-plusplus c-sharp fsharp
fortran nasm julia nim-lang crystal ceylon haxe hack ocaml reasonml rescript purescript elm
coffeescript vlang zig gleam solidity mono dotnet net nodejs deno bun v8 v8-ignition v8-turbofan
webassembly es6 ecma tsnode imba mint-lang clio-lang winglang autoit xtend spidermonkey hermes hhvm
io hoa""")

add("fw", """react react-router react-query react-spring react-styleguidist create-react-app preact
nextjs vue nuxt angular svelte svelte-kit solidjs astro remix gatsby gridsome eleventy hexo hugo
jekyll express nestjs fastify koa hapi sails adonisjs meteor django flask fastapi laravel lumen
cakephp codeigniter symfony phalcon rails sinatra hanami spring struts grails play quarkus ktor gin
phoenix dojo dojo-toolkit jquery jquery-mobile backbone ember marionette mithril aurelia polymer
lit alpinejs htmx stenciljs stimulus marko riot inferno hyperapp cyclejs knockout mootools d3
threejs pixijs p5js leaflet openlayers chartjs highcharts momentjs lodash ramda axios redux
redux-saga redux-observable mobx recoil jotai xstate stately reactivex immer zod trpc swr relay
apollostack graphene graphql grpc socket-io capacitorjs cordova ionic nativescript xamarin flutter
expo exponent electron tauri qt unity unrealengine godot opengl vulkan createjs openframeworks
processing tailwindcss bootstrap bulma foundation materializecss material-ui ant-design daisyui
unocss windi-css pandacss mantine naiveui vuetifyjs vueuse pinia semantic-ui uikit milligram bem
sass sass-doc less stylus postcss cssnext autoprefixer glamorous jss stylis myth neat bourbon susy
compass flat-ui blueprint evergreen headlessui element elemental-ui grommet framework7 blitzjs
redwoodjs t3 qwik million partytown malinajs lexical feathersjs loopback strongloop seneca micro
hono effect effector hookstate flux fluxxor famous flight canjs componentkit component webix titon
turret enact enyo reapp rax mern greensock snap-svg raphael font-awesome handlebars haml thymeleaf
jade pug slim wicket vaadin gwt jhipster liftweb lotus akka ampersand analog atomicojs celluloid
cinder derby dropzone eta evergreen falcor fresh glimmerjs grape haxl kemal kore koreio kraken
krakenjs meanio microcosm middleman moon nodal node-sass nodewebkit pepperoni phonegap q randomcolor
require rest-li sagui sencha steroids sugarss supersonic unjs yii zend-framework horizon
compose-multiplatform ink""")

add("dev", """git github github-actions github-octocat gitlab bitbucket gitkraken sourcetree gitup
gitboard mercurial subversion visual-studio-code visual-studio atom sublimetext brackets vim neovim
emacs jetbrains jetbrains-space intellij-idea webstorm pycharm clion goland rider rubymine datagrip
dataspell appcode phpstorm mps netbeans eclipse xcode terminal hyper bash zsh curl httpie postman
insomnia apidog apiary apitools apigee swagger openapi async-api npm yarn pnpm nvm jspm webpack
vite vitejs vitest rollupjs rolldown esbuild swc parcel snowpack turbopack turborepo nx lerna babel
eslint prettier stylelint stylefmt styleci biomejs oxc terser browserslist grunt gulp bower brunch
broccoli buck jest mocha chai jasmine karma cypress playwright puppeteer selenium webdriverio
testcafe testing-library nightwatch ava cucumber protractor unitjs testlodge testmunk applitools
saucelabs browserstack crossbrowsertesting cross-browser-testing browserling docker kitematic
kubernetes helm rancher vagrant packer terraform ansible chef puppet saltstack pulumi jenkins
circleci travis-ci buildkite drone teamcity bamboo codeship appveyor semaphore semaphoreci cirrus
cirrus-ci gocd argo spinnaker harness octopus-deploy fastlane bitrise appcenter appcircle wercker
shippable distelli deploy deployhq clickdeploy deppbot dependabot renovatebot dependencyci codecov
coveralls codeclimate codacy codebeat codefactor coverity sonarqube sonarcloud sonarlint rubocop
houndci sourcegraph codesandbox codepen jsfiddle jsbin glitch replit stackblitz cloud9 codium
gradle maven composer conda homebrew cocoapods verdaccio jfrog quay sentry rollbar bugsnag airbrake
crashlytics opbeat appsignal new-relic datadog dynatrace appdynamics splunk grafana prometheus
graylog logentries loggly logmatic logstash kibana opentelemetry lightstep epsagon sysdig zabbix
pagerduty opsgenie victorops incident statuspage pingdom runscope floodio loader lighthouse calibre
speedcurve perf-rocks ngrok msw faker storybook chromatic percy nodemon pm2 forever gunicorn uwsgi
tomcat undertow wildfly nginx lighttpd apache envoy envoyproxy envoyer nodebots commitizen madge
maestro manuscript kallithea katalon keymetrics kong launchdarkly growth-book imagemin emmet esdoc
editorconfig glint asciidoctor assembla aerogear amplication appcelerator apphub appium appmaker
apportable appveyor armory autocode bigpanda bitbar bosun brotli browserify browsersync bugherd
bugsee cachet capistrano carbide chalk codebase codeception codepicnic codepush codersrank
coderwall codeschool codesee codio crittercism crucible dat dimer dockbit docusaurus dreamfactory
drools eventsentry fabric fabric-io flow fogbugz forest forestadmin formkeep gaugeio gomix
harrow hosted-graphite infer jscs kops kustomer launchkit librato maildeveloper manifoldjs
mockaroo modernizr netuitive nuclide opsee opsmatic otto pingy pipedream pkg plastic-scm
platformio prerender pypi pyup quay raml refactor release replay rome ros rsmq rubygems run-above
runnable rush semantic-release sensu shields shipit sidekick sidekiq siphon skaffolder skylight
slidev solarwinds sourcetrail stash stdlib stepsize stetho stigg stoplight strider swimm
tastejs thimble todomvc trac trace vector volar wakatime watchman waypoint wayscript webhint
wmr x-ray-goggles xampp xray-for-jira yeoman swiftype concourse consul etcd helm gunjs
crossplane houndci hardhat-ignition vite-dark oxc-dark""")

add("cloud", """aws azure google-cloud google-cloud-platform google-cloud-functions
google-cloud-run vercel netlify heroku digital-ocean cloudflare cloudflare-workers linode vultr
fly hostgator dreamhost wpengine namecheap bluemix engine-yard appfog dotcloud modulus nodejitsu
jelastic surge divshot bitballoon now zeit akamai fastly keycdn maxcdn jsdelivr bunny-net section
sectionio edgio firebase supabase appwrite nhost pocket-base parse kinvey openshift openstack
coreos rkt tectonic giantswarm kontena supergiant containership clusterhq flocker mantl balena
multipass lets-cloud cpanel 100tb mesos mesosphere dcos nomad linkerd flannel weave morpheus
cloudinary pusher twilio iron jsdelivr graphcool serverless serveless sst webtask scaledrone
scaphold reindex redspread peer5 pagekite octodns losant kloudless juju elasticbox dyndns convox
tsuru tutum wiredtree webmin stacksmith neverinstall mapbox mapzen rackspace cloudlinux
hasura""")

add("db", """mysql postgresql mongodb mongolab mlab redis keydb memcached sqlite mariadb cassandra
couchbase couchdb pouchdb rethinkdb riak neo4j arangodb dgraph influxdb elasticsearch opensearch
solr lucene lucene-net algolia meilisearch typesense planetscale vitess yugabyte singlestore
memsql crateio nuodb foundationdb leveldb rocksdb pumpkindb dolt edgedb fauna surrealdb neon
upstash xata snowflake presto impala hbase hadoop spark apache-spark apache-flink kafka rabbitmq
nats vernemq aerospike realm prisma sequelize typeorm drizzle knex doctrine hibernate sqldep
database-labs data-station treasuredata dbt airflow astronomer memgraph milvus pinecone qdrant
chroma cloudant percona aurora looker metabase tableau qlik microsoft-power-bi observablehq
nocodb humongous heron cube stitch snaplet parsehub xplenty quobyte redsmin kinto importio
gunjs rxdb postgraphile apache-superset google-data-studio rsmq""")

add("design", """figma sketch sketchapp invision framer dribbble behance blender zeplin marvel
protoio prott pixate framed precursor mockflow zeroheight font-awesome svgator designernews
deviantart codrops smashingmagazine origami atomic blocs builder-io plasmic webflow pixelapse
eraser cloudcraft""")

add("social", """facebook instagram twitter x threads tiktok linkedin discord slack telegram
whatsapp messenger signal zoom amazon-chime microsoft-teams reddit pinterest mastodon bluesky vine
periscope yammer workplace gitter hipchat mattermost rocket-chat zulip campfire fleep wire disqus
discourse tumblr medium dev dailydev hashnode ello quora stackoverflow stackshare producthunt
delicious steemit noysi sameroom google-plus google-meet""")

add("pay", """stripe paypal visa visaelectron mastercard amex discover dinersclub jcb unionpay elo
hipercard apple-pay google-pay google-wallet square adyen ebanx chargebee xero bitcoin ethereum
cardano monero internet-computer torus metamask truffle ganache hardhat open-zeppelin ethers
web3js corda kickstarter patreon flattr gratipay changetip opencollective backerkit gusto mist""")

add("prod", """notion asana trello jira confluence linear monday airtable todoist basecamp taskade
miro loom coda dropbox box google-drive microsoft-onedrive zoho teamwork freedcamp taiga
targetprocess pivotal-tracker shortcut zenhub zube waffle leankit dapulse workboard producteev
obsidian grammarly languagetool frontapp google-calendar google-gmail google-keep google-inbox
google-workspace google-gsuite google-360suite google-currents google-docs ifttt zapier pipefy podio poeditor
dovetail planless productboard qordoba smartling unito xwiki youtrack geekbot blossom tuple
pushbullet retool teamgrid dropmark batch""")

add("shop", """shopify woocommerce magento xcart opencart prestashop spree moltin elasticpath
medusa wordpress drupal joomla typo3 concrete5 concretecms grav kirby craft processwire modx
pagekit apostrophe wagtail strapi contentful sanity datocms storyblok prismic ghost payload wix
squarespace weebly blogger shogun tapcart chevereto flarum keystonejs stackbit basekit cockpit
opencart bubble""")

add("media", """spotify netflix youtube twitch vimeo soundcloud lastfm tidal tunein steam flickr
500px picasa google-photos ffmpeg scribd speakerdeck slides storyblocks envato descript
webtorrent eventbrite""")

add("os", """android ios macos macosx microsoft-windows linux linux-mint linux-tux ubuntu debian
fedora centos archlinux manjaro mageia rocky-linux puppy-linux zorin-os elementary galliumos
freebsd aix haiku kaios fuchsia wearos raspberry-pi arduino chrome firefox safari opera vivaldi
brave microsoft-edge internetexplorer tor-browser arc duckduckgo kde gnome gnu gnu-net void
nodeos apple-app-store chrome-web-store google-play webkit""")

add("mkt", """google-analytics google-ads google-adsense google-adwords admob google-admob adroll
google-tag-manager google-optimize google-search-console google-marketing-platform doubleclick
mixpanel amplitude segment heap hotjar matomo posthog kissmetrics woopra vwo
visual-website-optimizer optimizely unbounce hubspot mailchimp mandrill mailgun sendgrid mailjet
sparkpost campaignmonitor customerio braze drip active-campaign intercom drift zendesk helpscout
desk groovehq uservoice salesforce pipedrive close hootsuite buffer mention brandfolder litmus
botanalytics game-analytics keen mparticle tealium branch apptentive delighted survicate typeform
wufoo onesignal amazon-connect get-satisfaction ethnio neonmetrics olapic olark overloop
positionly proofy prospect sparkcentral supportkit traackr user-testing walkme whalar mixmax
launchrock locent itsalive fomo flowxo mautic lookback""")

add("sec", """auth0 okta supertokens stytch oauth jwt rsa letsencrypt certbot gnupg passbolt
dashlane authy vault snyk hacker-one sigstore passport workos recaptcha hcaptcha geetest osquery
tor stormpath vaddy""")

add("web", """html-5 html5-boilerplate css css-3 css-3-official svg json json-ld json-schema yaml
toml markdown mdx webcomponents webgpu webrtc websocket w3c whatwg ietf ieee mdn open-graph pwa
amp webplatform web-fundamentals web-dev semantic-web rest webhooks jamstack opensource
freedomdefined copyleft gravatar wifi bluetooth zigbee zwave promises openjs-foundation solid
fetch oshw""")

add("corp", """google apple microsoft meta ibm intel amd nvidia samsung broadcom qualcomm tsmc
sk-hynix arm sap oracle vmware redhat suse mozilla atlassian hashicorp yahoo yandex-ru bing
airbnb angellist ycombinator coursera udemy udacity codecademy treehouse khan-academy pluralsight
egghead lynda tutsplus sitepoint oreilly upcase cloudacademy getyourguide upwork eventbrite
stickermule progress micron maps-me google-2014 google-maps google-home google-fit google-one
google-domains google-developers google-play-console tnw booqable""")

# last-pass fixes for recognizable leftovers
add("prod", "aha")
add("shop", "alfresco craftcms")
add("db", "appbase appbaseio cloudera datasette risingwave altair")
add("dev", "architect beats buddy compose conan-io embedly jsdom vector-timber bitnami")
add("fw", "flyjs hoodie immutable blockus lndev-ui shadcn-ui")
add("social", "skype")
add("mkt", "base")


# logos imported from svgl.app (auto-generated)
add("ai", """amazon-q basewell bolt buildship cerebras codex cody cohere conductor firebase-studio firecrawl glide granola groq hume-ai inflection-ai intlayer kilo-code kimi langchain leedlime locofy lovable manus microsoft-copilot midday ollama open-webui openclaw opencode openrouter poper replicate runway suno tembo together-ai v0""")
add("cloud", """adobe-experience-platform ahrefs godaddy intello microsoft-sharepoint orshot railway render soldera zeabur""")
add("corp", """cisco google-antigravity google-classroom google-colaboratory learnthis openbootcamp platzi uber upleveled""")
add("db", """bklit convex microsoft-access microsoft-sql-server plainsignal powersync turso""")
add("design", """adobe-aero adobe-capture adobe-fonts adobe-fresco adobe-stock affinity-designer axure canva fontfolio gimp layers lottiefiles lottielab microsoft-designer paper penpot photopea pitch substance-3d-designer substance-3d-painter substance-3d-sampler substance-3d-stager""")
add("dev", """alacritty cursor dotenv ghostty hoppscotch jetbrains-fleet mermaid nuget rsbuild rspack tabby uv volta warp windsurf zed""")
add("fw", """ahooks ark-ui base-ui chakra-ui discord-js effect-ts elysiajs exome flowbite heroui ivy-framework kibo-ui kokonut-ui magic-ui nuqs nuxt-content nuxt-studio nuxt-ui nuxthub pdf polars radix-ui react-wheel-picker refine remotion rxjs shiki styled-components svgl tanstack valibot webgl zyft""")
add("lang", """cobol matlab powershell""")
add("media", """apple-music disney-plus epic-games hulu kick obs playstation prime-video roblox sky voicemod xbox youtube-music""")
add("mkt", """trustpilot""")
add("os", """chromium zen-browser""")
add("other", """dracula hack-the-box voidzero""")
add("pay", """abacatepay algorand binance bnb buy-me-a-coffee chainlink coinbase dingocoin dodo-payments dogecoin leap-wallet lemon-squeezy litecoin mercado-pago nano opensea polar polygon solana tether ton tron trust-wallet xrp""")
add("prod", """acrobat-reader acrobat-scan adobe-audition adobe-bridge adobe-captivate adobe-captivate-prime adobe-character-animator adobe-connect adobe-digital-editions adobe-fill-and-sign adobe-framemaker adobe-framemaker-server adobe-http-dynamic-streaming adobe-indesign-server adobe-lightroom-classic adobe-media-encoder adobe-media-server adobe-portfolio adobe-premiere-elements adobe-premiere-rush adobe-presenter-video-express adobe-robohelp adobe-robohelp-server adobe-sign adobe-technical-communication-suite affinity-photo affinity-publisher apollo-io axiom beacon bento cal-com calendly clickup coldfusion coldfusion-builder designali documenso docus dub flow-launcher formance goil google-idx google-sheets google-slides heptabase inngest instatus interfere manifest mediawiki microsoft-clipchamp microsoft-defender microsoft-editor microsoft-excel microsoft-office microsoft-onenote microsoft-outlook microsoft-powerpoint microsoft-todo microsoft-word milanote mintlify monkeytype mulesoft n8n perspective photoshop-camera photoshop-elements photoshop-express powertoys proton-mail proton-vpn putio raindrop-io randevum rapid-api raycast reflex relagit resend runframe travelperk typegpu vlt ygeeker zaia-endless""")
add("sec", """1password auth-js better-auth bitwarden clerk dotenvx keycloak""")
add("shop", """aliexpress curseforge directus ebay elementor hotmart mercado-libre procure rowy tina whop""")
add("social", """carrd developer-student-club google-chat infojobs manzdev matrix midudev openhunts peerlist snapchat uxanarangel uxcorprangel vk""")
add("web", """home-assistant""")


# logos imported from SuperTinyIcons (auto-generated)
add("shop", "druplicon")
add("media", "itch-io")
add("dev", "linuxcontainers")
add("corp", "mcdonalds openstreetmap portronics")
add("sec", "tuta tutanota")
add("ai", """amazon-alexa chatgpt coderabbit google-assistant kaggle""")
add("cloud", """amazon-s3 gandi""")
add("corp", """amazon apereo baidu bambulab citrix datacamp ecosia espressif fitbit freecodecamp fritz geeksforgeeks gmail-old gojek google-drive-old google-findhub google-maps-old google-pay-old google-scholar hp kagi leetcode linux-foundation logitech malt nhs olympics orcid researchgate sonarqube-community sonarqube-server tata tripadvisor ubiquiti untappd vivino wikipedia yelp""")
add("db", """apache-age clickhouse elastic sparql victoriametrics""")
add("design", """inkscape""")
add("dev", """codeberg dovecot drawio gitea gitpod grafana-loki guacamole jsr librespeed opencores rclone sublimemerge svgomg""")
add("fw", """amberframework i18next luckyframework""")
add("media", """acast applepodcasts bandcamp deezer downpour ea floatplane foobar2000 gogcom google-podcasts humblebundle iheartradio imdb itunes-podcasts jacobin jellyfin kodi minecraft newpipe opencast overcast peertube plex pocketcasts rockstar slideshare stitcher thisamericanlife ubisoft uplay vlc webtoons ytmusic""")
add("mkt", """plausible""")
add("os", """alpinelinux css-new elementaryos endeavouros f-droid finder flatpak google-tv grapheneos homekit netbsd nixos nobara parrotos popos postmarketos samsung-internet wayland x11""")
add("pay", """cash-app coil coinpot gatehub justgiving ko-fi liberapay subscribestar tezos uphold upi venmo""")
add("prod", """dolibarr evernote filestash google-collaborative-content-tools google-docs-editors nextcloud outlook overleaf pinboard pocket proton-drive roundcube sogo wekan workato""")
add("sec", """andotp bugcrowd digidentity ente-auth google-authenticator keepassdx keepassxc keybase lastpass mcafee nordvpn openbugbounty openvpn symantec wireguard yubico""")
add("shop", """etsy expressionengine""")
add("social", """activitypub badoo briar fediverse friendica goodreads guilded hackernews imgur line lobsters meetup ok-ru pixelfed qq stackexchange strava stumbleupon teamspeak threema tox viber wechat xing""")
add("web", """epub internet-archive jsonfeed microformats rss unicode webmention xmpp""")


# famous brands fetched via logosear.ch (wappalyzer / wikimedia / cncf)
add("mkt", "klaviyo mailerlite")
add("pay", "indiegogo")
add("corp", "mercedes-benz")
add("db", "weaviate")

# famous brands imported from simple-icons (auto-generated)
add("ai", "anaconda")
add("cloud", "proxmox truenas")
add("corp", "acer asus bmw booking-com coca-cola corsair dell duolingo huawei lenovo oneplus razer starbucks tesla toyota xiaomi")
add("db", "airbyte cockroachdb databricks duckdb prefect scylladb talend timescale")
add("design", "excalidraw lucid tldraw")
add("dev", "caddy gitbook portainer rstudio traefik")
add("fw", "apollo-graphql")
add("media", "dailymotion rumble")
add("mkt", "brevo kit")
add("pay", "gofundme klarna monzo n26 revolut robinhood wise")
add("prod", "anydesk teamviewer")
add("sec", "pfsense tailscale zerotier")
add("social", "substack webex")


# brand icons imported from vectorlogo.zone (auto-generated)
add("cloud", """alibabacloud alidns alternate-dns banzaicloud belugacdn bettercloud bocloudcomcn caicloudio catalystcloud cloud66-maestro cloud66-skycap cloudbees cloudboostio cloudcannon cloudeventsio cloudfoundry cloudfoundry-application-runtime cloudfoundry-container-runtime cloudhealthtech cloudifyco cloudops cloudreach cloudsmithio cloudzero cloudzoneio corednsio dnsfilter dnsimple dnsmadeeasy dnsnetworksca dnstoys dnswatch ghostery ghostscript ibm-cloud jumpcloud knot-dnscz nextdnsio opendns owncloud powerdns""")
add("corp", """1800flowers 1and1 23gnl 2ndquadrant 3m 3scalenet 451research 6kites 8tracks 8x8 abcgo ablyio accentreviews accenture accolade aclu acorns acquia act acumos affirm afrinicnet afternic aggdata agilecraft agilestacks agilitycms agonesdev airbrakeio alcideio algorithmia alibabagroup alibris almworks alphavantageco alternativeto altmetric amazon-elasticcontainer ambassadorio amnesty ampproject anchoreio angel angieslist ansi antfin anthemis anymod anzcomau ao aol ap apartmenttherapy apexrun aporeto appcenterms appcues appdome appfire appharbor applause apple-objectivec apple-safari apple-xcode applied-duality appneta appoptics apprenda appscale appscode appwriteio apress aquasec arccodes arcdev archive archive-web archives argoprojio ariasystems arinnet arrikto arstechnica artsynet astartemedical atlassian-bamboo atlassian-jira atom-io atomist att audaorgau audioeye augurnet aureliaio autify automattic avaloniauinet avery avinetworks awesome-emoji awesomelogos axway azavea azurecontainerregistry azurefunctions backblaze backhubco backplaneio backyourstack badgennet bakkt balenaio ballerinaio balsamiq barclays barnesandnoble basho bazel bazzite bbb bbc bbt bbva bcorporationnet bcragobar beanstalkapp beardbrand bedrockdata begin bentley bignerdranch bigpandaio bigswitch bimigroup binaris bipm bitpesaco bitriseio blackducksoftware blacksquareio blockstack bloomberg bluefyreio blueprintsys bmc bnpparibas boeing bons-ai booking bootswatch bose boshio bostonglobe botfuelio botpressio botronsoft boum-tails bountysource boxboat bracketsio branchio brex brigadesh brikit buddybuild buildium buildpacksio bulldogcreative bunsenlabs bunsh bustle buzzfeed c9 ca cablelabs calisphere camunda canadalearningcodeca canonical car2go carbonite cardconnect caspio castboxfm catchpoint cbinsights cbs cdt censusgov centreon centurylink ceph cfengine chaostoolkit chartbeat chartmuseum checkfront cheddar chefio chocolatey cibc ciliumio circle circonus citusdata ckan claranetcouk classy clayrun cleanbrowsing clearbrain clearlydefinedio clearvision-cm clockifyme cmake cnbc cncf-cni cncfio cncfio-cortex cnet cnn cnniccomcn cockroachlabs codebarrelio codecentricde codecovio codefreshio codemirror cognitect cognitohq collabora comalatech comcast commarts common-lispnet commonmark communitybridge comodo concourse-ci conduitio confluentio consulio container-solutions containerdio containerops containershipio containerstorageinterface containous contegix continoio contiv contribsys-faktory convorelay coreboot coredial coreos-rkt coscale cosmopolitan costco coverallsio coyotecrk cprime craigslist creationline creativecommons credit-agricole cri-oio crossbario crunchbase csmonitor css-tricks cucumberio cultureamp cumulusnetworks curl-haxx cyberark daprio darkreader darksky dartlang dash dask dataarm datacomconz datadoghq datahub datarobot datasift datastax datawireio datical datproject dave dbscomsg dcu debeziumio decadisde deepcrawl deepl deiser delphix denicde deploybot deployplace deque deque-axe developerhubio developermedia devpost devto dgraphio diemendesign dieselrs diffusesh digg digidentityeu digitalasset digitalrosetta digitaltrends digitco dimerapp disney djangoproject dllgroup dnanexus docusign doczsite doi domainconnect domaintools dotdash dpconline dpla dragonflybsd dremio drizzleteam droneio druidio dupleio dwolla dynadot easyeuroeu easyredir eazybi ecchreu eclipse-che eclipse-jetty edgewall-trac edx eero eff eggheadio elasityio elasticco-kibana elasticco-logstash elementaryio elementio elixir-lang elm-lang elpais elsevier embarcadero emojisearch engadget entercom entrepreneur envoyproxyio equinix equisoft ericsson esolia everydollar exoscale expium expoio express-gatewayio ey eyesonteam f6s facebook-relay falco fastco fastcompany fastifyio federalreserve fedex feedly feedstyle feedzai fender fflint fileformatinfo filemaker fingoal firstdata firstinspires fissionio fiverr fivethirtyeight fivetran fizzed flarehr flathub flatio flexera flipboard flipgive fluentd flutterio fluxcdio flyio flywire fnproject fontfamous fontisto forbes ford forgerock formcake formspree formstack forrester fortune fossaio fossid fountain foursquare fourthestate fox frameryacoustics freedombox freedompress freelancer freeloaderwtf freenomworld freepik freshdesk fsf ft fullcycle fullstory fusion-reactor galileo-ft galvanize gardenio gartner gdal ge geekflare gemfury gemini geomanio geonames getaround getblockio getbootstrap getcrossbeam getdivvy getexpressive getfedora getflywheel getformio getgrav getguru getmeadow getmonero getmyboat getpepperoni getpinoio getpocket getpostman getpublii getshogun getzephyr giantswarmio gioui giphy git-scm git-tower gitclear giteaio github-jodconverter github-mholt-certmagic gitpodio gitterim givelify gizmodo glamour glassdoor glia gliffy glimpse-editor glovoapp glowforge gmu-edu gnod gnome-gedit gnu-guix go2group goaccessio goatcounter gobetweenio gocardless godbolt godotengine goeditio gog goharborio goldmansachs golinksio gongio google-appengine google-bigquery google-chrome google-fonts google-recaptcha google-stackdriver gorillatoolkit goshippo gospotcheck govuk gq grab granaryio graphiteapp gravitio greendot greenpeace greenplum gremlin grepapp gridgain groovy-lang groupon grpcio grubhub gtmetrix gumroad guneco gvisordev gwtproject habitica haeckdesign haiku-os haproxy hashrocket hasuraio hbr healthgrades hellocoop hellogrove helloinspire helmsh heptio hexbin hexoio hibu hindsightsoftware hiptest hitachi hive hockeyapp honeybadgerio honeycombio hooyu hortonworks hsbc html5up huffingtonpost humio humu hyper-sh hyperledger hypervelocityconsulting iana icann icinga iconsearch idatalabs idc igalia illumos imagemagick inc includeos influxdata infoblox infor informatica infoworld ing ingress ingress-enlightened ingress-resistance inloopx instana instantlogosearch internetsociety invisionapp ironio iso isocpp isostech issuehuntio istioio itextpdf jabra jaegertracingio jamendo jamf janestreet javaee-glassfish jekyllrb jestjsio jimdo jobicy joinmastodon joyent joyent-containerpilot js-ajv js-discord js-redux js-webpack jsfoundation jsrio jujucharms julialang jumoworld justinmind k15t kabbage kakaocorp-talk kantegano katacoda katacontainersio keboola kii kik kleraio knot-resolvercz knowbe4 konghq kony kotlinlang labelmakr languageicon latimes legalshield leverco lexisnexis lg libreoffice lifehacker liferay lightbend lingoapp linkerdio loc logdna logicmonitor logmein logosearch lola lucidchart lyrebirdai macquarie macstadium maersk manifoldco manning mapd mapquest mapr marcus marcuse-ink marcuseinfo-greta markdown-here marlinfw marqeta mashable matillion mattermark maxmind mercurial-scm mi microsoft-vb mifos milligramio minioio mint mit-scratch mitedu mojang mojeek mono-project moogsoft morganstanley moven msi msnbc msu-edu mui mullvadnet mumosystems muralco myfonts mypaga nabcomau nacha nagios namelintdev nasa nationalreview natsio nbc nearform nearlyfreespeech neovimio nerves-project neteller netspend networksolutions neustar newyorker next-intldev nextdoor ni ni-labview nianticlabs nist nlnetlabsnl nlnetlabsnl-unbound nodemonio nodeping nomadlist nordnetse nozbe npr ns1 numerify nvmsh nytimes ogpme ojkgoid okfn omiseco onepoint-projects onnxai open-std-c openaccessbutton openapis openbundleio opencontainers openculture openlibrary openmetricsio openoffice openpolicyagent openssl opentable opentechfund opentofu opentracingio optimusmine otechie overops packerio packet palletsprojects-flask pandadoc pantheonio papaparse papertrailapp parsely parseplatform particleio paxos pbs pdfsam peco people pepsi perforce perlu phalconphp phaserio philadelphiapact philly phosphoricons phpmyadmin picmonkey pingboard pingcap pingpilot pir pivotalio pixabay platform9 plotly pm2io pocoo-jinja podmanio politico postmarkapp postmates powerhrg pptrdev praecipio printfly productplan prometheusio protractortest pulumiio puntcat purelyenergycouk purism purplejsio pytest q2 qasymphony qemu qgis qmetry qtio quad9 quickbase quicken quicwg quip qwant r-project rbs rd react-svgr readcube readmeio readthedocsio recodenet reconfigureio redashio redirect2me redpoint reducer refinedwiki regexplanet remixrun repaircafe replicantus replicated resolutionde resolvers reuters riadase ricksoft rightstar ringcentral ripenet ripple ritekit roguewave roku rollingstone rookio rookout rpm rssstyle ruby-lang rundeck rust-lang sandcastlezone sangria-graphql sas sass-lang scala-lang scala-sbt scaleway scalyr scancafe scientificamerican sdkmanio sdxcentral seatgeek sematext semmle sendwyre sensaco sensuio sentryio septa servicenow servicerocket severalnines sfconservancy shareaholic shell shieldsio shoelacestyle siemens signalfx signalsciences signnow signupgenius simple simpleicons simplelegal simplesharedev siriusxm siroopch six-group skf skrill skymindai slashdot slb smartbear smartdraw smartsheet smtp2go snaplogic snapsvgio snort societegenerale sofi softagram softwareag softwarefreedom softwareheritage softwareplant soloio soloio-gloo sonos sourceforge-asymptote spartez specteropsio spectrum sphereinc spiffeio spiffeio-spire spoke springio stackpath stardog statsbotco statusfyco steamdeck steampowered stencila stickermule-rump stitchdata stockanalysis storjio stride styleshout stylus-lang sumologic supergiantio supertinyicons surgesh sveltetechnology svgo svgporn svgrepo swarmos swaywm swishnu synctera syncthingnet tablerio tabulatorinfo tandemcouk target tasktop tcl te teachaccess teamtreehouse techcrunch techradar techsoup techstars techtime telepresenceio tempoio tencent tenta terraformio tesselio testio testlio theatlantic theguardian theia-ide thenextweb thenounproject theonion theorchard theregistercouk thestreet theverge thoughtbot thoughtworks tiaa tibco ticketmaster tidelift tikv time timedoctor tipeee tito todogroup toptal torproject tradeshift traeai traefikio transfergo transferwise transitiontechnologies trayio trifacta trinet trivago tuckey-urlrewrite twistlock tyk typescriptlang uber-ludwig ubs ultimatesoftware un unicodebot unicodesearch unitedhealthgroup unity3d ups uqamca usatoday usefulcharts usepanda vagrantup valiantys varnish-cache varnish-software vaultproject vectaio vectaio-nano vectorlogozone vectorlogozone-lotd veeva venturebeat verisign vice virtualbox virustotal vitejsdev vitessio vividcortex vogue vox w3-activitypub w3-html5 w3-svg w3c-validator w3c-xml w3schools wallsync walmart wandbai wappalyzer wasabi washingtonpost waspsh wavefront waymo weaveworks webhintio weeklystandard weibo wellsfargo westpaccomau wework wikidata wikimedia wikimedia-commons wikisource wiley wired wireshark wmtransfer woises workday worldlabel wsj xfinity xmatters xmindapp xometry xregexp yandex yarnpkg yasoon yelp-paasta yodlee youneedabudget zagat zcash zenefits zeplinio ziglang zipkinio zoomus zuul-ci zycada""")
add("db", """bigchaindb kubedb pipelinedb prestodb yottadb""")
add("dev", """apache-activemq apache-ant apache-apex apache-avro apache-batik apache-beam apache-calcite apache-carbondata apache-cassandra apache-cordova apache-couchdb apache-guacamole apache-hadoop apache-heron apache-hive apache-kafka apache-kudu apache-lucene apache-maven apache-mesos apache-nifi apache-openwhisk apache-orc apache-pdfbox apache-pig apache-poi apache-rocketmq apache-solr apache-storm apache-struts apache-subversion apache-tomcat apache-zookeeper""")
add("fw", """afterjs alertifyjs asyncjs babeljs backbonejs blueprintjs broccolijs chaijs claudiajs clipboardjs cosmicjs eggjs electronjs emberjs gatsbyjs github-postgresjs gruntjs guess-js gulpjs handlebarsjs hapijs infernojs ionicframework koajs leafletjs lesscss lunrjs mochajs netlifyapp-watercss npmjs nuxtjs parceljs picocss pugjs requirejs sequelizejs theupdateframework-notary totaljs w3-css yiiframework""")
add("media", """heatmaptv plextv videolan videolan-vlc worldclocktv""")
add("mkt", """adaptavist addthis addtoany adguard adidas adl adobe-acrobat adp advocately creativemarket gmail heapanalytics marketo marketwatch moonmailio sugarcrm""")
add("pay", """aminopay atombank bankofamerica blendedperspectives blendoco braintreepayments chimebank coinranking filecoinio gitcoinco goodmoney lloydsbank mpay24 namecoin payarafish paychex payoneer peercoinnet rabobank radiusbank rbcroyalbank santanderbank scotiabank softbank starlingbank tdbank usbank""")
add("sec", """edgesecurity fusionauthio pcisecuritystandards""")
add("shop", """appaloosa-store bigcommerce cartaoelocombr gitstoreapp grasshopper instacart""")
add("social", """bskysocial chatwork messagebird revoltchat socialtables toxchat""")


# app icons imported from dashboard-icons (auto-generated)
add("cloud", """azure-dns balena-cloud bewcloud cloud66 cloudbeaver cloudflare-pages cloudflare-zero-trust cloudflared cloudpanel cloudreve cloudstream coredns ddns-updater dns-private-resolver dns-zone duckdns filecloud ghostfolio google-cloud-print hostinger icloud immich-public-proxy newshosting nextcloud-blue nextcloud-calendar nextcloud-contacts nextcloud-cookbook nextcloud-cospend nextcloud-deck nextcloud-files nextcloud-ncdownloader nextcloud-news nextcloud-notes nextcloud-photos nextcloud-social nextcloud-tables nextcloud-tasks nextcloud-timemanager nextcloud-white nextcloudpi nextdns oauth2-proxy open-cloud oracle-cloud pirate-proxy self-hosted-gateway stb-proxy traefik-proxy tsd-proxy wd-mycloud yuno-host yunohost""")
add("db", """azure-sql-db azure-sql-server libreoffice-colibre-database sqlitebrowser telegraf""")
add("dev", """adventure-log ai-on-the-edge-device application-gateway-container aws-dynamodb-logo azure-container-apps azure-container-instances azure-container-service azure-devops azure-kubernetes-services azure-log-analytics-workspaces azure-monitor bab-technologie chrome-dev chrome-devtools code codellm coder codestats ddev devuan docker-engine docker-moby docker-volume-backup edge-dev elastic-logstash firefox-developer-edition gitam-university gitbucket gitee gitsign heylogin kubernetes-dashboard kubetail logitech-gaming logitech-legacy logseq logto nrk-logo onedev openchangelog portainer-alt portainer-be proxmox-backup-server pvy-code pvy-code-wordmark pvy-devices pvy-devices-wordmark qnap-containers rhodecode simplelogin sst-dev symmetricom synology synology-dsm victorialogs vito-deploy vscode western-digital whats-up-docker woodpecker-ci xpenology zot-registry""")
add("media", """agregarr anime-kai apple-tv-plus audiobookshelf bazarr book-lore booklogr booklore booklore-wordmark booko bookstack byparr chaptarr configarr deployarr dispatcharr doplarr emby facebook-messenger freshbooks google-play-books google-play-games grandstream healarr hi-anime homarr jellyfin-vue jellyseerr jellystat jellywatch kapowarr librariarr lidarr livebook manga-dex media-manager mediafire mediathekview midarr mlb-tv movie-pilot mstream music-assistant musicbrainz musicbrainz-picard mythtv nodecast-tv notebook-lm notifiarr open-notebook oscarr pepperbox-tv plex-alt plex-rewind plexrequests prime-video-alt profilarr prowlarr pulsarr pvy-bookmarks pvy-bookmarks-wordmark pvy-media pvy-media-wordmark pvy-mediahub pvy-mediahub-wordmark radarr readarr recyclarr restreamer samsung-tv-plus servarr shokoanime simplex-chat sonarr streamyfin streamystats swingmusic swiparr tiny-media-manager tracearr trailarr tunarr tvdb tvheadend virgin-media vtvgo waipu-tv watcharr whisparr wizarr xbox-game-pass yarr your-spotify youtube-tv""")
add("mkt", """ciphermail docker-mailserver eu-mail fastmail mail-archiver mail-in-a-box mailbox mailcow mailfence mailpit notion-mail purelymail pvy-mailarchiver pvy-mailarchiver-wordmark pvy-mailr pvy-mailr-wordmark snappymail stalwart-mail-server tuta-mail twake-mail twake-mail-wordmark zohomail""")
add("pay", """actual-budget budget-board budgetbee cryptomator monarch-money paymenter proton-wallet rocket-money rocket-money-wordmark wise-moneytransfer""")
add("prod", """1337x 13ft 1panel 20i 2dehands 3cx 4chan 5etools 7zip 8311 9router a-mule aboard action1 activepieces adminer advanzia affine air-trail airsonic airtel akaunting akkoma aks-automatic albert-heijn alertmanager alexa alexandrie alist aliyun alloy alma-linux altcha amazon-luna amazon-prime amazon-web-services anaconda-wordmark anchor android-auto android-robot angel-studios anonaddy any-listen anything-llm anytype apache-airflow apache-answer apache-druid apache-iceberg apache-jena apache-jena-wordmark apache-openoffice apc apiscp app-service appflowy apple-alt apple-maps application-gateways ara-records-ansible arcane archidekt archivebox archivedotorg argo-cd armbian aroz-os artifacthub artifactory aruba asciinema asrock-rack asrock-rack-ipmi astral astrbot astuto asus-full asus-rog asus-router asustor atlassian-bitbucket atlassian-confluence atlassian-opsgenie atlassian-trello atuin audacity audora aura auracast aurral auto-cad autobangumi autobrr automad av1 avg avif avigilon avm-fritzbox avm-fritzbox-4060 avm-fritzbox-5690 avm-fritzbox-6820 avm-fritzbox-6890 avm-fritzbox-7490 avm-fritzbox-7590 avm-fritzbox-7590oem avm-fritzbox-7590real avm-powerline-1000 avm-powerline-546 avm-repeater-2400 avm-repeater-3000 avm-repeater-310 avm-repeater-600 awwesome awx axis azuracast azure-application-insights azure-bicep azure-cosmos-db azure-cost-management azure-data-factory azure-expressroute-cirtcuits azure-front-door azure-postgres-server azure-service-bus azure-storage-accounts azure-traffic-manager azure-virtual-desktop azure-virtual-network-gateways azure-vm azure-vnet backrest backstage baikal bale balena-etcher ballerina bar-assistant barco barrage baserow bazecor be-quiet beaver-habit-tracker bechtle beef bentopdf beszel biblioreads bigcapital bikerouter bilibili binner bitly bitly-wordmark bitmagnet black-forest-labs black-forest-labs-wordmark blocky blu-ray blu-ray-3d boltnew borg borgmatic bottom boundary brick-tracker bright-move broadcastchannel brocade brother browserless browsh budibase build-better bunkerweb bunny burpsuite bytestash cabernet cachyos-linux cacti calibre-web calyxos canvas-lms cap-cut capacities caprover carousell carrefour casaos castopod catppuccin cc cd cert-manager cert-warden cessna chainguard changedetection channels-dvr check-cle check-point check-point-wordmark checkmate checkmk chess chhoto-url chibisafe chimera-linux chirpy chocolate chrome-canary chrome-remote-desktop cilium cinny clam-av claude-ai cleanuperr cockpit-cms collabora-online comfyui comfyui-wordmark commafeed commento compreface confix confluent contabo control-d converse cooler-control coolify copyparty copyq cosign cosmic counter-analytics cozy cpp crafty-controller cronicle cronmaster crosswatch crowdin crowdsec crowdsec-web-ui crowdstrike crowdstrike-wordmark crunchyroll cryptpad ctfreak ctrader ctrader-wordmark cup cups cura cyber-power-full cyberchef czkawka d-link dagster dalibo dall-e dashboard-icons dashwise data-studio databasus davical dawarich ddclient debian-linux defguard deluge denodo denon dependency-track dependency-track-wordmark deq dia diagrams-net dictcc digi-kam digikey dilg dillinger directadmin distribution dixa dkb dlna docassemble dockge docking-station dockpeek docling docsify docspell docuseal dokemon dokploy dokuwiki donetick doozle doppler double-commander double-take dozzle draytek drop dropout droppy dufs dumbassets dumbpad duo duplicati dvd dynacat e-os easy-gate easyepg-lite eblocker ecosia-wordmark edge eisfair eitaa elabftw elastic-beats elastic-kibana electronic-arts electrum eleven-labs elgato-wave-link eliza-os elysian embraer emq emqx emsesp emulatorjs enbizcard enclosed endeavouros-linux endel endless endurain enhance entergy erste erste-george erugo espocrm etesync etherpad eu-calendar eu-docs eu-drive eu-presentation eu-spreadsheet eu-talk evcc everhour exercism f1-dash f4map fairphone fairphone-wordmark falcon-player falkon-breeze fast-com fasten-health fedora-alt feedbase feedbin feedlynx feishin fenrus ferdium ferretdb fhem fidelity fider filebot filebrowser filebrowser-quantum fileflows filegator filen filerun files files-community filezilla finamp finanzen-zero findroid fios firefly firefly-iii firefox-beta firefox-lite firefox-nightly firefox-reality firefox-send fittrackee fladder flaresolverr flatnotes fleetdm flightradar24 flood floorp flowise flowtunes fluent-reader fluidd flutter-wordmark flux-cd flux-operator fmd fnos focalboard font-awesome-icons foreflight forgejo formbricks forte fortinet fossil foxit franz free-sas freecad freeipa freenas freenom freepbx freshping freshrss frigate fritzbox fronius frp fruux fulcio funkwhale garage garuda-linux gatus gboard geckoview gentoo-linux genua geo-guessr gerbera gerrit get-iplayer gigaset gladys-assistant glance glances glinet glitchtip glpi gluetun gnustep goaccess godaddy-alt golang goldilocks golink gollum gomft gonic google-admin google-alerts google-colab google-compute-engine google-contacts google-earth google-fi google-find google-forms google-jules google-lens google-news google-sites google-street-view google-tasks google-translate google-voice google-wifi gopeed gose gotify gpt4free gramps gramps-web graphite gravit-designer greenbone gridscale grimoire grist grocy gsap hammond handbrake haptic harbor harvester hasheous hashicorp-boundary hashicorp-consul hashicorp-nomad hashicorp-packer hashicorp-terraform hashicorp-vagrant hashicorp-waypoint hastypaste hathway hatsh hbo hcl-verse hd-icons headlamp headplane headscale healthchecks hedgedoc heimdall helium-token helix hemmelig hermes-icon hestia hetzner hetzner-h hexedit hexos heyform hifiberry hikvision hilook hivedav hoarder hollo honda-jet hoobs hotio hpe html hubitat hubzilla huginn humhub hydra hypermind hyperpipe hyprland i-librarian i2p i2pd ical icecast icewarp icewarp-office icinga-full icon idealo ideco idrac idrive iliadbox-svg ilo immich immich-frame immich-kiosk immich-power-tools incus infinite-craft infisical infomaniak-k infomaniak-kdrive infomaniak-kmeet infomaniak-swisstransfer inoreader intellij inventree invidious invisioncommunity invoice-ninja invoiceplane invoke-ai iobroker iode-os ionos ipboard ipfs ispconfig issabel-pbx issabel-pbx-wordmark istio it-tools italki itop ivanti jackett jaeger jan jdownloader jdownloader2 jeedom jelu jetbrains-toolbox jetbrains-youtrack jetkvm jetkvm-full jio jitsi jitsi-meet joplin jotty jujutsu-vcs jumpserver k3s kaboai kali-linux kamatera kanboard kanidm karakeep kasm kasm-workspaces kasten-k10 kaufland kavita kbin keda keenetic keenetic-alt keepass keila kerberos kestra keybr keyoxide keyoxide-alt kimai kimi-ai kinopub kitana kitchenowl kiwix kleinanzeigen kleopatra klipper knx ko-insight koel koillection koito komga komodo komoot konica-minolta kontoj kook kopia koreader kpn krakend krokiet krusader ksuite kubuntu-linux kutt kyoo lab-dash lact lakefs lancache lancom lancom-wordmark lancommander laracasts lark latitudesh leanote leantime lemmy lexmark libation libreddit librenms libreoffice-colibre-graphic libreoffice-colibre-presentation libreoffice-colibre-spreadsheet libreoffice-colibre-text libretranslate librewolf librum lichess lidl limesurvey lineage linguacafe linkace linkding linkstack linksys linux linuxdo linuxgsm linuxserver-io liremdb listenbrainz listmonk lite-speed litlellm littlelink-custom lldap lms-mixtape lnbits local-content-share local-xpose locals lockheed-martin lodestone loki longhorn lostack lovable-wordmark loxone loxone-full lubuntu-linux ludus lunalytics lunasea lynx lyrion m3u-editor macmon mafl magicinfo mainsail maintainerr maker-world maltego maltego-wordmark manjaro-linux mantrae many-notes manyfold mapcomplete mapillary maptiler mapy marimo marktplaats material-design-icons matterbridge max mayan-edms maybe mbin mealie medama mediux mega-nz memories memos meraki mercusys mergeable meshping meshtastic metabrainz metallb metube microsoft-365 microsoft-365-admin-center microsoft-bing microsoft-dataverse microsoft-exchange microsoft-intune microsoft-power-automate mikrotik milinote miniflux minimax minio misskey mitra mixpost mkdocs ml-flow-wordmark mobilizon mobioffice mobotix modrinth monica moodist moodle morphos morss mosquitto motioneye mousehole mousetrap mqtt mtlynch-picoshare mubi mullvad mullvad-browser multi-scrobbler mumble mundraub murena murena-wordmark musescore myheats mympd myspeed mysterium name-silo natwest navidrome nebula neko neocities neodb neon-tech neonlink netalertx netapp netatmo netbird netboot netbootxyz netbox netbox-full netdata netgear netsurf network-ups-tools networking-toolbox newegg newsblur nextbike nextbike-wordmark nexterm nexus nginx-proxy-manager nicotine-plus nightscout nikku nintendo-switch niri niri-wordmark nitter node-red nodebb nodejs-alt noisedash nomie note-mark notediscovery notesnook notion-calendar novnc nsg ntfy nu-nl nuclino nut nut-webgui nutanix nuxt-js-wordmark nzbdav nzbget nzbhydra2 obico obtainium octoprint ocular oculus odoo odysee odysee-full odysseus oepnvmap office-365 office-eu office-eu-wordmark oh-my-posh olivetin omada ombi omnic-forge omnidb omnivore oneuptime onlyfans onlyoffice onshape ookla-speedtest open-central-control-unit open-classrooms open-observe open-regex open-resume open-source-initiative open-wb openbao openclaw-wordmark opencost openeats openemr opengist openhab openldap openlist openpanel openproject openreads openspeedtest opensuse opentalk openuem openvas openwebrx-plus openwrt openziti opera-touch opnform opnsense orange orb osmand osmapp osticket osu otter-wiki outline overseerr ovh ovirt owncast owntone owntracks oxker p-cal p1ib packetfence packetfence-full palemoon palo-alto pangolin paperless paperless-gpt paperless-ng paperless-ngx papermark papermerge papra paramount-plus parseable part-db partkeepr passwork pastebin patchmon pdf24 pdfding peacock peanut pelican-panel peppermint pepperminty-wiki pepperstone perlite pg-back-web pgadmin pgbackweb phanpy phase phoneinfoga phorge phoscon photonix photoprism photostructure photoview pi-coding-agent pi-hole pia picsur pigallery2 pigeonpod pikapods pikvm pingvin pingvin-share pinkary pioneer piped piwigo pkl plane plane-finder planka plantuml playstation-plus pleroma plesk plume pocket-id podfetch podify podman polaris polarisoffice policycontroller poly polywork poolside-ai portracker portus postal poste posteria postgres postgresus postiz powerbi premiumize pretix price-buddy primal printables printer pritunl privacyidea private-internet-access privatebin projectsend prolific prometheus-node-exporter proton proton-calendar proton-docs proton-lumo proton-meet proton-pass proton-sheets protondb proxcenter proxmenu prozilla-os prtg prunemate prusa-research pterodactyl public-pool pufferpanel pulse pure-storage pushfish pushover puter putty pvy-ai pvy-ai-wordmark pvy-analytics pvy-analytics-wordmark pvy-applytics pvy-applytics-wordmark pvy-archiver pvy-archiver-wordmark pvy-assets pvy-assets-wordmark pvy-automat pvy-automat-wordmark pvy-backup pvy-backup-wordmark pvy-base pvy-base-wordmark pvy-bot pvy-bot-wordmark pvy-buddy pvy-buddy-wordmark pvy-bugtracker pvy-bugtracker-wordmark pvy-businessos pvy-businessos-wordmark pvy-buttler pvy-buttler-wordmark pvy-cal pvy-cal-wordmark pvy-captcha pvy-captcha-wordmark pvy-central pvy-central-wordmark pvy-community pvy-community-wordmark pvy-files pvy-files-wordmark pvy-forms pvy-forms-wordmark pvy-groupware pvy-groupware-wordmark pvy-gtd pvy-gtd-wordmark pvy-id pvy-id-wordmark pvy-lnkr pvy-lnkr-wordmark pvy-local pvy-local-wordmark pvy-localize pvy-localize-wordmark pvy-maps pvy-maps-wordmark pvy-mdm pvy-mdm-wordmark pvy-meeting pvy-meeting-wordmark pvy-mesh pvy-mesh-wordmark pvy-messenger pvy-messenger-wordmark pvy-news pvy-news-wordmark pvy-notes pvy-notes-wordmark pvy-office pvy-office-wordmark pvy-pad pvy-pad-wordmark pvy-pbx pvy-pbx-wordmark pvy-photo pvy-photo-wordmark pvy-remote pvy-remote-wordmark pvy-safe pvy-safe-wordmark pvy-search pvy-search-wordmark pvy-servicedesk pvy-servicedesk-wordmark pvy-sign pvy-sign-wordmark pvy-snippets pvy-snippets-wordmark pvy-spreadsheet pvy-spreadsheet-wordmark pvy-start pvy-start-wordmark pvy-timer pvy-timer-wordmark pvy-ux pvy-ux-wordmark pvy-webcall pvy-webcall-wordmark pvy-wiki pvy-wiki-wordmark pvyaffiliate pvyaffiliate-wordmark pydio pyload pypi-wordmark qbittorrent qd-today qdirstat qinglong qlik2 qnap qnap-adra-ndr qnap-qsync qnap-qvr-center qnap-qvr-face qnap-qvr-human qnap-qvr-surveillance qnap-virtualization qobuz questdb quetre qui quickshare quickwit quizlet qutebrowser r rackpeek rackula radarr-4k radarr-dv radicale rainloop rallly ramp rapid7 rdt-client reactive-resume reactjs readeck readthedocs readwise-reader real-debrid recalbox receipt-wrangler recipesage recommander red-dead-redemption-2 red-dead-redemption-2-wordmark redhat-linux redict redlib redmine rekor release-argus remmina remnawave remnote renovate reolink requestly requestrr resiliosync resiliosync-full retrom revanced-manager revolt rhasspy richy rimgo ripe riverside-fm rockstor romm rook roon root-me rotki router rport rss-bridge rss-translator rstudioserver ruby-on-rails runonflux runson rustdesk rustfs rutorrent rybbit rygel ryot sabnzbd safari-ios safeline sailfishos salt-project saltcorn samba-server sandstorm sat-ip sat-ip-wordmark scanopy schedulearn scrcpy screenconnect scriberr scrutiny seafile searx searxng seelf seerr selfh-st send sendinblue series-troxide serviio session seznam shaarli shadow sharewood sharry shell-tips shellhub shellngn shelly shelly-wordmark shinkro shiori shlink shoko shoko-server sickbeard signaturepdf signoz silae simkl simpli sinusbot sipeed siyuan skribblio slash slice slskd snapcast snapdrop snapmaker snapmaker-wordmark snikket snowshare softmakerfreeoffice softmakeroffice solaar solarwinds-wordmark solidtime solus sonarr-4k sonarr-dv sophos sourcehut sourcehut-wordmark spamassassin sparkasse sparkleshare specifically-clementines sphinx sphinx-doc sphinx-relay spiceworks spliit sponsorblock spoolman springboot-initializer squidex squirrel-servers-manager sshwifty stackfield stacks stalwart standard-notes startpage startpage-wordmark statistics-for-strava statuspage-wordmark step-ca stirling-pdf stoat storj storm stormkit strato stremio stump stump-alt subatic sun-panel sunsama sunshine supermicro sure surfshark surveymonkey suwayomi svgedit swarmpit synapse syncplay syncthing sysreptor tabula tacticalrmm tailwind talos tandoor-recipes tangerine-ui taskcafe taskwarrior tasmocompiler tasmota tautulli teamtailor telekom teleport telmex tempo tenable tenda tensorflow-wordmark termix terramaster teslamate tether-wordmark thanos the-pirate-bay the-proxy-bay thehive theia thelounge theodinproject thin-linc thingsboard thread thread-wordmark threadfin thunderbird tianji ticky tiddlywiki timetagger ting-isp title-card-maker tmdb toggl tolgee tooljet toolz topdesk toshiba touitomamout tp-link tpdb traccar trackeep trading-view traggo trakt trala transmission trellix tricentis-tosca trilium triliumnext trmnl truecommand truenas-core truenas-scale tryhackme tubesync tunnelix tuta-calendar tux tweakers twingate tyepcho typemill ubiquiti-networks ubiquiti-unifi ubports ubuntu-linux ubuntu-linux-alt uc-browser uefi ugreen ultimate-guitar umami umbrel unbound uncomplicated-alert-receiver undb unifi unifi-drive unifi-voucher-site unimus university-applied-sciences-brandenburg unraid untangle upsnap uptime-kuma uptimerobot upvote-rss usermin valetudo valkey veeam velero vera-crypt verizon verriflo vertiv vi victron-energy vidzy viewtube vikunja vinchin-backup virtualmin virustotal-wordmark viseron vitalpbx vllm vmware-esxi vmware-workstation vn-stat vodafone void-linux voilib voip-ms volkszaehler volla voltaserve volumio voron vue-js vuetorrent wakapi wallabag wanderer warpgate watchtower waze wazuh web-check webdb webhook webhookd webtrees wero wetransfer wevr-labs wger whatnot whatseerr whishper wiki-go wikidata-wordmark wikidocs wikijs wikijs-alt willow windmill windows-10 windows-95 windows-explorer windows-retro wiz wolfi wolframalpha wooting worklenz wotdle wownero writefreely xbackbone xbrowsersync xcp-ng xen-orchestra xiaomi-global xigmanas xmr xmrig xpipe xray xubuntu-linux yac-reader yacd-blue yacht yamtrack ynab yopass yourls youtube-dl youtube-kids youtube-studio yt-dlp yts z-ai z-wave-js-ui zabka zalo zammad zappier zashboard zenarmor zenmux zigbee2mqtt zimbra zipcaptions zipline zipline-diced zitadel zomro zoom-alt zoraxy zorin-linux zyxel-communications zyxel-networks zyxel-networks-wordmark""")
add("sec", """2fauth adguard-home adguard-home-sync airvpn aliasvault authelia authentik authman azure-firewall azure-keyvault firewalla fusionauth hashicorp-vault keeper-security mullvad-vpn multifactor-authenticator openmediavault pvy-vault pvy-vault-wordmark pvy-vpn pvy-vpn-wordmark qnap-firewall qnap-vpn secureai-tools security-onion tinyauth vaultwarden vouchervault""")
add("shop", """app-store google-shopping our-shopping-list pvy-appstore pvy-appstore-wordmark sub-store""")
add("social", """chatpad-ai chatwoot diamond-aircraft fluffychat google-messages gotosocial librechat lobe-chat matrix-synapse socialhome""")
add("web", """esphome esphome-alt foldingathome hdhomerun home-assistant-alt homebox homebridge homehub homelabids homelable homer homey luxriot pvy-homeassistant pvy-homeassistant-wordmark smartfox telekom-magenta-smarthome""")


# cloud-native logos (auto-generated)
add("cloud", """3-scale aeraki-mesh afi-ai akana alibaba-cloud-container-service-for-kubernetes alibaba-cloud-file-storage alibaba-cloud-file-storage-cpfs alibaba-cloud-function-compute alibaba-nacos alibaba-sae alibaba-tengine alluxio amazon-ecs amazon-elastic-block-store antrea apache-camel-k apioak apisix armada asus-cloud-infra aws-cloud-map aws-sam azure-api-management azure-disk-storage azure-service-fabric backend-ai baidu-cfc bfe bootc canonical-charmed-distribution-of-kubernetes capsule carina catalyst-by-zoho chalice china-mobile-cloud-cnp china-mobile-panji-paas choreo clevercloud cloud-native-landscape cloudcasa clush-kube clusternet clusterpedia cni-genie cocktail-cloud commvault container-network-interface-cni container-storage-interface-csi contour cozystack cubefs cubex cumulus dashbird datacore-puls8 datenlord datera dell-emc desktop-kubernetes digital-ocean-kubernetes direktiv dockerswarm dolphin-scheduler drivescale easegress easemesh easystack-eks emissary-ingress encore envoy-gateway eventmesh expontech fabedge fdio firecracker fission flatcar flogo fluid fsm gardener glasnostic gloo gloomesh gluster godel-scheduler google-persistent-disk gravitee grey-matter guardi-core-centra gvisor h3-c-cloud-os hami hango hasura-graphqlengine higress hikube huawei-cloud-container-engine-cce huawei-functionstage hwameistor hyperlight ibm-kubernetes ibm-storage ibmcloud-codeengine ibmcloud-functions inclavare infinidat infoscale inlets interlink iomesh ionir isscloud isulad juicefs k0rdent k0rdent-logo-1 k0s-logo-2025 k3k k8gb k8s-the-easier-way k8up kanister karmada kasten kata katalyst kcp kilo kind kmesh knative knix koordinator koyeb krustlet kuadrant kube-green kube-ovn kube-router kube-rs kubeadmiral kubeasz kubebrain kubeclipper kubefleet kubegateway kubekey kubero kubeservice-stack kubeslice kubesphere kubespray kubevip kuma-stacked kured kurl kusk kwok kyma layotto ligato lima linstor logo-red-hat-openshift-dedicated-a-standard-rgb loxilb lumigo lunar-dev lxd mantech-accordion membrane merbridge metalstack-cloud microk8s midway minikube moosefs mosn-mosn msap-ai multus netflix-oss-eureka netflix-oss-zuul netlify-functions nia-k-paas nimbella nitric nocode nodelambda nokv nova nuagenetworks nuclio nuweba oci-runc ondat open-cluster-management open-nebula open-service-mesh open-v-switch openatom-nestos-kubernetes openebs openelb-io openfaas openfunction openio openresty opensandbox opensdn opensergo openstack-swift oracle-functions oras orka ovn-kubernetes oxia paasta palette pengyun pipeline-ai pipy piraeus platform-sh portworx prisma-cloud-palo-alto project-calico project-velero protego pub-nub-functions qingstor qumulo reactive-interaction-gateway red-hat-open-shift red-hat-openshift-ibm-cloud ring rke2 robin-systems saaras salad samsung-cloud sandstone sangfor scaleflash scalingo scar secloudit second-state-functions sentinel sermant serverless-devs service-mesh-interface service-mesh-performance shturval sighup-distribution simplyblock singularity skipper slappforge-sigma slime slimfaas slurm smartos soda-foundation sparta spiderpool spring-cloud-function stackery stackstorm standard-library starlingx stash-by-apps-code statefun storpool stratovirt stunner submariner superplane sysbox talos-linux tarook tata-vayu tencent-cloud-serverless-cloud-function threat-stack thundra traefik-mesh trilio triton-object-storage tsb twilio-functions typhoon urunc vineyard virtual-kubelet vmware-nsx volcano wasmedge webiny welkin workflow wso2 xline xsky yanrong yellowdog zenko""")
add("corp", """1crew 1nce 23-technologies 3-shake 3-shake-inc 42on 4intelligence 6wind 8gears 99-cloud-kcsp 99-cloud-ktp 99cloud-member a2a acc-ict access-quality-presentacion-digital accuknox acend ackstorm acorn-labs acornsoft adfolks adidas-supporter aembit aenix aeolabs afi afs agenda agent-development-kit agent-field agent-sandbox agentevaluation agentgateway agileops agno aikido-security aim aiven akamas akamas-member akatsuki-member akuity alasca alauda alauda-member alerant alibaba-cloud-kcsp alibaba-cloud-member alien6 allianz-direct alligator alpa-logo-cropped alpha-business alter-way altinity alvistack amadeus-supporter amazee-io ambassador-labs amberflo-io ambient-it american-cloud amesto-fortytwo amnic amoniac ampere-computing-member anchore andes-digital anova ant-financial-member anynines-member aoe aokumo apache-zeppelin ape-factory apecloud apica apiiro apollo apono appcd appddiction-studio applied37 appstellar appvia aqua arcfra archeros archestra arcjet arctera ardc argyle arima arks arm-member armo armored-gate armory-member arpio arrikto-member asml aspen-mesh asus-cloud atix-ag atlassian-member atolio atos attribute audi audit-board-supporter auristor authkeys authzed autocloud autogen autovia avesha aviatrix avisi awesome-information-technology axcelinno axiata-digital-labs axmos-technologies axoflow axolotl b-nova b1-systems back-market backslash baidu-kcsp baidu-member banco-de-credito-bcp bancolombia bankofmontreal bankware-global bayer bc-cloud bear begasoft bellsoft bentoml berrybytes bessystem better-stack binario-etico bindplane bitrock bizkube bizmicro blackrock blacksmith blakyaks blizzard block bloomberg-member blue-sentry bluebricks bo-cloud bo-cloud-beyond-container bo-cloud-kcsp bo-cloud-member bonc booz-allen-hamilton-kcsp border0 box-supporter braingu breqwatr brobridge-kcsp brobridge-member browser-use buf-technologies buoyant bxcloud bytesource cablelabs-snaps-k8s calyptia cambia-health-solutions-member camel camelai camptocamp-kcsp camptocamp-ktp camptocamp-member canada-infoway cann canonical-kcsp canonical-member capital-one cardinal cardinal-health cardinalhq cargurus cariad cars cast cast-ai cathay causely caylent cecloud celerdata celonis cengn-member centrica cfl chainloop chaitin charter checkly china-mobile-cmit china-mobile-cmit-all china-mobile-kcsp china-mobile-member china-systems china-telecom china-unicom chislitel-lab chkk chronosphere cielara cinq cinq-ict circle-ci-member ciroos cisco-container-platform cisel-informatique citi civo claion clastix cleanstart clockwork cloud-ace cloud-foundry-foundation-member cloud-kinetics cloud-native-texas cloud-ops-member cloudbase-solutions-member cloudbolt cloudboostr cloudcasa-by-catalogic cloudchipr cloudcontrol cloudeq cloudfabrix cloudferro cloudgeometry cloudical-kcsp cloudical-member cloudification cloudlink cloudmate cloudoor cloudsmith clush clyso-member cme-group cobank cocktail-io code-narrator cognizant comcast-member comforte compliancecow component-soft composio confidentialmind confluentis conoa constellation contrast-security control-plane control-plane-corporation controlmonkey controlplane controltheory cookpad-supporter cordial core247 coreweave cortex-member crafter-cms crewai cribl cruise crystaldb cto-ai cto2b ctrlstack cube-sandbox cue-labs cuemby cvshealth cybozu cycode cyso d2iq d2iq-dispatch dachs-it daekyo danm dao-cloud-member daocloud dash0-member datacore datacore-bolt datadog-member datadrivers-kcsp datadrivers-member datafy datagalaxy datree-logo-tall daugherty db-systel dbos de-novo decathlon decimal deepchecks deeperthanblue deepeval deepfactor deepfence deepflow deepshore deepspeed defense-unicorns dell-consulting dell-technologies deloitte-consulting-member deloitte-kcsp densify depot desotech detech-ai deutsche-telekom-ag devsoperative devtron devzero dfds dgi dhh diagrid diamanti didim365 dify digital-challengers digital-china digitalchina digitalrebar dina directv dlocal docomo dog doit dongobi door-dash-supporter dosec doubleword dr-droid draftt dragonflydb dynatrace-member e-bay-member e-on e2b easystack echo eclipse-foundation-member ecloudtech edb edera edgedelta edgeless-systems edgenesis edgeray effectual eidp eitco elastic-member elastiflow elastisys elastx elastx-member elephant elotl emagine-it emq-technologies-member endress-hauser entegral entigo enum env0 envzero epam-systems epsio equityzen ericsson-member erlang-ecosystem-foundation everquote eviden evolutio evolvere evonem excellion exein exoscale-member exostellar exotanium expedia-group expert-thinking f5 f5-member facets-cloud factory fairwinds falkordb fatmap feast fidelity-investments finout firehydrant fiserv flamingo flanksource flant flant-deckhouse flant-member flox fluid-icon fluxninja fongcon forge-utah-foundation form3-supporter formal fossa fournine fr0ntierx framework frontier fuga fujitsu-k5 fullstacks fullstaq fury futurewei g-research gaia garden-member gcore ge-healthcare geeks-solutions genezio german-edge-cloud giant-swarm-cncf giant-swarm-member gientech gim-uemoa giraffe gmx golden-gate-university-member goldman-sachs-member golem-cloud google-kubernetes-engine grafana-labs-member grape-up-kcsp grape-up-member grepr greptime groundcover guardrailsai guida guidance guidewire h3-c-technologies-member ha-proxy-technologies-member hammerspace-member harmony-cloud-member harmonycloud harness-member harpoon hatchet hawkstack haystack hazelcast-jet hcl hedgehog hidora highlight hitrust honeycomb hoopdev horovod horse hostersi hpe-kcsp hpe-ktp hpe-member hpe-storage hps huawei-kcsp hud huifu humanitec hunter-strategy hush-security hydrolix hyground hyperdx hyperopt hyve-managed-hosting i-cubed-systems-supporter iauro icubed if-information-systems ignw iguana iherb iits-consulting ilki-member incloud incloudos indeed-member infinyon infosys infracloud infros initializ innogrid inovex-kcsp inovex-ktp inovex-member inspur instructor instruqt intercept intercloud intuit-member isoftstone isovalent itgix itq jd-cloud jd-com jellyfish jetify jetstack jetstack-member jinareader jit jozu jp-morgan-chase-member juniper-networks jysk k-serve k0s kamaji kapa-ai kapstan katib kbsys kedify keep-alerting kentik-member kestrel keyfactor keymate kgateway king kinx kiowy kiratech kiratech-kcsp kiratech-ktp kiratech-member kiwi kloia kodekloud kodem komodor kong-member koperator kossa ksat kt-cloud kt-nexr kthena ktrust kubeark kubeclarity kubecube kubeflow kubeless kubeops kuberix kubermatic kubeshop kubesphere-member kubevisor kubex kublr kueue kumina kumina-member kusari kyverno-icon kyverno-json la-mobiliere-supporter lablup lacework lancedb lanfuse langgraph larsen-toubro last9 leaderworkerset lean-ix-member leaseweb legit-security leminnov lfeducation-navy lightrun like-minds-consulting linbit liquid-reply llamacpp llamafactory llamaindex llm-d llmaz llmguard lmevaluationharness lmql loft-labs loophole-labs lpi-japan lsd-open lseg ltimindtree lunar ly-corp m-sys-technologies-member mac-stadium-member magellano makinarocks mambu man-tech marqo massdriver masterclass mastercontrol materna mathworks-member matrixx matrixxsoftware mattermost-member mavenir mavensolutions maze mc-kinsey-company-member mcp mecha-systems megaease megatron megazonecloud meltwater-supporter mem0 merck merly meshcloud metalbear metis-data metoro metrostar mezmo miao-yun-kcsp miao-yun-member michelin micro-focus-member middleware midships min-io-member minimus mirantis mirantis-member miraxia-edge-technology mitre mlrun mogenius moment monostream-member moonlight-marketing moose moresec morgan-stanley-member morning-consult morpheus-data-member move2cloud msys myfitnesspal n3xgen nadrama naic-member namespace-labs namutech napptive narwhal nasdaq-supporter nasp navimentum nccl ndustrial nebius nec nemo nemoguardrails net-foundry-member netease nethopper netmatch netnod netris netways neuroglia nhn-cloud nia nimtech nipa nipr-member nirmata nirmata-member nlsiq nodeshift nokia-member noms nops northflank novaglobal novo-nordisk novo-norsidk nscale ntt-data nudgebee nunet nuvitek nuvotex nvidia-member obss occentus ochestra octo-consulting octopus odigos ogis-ri okahu okestro ollygarden on-prem onecause ongres oodle opa-icon opea-stacked open-compute open-ll-metry open-mpi open-source-consulting opencompass openflame openmaru openmaru-cop openmetal opennebula openpaya openvino operant opscruise opslevel opsmx opstrace optuna opus orcasio origoss-solutions-kcsp origoss-solutions-member orkes osso oteemo oteemo-member otterize outlines ovhcloud p0-security palark palo-alto-networks parity parler-cloud payit pcp-consulting pdt-partners pelanor pelotech peloton pengcheng-laboratory perfectscale peritus-logo-pink permit-io petasus-cloud pgedge pgvector picnic pilosa ping-an pinot pionative pipekit plakar platform-engineering-labs platform-engineering-masters platform9-managed-kubernetes platform9-member plural plusserver polar-signals polar-squad polar-squad-member polkadot porch-financial porsche port portworx-by-purestorage posedio posit post-finance-supporter previder prodigy-education prodvana prodyna prodyna-member project-contour prometheus-icon promptfoo promscale prosiebensat1 proximaops ps-cloud-services puffersoft pusher-supporter puzzle pydanticai q-aware-member qazaq-open-source-initiative qbo qiming qingcloud qleet qrt quail quali quality-cloud qualitysoft quantumcns qubex querydesk quesma rackner rad-security rafay raft ragas raincoat randoli rapidfort ray raydian-cloud raytheontechnologies rbg reblaze recinq red-hat-member reddit-supporter redeploy redkubes redpill-linpro reevo reevo-spa refinitiv releasehub relvy reo-dev replicated-member resolve-ai resolve-technology restate rewe-group ricardo ridge rig riptides-labs risc-v-international rng-technology roadie robin-systems-member robusta rookout-member roost root rootly royalbankofcanada runwhen rx-m saic salad-technologies saltware samsung-sds sap-concur-supporter sath sawmills scaleops scaleway-member scarf scribe-security scylla seacom seagate seal-security seal-sotware searce second-state secondfront section-member sedai seldon-idwf-vlclv-10 seleniumgrid semantickernel seowon-information servicememe services4-it sglang shandong-cvicse-middleware shanghai-hftech shanghai-mandao she-bash shinesoft shipfox shopify-supporter shoreline sidero sifamo sighup-kcsp sighup-member siglens signadot sigscalr sk-telecom sky-bet skyline skyloud slc-devopsdays slimai smallstep smart-cloud smartiful smartx smolagents sncf snow-software socradev-gmbh software-mind sokube solanica solo-io-member sonarsource sonatype sony-interactive-entertainment source-allies sourcefuse southworks spacelift sparkfabrik speakeasy-development spectro-cloud speedscale sphereex spitzkop spotify-member springer-nature square-keywhiz squarespace-member squer stack-io stack8s stackgen stackgenie stackguardian stackit stacklet stacklock stacklok stateful stclab steamhaus storm-reply stormforge strands strategic-education stratox streamnative streamsets structsure styra-member sue-b-v sup-info superorbital sva svix sw-engineering-lab-of-zhejiang-university-member sweet-security swisscom swisspost switch synadia-communications synax syntasso synx-data-labs syseleven t-mobile t-systems taiwan-ai-cloud tata-communications tcc-consulting-limited teciem telecommunications-technology-association-member telenor teletrace tempest temporal tencent-cloud tensor9 tensormesh tenxcloud terasky terracotta-ai terramate testifysec tetrate teuto-net teuto-stack-member teutostack thales the-new-york-times-supporter the-scale-factory the-scale-factory-kcsp the-scale-factory-member thermo-fisher thnk-big thoras-ai thought-machine ticket-master-supporter tigera tigris-data timecraft tintri tl-consulting-group tmaxcloud tno tokyo-gas tomtom tongtech toppan-merrill traas-chaos traceroute42 traefik-labs transposit transwarp transwarp-technologies-member travelping-member traversal trendmicroincorporated treyee triam-security trino triton true truefoundry truefullstaq trulens tungsten-fabric txtai ukg umb-ag under-armour unicloud unicom-cloud union-ai university-of-michigan unskript unsloth unstructured upbound-member upcloud upmc-enterprises upsider-supporter uptycs upwind-security uturn-data-solutions uws va-linux-systems-japan va-linux-systems-japan-member valve vcluster velocity veritas-automata verl vessl-ai vexxhost vhl viettel vijil vivo vllm-logo-text vmclarity vmware-tanzu vnet volcano-engine volvo vshn walmart-member wanclouds wand-cloud wandb-logo-yellow-dots-black-wb wasm-edge wasmedge-plugin wavecon wavestack wayfair weaviate-nav-logo wehkamp wescale whatap-labs whitestack whizus wiit wikimedia-member william-hill wind-river wing-programming-language wise2-c-kcsp wise2-c-member wocloud woqutech workday-supporter wowjoy-technology wso2-member x-cellent x-ion xenit xgboost xgeeks xigxog ybor-ai yellowbrick yld-kcsp yld-member yonder yovily yunikorn yusur zalando-supporter zededainc zelar zendesk-supporter zenduty zenml zesty ziax zoi zstack zte-kcsp zte-tecs zuplo""")
add("db", """amazon-kinesis apache-ignite apache-streampipes apicurio-registry arkflow automq azure-event-hubs beam carbondata cdevents cloud-events cloudnative-pg crunchy-data databend deepstream doris drasi druid eduplace endee flink glassflow google-cloud-dataflow graphscope greptimedb hazelcast ibmdb2 iguazio infinispan intersystemsiris kube-db-by-apps-code kubeblocks kubemq memphis nebulagraph numaproj oceanbase openeverest opengemini openmessaging orient-db pachyderm panweidb polardb pravega pulsar qubole scalardb schemahero seata shardingsphere siddhi software spicedb starrocks stolon strimzi talend-data-streams tarantool tdengine tidb tremor uqbar userver vald vertica-ot voltdb xtdb ydb yugabytedb""")
add("dev", """agentregistry agola airship akri alibaba-cloud-ahas alibaba-cloud-application-real-time-service alibaba-cloud-container-registry alibaba-cloud-log-service alibaba-fnf amazon-cloudwatch amazon-ecr anteon apollo-1 applications-manager aspecto aternity azure-pipelines azure-registry blue-matador botkube brigade bub bucket bucketeer buildpacks bunnyshell bytebase cadenceworkflow cape cartographer carvel cdk8s chaos-mesh chaos-meta chaosblade chaoskube chaterm chef-habitat chef-infra cloud-custodian cloudark-kubeplus cloudfoundry-bosh cloudhealth cloudify cloudpilot-ai cloudtty cloudwise-synthetic-monitoring codefresh codezero coroot cortex couler cyclops dalec dapr dataset daytona deploy-hub devcycle devfile devspace devstream distrsh docker-compose dragonfly dxo2-by-broadcom easeagent elastic-apm elastiflow-mermin fabric8-kubernetes-client falcon featurehub flagger flagsmith flipt flowmill fonio foreman foresight fortio gefyra gitness gocrane gofeatureflag gonzo google-cloud-build google-container-registry goose grafana-mimir grafana-pyroscope grafana-tempo granulate guance-cloud helios helmwave hertzbeat holmesgpt honeybadger huatuo hubble-rgb hyscale ibm-cloud-container-registry idem-project infracost inspektor-gadget irondb itopia j-frog-artifactory jenkins-x jreleaser k-inv k6 k8sgpt kagent kairos kaniko kapeta kapitan karpenter kcl keep kepler keploy keptn kiali kiosk kitops kloudfuse ko konveyor kosko kots kpt kratix krator krkn kruize kube-burner kubean kubecost kubectl-mcp-server kubediagrams kubedl kubefirst kubefwd kubeorbit kubereport kuberhealthy kubeskoop kubevela kubevirt kubevpn kubezoo kudo kui kunobi kusionstack lagoon lindb linux-kit liquibase loggie logging-operator logiq logz-io m3 maas mackerel manage-iq mergify meshinfra metal3 mia-platform microcks micrometer mirrord modelpack monocle monokle mplat netis netobserv nexclipper nightingale nmstate nocalhost nodesource oam okteto omni omnistrate open-tracing openchoreo openfeature opengitops openkruise openlit openllmetry openmetrics openrun openservicebrokerapi opentsdb openyurt operator-framework opsani ortelius ozone pandora perses pinpoint pipecd pixie podman-desktop porter-sh powerful-seal projectsyn radar radius raftt razee replex rizhiyi runme-notebooks score screwdriver sdc sealer servicecomb serviceradar shifu shipwright skaffold skooner sky-walking sofastack-sofa-tracer sosivio splitio spot spring-cloud-sleuth squash stacker stackstate steadybit sws tanka tekton telemetryhub-scoutapm telepresence tencent-cloud-log-service terranetes testkube tilt tingyun tinkerbell traas-bos traas-has tracetest trickster trink turbonomic unleash unryo updatecli vamp virtasant vmware-application-catalog vmware-aria-operations-for-applications vmware-vsphere volcano-engine-apmplus volcano-engine-vmp vscodek8stools werf xl-deploy xoap-plain xregistry yoke zipkin zot zuul""")
add("fw", """apache-brpc apache-thrift avro cloudwego connect-rpc dubbo easy-ngo go-zero gofr kratos sofastack-sofa-rpc srpc tars""")
add("lang", """ambient azure-kubernetes-service bytecode-alliance cargo casper container2wasm containerd cosmonic cosmwasm crates cri-o dapr-for-wasmedge dfinity docker-member elfconv eunomia fermyon filecoin flows-network fluvio gear golem grain kuasar kube-edge kwasm libsql llvm lunatic meshery metatype modsurfer moonbit near observe opengauss pyodide quai redpanda runwasi rustwasm scale sel4 spiderlightning spin spinkube superedge taikun taubyte tinygo unikraft wa-lang wasix wasm wasm2c wasm3 wasmcloud wasmedge-quickjs wasmer wavm wazero witc youki""")
add("sec", """airlock alcide apiclarity apolicy aserto athenz authing bank-vaults blackduck bloombase bpfman capsule8 cartography casdoor cedar cerbos chaitintech checkov chef-inspec china-mobile-cloud-cas clair cloudmatos community-bouncy-castle confidential-containers conjur containerssh copa curiefense datica dex ejbca-community external-secrets fairwinds-insights fugue gitguardian grafeas grype hexa in-toto jetstack-cert-manager keylime kics kube-bench kube-hunter kubearmor kubelinter kubescape kubewarden kyverno matano metarget mondoo neuvector notary-project opa opal open-policy-containers openfga openscap orcasec ory-hydra oxeye paladin-cloud paralus parsec passage permify pinniped pipelock pluto pomerium portshift project-sonobuoy qingteng ratify rbac-lookup rbac-manager rudder scribe securecodebox signserver-community slimtoolkit sops spiffe spire spyderbat sso stackhawk stackrox syft sysdig-secure teller tensor terrascan tesseral tetragon-logo-wormark the-update-framework-tuf threatmapper tokenetes topaz tracee trend-micro varmor veinmind white-source zettaset""")

# brand glyphs tinted with official colors (auto-generated)
add("ai", """ai-dungeon aib aiohttp aiqfome air-canada air-china air-france air-india air-serbia air-transat airasia airbus aircall clarifai data-ai grid-ai hyundai nextbillion-ai yabai""")
add("cloud", """bisecthosting cloud-native-build cloudron cloudways elastic-cloud fuga-cloud google-cloud-composer google-cloud-spanner google-cloud-storage linuxserver mixcloud netease-cloud-music omada-cloud server-fault sonarqube-cloud yandex-cloud""")
add("corp", """1-1-1-1 1001tracklists 2fas 2k 365-data-science 42 4d 99designs 9gag a-frame ab-download-manager abb abbott abbvie about-me abstract abuse-ch academia accusoft accuweather acm actigraph activeloop activision actix acura ada adafruit adaway adblock adblock-plus addy-io aeroflot afdian aftership agent-skills agora ajv akasa-air akiflow alamy alby alchemy aldi-nord alfred alibaba-com alienware allegro alliedmodders alltrails alwaysdata ameba american-airlines american-express amg amul ana analogue andela android-studio anichart anilist animal-planet ankermake anki answer ansys anta antena-3 antennapod anycubic apache-arrow apache-dolphinscheduler apache-doris apache-echarts apache-freemarker apache-groovy apache-hbase apache-jmeter apache-kylin apache-netbeans-ide apache-parquet apache-pulsar aparat apifox apm-terminals appgallery appian appimage apple-arcade apple-news appmanager appsmith aral arcgis archicad archive-of-our-own ardour ariakit ark-ecosystem arlo arm-keil artstation arxiv asda aseprite assemblyscript asterisk aston-martin astra at-and-t atari auchan audible audio-technica audioboom audiomack autentique autocannon autodesk autodesk-maya autodesk-revit autohotkey autozone avast avianca avira avm await awesome-lists awesomewm awwwards b-and-r-automation b4x babelio backendless bandlab bandsintown baremetrics barmenia basic-attention-token bastyon bat bata battledotnet beatport beats-by-dre beatstars beekeeper-studio beijing-subway bentobox bereal betfair betterdiscord bevy bigbasket bigbluebutton billboard bim bio-link bioconductor biome bit bitcomet bitdefender bitsy bittorrent bitwig black blackberry blackmagic-design blazemeter blazor blibli blockbench blockchain-com bloglovin bluesound bmc-software bnb-chain boat boehringer-ingelheim bohemia-interactive bombardier bookalope bookbub bookmeter bookmyshow boost boosty boots borgbackup bosch botble-cms boulanger boxy-svg braintree braintrust brandfetch breaker brenntag bricks british-airways bruno bspwm bt buefy bugatti buhl builtbybit bukalapak bungie bunnydotnet bunq burger-king burton bvg byju-s bytedance c-plusplus-builder cadillac cafepress cairo-graphics cairo-metro canvas capacitor car-throttle carlsberg-group castbox castorama castro caterpillar cbc ccc ccleaner cd-projekt ce celery celestron cesium channel-4 charles chartmogul chase checkio checkmarx cheerio chemex chess-com chevrolet chia-network china-eastern-airlines china-railway china-southern-airlines chrysler chupa-chups cinema-4d cinnamon circuitverse civicrm claris clarivate cline clockify clubforce clubhouse clyp cncf cnes co-op coding-ninjas coggle comicfury comma commodore common-lisp common-workflow-language compiler-explorer comptia comsol conan conda-forge conekta construct-3 contao contensis contentstack continente contributor-covenant conventional-commits convertio cookiecutter cooler-master copa-airlines coppel cora coreldraw corona-engine corona-renderer counter-strike countingworks-pro coze craftsman crayon creality creative-technology credly crehana crew-united critical-role crowdsource cryengine csdn css-design-awards css-modules css-wizardry cts cultura custom-ink cyberdefenders cycling-74 d d-edge d-wave-systems dacia daf darty das-erste dash0 dataiku date-fns datev datto davinci-resolve dazhong-dianping dazn dbeaver dblp dc-entertainment de-longhi debrid-link decap-cms decentraland deepcool deepgram deepin deepmind deepnote deliveroo delphi delta der-spiegel deutsche-bahn deutsche-post deutsche-telekom deutsche-welle dhl diagramsdotnet diaspora dicebear dictionary-com digi-key-electronics dior discogs disroot distrobox distrokid dji dlib dlthub dm dmm docs-rs dolby dolphin doordash dota-2 douban douban-read downdetector doxygen dpd dragonframe draugiem-lv dreamstime drooble ds-automobiles dts dtube ducati dungeons-and-dragons dunked dunzo dvc dwm e e-leclerc e3 eac eagle easyeda easyjet ebox eclipse-adoptium eclipse-ide eclipse-mosquitto eclipse-vert-x ecovacs edeka edge-impulse educative egnyte eight eight-sleep elastic-stack elavon electron-builder electron-fiddle elegoo elgato elixir elk embark emirates emlakjet enpass ens ente epel epson equinix-metal erpnext esea esoteric-software esri ethiopian-airlines etihad-airways european-union every-org exordo expedia expensify experts-exchange express-com eyeem f1 facebook-live faceit facepunch fandango fandom fanfou fantom farcaster fareharbor farfetch fathom favro fcc ferrari ferrari-n-v fi fiat fido-alliance fifa fig figshare fila filament file-io fillout fineco fing firefish firefox-browser fireship first fish-audio fish-shell fivem fizz flashforge flat flightaware flower fluent-bit fluke fluxer flyway fmod fnac folium folo fonoma fontbase fontforge foodpanda formik fortnite fossil-scm foundry-virtual-tabletop foxtel fozzy franprix frappe fraunhofer-gesellschaft freedesktop-org freelancermap freenet freetube frontend-mentor frontify fubo fueler fujitsu fur-affinity furry-network futurelearn fyle g2 g2a g2g galaxus garmin gatling general-electric general-motors genius gentoo geocaching geode geopandas getx globus glovo gltf gnome-terminal gnu-bash gnu-emacs gnu-icecat google-apps-script google-bigtable google-campaign-manager-360 google-cardboard google-cast google-chronicle google-dataflow google-dataproc google-earth-engine google-nearby google-pub-sub gotomeeting gplv3 grand-frais greasy-fork great-learning greenhouse groupme gsk gsma gsmarena-com gtk guangzhou-metro guitar-pro gumtree gurobi gutenberg h-and-m h3 habr hack-club hackaday hacker-noon hackerearth hackerrank hackmd hackster hal handshake happycow hashcat hatena-bookmark have-i-been-pwned havells hbo-max headphone-zone headspace hearth hearthis-at hedera helium helium-browser hellofresh helly-hansen helpdesk hepsiemlak here hevy hexlet hey hi-bob hilton hilton-hotels-and-resorts hivemq homeadvisor homepage homify honda honey honeygain honor hotels-com hotwire houdini houzz htc htc-vive html-academy htop hungry-jack-s husqvarna hyperskill hyperx hypothesis i3 iata ibeacon iberia iced iceland icomoon iconfinder iconify iconjar icons8 icq ifixit ifood ign ikea ilovepdf image-sc image-toolbox imagej immersive-translate imou improvmx indeed indian-super-league indie-hackers indieweb indigo inductive-automation inertia infiniti infinityfree infomaniak infoq infuse inkdrop inquirer inspire insta360 instapaper instructables instructure interaction-design-foundation interbase intermarche intigriti intuit iota iris irobot isc2 isro issuu iterm2 itunes itvx iveco jabber jameson japan-airlines jbl jdoodle jeep jet jetblue jetpack-compose jfrog-pipelines jinja jira-software jitpack john-deere jordan jouav jovian jpeg jr-group json-web-tokens juce juejin juke junit5 just just-eat kahoot kakao kakaotalk kando karlsruher-verkehrsverbund kasa-smart kashflow kaspersky katana kde-neon kde-plasma kdenlive kedro keep-a-changelog keeper keeweb kenmei kentico keras keystone kfc khronos-group kia kicad kingston-technology kinopoisk kinsta kitsu klm klook knime knip knowledgebase known koc kodak kodular koenigsegg kofax konami kongregate konva kred krita ktm kuaishou kubuntu kueski kuma kununu kuula kx kyocera labex labview lada lamborghini langchain-corporate langflow lapce laragon laravel-horizon laravel-nova latex launchpad lazarus lazyvim lbry leader-price league-of-legends leanpub lefthook leica lens leroy-merlin les-libraires letterboxd levels-fyi li-ning libraries-io librarything libreoffice-base libreoffice-calc libreoffice-draw libreoffice-impress libreoffice-math libreoffice-writer libretube libuv lifx lightburn lightning linkfire linktree linkvertise linphone lion-air listenhub literal litiengine livejournal livekit livewire lm-studio lmms local localsend locust loop loops loot-crate lospec lot-polish-airlines ltspice luanti luau lubuntu lucia lucide ludwig lufthansa lunacy luogu lutris lvgl lydia lyft m5stack macpaw macports macy-s magasins-u magic magisk mahindra mainwp major-league-hacking make makerbot malwarebytes mamp man mangacollec mangaupdates maplibre mariadb-foundation marriott marvelapp maserati mastercomfig material-design material-for-mkdocs matternet max-planck-gesellschaft maytag mazda mclaren mdblist mdbook mdn-web-docs mediamarkt mediapipe mediatek medibang-paint mega meituan meizu mendeley mentorcruise metacritic metafilter metager metasploit metro metro-de-madrid mewe mg micro-bit micro-blog micro-editor microstation microstrategy midi migadu mihon mihoyo minds mingw-w64 mini miraheze mitsubishi mix mlb mlflow mobx-state-tree mock-service-worker modal modelscope modin moleculer momenteo mongoose monkey-tie monoprix monster moo moonrepo moq moqups morrisons moscow-metro motorola movistar mpv msi-business mta mtr multisim muo mural myanimelist myget myob myshows myspace namebase namemc namu-wiki napster national-grid national-rail naver nba nbb ndi ndr nederlandse-spoorwegen neptune netcup netim nette netto new-balance new-japan-pro-wrestling new-york-times newgrounds nexon nextflow nextra nf-core nfc ngrx nhl nicehash niconico nike nikon nim nissan nokia norco nordic-semiconductor norton norwegian note notepad-plus-plus notist noun-project novu nrwl nsis nucleo nuke numba nunjucks nushell nxp nzxt o2 obs-studio observable oclc oclif octane-render octave october-cms odido odin odnoklassniki oh-dear okcupid okx omarchy onnx onstar opel open-access open-badges open-containers-initiative open-source-hardware open3d openai-gym openapi-initiative opencage opencritic openid openjdk openmined openscad opentext openverse openzfs opera-gx oppo optimism orchard-core org organic-maps ory osano osf osgeo oshkosh osmc owasp owasp-dependency-check oxygen oyo packagist packt paddle paddlepaddle paddy-power padlet pagespeed-insights pagseguro palantir palo-alto-software panasonic pandoc pantheon paperspace paradox-interactive parity-substrate pdm pdq peak-design pearson pegasus-airlines pelican penny persistent personio pets-at-home peugeot pexels phabricator philips-hue phonepe photobucket photocrowd photon phpbb pi pi-network piaggio-group piapro picrew picsart picxy pimcore pine-script pino pioneer-dj pipecat pipx pix pixiv pixlr pkgsrc planet plangrid plurk poe poetry polestar polymer-project pond5 porkbun portableapps-com portswigger powers pr-co pre-commit prek premid premier-league prepbytes pretzel prevention prezi primefaces primeng pro-tools probot processing-foundation processon progate pronouns-page prosemirror prosieben proteus protocols-io pubg publons pubmed puma pycqa pydantic pyg pypy pyscaffold pysyft pythonanywhere qantas qase qatar-airways qi qiita qiskit qiwi qlty qmk qodo qualtrics qualys quantcast quantconnect quarto quasar quest quickbooks quicklook quicktime quicktype qwiklabs qzone r3 racket rad-studio rainmeter rainyun rakuten rakuten-kobo ram rapid rarible rasa ravelry raylib read-cv readme reason red red-bull redash redbubble redox redragon redsys reebok reliance-industries-limited remark remedy-entertainment remove-bg ren-py renault renren rescuetime resharper retro-achievements retroarch retropie revanced revenuecat reverbnation rewe rezgo rich rimac-automobili rime risc-v riseup ritz-carlton rive roadmap-sh roam-research roblox-studio roboflow rocket rockwell-automation roll20 rolls-royce roots roots-bedrock roots-sage rossmann rotary-international rotten-tomatoes rsocket rstudio-ide rtl rtlzwei rtm ruby-sinatra ruff rumahweb runkeeper runkit runrun-it ryanair rye s7-airlines sabanci sage sagemath sahibinden salla sam-s-club san-francisco-municipal-railway sanic sartorius sat-1 satellite saturn saudia scalar scan scania schneider-electric scikit-learn scilab scipy scopus scp-foundation scrapbox scrapy scratch screencastify scrimba scrollreveal scrum-alliance scrutinizer-ci seat sefaria sega sellfy semantic-scholar semrush semver sennheiser sepa servbay sessionize setapp setuptools sfml shanghai-metro sharex sharp shazam shenzhen-metro shikimori showpad showtime showwcase sidequest sifive silver-airways similarweb simplelocalize simplenote simplex sina-weibo singapore-airlines sitecore skeleton sketchfab sketchup skillshare skypack slackware slickpic smart smartthings smoothcomp smrt smugmug snapcraft snapdragon society6 socket softpedia sogou sololearn solved-ac sonar sonarqube-for-ide songkick songoda sonicwall sony soriana soundcharts source-engine sourceforge southwest-airlines spacemacs spaceship spacex spacy spark-ar sparkfun spdx speedtest speedypage sphere-online-judge spigotmc spine spond spotlight spreadshirt spreaker spring-boot spyder-ide square-enix srg-ssr ssrn stackedit stadia staffbase stagetimer standard-resume star-trek stardock starship start-gg starz statamic statista statuspal steamworks steelseries steem steinberg stellar stencil stencyl stmicroelectronics stockx stopstalk strongswan stryker stubhub studio-3t styleshare subaru subtitle-edit suckless suitest sunrise super-user supercell supercrease suzuki svgtrace swarm sway swiggy swiper swisscows symbolab symphony sympy system76 tabelog tablecheck taco-bell tado taichi-graphics taichi-lang tails taipy take-two-interactive-software talenthouse tamiya tampermonkey taobao tapas tarom tarteaucitron task tata-consultancy-services taxbuzz teal ted teepublic teespring tele-5 telegraph teradata teratail termius tesco testin testrail textpattern textual tga thangs the-algorithms the-boring-company the-conversation the-finals the-irish-times the-mighty the-models-resource the-north-face the-planetary-society the-register the-sounds-resource the-spriters-resource the-storygraph the-washington-post the-weather-channel thingiverse things thinkpad thirdweb threadless thumbtack ticket-tailor ticktick tide tidyverse tietoevry tilda-publishing tile tinder tindie tinkercad tinygrad tinyletter tistory tmux toggl-track tokio tokyo-metro toll tomorrowland top-gg torizon totvs tourbox tower tqdm trailforks trainerroad transifex transport-for-ireland transport-for-london tresorit treyarch trezor tricentis triller trimble trip-com trivy trove trueup trulia try-it-online tubi turbo turbosquid turkish-airlines tuxedo-computers tv-time twenty twinkly twinmotion ty typer typst u-s-news uber-eats ublock-origin ubuntu-mate ufc uipath ukca ultralytics ulule umbraco uml unacademy undertale unilever uniqlo united-airlines united-nations unlicense unpkg unsplash unstop uplabs upptime usps utorrent v v2ex vala valorant vanilla-extract vapor vauxhall vbulletin vectary vectorworks veed veepee vega vegas velog vencord veritas vespa vestel vfairs viadeo viblo vinted virgin virgin-atlantic visual-paradigm visx vitepress vivint voelkner volkswagen vonage voron-design vowpal-wabbit vsco vscodium vtex vyond wacom wagmi wails walkman wantedly wattpad wazirx weasyl web-awesome web-de webcomponents-org weblate webtoon weights-and-biases welcome-to-the-jungle wellfound wemo weread western-union wezterm wgpu what3words when-i-work wiki-gg wikibooks wikimedia-foundation wikiquote wikiversity wikivoyage winamp wine wipro wish wistia wizz-air wolfram wolfram-language wolfram-mathematica wondershare woo world-health-organization wp-rocket wpexplorer write-as wwe wwise wxt wykop wyze x-org xendit xfce xiaohongshu xml xo xsplit xubuntu xyflow yaak yale yamaha-corporation yamaha-motor-corporation yeti yew yoast yolo youhodler youtube-shorts yr zaim zalando zap zara zazzle zcool zdf zebra-technologies zed-industries zelle zend zenn zenodo zensar zerodha zettlr zhihu ziggo zilch zillow zincsearch zingat zoiper zola zomato zorin zotero zyte""")
add("db", """cratedb enterprisedb h2-database igdb sqlalchemy steamdb the-movie-database""")
add("dev", """30-seconds-of-code acode advent-of-code claude-code code-blocks codechef codecrafters codeforces codemagic codementor codenewbie codeproject codesignal codewars commitlint deno-deploy devbox development-containers devexpress devrant git-extensions git-for-windows git-lfs gitcode gitconnected github-pages github-sponsors gitignore-io google-summer-of-code lintcode papers-with-code refined-github slint topcoder xda-developers""")
add("fw", """anime-js avajs avaloniaui babylon-js chedraui codeceptjs cytoscape-js ejs interactjs knex-js mamba-ui matter-js neutralinojs nodegui normalize-css opentui phoenix-framework primereact primevue purgecss ratatui react-bootstrap react-hook-form react-table reactos reka-ui reveal-js robot-framework sails-js semantic-ui-react standardjs sui svg-js tui underscore-js vuetify""")
add("media", """airplay-audio airplay-video antv apple-tv boardgamegeek codestream codingame eslgaming facebook-gaming fujifilm game-developer game-jolt game-science gamebanana gameloft gamemaker google-display-and-video-360 gradle-play-publisher gstreamer heroic-games-launcher legacy-games monogame onestream pcgamingwiki playcanvas player-fm player-me playstation-2 playstation-3 playstation-4 playstation-5 playstation-portable playstation-vita podcast-addict podcast-index radio-france red-candle-games republic-of-gamers riot-games rockstar-games streamlabs streamrunners trillertv tv4-play viaplay vimeo-livestream vlc-media-player wegame wondershare-filmora youtube-gaming""")
add("mkt", """buysellads cardmarket kamailio mail-com mail-ru mailtrap minutemailer plausible-analytics simple-analytics""")
add("os", """argos artix-linux asahi-linux atlasos bsd cachyos cocos depositphotos google-container-optimized-os harmonyos leptos lineageos linux-professional-institute mx-linux nobara-linux openbsd qubes-os reason-studios resurrection-remix-os rhinoceros""")
add("pay", """afterpay alipay axis-bank bitcoin-cash bitcoin-sv caixabank coinmarketcap commerzbank contactless-payment deutsche-bank fampay hdfc-bank icici-bank kucoin moneygram nubank payback payhip payload-cms paysafe paytm picpay razorpay samsung-pay thurgauer-kantonalbank viva-wallet walletconnect webmoney zebpay""")
add("sec", """aegis-authenticator expressvpn gnu-privacy-guard parrot-security private-division securityscorecard spring-security webauthn""")
add("shop", """big-cartel carto event-store home-assistant-community-store nano-stores picarto-tv shopee shopware thunderstore trusted-shops""")
add("social", """chatbot gnu-social imessage libera-chat livechat social-blade vrchat""")

# ============================================================
# CONTRIBUTED LOGOS — add yours here!
# Pick a category key: ai lang fw dev cloud db design social pay
# prod shop media os mkt sec web corp
# Example:  add("dev", "my-awesome-tool")
# ============================================================

SUFFIXES = ["-wordmark", "-icon-alt", "-icon-round", "-icon-dark", "-dark", "-monochrome",
            "-monochromatic", "-classic", "-old", "-2", "-alt", "-vertical", "-digital",
            "-color", "-freddie", "-shield", "-burger", "-tomster", "-octocat", "-bot",
            "-pirate", "-tux", "-net"]

def categorize(name):
    if name in M:
        return M[name]
    b = name
    changed = True
    while changed:
        changed = False
        for s in SUFFIXES:
            if b.endswith(s) and len(b) > len(s):
                b2 = b[: -len(s)]
                if b2 in M:
                    return M[b2]
                b = b2
                changed = True
                break
    if b in M:
        return M[b]
    # prefix rules
    if name.startswith("aws-") or name.startswith("amazon-"):
        return "cloud"
    if name.startswith("adobe"):
        return "design"
    if name.startswith("google-cloud"):
        return "cloud"
    if name.startswith("apache"):
        return "dev"
    if name.startswith("google-"):
        return "corp"
    if name.startswith("microsoft-"):
        return "corp"
    if name.startswith("heroku-"):
        return "cloud"
    if name.startswith("cloudflare"):
        return "cloud"
    return "other"

files = sorted(f[:-4] for f in os.listdir(os.path.join(SRC, "logos")) if f.endswith(".svg"))
groups = {k: [] for k, _ in CATS}
for n in files:
    groups[categorize(n)].append(n)

total = len(files)
print(f"Total: {total}")
for k, t in CATS:
    print(f"  {t}: {len(groups[k])}")
print("\nSample of Others:", " ".join(groups["other"][:120]))

# ---------------- README ----------------
COLS = 6

def cell(n):
    return (f'<td align="center"><a href="./logos/{n}.svg">'
            f'<img src="./logos/{n}.svg" width="38" height="38" alt="{n}"/><br/>'
            f'<sub><code>{n}</code></sub></a></td>')

def table(names):
    rows = []
    for i in range(0, len(names), COLS):
        chunk = names[i:i + COLS]
        rows.append("<tr>" + "".join(cell(n) for n in chunk) + "</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"

# one markdown file per category — the full table no longer fits GitHub's
# 512KB README render limit; big categories are paginated for the same reason
PER_PAGE_MD = 2400
cat_dir = os.path.join(SRC, "categories")
os.makedirs(cat_dir, exist_ok=True)
# clean stale pages before regenerating
for old in os.listdir(cat_dir):
    if old.endswith(".md"):
        os.remove(os.path.join(cat_dir, old))
toc_lines = []
for k, t in CATS:
    names = groups[k]
    if not names:
        continue
    pages = [names[i:i + PER_PAGE_MD] for i in range(0, len(names), PER_PAGE_MD)]
    toc_lines.append(f'- [{t}](./categories/{k}.md) — **{len(names)}**')
    fname = lambda i: f"{k}.md" if i == 0 else f"{k}-{i + 1}.md"
    for i, chunk in enumerate(pages):
        pager = ""
        if len(pages) > 1:
            links = " · ".join(
                (f"**{j + 1}**" if j == i else f"[{j + 1}](./{fname(j)})")
                for j in range(len(pages)))
            pager = f"\n\nPage {links}\n"
        page = (f'# {t} <sub>({len(names)})</sub>\n\n'
                f'[⬅️ Back to the full catalog](../README.md) · '
                f'[🖼️ Browse & download on the website]({PAGES_URL})'
                f'{pager}\n'
                f'{table(chunk)}\n'
                f'{pager}\n'
                f'[⬅️ Back to the full catalog](../README.md)\n')
        page = page.replace('href="./logos/', 'href="../logos/').replace('src="./logos/', 'src="../logos/')
        with open(os.path.join(cat_dir, fname(i)), "w") as f:
            f.write(page)

readme = f"""<div align="center">

# 🎨 Logos Apps

### A free, open collection of **{total:,}** clean SVG logos for apps, tools & tech brands.

<p>
  <img alt="Logos" src="https://img.shields.io/badge/logos-{total}-6366f1?style=for-the-badge" />
  <img alt="Format" src="https://img.shields.io/badge/format-SVG-f59e0b?style=for-the-badge" />
  <img alt="Price" src="https://img.shields.io/badge/price-free-22c55e?style=for-the-badge" />
</p>

<p>
  <a href="{ZIP_URL}">
    <img alt="Download all" src="https://img.shields.io/badge/⬇️_Download_all_logos-.zip-111827?style=for-the-badge" />
  </a>
  <a href="{PAGES_URL}">
    <img alt="Browse the gallery" src="https://img.shields.io/badge/🖼️_Browse_&_download_1--click-website-3b82f6?style=for-the-badge" />
  </a>
</p>

**[🖼️ Open the interactive gallery]({PAGES_URL})** — search, filter by category, and download any logo in one click.

</div>

---

## 🚀 Quick start

**Download everything:** [grab the full pack (.zip)]({ZIP_URL}) · **Clone:** `git clone https://github.com/{REPO}.git`

**Hotlink a single logo:**

```html
<img src="https://raw.githubusercontent.com/{REPO}/master/logos/github.svg" height="32" alt="GitHub" />
```

**Naming convention:** `brand.svg` = icon only · `brand-wordmark.svg` = logotype (icon + name).

> 💡 In the category tables, **click any icon** to open its file — then use GitHub's download button, or visit the [gallery]({PAGES_URL}) for true 1-click downloads.

---

<a id="toc"></a>

## 📚 Browse the catalog

Every logo, organized by category — open a category to see its full table:

{chr(10).join(toc_lines)}

> ⚠️ Categories are auto-generated — spotted a logo in the wrong place? PRs welcome!

---

## 🤝 Contributing

Missing a logo? Read the [contribution guide](./CONTRIBUTING.md) — TL;DR: add `logos/brand.svg`, declare its category in `scripts/gen.py`, run `python3 scripts/gen_site.py`, open a PR 🎉

## ⚖️ License & trademarks

The code, website and organization of this repository are released under the [MIT License](./LICENSE).

**The logos themselves are trademarks and property of their respective owners** and are **not** covered by the MIT license. They are provided for convenience only — check each brand's guidelines before use. Inclusion here does **not** grant usage rights nor imply affiliation or endorsement.

---

<div align="center">

Made with ❤️ by [**ln-dev7**](https://github.com/ln-dev7) — if this saved you time, drop a ⭐!

</div>
"""

with open(os.path.join(SRC, "README.md"), "w") as f:
    f.write(readme)
print(f"\nREADME.md written: {len(readme)/1024:.0f} KB")

# ---------------- index.html ----------------
data = {CAT_TITLES[k]: groups[k] for k, _ in CATS if groups[k]}

index = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Logos Apps — __TOTAL__ free SVG logos</title>
<meta name="description" content="A free collection of __TOTAL__ clean SVG logos for apps, tools & tech brands. Search, filter and download in one click." />
<style>
:root{--bg:#fafafa;--card:#fff;--text:#111827;--muted:#6b7280;--border:#e5e7eb;--accent:#6366f1;--accent2:#4f46e5;--chip:#eef2ff}
@media(prefers-color-scheme:dark){:root{--bg:#0b0f1a;--card:#111827;--text:#f3f4f6;--muted:#9ca3af;--border:#1f2937;--accent:#818cf8;--accent2:#a5b4fc;--chip:#1e1b4b}}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--text)}
header{padding:48px 16px 24px;text-align:center}
header h1{font-size:2rem}
header p{color:var(--muted);margin-top:8px}
header .actions{margin-top:16px;display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:6px;padding:9px 16px;border-radius:10px;border:1px solid var(--border);background:var(--card);color:var(--text);text-decoration:none;font-size:.875rem;font-weight:600;cursor:pointer;transition:.15s}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.btn.primary:hover{background:var(--accent2);color:#fff}
.toolbar{position:sticky;top:0;z-index:10;background:var(--bg);padding:12px 16px;border-bottom:1px solid var(--border)}
.toolbar .inner{max-width:1200px;margin:0 auto}
#search{width:100%;padding:12px 16px;font-size:1rem;border-radius:12px;border:1px solid var(--border);background:var(--card);color:var(--text);outline:none}
#search:focus{border-color:var(--accent)}
.chips{display:flex;gap:8px;overflow-x:auto;padding:10px 0 2px;scrollbar-width:thin}
.chip{white-space:nowrap;padding:6px 12px;border-radius:999px;border:1px solid var(--border);background:var(--card);color:var(--muted);font-size:.8rem;cursor:pointer;transition:.15s}
.chip.active{background:var(--chip);border-color:var(--accent);color:var(--accent);font-weight:600}
main{max-width:1200px;margin:0 auto;padding:24px 16px 64px}
#count{color:var(--muted);font-size:.875rem;margin-bottom:16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:18px 12px 12px;display:flex;flex-direction:column;align-items:center;gap:10px;transition:.15s}
.card:hover{border-color:var(--accent);transform:translateY(-2px)}
.card img{width:44px;height:44px;object-fit:contain}
.card .name{font-size:.72rem;color:var(--muted);font-family:ui-monospace,monospace;text-align:center;word-break:break-all}
.card .row{display:flex;gap:6px}
.iconbtn{padding:5px 10px;font-size:.72rem;border-radius:8px;border:1px solid var(--border);background:transparent;color:var(--muted);cursor:pointer;text-decoration:none;transition:.15s}
.iconbtn:hover{border-color:var(--accent);color:var(--accent)}
footer{text-align:center;padding:32px 16px;color:var(--muted);font-size:.875rem;border-top:1px solid var(--border)}
footer a{color:var(--accent)}
.cat-title{margin:28px 0 12px;font-size:1.1rem}
.cat-title sub{color:var(--muted);font-weight:400}
</style>
</head>
<body>
<header>
  <h1>🎨 Logos Apps</h1>
  <p><strong>__TOTAL__</strong> free SVG logos for apps, tools &amp; tech brands — search, filter, download.</p>
  <div class="actions">
    <a class="btn primary" href="__ZIP__">⬇️ Download all (.zip)</a>
    <a class="btn" href="https://github.com/__REPO__">⭐ Star on GitHub</a>
  </div>
</header>
<div class="toolbar"><div class="inner">
  <input id="search" type="search" placeholder="Search __TOTAL__ logos… (e.g. react, stripe, figma)" autocomplete="off" />
  <div class="chips" id="chips"></div>
</div></div>
<main>
  <div id="count"></div>
  <div id="content"></div>
</main>
<footer>Logos are trademarks of their respective owners. Made with ❤️ by <a href="https://github.com/ln-dev7">ln-dev7</a>.</footer>
<script>
const DATA = __DATA__;
const ALL = "All";
let activeCat = ALL, query = "";
const chipsEl = document.getElementById("chips");
const contentEl = document.getElementById("content");
const countEl = document.getElementById("count");

const cats = [ALL, ...Object.keys(DATA)];
cats.forEach(c => {
  const b = document.createElement("button");
  b.className = "chip" + (c === ALL ? " active" : "");
  const n = c === ALL ? Object.values(DATA).flat().length : DATA[c].length;
  b.textContent = c + " (" + n + ")";
  b.onclick = () => { activeCat = c; document.querySelectorAll(".chip").forEach(x => x.classList.remove("active")); b.classList.add("active"); render(); };
  chipsEl.appendChild(b);
});

document.getElementById("search").addEventListener("input", e => { query = e.target.value.trim().toLowerCase(); render(); });

function card(n) {
  return `<div class="card">
    <img src="logos/${n}.svg" alt="${n}" loading="lazy" />
    <div class="name">${n}</div>
    <div class="row">
      <a class="iconbtn" href="logos/${n}.svg" download="${n}.svg">⬇️ SVG</a>
      <button class="iconbtn" onclick="copySvg('${n}', this)">📋 Copy</button>
    </div>
  </div>`;
}

async function copySvg(n, btn) {
  try {
    const txt = await (await fetch("logos/" + n + ".svg")).text();
    await navigator.clipboard.writeText(txt);
    btn.textContent = "✅ Copied"; setTimeout(() => btn.textContent = "📋 Copy", 1200);
  } catch { btn.textContent = "❌"; setTimeout(() => btn.textContent = "📋 Copy", 1200); }
}

function render() {
  let total = 0, htmlStr = "";
  const entries = activeCat === ALL ? Object.entries(DATA) : [[activeCat, DATA[activeCat]]];
  for (const [cat, names] of entries) {
    const f = names.filter(n => n.includes(query));
    if (!f.length) continue;
    total += f.length;
    htmlStr += `<h2 class="cat-title">${cat} <sub>(${f.length})</sub></h2><div class="grid">` + f.map(card).join("") + `</div>`;
  }
  contentEl.innerHTML = htmlStr || `<p style="color:var(--muted)">No logo found for “${query}” 🤷</p>`;
  countEl.textContent = total + " logo" + (total > 1 ? "s" : "") + (query ? ` matching “${query}”` : "");
}
render();
</script>
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
"""
index = (index.replace("__TOTAL__", f"{total:,}")
              .replace("__ZIP__", ZIP_URL)
              .replace("__REPO__", REPO)
              .replace("__DATA__", json.dumps(data)))

with open(os.path.join(SRC, "index.html"), "w") as f:
    f.write(index)
print(f"index.html written: {len(index)/1024:.0f} KB")
