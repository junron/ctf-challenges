const sleep = time => new Promise(resolve => setTimeout(resolve, time))

const challenges = new Map([
  ['xs-search', {
    name: 'eXceptional Site Searcher',
    timeout: 10000,
    handler: async (url, ctx) => {
      const page = await ctx.newPage()
      await page.goto("http://xs-search:8080/", { timeout: 3000, waitUntil: 'domcontentloaded' })
      await page.evaluate((flag)=>{
        localStorage.setItem('favorite_site', flag);
      }, process.env.FLAG);
      await page.goto(url, { timeout: 10000, waitUntil: 'domcontentloaded' })
      await sleep(5000)
    }
  }]
])

module.exports = {
  challenges
}