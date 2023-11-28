import chess

board = chess.Board()
board


peao = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

cavalo = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]
bispo = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]
torre = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]
rainha = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]
rei = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]
def evaluation_move():
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    peao_branco = len(board.pieces(chess.PAWN, chess.WHITE))
    peao_preto = len(board.pieces(chess.PAWN, chess.BLACK))
    cavalo_branco = len(board.pieces(chess.KNIGHT, chess.WHITE))
    cavalo_preto = len(board.pieces(chess.KNIGHT, chess.BLACK))
    bispo_branco = len(board.pieces(chess.BISHOP, chess.WHITE))
    bispo_preto = len(board.pieces(chess.BISHOP, chess.BLACK))
    torre_branca = len(board.pieces(chess.ROOK, chess.WHITE))
    torre_preta = len(board.pieces(chess.ROOK, chess.BLACK))
    rainha_branca = len(board.pieces(chess.QUEEN, chess.WHITE))
    rainha_preta = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = 100 * (peao_branco - peao_preto) + 320 * (cavalo_branco - cavalo_preto) + 330 * (bispo_branco - bispo_preto) + 500 * (torre_branca - torre_preta) + 900 * (rainha_branca - rainha_preta)

    peaosq = sum([peao[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    peaosq = peaosq + sum([-peao[chess.square_mirror(i)]
                       for i in board.pieces(chess.PAWN, chess.BLACK)])
    cavalosq = sum([cavalo[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    cavalosq = cavalosq + sum([-cavalo[chess.square_mirror(i)]
                           for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bisposq = sum([bispo[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bisposq = bisposq + sum([-bispo[chess.square_mirror(i)]
                           for i in board.pieces(chess.BISHOP, chess.BLACK)])
    torresq = sum([torre[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    torresq = torresq + sum([-torre[chess.square_mirror(i)]
                       for i in board.pieces(chess.ROOK, chess.BLACK)])
    rainhasq = sum([rainha[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    rainhasq = rainhasq + sum([-rainha[chess.square_mirror(i)]
                         for i in board.pieces(chess.QUEEN, chess.BLACK)])
    reisq = sum([rei[i] for i in board.pieces(chess.KING, chess.WHITE)])
    reisq = reisq + sum([-rei[chess.square_mirror(i)]
                       for i in board.pieces(chess.KING, chess.BLACK)])

    eval = material + peaosq + cavalosq + bisposq + torresq + rainhasq + reisq
    if board.turn:
        return eval
    else:
        return -eval
    
def selectmove(depth):
    bestMove = chess.Move.null()
    bestValue = -99999
    alpha = -100000
    beta = 100000
    for move in board.legal_moves:
        board.push(move)
        boardValue = -alphabeta(-beta, -alpha, depth - 1)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if (boardValue > alpha):
            alpha = boardValue
        board.pop()
    return bestMove

def alphabeta(alpha, beta, depthleft):
    bestscore = -9999
    if (depthleft == 0):
        return quiesce(alpha, beta)
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(-beta, -alpha, depthleft - 1)
        board.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore


def quiesce(alpha, beta):
    stand_pat = evaluation_move()
    if (stand_pat >= beta):
        return beta
    if (alpha < stand_pat):
        alpha = stand_pat
    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiesce(-beta, -alpha)
            board.pop()
            if (score >= beta):
                return beta
            if (score > alpha):
                alpha = score
    return alpha

mov = selectmove(1)
board.push(mov)

print(board)

"""class Tabuleiro:
    def __init__(self):
        self.historico = []
    def registrar_posicao(self,pieces):
        self.historico.append(pieces)
    def verificar_tripla_repeticao(self):
        contador = 0
        for pieces in reversed(self.historico):
            if self.historico.count(pieces) >= 3:
                contador += 1
            else:
                break
        return contador >= 3

board = Tabuleiro()

board.registrar_posicao('posição1')
board.registrar_posicao('posição2')
board.registrar_posicao('posição1')
board.registrar_posicao('posição3')
board.registrar_posicao('posição2')
board.registrar_posicao('posição1')

#verificando a repetição de mesma jogada 3 vezes

triplice_repeticao = board.verificar_tripla_repeticao()
print('Tríplice repetição: ', triplice_repeticao)"""



#board.push_san('a5')
#print(board)

#mov = selectmove(1)
#board.push(mov)
#print(board)

#board.push_san('b5')
#print(board)



