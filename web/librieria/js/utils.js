export function listObject(data) {
    return Object.keys(data).map(id => ({ id, ...data[id] }));
}