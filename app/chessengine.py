import chess.pgn
import chess.engine
import io


STOCKFISH_PATH = "/home/gary/stockfish/stockfish-ubuntu-x86-64-avx2"
 
pgn1 = '[Event "Live Chess"]\n[Site "Chess.com"]\n[Date "2025.03.25"]\n[Round "-"]\n[White "garymark5"]\n[Black "Mayank_9696"]\n[Result "1-0"]\n[CurrentPosition "r1b1k2r/pp1p2pp/n7/2p1N3/4P3/4P3/PPP3PP/RNB1K2R b KQkq -"]\n[Timezone "UTC"]\n[ECO "C20"]\n[ECOUrl "https://www.chess.com/openings/Kings-Pawn-Opening-1...e5"]\n[UTCDate "2025.03.25"]\n[UTCTime "06:35:15"]\n[WhiteElo "108"]\n[BlackElo "100"]\n[TimeControl "600"]\n[Termination "garymark5 won by resignation"]\n[StartTime "06:35:15"]\n[EndDate "2025.03.25"]\n[EndTime "06:39:40"]\n[Link "https://www.chess.com/game/live/136646053326"]\n\n1. e4 {[%clk 0:09:58.8]} 1... e5 {[%clk 0:09:59.2]} 2. Qh5 {[%clk 0:09:55.9]} 2... Nf6 {[%clk 0:09:54.8]} 3. Qxe5+ {[%clk 0:09:50.2]} 3... Qe7 {[%clk 0:09:49.7]} 4. Qd4 {[%clk 0:09:40.4]} 4... Na6 {[%clk 0:09:41.9]} 5. e5 {[%clk 0:09:26.4]} 5... c5 {[%clk 0:09:33.7]} 6. Qc3 {[%clk 0:09:17.2]} 6... Ne4 {[%clk 0:09:26.4]} 7. Qe3 {[%clk 0:08:47.5]} 7... f5 {[%clk 0:09:23.1]} 8. Bd3 {[%clk 0:08:37.3]} 8... Qxe5 {[%clk 0:09:08.6]} 9. Bxe4 {[%clk 0:08:23.3]} 9... fxe4 {[%clk 0:09:06.5]} 10. f3 {[%clk 0:08:14.7]} 10... Bd6 {[%clk 0:08:58]} 11. fxe4 {[%clk 0:08:05.8]} 11... Qd4 {[%clk 0:08:44.3]} 12. Nf3 {[%clk 0:07:37.3]} 12... Qxe3+ {[%clk 0:08:35.8]} 13. dxe3 {[%clk 0:07:34.5]} 13... Be5 {[%clk 0:08:22.8]} 14. Nxe5 {[%clk 0:07:29.6]} 1-0\n'
def analysegame():
    game = chess.pgn.read_game(io.StringIO(pgn1))
    board = game.board()
    analysis = []

    depth = 15
    try: 
        with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
            for move in game.mainline_moves():
                # Get the SAN notation before pushing the move
                san_move = board.san(move)
                board.push(move)
                
                info = engine.analyse(board, chess.engine.Limit(depth=depth))
                
                score = info["score"].relative
                if score.is_mate():
                    evaluation = f"Mate in {score.mate()}"
                else:
                    evaluation = score.score()
                
                analysis.append({
                    "move": san_move,  # Use the SAN we got before pushing
                    "evaluation": evaluation
                })
    except Exception as e:
        print(f"Error during analysis: {e}")
        return []
    return {"analysis": analysis}
    