embed
&1&
<drac2>
experience = int(get("exp"))
arg1 = '&1&' if '&1'+'&' != '&1&' else ''
experience = experience + int(float(arg1))
character().set_cvar_nx("exp", experience)
</drac2>
-title "{{f"{name} currently have __{exp}__ experience"}}"
-desc "after adding &1& experience to your character."
-thumb "https://cdn.discordapp.com/attachments/683614763716050944/777256220876341248/book-pile.png"
-footer "!help exp | made by Jaymes#8096"
