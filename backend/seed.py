import csv
from datetime import datetime
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.consumidor import Consumidor
from app.models.produto import Produto
from app.models.vendedor import Vendedor
from app.models.pedido import Pedido
from app.models.item_pedido import ItemPedido
from app.models.avaliacao_pedido import AvaliacaoPedido
from app.models.imagem_categoria import CategoriaImagem

def parse_datetime(date_str):
    if not date_str or date_str.strip() == '':
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None

def parse_date(date_str):
    if not date_str or date_str.strip() == '':
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def parse_float(value_str):
    if not value_str or value_str.strip() == '':
        return None
    try:
        return float(value_str)
    except ValueError:
        return None

def run_database_seed():
    db: Session = SessionLocal()
    data_path = "./data"

    try:
        print("📊 Iniciando carga de dados...")

        # 1. Tabelas Independentes
        
        # PRODUTOS
        with open(f"{data_path}/dim_produtos.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            produtos = []
            for row in reader:
                row['peso_produto_gramas'] = parse_float(row.get('peso_produto_gramas'))
                row['comprimento_centimetros'] = parse_float(row.get('comprimento_centimetros'))
                row['altura_centimetros'] = parse_float(row.get('altura_centimetros'))
                row['largura_centimetros'] = parse_float(row.get('largura_centimetros'))
                produtos.append(Produto(**row))
            db.bulk_save_objects(produtos)
        print("✅ Produtos carregados.")

        # CONSUMIDORES
        with open(f"{data_path}/dim_consumidores.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            consumidores = [Consumidor(**row) for row in reader]
            db.bulk_save_objects(consumidores)
        print("✅ Consumidores carregados.")

        # VENDEDORES
        with open(f"{data_path}/dim_vendedores.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            vendedores = [Vendedor(**row) for row in reader]
            db.bulk_save_objects(vendedores)
        print("✅ Vendedores carregados.")

        # 2. Tabelas Dependentes
        
        # PEDIDOS
        with open(f"{data_path}/fat_pedidos.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            pedidos = []
            for row in reader:
                # Converter campos de data/hora
                row['pedido_compra_timestamp'] = parse_datetime(row.get('pedido_compra_timestamp', ''))
                row['pedido_entregue_timestamp'] = parse_datetime(row.get('pedido_entregue_timestamp', ''))
                row['data_estimada_entrega'] = parse_date(row.get('data_estimada_entrega', ''))
                row['tempo_entrega_dias'] = parse_float(row.get('tempo_entrega_dias', ''))
                row['tempo_entrega_estimado_dias'] = parse_float(row.get('tempo_entrega_estimado_dias', ''))
                row['diferenca_entrega_dias'] = parse_float(row.get('diferenca_entrega_dias', ''))
                pedidos.append(Pedido(**row))
            db.bulk_save_objects(pedidos)
        print("✅ Pedidos carregados.")

        # ITENS DE PEDIDOS
        with open(f"{data_path}/fat_itens_pedidos.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            itens = []
            for row in reader:
                # Converter campos numéricos
                row['id_item'] = int(row.get('id_item', 0))
                row['preco_BRL'] = float(row.get('preco_BRL', 0.0))
                row['preco_frete'] = float(row.get('preco_frete', 0.0))
                itens.append(ItemPedido(**row))
            db.bulk_save_objects(itens)
        print("✅ Itens de Pedidos carregados.")

        # AVALIAÇÕES DE PEDIDOS
        with open(f"{data_path}/fat_avaliacoes_pedidos.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            avaliacoes = []
            ids_vistos = set() # Conjunto para rastrear IDs únicos e evitar o IntegrityError

            for row in reader:
                id_atual = row.get('id_avaliacao')
                
                if id_atual and id_atual not in ids_vistos:
                    row['avaliacao'] = int(row.get('avaliacao', 0))
                    row['data_comentario'] = parse_datetime(row.get('data_comentario', ''))
                    row['data_resposta'] = parse_datetime(row.get('data_resposta', ''))
                    
                    avaliacoes.append(AvaliacaoPedido(**row))
                    ids_vistos.add(id_atual)

            db.bulk_save_objects(avaliacoes)

        print(f"✅ {len(avaliacoes)} Avaliações de Pedidos carregadas (duplicatas ignoradas).")

        # CATEGORIAS E IMAGENS        
        with open(f"{data_path}/dim_categoria_imagens.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            categorias = []
            for row in reader:
                categoria = CategoriaImagem(
                    categoria_produto=row['Categoria'],
                    link_imagem=row['Link']
                )
                categorias.append(categoria)
            db.bulk_save_objects(categorias)
        print("✅ Categorias e Imagens carregadas.")

        print("🔄 Calculando média de avaliações dos produtos...")
        from sqlalchemy import text
        db.execute(text("""
            UPDATE produtos
            SET media_avaliacao = COALESCE((
                SELECT AVG(ap.avaliacao)
                FROM itens_pedidos ip
                JOIN avaliacoes_pedidos ap ON ip.id_pedido = ap.id_pedido
                WHERE ip.id_produto = produtos.id_produto
            ), 0.0)
        """))
        print("✅ Médias calculadas e atualizadas com sucesso.")
        
        print("🔄 Distribuindo imagens base das categorias aos produtos...")
        db.execute(text("""
            UPDATE produtos
            SET imagem_produto = (
                SELECT link_imagem 
                FROM categorias_imagens 
                WHERE categorias_imagens.categoria_produto = produtos.categoria_produto
            )
        """))
        print("✅ Imagens distribuídas aos produtos com sucesso.")

        db.commit()

        print("🎉 Ingestão concluída com sucesso!")

    except Exception as e:
        print(f"❌ Erro na ingestão: {e}")
        db.rollback()
    finally:
        db.close()

run_database_seed()