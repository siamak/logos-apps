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
# 512KB README render limit
cat_dir = os.path.join(SRC, "categories")
os.makedirs(cat_dir, exist_ok=True)
toc_lines = []
for k, t in CATS:
    names = groups[k]
    if not names:
        continue
    toc_lines.append(f'- [{t}](./categories/{k}.md) — **{len(names)}**')
    page = (f'# {t} <sub>({len(names)})</sub>\n\n'
            f'[⬅️ Back to the full catalog](../README.md) · '
            f'[🖼️ Browse & download on the website]({PAGES_URL})\n\n'
            f'{table(names)}\n\n'
            f'[⬅️ Back to the full catalog](../README.md)\n')
    page = page.replace('href="./logos/', 'href="../logos/').replace('src="./logos/', 'src="../logos/')
    with open(os.path.join(cat_dir, k + ".md"), "w") as f:
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
