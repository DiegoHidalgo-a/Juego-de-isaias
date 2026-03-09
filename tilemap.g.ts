// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile1 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile2 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile3 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level1":
            case "level1":return tiles.createTilemap(hex`1000100004000000000000000000000000000000000000000000000000000101010100000101010101010201010100000000000000000000000000000000000000000004000004040100000000000101010100000400010101000000000000000000000000000000000000010101020000000000000002010100000000000101010100000000000000010000000000000000000000000000000000000000000000000000020101010100020101010200000000000000000000000000000000000400000000000002010101010202010101010102000404000000000000000000000000000201010200040000010102000000000003030303030303030303030303030303`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . 2 2 2 2 . . 
2 2 2 2 2 2 . 2 2 2 . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . 2 . . . . . 2 2 2 2 . . 
. . 2 2 2 . . . . . . . . . . . 
. . . . . . . 2 2 2 . . . . . . 
. . . 2 2 . . . . . 2 2 2 2 . . 
. . . . . 2 . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. 2 2 2 2 . . 2 2 2 . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . 2 2 2 2 . . 2 2 2 2 2 . 
. . . . . . . . . . . . . . . . 
. 2 2 . . . . . 2 2 . . . . . . 
. . . . . . . . . . . . . . . . 
`, [myTiles.transparency16,sprites.builtin.brick,myTiles.tile1,myTiles.tile2,myTiles.tile3], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
            case "myTile":
            case "tile1":return tile1;
            case "myTile0":
            case "tile2":return tile2;
            case "myTile1":
            case "tile3":return tile3;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
