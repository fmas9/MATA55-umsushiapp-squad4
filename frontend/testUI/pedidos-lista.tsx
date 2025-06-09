"use client"

import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Separator } from "@/components/ui/separator"
import { Fish, Heart, Clock, ShoppingCart, RotateCcw, ArrowLeft, Calendar, MapPin } from "lucide-react"
import { useState } from "react"

interface Pedido {
  id: string
  nome: string
  descricao: string
  preco: number
  data: string
  status: "entregue" | "preparando" | "cancelado"
  imagem: string
  isFavorito: boolean
  quantidade: number
  endereco?: string
}

export default function Component() {
  const [pedidosFavoritos, setPedidosFavoritos] = useState<Pedido[]>([
    {
      id: "1",
      nome: "Combo Salmão Premium",
      descricao: "10 peças de salmão fresco + 8 uramakis + 2 temakis",
      preco: 89.9,
      data: "2024-01-15",
      status: "entregue",
      imagem: "/placeholder.svg?height=80&width=80",
      isFavorito: true,
      quantidade: 1,
    },
    {
      id: "2",
      nome: "Hot Philadelphia",
      descricao: "8 peças com salmão, cream cheese e cebolinha",
      preco: 32.9,
      data: "2024-01-10",
      status: "entregue",
      imagem: "/placeholder.svg?height=80&width=80",
      isFavorito: true,
      quantidade: 2,
    },
    {
      id: "3",
      nome: "Yakisoba Especial",
      descricao: "Macarrão oriental com legumes e molho especial",
      preco: 28.5,
      data: "2024-01-08",
      status: "entregue",
      imagem: "/placeholder.svg?height=80&width=80",
      isFavorito: true,
      quantidade: 1,
    },
  ])

  const [ultimosPedidos, setUltimosPedidos] = useState<Pedido[]>([
    {
      id: "4",
      nome: "Combo Executivo",
      descricao: "6 sashimis + 6 niguiris + 8 uramakis + missoshiru",
      preco: 65.9,
      data: "2024-01-20",
      status: "entregue",
      imagem: "/placeholder.svg?height=80&width=80",
      isFavorito: false,
      quantidade: 1,
      endereco: "Rua das Flores, 123",
    },
    {
      id: "5",
      nome: "Temaki Salmão Grelhado",
      descricao: "Cone de alga com salmão grelhado e cream cheese",
      preco: 18.9,
      data: "2024-01-18",
      status: "preparando",
      imagem: "/placeholder.svg?height=80&width=80",
      isFavorito: true,
      quantidade: 3,
      endereco: "Av. Principal, 456",
    },
    {
      id: "6",
      nome: "Barca Mista Grande",
      descricao: "50 peças variadas para 4 pessoas",
      preco: 159.9,
      data: "2024-01-16",
      status: "entregue",
      imagem: "/placeholder.svg?height=80&width=80",
      isFavorito: false,
      quantidade: 1,
      endereco: "Rua do Sushi, 789",
    },
    {
      id: "7",
      nome: "Combo Vegetariano",
      descricao: "8 uramakis de pepino + 6 niguiris de abacate",
      preco: 42.9,
      data: "2024-01-14",
      status: "cancelado",
      imagem: "/placeholder.svg?height=80&width=80",
      isFavorito: false,
      quantidade: 1,
      endereco: "Rua Verde, 321",
    },
  ])

  const toggleFavorito = (pedidoId: string, isFromFavoritos: boolean) => {
    if (isFromFavoritos) {
      setPedidosFavoritos((prev) =>
        prev.map((pedido) => (pedido.id === pedidoId ? { ...pedido, isFavorito: !pedido.isFavorito } : pedido)),
      )
    } else {
      setUltimosPedidos((prev) =>
        prev.map((pedido) => (pedido.id === pedidoId ? { ...pedido, isFavorito: !pedido.isFavorito } : pedido)),
      )
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case "entregue":
        return "bg-green-100 text-green-800"
      case "preparando":
        return "bg-yellow-100 text-yellow-800"
      case "cancelado":
        return "bg-red-100 text-red-800"
      default:
        return "bg-gray-100 text-gray-800"
    }
  }

  const getStatusIcon = (status: string) => {
    switch (status) {
      case "entregue":
        return <Clock className="w-3 h-3" />
      case "preparando":
        return <ShoppingCart className="w-3 h-3" />
      case "cancelado":
        return <Clock className="w-3 h-3" />
      default:
        return <Clock className="w-3 h-3" />
    }
  }

  const formatDate = (dateString: string) => {
    const date = new Date(dateString)
    return date.toLocaleDateString("pt-BR", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    })
  }

  const PedidoCard = ({ pedido, isFromFavoritos = false }: { pedido: Pedido; isFromFavoritos?: boolean }) => (
    <Card className="hover:shadow-md transition-shadow duration-200">
      <CardContent className="p-4">
        <div className="flex gap-4">
          <div className="flex-shrink-0">
            <img
              src={pedido.imagem || "/placeholder.svg"}
              alt={pedido.nome}
              className="w-20 h-20 rounded-lg object-cover bg-gray-100"
            />
          </div>

          <div className="flex-1 min-w-0">
            <div className="flex items-start justify-between mb-2">
              <div>
                <h3 className="font-semibold text-gray-900 truncate">{pedido.nome}</h3>
                <p className="text-sm text-gray-600 line-clamp-2">{pedido.descricao}</p>
              </div>
              <button
                onClick={() => toggleFavorito(pedido.id, isFromFavoritos)}
                className="ml-2 p-1 rounded-full hover:bg-gray-100 transition-colors"
              >
                <Heart
                  className={`w-5 h-5 ${
                    pedido.isFavorito ? "fill-red-500 text-red-500" : "text-gray-400 hover:text-red-500"
                  }`}
                />
              </button>
            </div>

            <div className="flex items-center gap-2 mb-3">
              <Badge className={`text-xs ${getStatusColor(pedido.status)}`}>
                {getStatusIcon(pedido.status)}
                <span className="ml-1 capitalize">{pedido.status}</span>
              </Badge>
              <span className="text-xs text-gray-500 flex items-center">
                <Calendar className="w-3 h-3 mr-1" />
                {formatDate(pedido.data)}
              </span>
              {pedido.quantidade > 1 && <span className="text-xs text-gray-500">Qtd: {pedido.quantidade}</span>}
            </div>

            {pedido.endereco && (
              <div className="flex items-center text-xs text-gray-500 mb-3">
                <MapPin className="w-3 h-3 mr-1" />
                <span className="truncate">{pedido.endereco}</span>
              </div>
            )}

            <div className="flex items-center justify-between">
              <span className="text-lg font-bold text-red-600">R$ {pedido.preco.toFixed(2).replace(".", ",")}</span>
              <Button size="sm" className="bg-red-600 hover:bg-red-700 text-white">
                <RotateCcw className="w-4 h-4 mr-1" />
                Pedir Novamente
              </Button>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  )

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <div className="flex items-center gap-4">
            <Button variant="ghost" size="sm" className="p-2">
              <ArrowLeft className="w-5 h-5" />
            </Button>
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-red-600 rounded-full flex items-center justify-center">
                <Fish className="w-5 h-5 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">Meus Pedidos</h1>
                <p className="text-sm text-gray-600">UmSushiApp</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-4xl mx-auto px-4 py-6">
        {/* Pedidos Favoritos */}
        <section className="mb-8">
          <div className="flex items-center gap-2 mb-4">
            <Heart className="w-5 h-5 text-red-600" />
            <h2 className="text-xl font-bold text-gray-900">Pedidos Favoritos</h2>
            <Badge variant="secondary" className="ml-2">
              {pedidosFavoritos.length}
            </Badge>
          </div>

          {pedidosFavoritos.length > 0 ? (
            <div className="space-y-4">
              {pedidosFavoritos.map((pedido) => (
                <PedidoCard key={pedido.id} pedido={pedido} isFromFavoritos={true} />
              ))}
            </div>
          ) : (
            <Card className="p-8 text-center">
              <Heart className="w-12 h-12 text-gray-300 mx-auto mb-4" />
              <h3 className="text-lg font-medium text-gray-900 mb-2">Nenhum favorito ainda</h3>
              <p className="text-gray-600">Marque seus pratos favoritos para encontrá-los facilmente aqui!</p>
            </Card>
          )}
        </section>

        <Separator className="my-8" />

        {/* Últimos Pedidos */}
        <section>
          <div className="flex items-center gap-2 mb-4">
            <Clock className="w-5 h-5 text-gray-600" />
            <h2 className="text-xl font-bold text-gray-900">Últimos Pedidos</h2>
            <Badge variant="secondary" className="ml-2">
              {ultimosPedidos.length}
            </Badge>
          </div>

          {ultimosPedidos.length > 0 ? (
            <div className="space-y-4">
              {ultimosPedidos.map((pedido) => (
                <PedidoCard key={pedido.id} pedido={pedido} />
              ))}
            </div>
          ) : (
            <Card className="p-8 text-center">
              <ShoppingCart className="w-12 h-12 text-gray-300 mx-auto mb-4" />
              <h3 className="text-lg font-medium text-gray-900 mb-2">Nenhum pedido ainda</h3>
              <p className="text-gray-600">Faça seu primeiro pedido e ele aparecerá aqui!</p>
              <Button className="mt-4 bg-red-600 hover:bg-red-700">Ver Cardápio</Button>
            </Card>
          )}
        </section>
      </div>
    </div>
  )
}
