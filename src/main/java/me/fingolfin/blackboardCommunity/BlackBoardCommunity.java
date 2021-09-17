package me.fingolfin.blackboardCommunity;

import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.requests.GatewayIntent;
import net.dv8tion.jda.api.utils.Compression;
import net.dv8tion.jda.api.utils.cache.CacheFlag;

import javax.security.auth.login.LoginException;

public class BlackBoardCommunity {

    public static JDABuilder builder;

    public static void main(String[] args) {
        String token = "ODg4MTA3NTcwMTgxNTc0Njc2.YUN4oA.e05R8SpLdcKeYFQuygoXXvMXqwA";
        builder = JDABuilder.createDefault(token);
        builder.disableCache(CacheFlag.MEMBER_OVERRIDES, CacheFlag.VOICE_STATE);
        builder.setBulkDeleteSplittingEnabled(false);
        builder.setCompression(Compression.NONE);
        builder.setActivity(Activity.watching("H3ntai (seggs wideos)"));
        //builder.enableIntents(GatewayIntent.GUILD_MEMBERS);
        try {
            builder.build();
        } catch (LoginException e) {
            e.printStackTrace();
        }
    }
}
